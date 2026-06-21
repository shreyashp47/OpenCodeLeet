import sys
import os
import subprocess
import tempfile
import time

class CodeRunner:
    def __init__(self, timeout=3.0):
        self.timeout = timeout

    def run(self, code):
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
            return {
                "success": False,
                "status": "Time Limit Exceeded",
                "message": f"Execution timed out (limit: {self.timeout}s). Check for infinite loops.",
                "elapsed_ms": int(self.timeout * 1000),
            }
        finally:
            try:
                os.remove(path)
            except OSError:
                pass

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
            resp.update(success=False, status="Runtime Error", message=msg)
        elif stderr:
            resp.update(
                success=False,
                status="Runtime / Compilation Error",
                message=stderr.strip().split("\n")[-1],
            )
        else:
            resp.update(
                success=False,
                status="Wrong Answer",
                message="Execution finished but no tests were run or output was unexpected.",
            )
        return resp
