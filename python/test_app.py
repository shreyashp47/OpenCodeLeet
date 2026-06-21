import unittest
import sys
import os
import json
from collections import OrderedDict

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from app import app
from challenges import CHALLENGES, DIFFICULTY_ORDER
from runner import CodeRunner


class TestConfig(unittest.TestCase):
    def test_difficulty_order(self):
        self.assertEqual(DIFFICULTY_ORDER, ['Easy', 'Medium', 'Hard'])

    def test_all_challenges_have_required_fields(self):
        required = {'id', 'title', 'difficulty', 'description', 'starter_code', 'test_code'}
        for cid, ch in CHALLENGES.items():
            with self.subTest(challenge=cid):
                self.assertEqual(cid, ch['id'])
                self.assertIn(ch['difficulty'], DIFFICULTY_ORDER)
                self.assertTrue(all(k in ch for k in required))

    def test_no_duplicate_ids(self):
        ids = [ch['id'] for ch in CHALLENGES.values()]
        self.assertEqual(len(ids), len(set(ids)))


class TestCodeRunner(unittest.TestCase):
    def setUp(self):
        self.runner = CodeRunner(timeout=3.0)

    def test_correct_code_returns_success(self):
        code = '''class Solution:
    def twoSum(self, nums, target):
        lookup = {}
        for i, num in enumerate(nums):
            if target - num in lookup:
                return [lookup[target - num], i]
            lookup[num] = i

if __name__ == "__main__":
    try:
        sol = Solution()
        res = sol.twoSum([2,7,11,15], 9)
        assert sorted(res) == [0, 1]
        print("ALL_TESTS_PASSED")
    except AssertionError as ae:
        print(f"TEST_FAILED: {ae}")
    except Exception as e:
        print(f"ERROR: {e}")
'''
        result = self.runner.run(code)
        self.assertTrue(result['success'])
        self.assertEqual(result['status'], 'Accepted')
        self.assertIn('elapsed_ms', result)

    def test_wrong_code_returns_failure(self):
        code = '''class Solution:
    def twoSum(self, nums, target):
        return [0, 0]

if __name__ == "__main__":
    try:
        sol = Solution()
        res = sol.twoSum([2,7,11,15], 9)
        assert sorted(res) == [0, 1]
        print("ALL_TESTS_PASSED")
    except AssertionError as ae:
        print(f"TEST_FAILED: {ae}")
    except Exception as e:
        print(f"ERROR: {e}")
'''
        result = self.runner.run(code)
        self.assertFalse(result['success'])
        self.assertEqual(result['status'], 'Wrong Answer')

    def test_syntax_error(self):
        code = '''class Solution
    def twoSum(self, nums, target):
        pass
'''
        result = self.runner.run(code)
        self.assertFalse(result['success'])
        self.assertIn('Error', result['status'])

    def test_timeout(self):
        runner = CodeRunner(timeout=0.01)
        code = '''class Solution:
    def twoSum(self, nums, target):
        while True:
            pass
'''
        result = runner.run(code)
        self.assertFalse(result['success'])
        self.assertEqual(result['status'], 'Time Limit Exceeded')


class TestFlaskApp(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_index_route(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'OpenCodeLeet', response.data.replace(b' ', b''))
        self.assertIn(b'Two Sum', response.data)

    def test_index_route_invalid_challenge_defaults(self):
        response = self.app.get('/?challenge=nonexistent')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'two-sum', response.data)

    def test_run_unknown_challenge(self):
        response = self.app.post('/run/unknown',
                                 data=json.dumps({"code": "x"}),
                                 content_type='application/json')
        self.assertEqual(response.status_code, 404)

    def test_run_empty_code(self):
        response = self.app.post('/run/two-sum',
                                 data=json.dumps({"code": ""}),
                                 content_type='application/json')
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        self.assertEqual(data['status'], 'Error')

    def test_run_code_success(self):
        correct_code = """class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        lookup = {}
        for i, num in enumerate(nums):
            if target - num in lookup:
                return [lookup[target - num], i]
            lookup[num] = i
"""
        response = self.app.post('/run/two-sum',
                                 data=json.dumps({"code": correct_code}),
                                 content_type='application/json')
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        self.assertTrue(data['success'])
        self.assertEqual(data['status'], 'Accepted')

    def test_run_code_failure(self):
        wrong_code = """class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        return [0, 0]
"""
        response = self.app.post('/run/two-sum',
                                 data=json.dumps({"code": wrong_code}),
                                 content_type='application/json')
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        self.assertFalse(data['success'])
        self.assertEqual(data['status'], 'Wrong Answer')

    def test_run_code_syntax_error(self):
        syntax_error_code = """class Solution
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        pass
"""
        response = self.app.post('/run/two-sum',
                                 data=json.dumps({"code": syntax_error_code}),
                                 content_type='application/json')
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        self.assertFalse(data['success'])
        self.assertIn('Error', data['status'])

    def test_all_challenges_load_in_index(self):
        response = self.app.get('/')
        for cid, ch in CHALLENGES.items():
            with self.subTest(challenge=cid):
                self.assertIn(ch['title'].encode(), response.data)

    def test_medium_challenge_run(self):
        code = """class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_set = set()
        left = 0
        result = 0
        for right in range(len(s)):
            while s[right] in char_set:
                char_set.remove(s[left])
                left += 1
            char_set.add(s[right])
            result = max(result, right - left + 1)
        return result
"""
        response = self.app.post('/run/longest-substring',
                                 data=json.dumps({"code": code}),
                                 content_type='application/json')
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        self.assertTrue(data['success'], msg=data.get('message', ''))
        self.assertEqual(data['status'], 'Accepted')


if __name__ == '__main__':
    unittest.main()
