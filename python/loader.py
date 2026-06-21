import os
import re
import importlib.util

CHALLENGES_DIR = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'challenges')
DIFFICULTY_ORDER = ['Easy', 'Medium', 'Hard']


def _challenge_sort_key(ch):
    match = re.match(r'^(\d+)', ch['title'])
    num = int(match.group(1)) if match else 9999
    return num


def _load_challenges():
    items = []
    for fname in os.listdir(CHALLENGES_DIR):
        if fname.endswith('.py') and fname != '__init__.py':
            path = os.path.join(CHALLENGES_DIR, fname)
            spec = importlib.util.spec_from_file_location(fname[:-3], path)
            mod = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(mod)
            items.append(mod.CHALLENGE)

    items.sort(key=_challenge_sort_key)
    return {ch['id']: ch for ch in items}


CHALLENGES = _load_challenges()
