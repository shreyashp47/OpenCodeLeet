import os
import importlib.util

CHALLENGES_DIR = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'challenges')
DIFFICULTY_ORDER = ['Easy', 'Medium', 'Hard']


def _load_challenges():
    challenges = {}
    for fname in sorted(os.listdir(CHALLENGES_DIR)):
        if fname.endswith('.py') and fname != '__init__.py':
            path = os.path.join(CHALLENGES_DIR, fname)
            spec = importlib.util.spec_from_file_location(fname[:-3], path)
            mod = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(mod)
            ch = mod.CHALLENGE
            challenges[ch['id']] = ch
    return challenges


CHALLENGES = _load_challenges()
