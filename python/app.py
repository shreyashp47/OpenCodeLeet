import sys
import os
from collections import OrderedDict
from flask import Flask, render_template, request, jsonify

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from config import APP_NAME, APP_VERSION, HOST, PORT, DEBUG, EXECUTION_TIMEOUT
from challenges import CHALLENGES, DIFFICULTY_ORDER
from runner import CodeRunner

app = Flask(__name__, template_folder='templates', static_folder='static')
runner = CodeRunner(timeout=EXECUTION_TIMEOUT)


@app.route('/')
def index():
    challenge_id = request.args.get('challenge', 'two-sum')
    if challenge_id not in CHALLENGES:
        challenge_id = 'two-sum'

    challenge = CHALLENGES[challenge_id]

    grouped = OrderedDict()
    for diff in DIFFICULTY_ORDER:
        items = [(cid, ch) for cid, ch in CHALLENGES.items() if ch['difficulty'] == diff]
        if items:
            grouped[diff] = items

    return render_template('index.html',
                           app_name=APP_NAME,
                           app_version=APP_VERSION,
                           challenges=CHALLENGES,
                           grouped_challenges=grouped,
                           current_challenge=challenge)


@app.route('/run/<challenge_id>', methods=['POST'])
def run_code(challenge_id):
    if challenge_id not in CHALLENGES:
        return jsonify({"success": False, "error": "Challenge not found"}), 404

    data = request.get_json() or {}
    user_code = data.get('code', '')

    if not user_code.strip():
        return jsonify(success=False, status="Error", message="Code cannot be empty.")

    challenge = CHALLENGES[challenge_id]
    full_code = f"{user_code}\n\n{challenge['test_code']}"
    result = runner.run(full_code)

    return jsonify(result)


if __name__ == '__main__':
    app.run(host=HOST, port=PORT, debug=DEBUG)
