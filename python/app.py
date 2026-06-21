import sys
import os
import subprocess
import tempfile
from flask import Flask, render_template, request, jsonify

# Add current directory to path to ensure importing challenges works
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from challenges import CHALLENGES

# Initialize Flask with templates and static folders relative to this file's directory
app = Flask(__name__, template_folder='templates', static_folder='static')

@app.route('/')
def index():
    # If no challenge selected, default to the first one
    challenge_id = request.args.get('challenge', 'two-sum')
    if challenge_id not in CHALLENGES:
        challenge_id = 'two-sum'
    
    challenge = CHALLENGES[challenge_id]
    return render_template('index.html', 
                           challenges=CHALLENGES, 
                           current_challenge=challenge)

@app.route('/run/<challenge_id>', methods=['POST'])
def run_code(challenge_id):
    if challenge_id not in CHALLENGES:
        return jsonify({"success": False, "error": "Challenge not found"}), 404
        
    data = request.get_json() or {}
    user_code = data.get('code', '')
    
    if not user_code.strip():
        return jsonify({
            "success": False,
            "status": "Error",
            "message": "Code cannot be empty."
        })
        
    challenge = CHALLENGES[challenge_id]
    
    # Combine user's code with the evaluation script
    full_code = f"{user_code}\n\n{challenge['test_code']}"
    
    # Write to a secure temporary file and run it
    temp_dir = tempfile.gettempdir()
    temp_file_fd, temp_file_path = tempfile.mkstemp(suffix='.py', dir=temp_dir)
    
    try:
        with os.fdopen(temp_file_fd, 'w') as f:
            f.write(full_code)
            
        # Execute the code in a separate process with a timeout of 3 seconds
        result = subprocess.run(
            [sys.executable, temp_file_path],
            capture_output=True,
            text=True,
            timeout=3.0
        )
        
        stdout = result.stdout
        stderr = result.stderr
        
        # Check standard output and error stream for result
        if "ALL_TESTS_PASSED" in stdout:
            return jsonify({
                "success": True,
                "status": "Accepted",
                "message": "All tests passed successfully! 🎉",
                "stdout": stdout.replace("ALL_TESTS_PASSED\n", "").strip()
            })
        elif "TEST_FAILED:" in stdout:
            # Extract test failure message
            failure_line = [line for line in stdout.split('\n') if "TEST_FAILED:" in line][0]
            failure_msg = failure_line.replace("TEST_FAILED:", "").strip()
            return jsonify({
                "success": False,
                "status": "Wrong Answer",
                "message": failure_msg,
                "stdout": stdout.strip()
            })
        elif "ERROR:" in stdout:
            # Extract run-time exception message
            error_line = [line for line in stdout.split('\n') if "ERROR:" in line][0]
            error_msg = error_line.replace("ERROR:", "").strip()
            return jsonify({
                "success": False,
                "status": "Runtime Error",
                "message": error_msg,
                "stdout": stdout.strip()
            })
        elif stderr:
            # Syntax errors or other critical uncaught exceptions
            return jsonify({
                "success": False,
                "status": "Runtime / Compilation Error",
                "message": stderr.strip().split('\n')[-1],
                "stdout": stdout.strip(),
                "stderr": stderr.strip()
            })
        else:
            return jsonify({
                "success": False,
                "status": "Wrong Answer",
                "message": "Execution finished but no tests were run or standard outputs were unexpected.",
                "stdout": stdout.strip()
            })
            
    except subprocess.TimeoutExpired:
        return jsonify({
            "success": False,
            "status": "Time Limit Exceeded",
            "message": "Your code execution timed out (Limit: 3 seconds). Check for infinite loops."
        })
    except Exception as e:
        return jsonify({
            "success": False,
            "status": "System Error",
            "message": f"An error occurred while evaluating your code: {str(e)}"
        })
    finally:
        # Always clean up the temporary file
        try:
            os.remove(temp_file_path)
        except OSError:
            pass

if __name__ == '__main__':
    # Listen on localhost:5000
    app.run(host='127.0.0.1', port=5000, debug=True)
