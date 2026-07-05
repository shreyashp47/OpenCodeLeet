CHALLENGE = {
    "id": "longest-valid-parentheses",
    "title": "Longest Valid Parentheses",
    "difficulty": "Hard",
    "description": """<p>Given a string containing just the characters <code>'('</code> and <code>')'</code>, find the length of the longest valid (well-formed) parentheses substring.</p>

<h3 class="text-lg font-semibold mt-4 mb-2">Example 1:</h3>
<pre class="bg-gray-800 text-gray-100 p-3 rounded-lg font-mono text-sm mb-4">
<strong>Input:</strong> s = "(()"
<strong>Output:</strong> 2
<strong>Explanation:</strong> The longest valid parentheses substring is "()".
</pre>

<h3 class="text-lg font-semibold mt-4 mb-2">Example 2:</h3>
<pre class="bg-gray-800 text-gray-100 p-3 rounded-lg font-mono text-sm mb-4">
<strong>Input:</strong> s = ")()())"
<strong>Output:</strong> 4
<strong>Explanation:</strong> The longest valid parentheses substring is "()()".
</pre>

<h3 class="text-lg font-semibold mt-4 mb-2">Example 3:</h3>
<pre class="bg-gray-800 text-gray-100 p-3 rounded-lg font-mono text-sm mb-4">
<strong>Input:</strong> s = ""
<strong>Output:</strong> 0
</pre>

<h3 class="text-lg font-semibold mt-4 mb-2">Constraints:</h3>
<ul class="list-disc pl-5 space-y-1 text-gray-300">
  <li><code>0 &lt;= s.length &lt;= 3 * 10<sup>4</sup></code></li>
  <li><code>s[i]</code> is either <code>'('</code> or <code>')'</code>.</li>
</ul>""",
    "starter_code": {
        "python": """class Solution:
    def longestValidParentheses(self, s: str) -> int:
        pass
""",
        "kotlin": """class Solution {
    fun longestValidParentheses(s: String): Int {
        // Write your code here
        return 0
    }
}
""",
    },
    "solution_code": {
        "python": """class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stack = [-1]
        max_len = 0
        for i, ch in enumerate(s):
            if ch == '(':
                stack.append(i)
            else:
                stack.pop()
                if not stack:
                    stack.append(i)
                else:
                    max_len = max(max_len, i - stack[-1])
        return max_len
""",
        "kotlin": """class Solution {
    fun longestValidParentheses(s: String): Int {
        val stack = ArrayDeque<Int>()
        stack.addLast(-1)
        var maxLen = 0
        for ((i, ch) in s.withIndex()) {
            if (ch == '(') {
                stack.addLast(i)
            } else {
                stack.removeLast()
                if (stack.isEmpty()) {
                    stack.addLast(i)
                } else {
                    maxLen = maxOf(maxLen, i - stack.last())
                }
            }
        }
        return maxLen
    }
}
""",
    },
    "test_code": {
        "python": """
if __name__ == "__main__":
    try:
        sol = Solution()
        res1 = sol.longestValidParentheses("(()")
        assert res1 is not None, "Test 1 failed. Returned None."
        assert res1 == 2, f"Test 1 failed. Expected 2, got {res1}"
        res2 = sol.longestValidParentheses(")()())")
        assert res2 is not None, "Test 2 failed. Returned None."
        assert res2 == 4, f"Test 2 failed. Expected 4, got {res2}"
        res3 = sol.longestValidParentheses("")
        assert res3 is not None, "Test 3 failed. Returned None."
        assert res3 == 0, f"Test 3 failed. Expected 0, got {res3}"
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
        val res1 = sol.longestValidParentheses("(()")
        require(res1 == 2) { "Test 1 failed. Expected 2, got $res1" }
        val res2 = sol.longestValidParentheses(")()())")
        require(res2 == 4) { "Test 2 failed. Expected 4, got $res2" }
        val res3 = sol.longestValidParentheses("")
        require(res3 == 0) { "Test 3 failed. Expected 0, got $res3" }
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
