CHALLENGE = {
    "id": "palindrome-number",
    "title": "Palindrome Number",
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
    "starter_code": {
        "python": """class Solution:
    def isPalindrome(self, x: int) -> bool:
        pass
""",
        "kotlin": """class Solution {
    fun isPalindrome(x: Int): Boolean {
        // Write your code here
        return false
    }
}
""",
    },
    "solution_code": {
        "python": """class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0 or (x % 10 == 0 and x != 0):
            return False
        reversed_half = 0
        while x > reversed_half:
            reversed_half = reversed_half * 10 + x % 10
            x //= 10
        return x == reversed_half or x == reversed_half // 10
""",
        "kotlin": """class Solution {
    fun isPalindrome(x: Int): Boolean {
        if (x < 0 || (x % 10 == 0 && x != 0)) return false
        var num = x
        var reversed = 0
        while (num > reversed) {
            reversed = reversed * 10 + num % 10
            num /= 10
        }
        return num == reversed || num == reversed / 10
    }
}
""",
    },
    "test_code": {
        "python": """
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
""",
        "kotlin": """
fun main() {
    try {
        val sol = Solution()
        require(sol.isPalindrome(121) == true) { "Test 1 failed. Expected true for 121" }
        require(sol.isPalindrome(-121) == false) { "Test 2 failed. Expected false for -121" }
        require(sol.isPalindrome(10) == false) { "Test 3 failed. Expected false for 10" }
        require(sol.isPalindrome(12321) == true) { "Test 4 failed. Expected true for 12321" }
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
