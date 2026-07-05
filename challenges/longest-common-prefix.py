CHALLENGE = {
    "id": "longest-common-prefix",
    "title": "Longest Common Prefix",
    "difficulty": "Easy",
    "description": """<p>Write a function to find the longest common prefix string amongst an array of strings.</p>
<p>If there is no common prefix, return an empty string <code>""</code>.</p>

<h3 class="text-lg font-semibold mt-4 mb-2">Example 1:</h3>
<pre class="bg-gray-800 text-gray-100 p-3 rounded-lg font-mono text-sm mb-4">
<strong>Input:</strong> strs = ["flower","flow","flight"]
<strong>Output:</strong> "fl"
</pre>

<h3 class="text-lg font-semibold mt-4 mb-2">Example 2:</h3>
<pre class="bg-gray-800 text-gray-100 p-3 rounded-lg font-mono text-sm mb-4">
<strong>Input:</strong> strs = ["dog","racecar","car"]
<strong>Output:</strong> ""
<strong>Explanation:</strong> There is no common prefix among the input strings.
</pre>

<h3 class="text-lg font-semibold mt-4 mb-2">Constraints:</h3>
<ul class="list-disc pl-5 space-y-1 text-gray-300">
  <li><code>1 &lt;= strs.length &lt;= 200</code></li>
  <li><code>0 &lt;= strs[i].length &lt;= 200</code></li>
  <li><code>strs[i]</code> consists of only lowercase English letters.</li>
</ul>""",
    "starter_code": {
        "python": """class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        pass
""",
        "kotlin": """class Solution {
    fun longestCommonPrefix(strs: Array<String>): String {
        // Write your code here
        return ""
    }
}
""",
    },
    "solution_code": {
        "python": """class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        if not strs:
            return ""
        prefix = strs[0]
        for s in strs[1:]:
            while not s.startswith(prefix):
                prefix = prefix[:-1]
                if not prefix:
                    return ""
        return prefix
""",
        "kotlin": """class Solution {
    fun longestCommonPrefix(strs: Array<String>): String {
        if (strs.isEmpty()) return ""
        var prefix = strs[0]
        for (i in 1 until strs.size) {
            while (!strs[i].startsWith(prefix)) {
                prefix = prefix.dropLast(1)
                if (prefix.isEmpty()) return ""
            }
        }
        return prefix
    }
}
""",
    },
    "test_code": {
        "python": """
if __name__ == "__main__":
    try:
        sol = Solution()
        res1 = sol.longestCommonPrefix(["flower", "flow", "flight"])
        assert res1 == "fl", f"Test 1 failed. Expected 'fl', got '{res1}'"
        res2 = sol.longestCommonPrefix(["dog", "racecar", "car"])
        assert res2 == "", f"Test 2 failed. Expected '', got '{res2}'"
        res3 = sol.longestCommonPrefix(["a"])
        assert res3 == "a", f"Test 3 failed. Expected 'a', got '{res3}'"
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
        val res1 = sol.longestCommonPrefix(arrayOf("flower", "flow", "flight"))
        require(res1 == "fl") { "Test 1 failed. Expected 'fl', got '$res1'" }
        val res2 = sol.longestCommonPrefix(arrayOf("dog", "racecar", "car"))
        require(res2 == "") { "Test 2 failed. Expected '', got '$res2'" }
        val res3 = sol.longestCommonPrefix(arrayOf("a"))
        require(res3 == "a") { "Test 3 failed. Expected 'a', got '$res3'" }
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
