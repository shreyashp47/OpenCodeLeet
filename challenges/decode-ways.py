CHALLENGE = {
    "id": "decode-ways",
    "title": "Decode Ways",
    "difficulty": "Medium",
    "description": """<p>A message containing letters from <code>A-Z</code> can be <strong>encoded</strong> into numbers using the following mapping:</p>
<pre class="bg-gray-800 text-gray-100 p-3 rounded-lg font-mono text-sm mb-4">
'A' -> "1"
'B' -> "2"
...
'Z' -> "26"
</pre>
<p>To <strong>decode</strong> an encoded message, all the digits must be grouped then mapped back into letters using the reverse of the mapping above (there may be multiple ways). For example, <code>"11106"</code> can be mapped into:</p>
<ul class="list-disc pl-5 space-y-1 text-gray-300">
  <li><code>"AAJF"</code> with the grouping <code>(1 1 10 6)</code></li>
  <li><code>"KJF"</code> with the grouping <code>(11 10 6)</code></li>
</ul>
<p>Note that the grouping <code>(1 11 06)</code> is invalid because <code>"06"</code> cannot be mapped into <code>'F'</code> since <code>"6"</code> is different from <code>"06"</code>.</p>
<p>Given a string <code>s</code> containing only digits, return <em>the <strong>number</strong> of ways to decode it</em>.</p>

<h3 class="text-lg font-semibold mt-4 mb-2">Example 1:</h3>
<pre class="bg-gray-800 text-gray-100 p-3 rounded-lg font-mono text-sm mb-4">
<strong>Input:</strong> s = "12"
<strong>Output:</strong> 2
<strong>Explanation:</strong> "12" could be decoded as "AB" (1 2) or "L" (12).
</pre>

<h3 class="text-lg font-semibold mt-4 mb-2">Example 2:</h3>
<pre class="bg-gray-800 text-gray-100 p-3 rounded-lg font-mono text-sm mb-4">
<strong>Input:</strong> s = "226"
<strong>Output:</strong> 3
<strong>Explanation:</strong> "226" could be decoded as "BZ" (2 26), "VF" (22 6), or "BBF" (2 2 6).
</pre>

<h3 class="text-lg font-semibold mt-4 mb-2">Example 3:</h3>
<pre class="bg-gray-800 text-gray-100 p-3 rounded-lg font-mono text-sm mb-4">
<strong>Input:</strong> s = "06"
<strong>Output:</strong> 0
<strong>Explanation:</strong> "06" cannot be mapped to "F" because of the leading zero.
</pre>

<h3 class="text-lg font-semibold mt-4 mb-2">Constraints:</h3>
<ul class="list-disc pl-5 space-y-1 text-gray-300">
  <li><code>1 &lt;= s.length &lt;= 100</code></li>
  <li><code>s</code> contains only digits and may contain leading zero(s).</li>
</ul>""",
    "starter_code": {
        "python": """class Solution:
    def numDecodings(self, s: str) -> int:
        pass
""",
        "kotlin": """class Solution {
    fun numDecodings(s: String): Int {
        // Write your code here
        return 0
    }
}
""",
    },
    "solution_code": {
        "python": """class Solution:
    def numDecodings(self, s: str) -> int:
        if not s or s[0] == '0':
            return 0
        n = len(s)
        dp = [0] * (n + 1)
        dp[0] = 1
        dp[1] = 1
        for i in range(2, n + 1):
            one = int(s[i - 1:i])
            two = int(s[i - 2:i])
            if 1 <= one <= 9:
                dp[i] += dp[i - 1]
            if 10 <= two <= 26:
                dp[i] += dp[i - 2]
        return dp[n]
""",
        "kotlin": """class Solution {
    fun numDecodings(s: String): Int {
        if (s.isEmpty() || s[0] == '0') return 0
        val n = s.length
        val dp = IntArray(n + 1)
        dp[0] = 1
        dp[1] = 1
        for (i in 2..n) {
            val one = s.substring(i - 1, i).toInt()
            val two = s.substring(i - 2, i).toInt()
            if (one in 1..9) dp[i] += dp[i - 1]
            if (two in 10..26) dp[i] += dp[i - 2]
        }
        return dp[n]
    }
}
""",
    },
    "test_code": {
        "python": """
if __name__ == "__main__":
    try:
        sol = Solution()
        assert sol.numDecodings("12") == 2, "Test 1 failed."
        assert sol.numDecodings("226") == 3, "Test 2 failed."
        assert sol.numDecodings("06") == 0, "Test 3 failed."
        assert sol.numDecodings("10") == 1, "Test 4 failed."
        assert sol.numDecodings("0") == 0, "Test 5 failed."
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
        require(sol.numDecodings("12") == 2) { "Test 1 failed." }
        require(sol.numDecodings("226") == 3) { "Test 2 failed." }
        require(sol.numDecodings("06") == 0) { "Test 3 failed." }
        require(sol.numDecodings("10") == 1) { "Test 4 failed." }
        require(sol.numDecodings("0") == 0) { "Test 5 failed." }
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
