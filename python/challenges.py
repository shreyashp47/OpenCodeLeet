DIFFICULTY_ORDER = ['Easy', 'Medium', 'Hard']

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
  <li><code>2 &lt;= nums.length &lt;= 10<sup>4</sup></code></li>
  <li><code>-10<sup>9</sup> &lt;= nums[i] &lt;= 10<sup>9</sup></code></li>
  <li><code>-10<sup>9</sup> &lt;= target &lt;= 10<sup>9</sup></code></li>
  <li><strong>Only one valid answer exists.</strong></li>
</ul>""",
        "starter_code": """class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        pass
""",
        "solution_code": """class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        lookup = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in lookup:
                return [lookup[complement], i]
            lookup[num] = i
""",
        "test_code": """
if __name__ == "__main__":
    try:
        sol = Solution()
        res1 = sol.twoSum([2, 7, 11, 15], 9)
        assert res1 is not None, "Test 1 failed. Returned None."
        assert sorted(res1) == [0, 1], f"Test 1 failed. Expected [0, 1], got {res1}"
        res2 = sol.twoSum([3, 2, 4], 6)
        assert res2 is not None, "Test 2 failed. Returned None."
        assert sorted(res2) == [1, 2], f"Test 2 failed. Expected [1, 2], got {res2}"
        res3 = sol.twoSum([3, 3], 6)
        assert res3 is not None, "Test 3 failed. Returned None."
        assert sorted(res3) == [0, 1], f"Test 3 failed. Expected [0, 1], got {res3}"
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
  <li><code>1 &lt;= s.length &lt;= 10<sup>5</sup></code></li>
  <li><code>s[i]</code> is a printable ascii character.</li>
</ul>""",
        "starter_code": """class Solution:
    def reverseString(self, s: list[str]) -> None:
        \"\"\"
        Do not return anything, modify s in-place instead.
        \"\"\"
        pass
""",
        "solution_code": """class Solution:
    def reverseString(self, s: list[str]) -> None:
        left, right = 0, len(s) - 1
        while left < right:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1
""",
        "test_code": """
if __name__ == "__main__":
    try:
        sol = Solution()
        s1 = ["h","e","l","l","o"]
        sol.reverseString(s1)
        assert s1 == ["o","l","l","e","h"], f"Test 1 failed. Expected ['o','l','l','e','h'], got {s1}"
        s2 = ["H","a","n","n","a","h"]
        sol.reverseString(s2)
        assert s2 == ["h","a","n","n","a","H"], f"Test 2 failed. Expected ['h','a','n','n','a','H'], got {s2}"
        s3 = ["a"]
        sol.reverseString(s3)
        assert s3 == ["a"], f"Test 3 failed. Expected ['a'], got {s3}"
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
  <li><code>-2<sup>31</sup> &lt;= x &lt;= 2<sup>31</sup> - 1</code></li>
</ul>""",
        "starter_code": """class Solution:
    def isPalindrome(self, x: int) -> bool:
        pass
""",
        "solution_code": """class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0 or (x % 10 == 0 and x != 0):
            return False
        reversed_half = 0
        while x > reversed_half:
            reversed_half = reversed_half * 10 + x % 10
            x //= 10
        return x == reversed_half or x == reversed_half // 10
""",
        "test_code": """
if __name__ == "__main__":
    try:
        sol = Solution()
        res1 = sol.isPalindrome(121)
        assert res1 is True, f"Test 1 failed. Expected True for 121, got {res1}"
        res2 = sol.isPalindrome(-121)
        assert res2 is False, f"Test 2 failed. Expected False for -121, got {res2}"
        res3 = sol.isPalindrome(10)
        assert res3 is False, f"Test 3 failed. Expected False for 10, got {res3}"
        res4 = sol.isPalindrome(12321)
        assert res4 is True, f"Test 4 failed. Expected True for 12321, got {res4}"
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
  <li><code>1 &lt;= s.length &lt;= 10<sup>4</sup></code></li>
  <li><code>s</code> consists of parentheses only <code>'()[]{}'</code>.</li>
</ul>""",
        "starter_code": """class Solution:
    def isValid(self, s: str) -> bool:
        pass
