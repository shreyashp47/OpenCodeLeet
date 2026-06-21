CHALLENGE = {
    "id": "reverse-string",
    "title": "Reverse String",
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
    "starter_code": {
        "python": """class Solution:
    def reverseString(self, s: list[str]) -> None:
        \"\"\"
        Do not return anything, modify s in-place instead.
        \"\"\"
        pass
""",
        "kotlin": """class Solution {
    fun reverseString(s: CharArray): Unit {
        // Write your code here
    }
}
""",
    },
    "solution_code": {
        "python": """class Solution:
    def reverseString(self, s: list[str]) -> None:
        left, right = 0, len(s) - 1
        while left < right:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1
""",
        "kotlin": """class Solution {
    fun reverseString(s: CharArray) {
        var left = 0
        var right = s.size - 1
        while (left < right) {
            val tmp = s[left]
            s[left] = s[right]
            s[right] = tmp
            left++
            right--
        }
    }
}
""",
    },
    "test_code": {
        "python": """
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
""",
        "kotlin": """
fun main() {
    try {
        val sol = Solution()
        val s1 = charArrayOf('h','e','l','l','o')
        sol.reverseString(s1)
        require(s1 contentEquals charArrayOf('o','l','l','e','h')) { "Test 1 failed. Got ${s1.contentToString()}" }
        val s2 = charArrayOf('H','a','n','n','a','h')
        sol.reverseString(s2)
        require(s2 contentEquals charArrayOf('h','a','n','n','a','H')) { "Test 2 failed. Got ${s2.contentToString()}" }
        val s3 = charArrayOf('a')
        sol.reverseString(s3)
        require(s3 contentEquals charArrayOf('a')) { "Test 3 failed. Got ${s3.contentToString()}" }
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
