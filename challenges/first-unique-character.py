CHALLENGE = {
    "id": "first-unique-character",
    "title": "First Unique Character in a String",
    "difficulty": "Easy",
    "description": """<p>Given a string <code>s</code>, find the <strong>first non-repeating character</strong> in it and return its index. If it does not exist, return <code>-1</code>.</p>

<h3 class="text-lg font-semibold mt-4 mb-2">Example 1:</h3>
<pre class="bg-gray-800 text-gray-100 p-3 rounded-lg font-mono text-sm mb-4">
<strong>Input:</strong> s = "leetcode"
<strong>Output:</strong> 0
</pre>

<h3 class="text-lg font-semibold mt-4 mb-2">Example 2:</h3>
<pre class="bg-gray-800 text-gray-100 p-3 rounded-lg font-mono text-sm mb-4">
<strong>Input:</strong> s = "loveleetcode"
<strong>Output:</strong> 2
</pre>

<h3 class="text-lg font-semibold mt-4 mb-2">Example 3:</h3>
<pre class="bg-gray-800 text-gray-100 p-3 rounded-lg font-mono text-sm mb-4">
<strong>Input:</strong> s = "aabb"
<strong>Output:</strong> -1
</pre>

<h3 class="text-lg font-semibold mt-4 mb-2">Constraints:</h3>
<ul class="list-disc pl-5 space-y-1 text-gray-300">
  <li><code>1 &lt;= s.length &lt;= 10<sup>5</sup></code></li>
  <li><code>s</code> consists of only lowercase English letters.</li>
</ul>""",
    "starter_code": {
        "python": """class Solution:
    def firstUniqChar(self, s: str) -> int:
        pass
""",
        "kotlin": """class Solution {
    fun firstUniqChar(s: String): Int {
        // Write your code here
        return -1
    }
}
""",
    },
    "solution_code": {
        "python": """class Solution:
    def firstUniqChar(self, s: str) -> int:
        count = {}
        for ch in s:
            count[ch] = count.get(ch, 0) + 1
        for i, ch in enumerate(s):
            if count[ch] == 1:
                return i
        return -1
""",
        "kotlin": """class Solution {
    fun firstUniqChar(s: String): Int {
        val count = mutableMapOf<Char, Int>()
        for (ch in s) {
            count[ch] = count.getOrDefault(ch, 0) + 1
        }
        for ((i, ch) in s.withIndex()) {
            if (count[ch] == 1) return i
        }
        return -1
    }
}
""",
    },
    "test_code": {
        "python": """
if __name__ == "__main__":
    try:
        sol = Solution()
        res1 = sol.firstUniqChar("leetcode")
        assert res1 == 0, f"Test 1 failed. Expected 0, got {res1}"
        res2 = sol.firstUniqChar("loveleetcode")
        assert res2 == 2, f"Test 2 failed. Expected 2, got {res2}"
        res3 = sol.firstUniqChar("aabb")
        assert res3 == -1, f"Test 3 failed. Expected -1, got {res3}"
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
        val res1 = sol.firstUniqChar("leetcode")
        require(res1 == 0) { "Test 1 failed. Expected 0, got $res1" }
        val res2 = sol.firstUniqChar("loveleetcode")
        require(res2 == 2) { "Test 2 failed. Expected 2, got $res2" }
        val res3 = sol.firstUniqChar("aabb")
        require(res3 == -1) { "Test 3 failed. Expected -1, got $res3" }
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