""",
        "solution_code": """class Solution:
    def isValid(self, s: str) -> bool:
        pairs = {')': '(', '}': '{', ']': '['}
        stack = []
        for ch in s:
            if ch in pairs:
                if not stack or stack.pop() != pairs[ch]:
                    return False
            else:
                stack.append(ch)
        return not stack
""",
        "test_code": """
if __name__ == "__main__":
    try:
        sol = Solution()
        assert sol.isValid("()") is True, "Test 1 failed. Expected True for '()'."
        assert sol.isValid("()[]{}") is True, "Test 2 failed. Expected True for '()[]{}'."
        assert sol.isValid("(]") is False, "Test 3 failed. Expected False for '(]'."
        assert sol.isValid("([)]") is False, "Test 4 failed. Expected False for '([)]'."
        assert sol.isValid("{[]}") is True, "Test 5 failed. Expected True for '{[]}'."
        print("ALL_TESTS_PASSED")
    except AssertionError as ae:
        print(f"TEST_FAILED: {ae}")
    except Exception as e:
        print(f"ERROR: {e}")
"""
    },
    "longest-substring": {
        "id": "longest-substring",
        "title": "3. Longest Substring Without Repeating Characters",
        "difficulty": "Medium",
        "description": """<p>Given a string <code>s</code>, find the length of the <strong>longest substring</strong> without repeating characters.</p>

<h3 class="text-lg font-semibold mt-4 mb-2">Example 1:</h3>
<pre class="bg-gray-800 text-gray-100 p-3 rounded-lg font-mono text-sm mb-4">
<strong>Input:</strong> s = "abcabcbb"
<strong>Output:</strong> 3
<strong>Explanation:</strong> The answer is "abc", with the length of 3.
</pre>

<h3 class="text-lg font-semibold mt-4 mb-2">Example 2:</h3>
<pre class="bg-gray-800 text-gray-100 p-3 rounded-lg font-mono text-sm mb-4">
<strong>Input:</strong> s = "bbbbb"
<strong>Output:</strong> 1
<strong>Explanation:</strong> The answer is "b", with the length of 1.
</pre>

<h3 class="text-lg font-semibold mt-4 mb-2">Example 3:</h3>
<pre class="bg-gray-800 text-gray-100 p-3 rounded-lg font-mono text-sm mb-4">
<strong>Input:</strong> s = "pwwkew"
<strong>Output:</strong> 3
<strong>Explanation:</strong> The answer is "wke", with the length of 3. Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
</pre>

<h3 class="text-lg font-semibold mt-4 mb-2">Constraints:</h3>
<ul class="list-disc pl-5 space-y-1 text-gray-300">
  <li><code>0 &lt;= s.length &lt;= 5 * 10<sup>4</sup></code></li>
  <li><code>s</code> consists of English letters, digits, symbols and spaces.</li>
</ul>""",
        "starter_code": """class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        pass
""",
        "solution_code": """class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = {}
        left = result = 0
        for right, ch in enumerate(s):
            if ch in seen and seen[ch] >= left:
                left = seen[ch] + 1
            seen[ch] = right
            result = max(result, right - left + 1)
        return result
""",
        "test_code": """
if __name__ == "__main__":
    try:
        sol = Solution()
        res1 = sol.lengthOfLongestSubstring("abcabcbb")
        assert res1 == 3, f"Test 1 failed. Expected 3, got {res1}"
        res2 = sol.lengthOfLongestSubstring("bbbbb")
        assert res2 == 1, f"Test 2 failed. Expected 1, got {res2}"
        res3 = sol.lengthOfLongestSubstring("pwwkew")
        assert res3 == 3, f"Test 3 failed. Expected 3, got {res3}"
        res4 = sol.lengthOfLongestSubstring("")
        assert res4 == 0, f"Test 4 failed. Expected 0 for empty string, got {res4}"
        res5 = sol.lengthOfLongestSubstring(" ")
        assert res5 == 1, f"Test 5 failed. Expected 1 for space, got {res5}"
        print("ALL_TESTS_PASSED")
    except AssertionError as ae:
        print(f"TEST_FAILED: {ae}")
    except Exception as e:
        print(f"ERROR: {e}")
