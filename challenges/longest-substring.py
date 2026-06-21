CHALLENGE = {
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
""",
}
