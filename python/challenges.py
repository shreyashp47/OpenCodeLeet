CHALLENGES = {
    "two-sum": {
        "id": "two-sum",
        "title": "1. Two Sum",
        "difficulty": "Easy",
        "description": """<p>Given an array of integers <code>nums</code> and an integer <code>target</code>, return <em>indices of the two numbers such that they add up to <code>target</code></em>.</p>
<p>You may assume that each input would have <strong><em>exactly</em> one solution</strong>, and you may not use the <em>same</em> element twice.</p>
<p>You can return the answer in any order.</p>

<h3 class="text-lg font-semibold mt-4 mb-2">Example 1:</h3>
<pre class="bg-gray-800 text-gray-100 p-3 rounded-lg font-mono text-sm mb-4">
<strong>Input:</strong> nums = [2,7,11,15], target = 9
<strong>Output:</strong> [0,1]
<strong>Explanation:</strong> Because nums[0] + nums[1] == 9, we return [0, 1].
</pre>

<h3 class="text-lg font-semibold mt-4 mb-2">Example 2:</h3>
<pre class="bg-gray-800 text-gray-100 p-3 rounded-lg font-mono text-sm mb-4">
<strong>Input:</strong> nums = [3,2,4], target = 6
<strong>Output:</strong> [1,2]
</pre>

<h3 class="text-lg font-semibold mt-4 mb-2">Example 3:</h3>
<pre class="bg-gray-800 text-gray-100 p-3 rounded-lg font-mono text-sm mb-4">
<strong>Input:</strong> nums = [3,3], target = 6
<strong>Output:</strong> [0,1]
</pre>

<h3 class="text-lg font-semibold mt-4 mb-2">Constraints:</h3>
<ul class="list-disc pl-5 space-y-1 text-gray-300">
  <li><code>2 <= nums.length <= 10<sup>4</sup></code></li>
  <li><code>-10<sup>9</sup> <= nums[i] <= 10<sup>9</sup></code></li>
  <li><code>-10<sup>9</sup> <= target <= 10<sup>9</sup></code></li>
  <li><strong>Only one valid answer exists.</strong></li>
</ul>""",
        "starter_code": """class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        # Write your code here
        pass
""",
        "test_code": """
if __name__ == "__main__":
    try:
        sol = Solution()
        # Test 1
        res1 = sol.twoSum([2, 7, 11, 15], 9)
        assert res1 is not None, "Test case 1 failed. Returned None."
        assert sorted(res1) == [0, 1], f"Test case 1 failed. Expected [0, 1], got {res1}"
        # Test 2
        res2 = sol.twoSum([3, 2, 4], 6)
        assert res2 is not None, "Test case 2 failed. Returned None."
        assert sorted(res2) == [1, 2], f"Test case 2 failed. Expected [1, 2], got {res2}"
        # Test 3
        res3 = sol.twoSum([3, 3], 6)
        assert res3 is not None, "Test case 3 failed. Returned None."
        assert sorted(res3) == [0, 1], f"Test case 3 failed. Expected [0, 1], got {res3}"
        print("ALL_TESTS_PASSED")
    except AssertionError as ae:
        print(f"TEST_FAILED: {ae}")
    except Exception as e:
        print(f"ERROR: {e}")
"""
    },
    "reverse-string": {
        "id": "reverse-string",
        "title": "344. Reverse String",
        "difficulty": "Easy",
        "description": """<p>Write a function that reverses a string. The input string is given as an array of characters <code>s</code>.</p>
<p>You must do this by modifying the input array <strong>in-place</strong> with <code>O(1)</code> extra memory.</p>

<h3 class="text-lg font-semibold mt-4 mb-2">Example 1:</h3>
<pre class="bg-gray-800 text-gray-100 p-3 rounded-lg font-mono text-sm mb-4">
<strong>Input:</strong> s = ["h","e","l","l","o"]
<strong>Output:</strong> ["o","l","l","e","h"]
</pre>

<h3 class="text-lg font-semibold mt-4 mb-2">Example 2:</h3>
<pre class="bg-gray-800 text-gray-100 p-3 rounded-lg font-mono text-sm mb-4">
<strong>Input:</strong> s = ["H","a","n","n","a","h"]
<strong>Output:</strong> ["h","a","n","n","a","H"]
</pre>

<h3 class="text-lg font-semibold mt-4 mb-2">Constraints:</h3>
<ul class="list-disc pl-5 space-y-1 text-gray-300">
  <li><code>1 <= s.length <= 10<sup>5</sup></code></li>
  <li><code>s[i]</code> is a printable ascii character.</li>
</ul>""",
        "starter_code": """class Solution:
    def reverseString(self, s: list[str]) -> None:
        \"\"\"
        Do not return anything, modify s in-place instead.
        \"\"\"
        # Write your code here
        pass
""",
        "test_code": """
if __name__ == "__main__":
    try:
        sol = Solution()
        # Test 1
        s1 = ["h","e","l","l","o"]
        sol.reverseString(s1)
        assert s1 == ["o","l","l","e","h"], f"Test case 1 failed. Expected ['o', 'l', 'l', 'e', 'h'], got {s1}"
        # Test 2
        s2 = ["H","a","n","n","a","h"]
        sol.reverseString(s2)
        assert s2 == ["h","a","n","n","a","H"], f"Test case 2 failed. Expected ['h', 'a', 'n', 'n', 'a', 'H'], got {s2}"
        print("ALL_TESTS_PASSED")
    except AssertionError as ae:
        print(f"TEST_FAILED: {ae}")
    except Exception as e:
        print(f"ERROR: {e}")
"""
    },
    "palindrome-number": {
        "id": "palindrome-number",
        "title": "9. Palindrome Number",
        "difficulty": "Easy",
        "description": """<p>Given an integer <code>x</code>, return <code>true</code> if <code>x</code> is a <strong>palindrome</strong>, and <code>false</code> otherwise.</p>

<h3 class="text-lg font-semibold mt-4 mb-2">Example 1:</h3>
<pre class="bg-gray-800 text-gray-100 p-3 rounded-lg font-mono text-sm mb-4">
<strong>Input:</strong> x = 121
<strong>Output:</strong> true
<strong>Explanation:</strong> 121 reads as 121 from left to right and from right to left.
</pre>

<h3 class="text-lg font-semibold mt-4 mb-2">Example 2:</h3>
<pre class="bg-gray-800 text-gray-100 p-3 rounded-lg font-mono text-sm mb-4">
<strong>Input:</strong> x = -121
<strong>Output:</strong> false
<strong>Explanation:</strong> From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
</pre>

<h3 class="text-lg font-semibold mt-4 mb-2">Example 3:</h3>
<pre class="bg-gray-800 text-gray-100 p-3 rounded-lg font-mono text-sm mb-4">
<strong>Input:</strong> x = 10
<strong>Output:</strong> false
<strong>Explanation:</strong> Reads 01 from right to left. Therefore it is not a palindrome.
</pre>

<h3 class="text-lg font-semibold mt-4 mb-2">Constraints:</h3>
<ul class="list-disc pl-5 space-y-1 text-gray-300">
  <li><code>-2<sup>31</sup> <= x <= 2<sup>31</sup> - 1</code></li>
</ul>""",
        "starter_code": """class Solution:
    def isPalindrome(self, x: int) -> bool:
        # Write your code here
        pass
""",
        "test_code": """
if __name__ == "__main__":
    try:
        sol = Solution()
        # Test 1
        res1 = sol.isPalindrome(121)
        assert res1 is True, f"Test case 1 failed. Expected True for 121, got {res1}"
        # Test 2
        res2 = sol.isPalindrome(-121)
        assert res2 is False, f"Test case 2 failed. Expected False for -121, got {res2}"
        # Test 3
        res3 = sol.isPalindrome(10)
        assert res3 is False, f"Test case 3 failed. Expected False for 10, got {res3}"
        # Test 4
        res4 = sol.isPalindrome(12321)
        assert res4 is True, f"Test case 4 failed. Expected True for 12321, got {res4}"
        print("ALL_TESTS_PASSED")
    except AssertionError as ae:
        print(f"TEST_FAILED: {ae}")
    except Exception as e:
        print(f"ERROR: {e}")
"""
    },
    "valid-parentheses": {
        "id": "valid-parentheses",
        "title": "20. Valid Parentheses",
        "difficulty": "Easy",
        "description": """<p>Given a string <code>s</code> containing just the characters <code>'('</code>, <code>')'</code>, <code>'{'</code>, <code>'}'</code>, <code>'['</code> and <code>']'</code>, determine if the input string is valid.</p>
<p>An input string is valid if:</p>
<ol class="list-decimal pl-5 space-y-1 text-gray-300">
  <li>Open brackets must be closed by the same type of brackets.</li>
  <li>Open brackets must be closed in the correct order.</li>
  <li>Every close bracket has a corresponding open bracket of the same type.</li>
</ol>

<h3 class="text-lg font-semibold mt-4 mb-2">Example 1:</h3>
<pre class="bg-gray-800 text-gray-100 p-3 rounded-lg font-mono text-sm mb-4">
<strong>Input:</strong> s = "()"
<strong>Output:</strong> true
</pre>

<h3 class="text-lg font-semibold mt-4 mb-2">Example 2:</h3>
<pre class="bg-gray-800 text-gray-100 p-3 rounded-lg font-mono text-sm mb-4">
<strong>Input:</strong> s = "()[]{}"
<strong>Output:</strong> true
</pre>

<h3 class="text-lg font-semibold mt-4 mb-2">Example 3:</h3>
<pre class="bg-gray-800 text-gray-100 p-3 rounded-lg font-mono text-sm mb-4">
<strong>Input:</strong> s = "(]"
<strong>Output:</strong> false
</pre>

<h3 class="text-lg font-semibold mt-4 mb-2">Constraints:</h3>
<ul class="list-disc pl-5 space-y-1 text-gray-300">
  <li><code>1 <= s.length <= 10<sup>4</sup></code></li>
  <li><code>s</code> consists of parentheses only <code>'()[]{}'</code>.</li>
</ul>""",
        "starter_code": """class Solution:
    def isValid(self, s: str) -> bool:
        # Write your code here
        pass
""",
        "test_code": """
if __name__ == "__main__":
    try:
        sol = Solution()
        assert sol.isValid("()") is True, "Test case 1 failed. Expected True for '()'."
        assert sol.isValid("()[]{}") is True, "Test case 2 failed. Expected True for '()[]{}'."
        assert sol.isValid("(]") is False, "Test case 3 failed. Expected False for '(]'."
        assert sol.isValid("([)]") is False, "Test case 4 failed. Expected False for '([)]'."
        assert sol.isValid("{[]}") is True, "Test case 5 failed. Expected True for '{[]}'."
        print("ALL_TESTS_PASSED")
    except AssertionError as ae:
        print(f"TEST_FAILED: {ae}")
    except Exception as e:
        print(f"ERROR: {e}")
"""
    }
}