"""
    },
    "three-sum": {
        "id": "three-sum",
        "title": "15. 3Sum",
        "difficulty": "Medium",
        "description": """<p>Given an integer array <code>nums</code>, return all the triplets <code>[nums[i], nums[j], nums[k]]</code> such that <code>i != j</code>, <code>i != k</code>, and <code>j != k</code>, and <code>nums[i] + nums[j] + nums[k] == 0</code>.</p>
<p>Notice that the solution set must not contain duplicate triplets.</p>

<h3 class="text-lg font-semibold mt-4 mb-2">Example 1:</h3>
<pre class="bg-gray-800 text-gray-100 p-3 rounded-lg font-mono text-sm mb-4">
<strong>Input:</strong> nums = [-1,0,1,2,-1,-4]
<strong>Output:</strong> [[-1,-1,2],[-1,0,1]]
<strong>Explanation:</strong> nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
The distinct triplets are [-1,0,1] and [-1,-1,2].
</pre>

<h3 class="text-lg font-semibold mt-4 mb-2">Example 2:</h3>
<pre class="bg-gray-800 text-gray-100 p-3 rounded-lg font-mono text-sm mb-4">
<strong>Input:</strong> nums = [0,1,1]
<strong>Output:</strong> []
<strong>Explanation:</strong> The only possible triplet does not sum up to 0.
</pre>

<h3 class="text-lg font-semibold mt-4 mb-2">Example 3:</h3>
<pre class="bg-gray-800 text-gray-100 p-3 rounded-lg font-mono text-sm mb-4">
<strong>Input:</strong> nums = [0,0,0]
<strong>Output:</strong> [[0,0,0]]
<strong>Explanation:</strong> The only possible triplet sums up to 0.
</pre>

<h3 class="text-lg font-semibold mt-4 mb-2">Constraints:</h3>
<ul class="list-disc pl-5 space-y-1 text-gray-300">
  <li><code>3 &lt;= nums.length &lt;= 3000</code></li>
  <li><code>-10<sup>5</sup> &lt;= nums[i] &lt;= 10<sup>5</sup></code></li>
</ul>""",
        "starter_code": """class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        pass
""",
        "solution_code": """class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        result = []
        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            left, right = i + 1, len(nums) - 1
            while left < right:
                total = nums[i] + nums[left] + nums[right]
                if total < 0:
                    left += 1
                elif total > 0:
                    right -= 1
                else:
                    result.append([nums[i], nums[left], nums[right]])
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    left += 1
                    right -= 1
        return result
""",
        "test_code": """
if __name__ == "__main__":
    try:
        sol = Solution()
        res1 = sol.threeSum([-1,0,1,2,-1,-4])
        assert sorted(res1) == sorted([[-1,-1,2],[-1,0,1]]), f"Test 1 failed. Got {res1}"
        res2 = sol.threeSum([0,1,1])
        assert res2 == [], f"Test 2 failed. Expected [], got {res2}"
        res3 = sol.threeSum([0,0,0])
        assert sorted(res3) == [[0,0,0]], f"Test 3 failed. Expected [[0,0,0]], got {res3}"
        res4 = sol.threeSum([1,2,-2,-1])
        assert res4 == [], f"Test 4 failed. Expected [], got {res4}"
        print("ALL_TESTS_PASSED")
    except AssertionError as ae:
        print(f"TEST_FAILED: {ae}")
    except Exception as e:
        print(f"ERROR: {e}")
"""
    },
    "group-anagrams": {
        "id": "group-anagrams",
        "title": "49. Group Anagrams",
        "difficulty": "Medium",
        "description": """<p>Given an array of strings <code>strs</code>, group <strong>the anagrams</strong> together. You can return the answer in <strong>any order</strong>.</p>
<p>An <strong>anagram</strong> is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.</p>

<h3 class="text-lg font-semibold mt-4 mb-2">Example 1:</h3>
<pre class="bg-gray-800 text-gray-100 p-3 rounded-lg font-mono text-sm mb-4">
<strong>Input:</strong> strs = ["eat","tea","tan","ate","nat","bat"]
<strong>Output:</strong> [["bat"],["nat","tan"],["ate","eat","tea"]]
</pre>

