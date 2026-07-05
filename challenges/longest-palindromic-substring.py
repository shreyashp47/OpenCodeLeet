CHALLENGE = {
    "id": "longest-palindromic-substring",
    "title": "Longest Palindromic Substring",
    "difficulty": "Medium",
    "description": """<p>Given a string <code>s</code>, return <em>the longest palindromic substring</em> in <code>s</code>.</p>

<h3 class="text-lg font-semibold mt-4 mb-2">Example 1:</h3>
<pre class="bg-gray-800 text-gray-100 p-3 rounded-lg font-mono text-sm mb-4">
<strong>Input:</strong> s = "babad"
<strong>Output:</strong> "bab"
<strong>Explanation:</strong> "aba" is also a valid answer.
</pre>

<h3 class="text-lg font-semibold mt-4 mb-2">Example 2:</h3>
<pre class="bg-gray-800 text-gray-100 p-3 rounded-lg font-mono text-sm mb-4">
<strong>Input:</strong> s = "cbbd"
<strong>Output:</strong> "bb"
</pre>

<h3 class="text-lg font-semibold mt-4 mb-2">Constraints:</h3>
<ul class="list-disc pl-5 space-y-1 text-gray-300">
  <li><code>1 &lt;= s.length &lt;= 1000</code></li>
  <li><code>s</code> consist of only digits and English letters.</li>
</ul>""",
    "starter_code": {
        "python": """class Solution:
    def longestPalindrome(self, s: str) -> str:
        pass
""",
        "kotlin": """class Solution {
    fun longestPalindrome(s: String): String {
        // Write your code here
        return ""
    }
}
""",
    },
    "solution_code": {
        "python": """class Solution:
    def longestPalindrome(self, s: str) -> str:
        def expand(l: int, r: int) -> str:
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1
            return s[l + 1:r]

        res = ""
        for i in range(len(s)):
            odd = expand(i, i)
            even = expand(i, i + 1)
            res = max(res, odd, even, key=len)
        return res
""",
        "kotlin": """class Solution {
    fun longestPalindrome(s: String): String {
        fun expand(l: Int, r: Int): String {
            var left = l
            var right = r
            while (left >= 0 && right < s.length && s[left] == s[right]) {
                left--
                right++
            }
            return s.substring(left + 1, right)
        }

        var res = ""
        for (i in s.indices) {
            val odd = expand(i, i)
            val even = expand(i, i + 1)
            res = listOf(res, odd, even).maxBy { it.length }
        }
        return res
    }
}
""",
    },
    "test_code": {
        "python": """
if __name__ == "__main__":
    try:
        sol = Solution()
        res1 = sol.longestPalindrome("babad")
        assert res1 is not None, "Test 1 failed. Returned None."
        assert res1 == "bab" or res1 == "aba", f"Test 1 failed. Expected 'bab' or 'aba', got '{res1}'"
        res2 = sol.longestPalindrome("cbbd")
        assert res2 is not None, "Test 2 failed. Returned None."
        assert res2 == "bb", f"Test 2 failed. Expected 'bb', got '{res2}'"
        res3 = sol.longestPalindrome("a")
        assert res3 is not None, "Test 3 failed. Returned None."
        assert res3 == "a", f"Test 3 failed. Expected 'a', got '{res3}'"
        res4 = sol.longestPalindrome("ac")
        assert res4 is not None, "Test 4 failed. Returned None."
        assert res4 == "a" or res4 == "c", f"Test 4 failed. Expected 'a' or 'c', got '{res4}'"
        print("ALL_TESTS_PASSED")
    except AssertionError as ae:
        print(f"TEST_FAILED: {ae}")
    except Exception as e:
        print(f"ERROR: {e}")
""",
        "kotlin": """
fun main() {
    try {
        val sol = Solution()
        val res1 = sol.longestPalindrome("babad")
        require(res1 == "bab" || res1 == "aba") { "Test 1 failed. Expected 'bab' or 'aba', got '$res1'" }
        val res2 = sol.longestPalindrome("cbbd")
        require(res2 == "bb") { "Test 2 failed. Expected 'bb', got '$res2'" }
        val res3 = sol.longestPalindrome("a")
        require(res3 == "a") { "Test 3 failed. Expected 'a', got '$res3'" }
        val res4 = sol.longestPalindrome("ac")
        require(res4 == "a" || res4 == "c") { "Test 4 failed. Expected 'a' or 'c', got '$res4'" }
        println("ALL_TESTS_PASSED")
    } catch (e: IllegalArgumentException) {
        println("TEST_FAILED: ${e.message}")
    } catch (e: Exception) {
        println("ERROR: ${e.message}")
    }
}
""",
    },
}
