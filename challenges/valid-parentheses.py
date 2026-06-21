CHALLENGE = {
    "id": "valid-parentheses",
    "title": "Valid Parentheses",
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
    "starter_code": {
        "python": """class Solution:
    def isValid(self, s: str) -> bool:
        pass
""",
        "kotlin": """class Solution {
    fun isValid(s: String): Boolean {
        // Write your code here
        return false
    }
}
""",
    },
    "solution_code": {
        "python": """class Solution:
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
        "kotlin": """class Solution {
    fun isValid(s: String): Boolean {
        val pairs = mapOf(')' to '(', '}' to '{', ']' to '[')
        val stack = mutableListOf<Char>()
        for (ch in s) {
            when (ch) {
                in pairs -> {
                    if (stack.isEmpty() || stack.removeLast() != pairs[ch]) return false
                }
                else -> stack.add(ch)
            }
        }
        return stack.isEmpty()
    }
}
""",
    },
    "test_code": {
        "python": """
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
""",
        "kotlin": """
fun main() {
    try {
        val sol = Solution()
        require(sol.isValid("()") == true) { "Test 1 failed. Expected true for '()'" }
        require(sol.isValid("()[]{}") == true) { "Test 2 failed. Expected true for '()[]{}'" }
        require(sol.isValid("(]") == false) { "Test 3 failed. Expected false for '(]'" }
        require(sol.isValid("([)]") == false) { "Test 4 failed. Expected false for '([)]'" }
        require(sol.isValid("{[]}") == true) { "Test 5 failed. Expected true for '{[]}'" }
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