<h3 class="text-lg font-semibold mt-4 mb-2">Example 2:</h3>
<pre class="bg-gray-800 text-gray-100 p-3 rounded-lg font-mono text-sm mb-4">
<strong>Input:</strong> strs = [""]
<strong>Output:</strong> [[""]]
</pre>

<h3 class="text-lg font-semibold mt-4 mb-2">Example 3:</h3>
<pre class="bg-gray-800 text-gray-100 p-3 rounded-lg font-mono text-sm mb-4">
<strong>Input:</strong> strs = ["a"]
<strong>Output:</strong> [["a"]]
</pre>

<h3 class="text-lg font-semibold mt-4 mb-2">Constraints:</h3>
<ul class="list-disc pl-5 space-y-1 text-gray-300">
  <li><code>1 &lt;= strs.length &lt;= 10<sup>4</sup></code></li>
  <li><code>0 &lt;= strs[i].length &lt;= 100</code></li>
  <li><code>strs[i]</code> consists of lowercase English letters.</li>
</ul>""",
        "starter_code": """class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        pass
""",
        "solution_code": """class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        groups = {}
        for s in strs:
            key = "".join(sorted(s))
            if key in groups:
                groups[key].append(s)
            else:
                groups[key] = [s]
        return list(groups.values())
""",
        "test_code": """
if __name__ == "__main__":
    try:
        sol = Solution()
        res1 = sol.groupAnagrams(["eat","tea","tan","ate","nat","bat"])
        sorted_res1 = sorted([sorted(g) for g in res1])
        sorted_exp1 = sorted([["bat"],["nat","tan"],["ate","eat","tea"]])
        assert sorted_res1 == sorted_exp1, f"Test 1 failed. Got {res1}"
        res2 = sol.groupAnagrams([""])
        assert res2 == [[""]], f"Test 2 failed. Got {res2}"
        res3 = sol.groupAnagrams(["a"])
        assert res3 == [["a"]], f"Test 3 failed. Got {res3}"
        print("ALL_TESTS_PASSED")
    except AssertionError as ae:
        print(f"TEST_FAILED: {ae}")
    except Exception as e:
        print(f"ERROR: {e}")
"""
    },
    "trapping-rain-water": {
        "id": "trapping-rain-water",
        "title": "42. Trapping Rain Water",
        "difficulty": "Hard",
        "description": """<p>Given <code>n</code> non-negative integers representing an elevation map where the width of each bar is <code>1</code>, compute how much water it can trap after raining.</p>

<h3 class="text-lg font-semibold mt-4 mb-2">Example 1:</h3>
<pre class="bg-gray-800 text-gray-100 p-3 rounded-lg font-mono text-sm mb-4">
<strong>Input:</strong> height = [0,1,0,2,1,0,1,3,2,1,2,1]
<strong>Output:</strong> 6
<strong>Explanation:</strong> The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water are trapped.
</pre>

<h3 class="text-lg font-semibold mt-4 mb-2">Example 2:</h3>
<pre class="bg-gray-800 text-gray-100 p-3 rounded-lg font-mono text-sm mb-4">
<strong>Input:</strong> height = [4,2,0,3,2,5]
<strong>Output:</strong> 9
</pre>

<h3 class="text-lg font-semibold mt-4 mb-2">Constraints:</h3>
<ul class="list-disc pl-5 space-y-1 text-gray-300">
  <li><code>n == height.length</code></li>
  <li><code>1 &lt;= n &lt;= 2 * 10<sup>4</sup></code></li>
  <li><code>0 &lt;= height[i] &lt;= 10<sup>5</sup></code></li>
</ul>""",
        "starter_code": """class Solution:
    def trap(self, height: list[int]) -> int:
        pass
""",
        "solution_code": """class Solution:
    def trap(self, height: list[int]) -> int:
        left, right = 0, len(height) - 1
        left_max = right_max = water = 0
        while left < right:
            if height[left] < height[right]:
                if height[left] >= left_max:
                    left_max = height[left]
                else:
                    water += left_max - height[left]
                left += 1
            else:
                if height[right] >= right_max:
                    right_max = height[right]
                else:
                    water += right_max - height[right]
                right -= 1
        return water
