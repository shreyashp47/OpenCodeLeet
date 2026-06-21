import sys
import os
import re
import subprocess
import tempfile
import time
import shutil


class CodeRunner:
    def __init__(self, timeout=3.0):
        self.timeout = timeout

    def run(self, code, language="python"):
        if language == "kotlin":
            return self._run_kotlin(code)
        return self._run_python(code)

    def _run_python(self, code):
        fd, path = tempfile.mkstemp(suffix='.py', dir=tempfile.gettempdir())
        try:
            with os.fdopen(fd, 'w') as f:
                f.write(code)

            start = time.time()
            result = subprocess.run(
                [sys.executable, path],
                capture_output=True, text=True, timeout=self.timeout
            )
            elapsed = time.time() - start
            return self._parse(result, elapsed)

        except subprocess.TimeoutExpired:
            return self._timeout_error()
        finally:
            try:
                os.remove(path)
            except OSError:
                pass

    def _run_kotlin(self, code):
        tmp = tempfile.gettempdir()
        src_path = os.path.join(tmp, f"Solution_{int(time.time() * 1000)}.kt")
        jar_path = src_path.replace(".kt", ".jar")
        try:
            with open(src_path, 'w') as f:
                f.write(code)

            start = time.time()
            compile_result = subprocess.run(
                ["kotlinc", src_path, "-include-runtime", "-d", jar_path],
                capture_output=True, text=True, timeout=self.timeout
            )
            if compile_result.returncode != 0:
                elapsed = time.time() - start
                return {
                    "success": False,
                    "status": "Runtime / Compilation Error",
                    "message": compile_result.stderr.strip().split("\n")[-1] if compile_result.stderr else compile_result.stdout.strip().split("\n")[-1],
                    "elapsed_ms": round(elapsed * 1000),
                    "stdout": "",
                    "stderr": (compile_result.stderr or compile_result.stdout).strip(),
                    "error_line": self._parse_error_line(compile_result.stderr or compile_result.stdout),
                }

            result = subprocess.run(
                ["java", "-jar", jar_path],
                capture_output=True, text=True, timeout=self.timeout
            )
            elapsed = time.time() - start
            return self._parse(result, elapsed)

        except subprocess.TimeoutExpired:
            return self._timeout_error()
        except FileNotFoundError:
            return {
                "success": False,
                "status": "System Error",
                "message": "Kotlin compiler not found. Install Kotlin: https://kotlinlang.org",
                "elapsed_ms": 0,
                "stdout": "",
                "stderr": "",
            }
        finally:
            for p in [src_path, jar_path]:
                try:
                    os.remove(p)
                except OSError:
                    pass

    def _timeout_error(self):
        return {
            "success": False,
            "status": "Time Limit Exceeded",
            "message": f"Execution timed out (limit: {self.timeout}s). Check for infinite loops.",
            "elapsed_ms": int(self.timeout * 1000),
        }

    @staticmethod
    def _parse_error_line(text):
        match = re.search(r'line (\d+)', text)
        return int(match.group(1)) if match else None

    def _parse(self, result, elapsed):
        stdout = result.stdout
        stderr = result.stderr

        resp = {
            "elapsed_ms": round(elapsed * 1000),
            "stdout": stdout.strip(),
            "stderr": stderr.strip(),
        }

        if "ALL_TESTS_PASSED" in stdout:
            clean = stdout.replace("ALL_TESTS_PASSED\n", "").replace("ALL_TESTS_PASSED", "").strip()
            resp.update(success=True, status="Accepted", message="All tests passed successfully!", stdout=clean)
        elif "TEST_FAILED:" in stdout:
            line = next((l for l in stdout.split("\n") if "TEST_FAILED:" in l), "")
            msg = line.replace("TEST_FAILED:", "").strip()
            resp.update(success=False, status="Wrong Answer", message=msg)
        elif "ERROR:" in stdout:
            line = next((l for l in stdout.split("\n") if "ERROR:" in l), "")
            msg = line.replace("ERROR:", "").strip()
            resp.update(success=False, status="Runtime Error", message=msg, error_line=self._parse_error_line(msg))
        elif stderr:
            resp.update(
                success=False,
                status="Runtime / Compilation Error",
                message=stderr.strip().split("\n")[-1],
                error_line=self._parse_error_line(stderr),
            )
        else:
            resp.update(
                success=False,
                status="Wrong Answer",
                message="Execution finished but no tests were run or output was unexpected.",
            )
        return resp
