import unittest
import sys
import os
import json

# Ensure python directory is in path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from app import app
from challenges import CHALLENGES

class TestLeetCodeApp(unittest.TestCase):
    def setUp(self):
        # Set up Flask test client
        self.app = app.test_client()
        self.app.testing = True

    def test_index_route(self):
        # Verify index page loads successfully
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'OpenCodeLeet', response.data.replace(b' ', b''))
        self.assertIn(b'Two Sum', response.data)

    def test_run_code_success(self):
        # Verify submitting a correct Two Sum solution
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
        self.assertIn('All tests passed', data['message'])

    def test_run_code_failure(self):
        # Verify submitting an incorrect Two Sum solution
        wrong_code = """class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        return [0, 0] # Obviously wrong
"""
        response = self.app.post('/run/two-sum', 
                                 data=json.dumps({"code": wrong_code}),
                                 content_type='application/json')
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        self.assertFalse(data['success'])
        self.assertEqual(data['status'], 'Wrong Answer')
        self.assertIn('Test case 1 failed', data['message'])

    def test_run_code_syntax_error(self):
        # Verify syntax error handling
        syntax_error_code = """class Solution
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        pass
""" # Missing colon on class definition
        response = self.app.post('/run/two-sum', 
                                 data=json.dumps({"code": syntax_error_code}),
                                 content_type='application/json')
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        self.assertFalse(data['success'])
        self.assertEqual(data['status'], 'Runtime / Compilation Error')

if __name__ == '__main__':
    unittest.main()