""",
        "test_code": """
if __name__ == "__main__":
    try:
        sol = Solution()
        res1 = sol.trap([0,1,0,2,1,0,1,3,2,1,2,1])
        assert res1 == 6, f"Test 1 failed. Expected 6, got {res1}"
        res2 = sol.trap([4,2,0,3,2,5])
        assert res2 == 9, f"Test 2 failed. Expected 9, got {res2}"
        res3 = sol.trap([1,0,1])
        assert res3 == 1, f"Test 3 failed. Expected 1, got {res3}"
        res4 = sol.trap([5])
        assert res4 == 0, f"Test 4 failed. Expected 0 for single bar, got {res4}"
        res5 = sol.trap([0,0,0])
        assert res5 == 0, f"Test 5 failed. Expected 0, got {res5}"
        print("ALL_TESTS_PASSED")
    except AssertionError as ae:
        print(f"TEST_FAILED: {ae}")
    except Exception as e:
        print(f"ERROR: {e}")
"""
    },
    "first-missing-positive": {
        "id": "first-missing-positive",
        "title": "41. First Missing Positive",
        "difficulty": "Hard",
        "description": """<p>Given an unsorted integer array <code>nums</code>, return the <strong>smallest positive integer</strong> that is <strong>not present</strong> in <code>nums</code>.</p>
<p>You must implement an algorithm that runs in <code>O(n)</code> time and uses <code>O(1)</code> auxiliary space.</p>

<h3 class="text-lg font-semibold mt-4 mb-2">Example 1:</h3>
<pre class="bg-gray-800 text-gray-100 p-3 rounded-lg font-mono text-sm mb-4">
<strong>Input:</strong> nums = [1,2,0]
<strong>Output:</strong> 3
<strong>Explanation:</strong> The numbers in the range [1,2] are all in the array.
</pre>

<h3 class="text-lg font-semibold mt-4 mb-2">Example 2:</h3>
<pre class="bg-gray-800 text-gray-100 p-3 rounded-lg font-mono text-sm mb-4">
<strong>Input:</strong> nums = [3,4,-1,1]
<strong>Output:</strong> 2
<strong>Explanation:</strong> 1 is in the array but 2 is missing.
</pre>

<h3 class="text-lg font-semibold mt-4 mb-2">Example 3:</h3>
<pre class="bg-gray-800 text-gray-100 p-3 rounded-lg font-mono text-sm mb-4">
<strong>Input:</strong> nums = [7,8,9,11,12]
<strong>Output:</strong> 1
<strong>Explanation:</strong> The smallest positive integer 1 is missing.
</pre>

<h3 class="text-lg font-semibold mt-4 mb-2">Constraints:</h3>
<ul class="list-disc pl-5 space-y-1 text-gray-300">
  <li><code>1 &lt;= nums.length &lt;= 10<sup>5</sup></code></li>
  <li><code>-2<sup>31</sup> &lt;= nums[i] &lt;= 2<sup>31</sup> - 1</code></li>
</ul>""",
        "starter_code": """class Solution:
    def firstMissingPositive(self, nums: list[int]) -> int:
        pass
""",
        "solution_code": """class Solution:
    def firstMissingPositive(self, nums: list[int]) -> int:
        n = len(nums)
        for i in range(n):
            while 1 <= nums[i] <= n and nums[nums[i] - 1] != nums[i]:
                nums[nums[i] - 1], nums[i] = nums[i], nums[nums[i] - 1]
        for i in range(n):
            if nums[i] != i + 1:
                return i + 1
        return n + 1
""",
        "test_code": """
if __name__ == "__main__":
    try:
        sol = Solution()
        res1 = sol.firstMissingPositive([1,2,0])
        assert res1 == 3, f"Test 1 failed. Expected 3, got {res1}"
        res2 = sol.firstMissingPositive([3,4,-1,1])
        assert res2 == 2, f"Test 2 failed. Expected 2, got {res2}"
        res3 = sol.firstMissingPositive([7,8,9,11,12])
        assert res3 == 1, f"Test 3 failed. Expected 1, got {res3}"
        res4 = sol.firstMissingPositive([1,2,3])
        assert res4 == 4, f"Test 4 failed. Expected 4, got {res4}"
        res5 = sol.firstMissingPositive([-1,-2])
        assert res5 == 1, f"Test 5 failed. Expected 1 for all negatives, got {res5}"
        print("ALL_TESTS_PASSED")
    except AssertionError as ae:
        print(f"TEST_FAILED: {ae}")
    except Exception as e:
        print(f"ERROR: {e}")
