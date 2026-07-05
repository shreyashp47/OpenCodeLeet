CHALLENGE = {
    "id": "minimum-window-substring",
    "title": "Minimum Window Substring",
    "difficulty": "Hard",
    "description": """<p>Given two strings <code>s</code> and <code>t</code> of lengths <code>m</code> and <code>n</code> respectively, return the minimum window substring of <code>s</code> such that every character in <code>t</code> (including duplicates) is included in the window. If there is no such substring, return the empty string <code>""</code>.</p>
<p>The testcases will be generated such that the answer is <strong>unique</strong>.</p>

<h3 class="text-lg font-semibold mt-4 mb-2">Example 1:</h3>
<pre class="bg-gray-800 text-gray-100 p-3 rounded-lg font-mono text-sm mb-4">
<strong>Input:</strong> s = "ADOBECODEBANC", t = "ABC"
<strong>Output:</strong> "BANC"
<strong>Explanation:</strong> The minimum window substring "BANC" includes 'A', 'B', and 'C' from string t.
</pre>

<h3 class="text-lg font-semibold mt-4 mb-2">Example 2:</h3>
<pre class="bg-gray-800 text-gray-100 p-3 rounded-lg font-mono text-sm mb-4">
<strong>Input:</strong> s = "a", t = "a"
<strong>Output:</strong> "a"
</pre>

<h3 class="text-lg font-semibold mt-4 mb-2">Example 3:</h3>
<pre class="bg-gray-800 text-gray-100 p-3 rounded-lg font-mono text-sm mb-4">
<strong>Input:</strong> s = "a", t = "aa"
<strong>Output:</strong> ""
</pre>

<h3 class="text-lg font-semibold mt-4 mb-2">Constraints:</h3>
<ul class="list-disc pl-5 space-y-1 text-gray-300">
  <li><code>m == s.length</code></li>
  <li><code>n == t.length</code></li>
  <li><code>1 &lt;= m, n &lt;= 10<sup>5</sup></code></li>
  <li><code>s</code> and <code>t</code> consist of uppercase and lowercase English letters.</li>
</ul>""",
    "starter_code": {
        "python": """class Solution:
    def minWindow(self, s: str, t: str) -> str:
        pass
""",
        "kotlin": """class Solution {
    fun minWindow(s: String, t: String): String {
        // Write your code here
        return ""
    }
}
""",
    },
    "solution_code": {
        "python": """from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        need = Counter(t)
        have = 0
        need_len = len(need)
        left = 0
        res, res_len = "", float('inf')
        for right, ch in enumerate(s):
            if ch in need:
                need[ch] -= 1
                if need[ch] == 0:
                    have += 1
            while have == need_len:
                if right - left + 1 < res_len:
                    res = s[left:right + 1]
                    res_len = right - left + 1
                if s[left] in need:
                    need[s[left]] += 1
                    if need[s[left]] > 0:
                        have -= 1
                left += 1
        return res
""",
        "kotlin": """class Solution {
    fun minWindow(s: String, t: String): String {
        val need = mutableMapOf<Char, Int>()
        for (c in t) need[c] = need.getOrDefault(c, 0) + 1
        var have = 0
        val needLen = need.size
        var left = 0
        var res = ""
        var resLen = Int.MAX_VALUE
        val window = mutableMapOf<Char, Int>()
        for (right in s.indices) {
            val ch = s[right]
            window[ch] = window.getOrDefault(ch, 0) + 1
            if (need.containsKey(ch) && window[ch] == need[ch]) have++
            while (have == needLen) {
                if (right - left + 1 < resLen) {
                    res = s.substring(left, right + 1)
                    resLen = right - left + 1
                }
                val leftCh = s[left]
                if (need.containsKey(leftCh)) {
                    if (window[leftCh] == need[leftCh]) have--
                    window[leftCh] = window[leftCh]!! - 1
                }
                left++
            }
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
        res1 = sol.minWindow("ADOBECODEBANC", "ABC")
        assert res1 is not None, "Test 1 failed. Returned None."
        assert res1 == "BANC", f"Test 1 failed. Expected 'BANC', got '{res1}'"
        res2 = sol.minWindow("a", "a")
        assert res2 is not None, "Test 2 failed. Returned None."
        assert res2 == "a", f"Test 2 failed. Expected 'a', got '{res2}'"
        res3 = sol.minWindow("a", "aa")
        assert res3 is not None, "Test 3 failed. Returned None."
        assert res3 == "", f"Test 3 failed. Expected '', got '{res3}'"
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
        val res1 = sol.minWindow("ADOBECODEBANC", "ABC")
        require(res1 == "BANC") { "Test 1 failed. Expected 'BANC', got '$res1'" }
        val res2 = sol.minWindow("a", "a")
        require(res2 == "a") { "Test 2 failed. Expected 'a', got '$res2'" }
        val res3 = sol.minWindow("a", "aa")
        require(res3 == "") { "Test 3 failed. Expected '', got '$res3'" }
        println("ALL_TESTS_PASSED")
    } catch (e: IllegalArgumentException) {
        println("TEST_FAILED: \${e.message}")
    } catch (e: Exception) {
        println("ERROR: \${e.message}")
    }
}
""",
    },
}