"""
    },
    "median-two-arrays": {
        "id": "median-two-arrays",
        "title": "4. Median of Two Sorted Arrays",
        "difficulty": "Hard",
        "description": """<p>Given two sorted arrays <code>nums1</code> and <code>nums2</code> of size <code>m</code> and <code>n</code> respectively, return <strong>the median</strong> of the two sorted arrays.</p>
<p>The overall run time complexity should be <code>O(log (m+n))</code>.</p>

<h3 class="text-lg font-semibold mt-4 mb-2">Example 1:</h3>
<pre class="bg-gray-800 text-gray-100 p-3 rounded-lg font-mono text-sm mb-4">
<strong>Input:</strong> nums1 = [1,3], nums2 = [2]
<strong>Output:</strong> 2.00000
<strong>Explanation:</strong> Merged array = [1,2,3] and median is 2.
</pre>

<h3 class="text-lg font-semibold mt-4 mb-2">Example 2:</h3>
<pre class="bg-gray-800 text-gray-100 p-3 rounded-lg font-mono text-sm mb-4">
<strong>Input:</strong> nums1 = [1,2], nums2 = [3,4]
<strong>Output:</strong> 2.50000
<strong>Explanation:</strong> Merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.
</pre>

<h3 class="text-lg font-semibold mt-4 mb-2">Constraints:</h3>
<ul class="list-disc pl-5 space-y-1 text-gray-300">
  <li><code>0 &lt;= m, n &lt;= 1000</code></li>
  <li><code>1 &lt;= m + n &lt;= 2000</code></li>
  <li><code>-10<sup>6</sup> &lt;= nums1[i], nums2[i] &lt;= 10<sup>6</sup></code></li>
</ul>""",
        "starter_code": """class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        pass
""",
        "solution_code": """class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        m, n = len(nums1), len(nums2)
        total = m + n
        half = total // 2
        left, right = 0, m
        while left <= right:
            i = (left + right) // 2
            j = half - i
            left1 = nums1[i - 1] if i > 0 else float("-inf")
            right1 = nums1[i] if i < m else float("inf")
            left2 = nums2[j - 1] if j > 0 else float("-inf")
            right2 = nums2[j] if j < n else float("inf")
            if left1 <= right2 and left2 <= right1:
                if total % 2:
                    return min(right1, right2)
                return (max(left1, left2) + min(right1, right2)) / 2
            elif left1 > right2:
                right = i - 1
            else:
                left = i + 1
""",
        "test_code": """
if __name__ == "__main__":
    try:
        sol = Solution()
        res1 = sol.findMedianSortedArrays([1,3], [2])
        assert abs(res1 - 2.0) < 1e-5, f"Test 1 failed. Expected 2.0, got {res1}"
        res2 = sol.findMedianSortedArrays([1,2], [3,4])
        assert abs(res2 - 2.5) < 1e-5, f"Test 2 failed. Expected 2.5, got {res2}"
        res3 = sol.findMedianSortedArrays([0,0], [0,0])
        assert abs(res3 - 0.0) < 1e-5, f"Test 3 failed. Expected 0.0, got {res3}"
        res4 = sol.findMedianSortedArrays([], [1])
        assert abs(res4 - 1.0) < 1e-5, f"Test 4 failed. Expected 1.0, got {res4}"
        res5 = sol.findMedianSortedArrays([2], [])
        assert abs(res5 - 2.0) < 1e-5, f"Test 5 failed. Expected 2.0, got {res5}"
        print("ALL_TESTS_PASSED")
    except AssertionError as ae:
        print(f"TEST_FAILED: {ae}")
    except Exception as e:
        print(f"ERROR: {e}")
"""
    },
}
