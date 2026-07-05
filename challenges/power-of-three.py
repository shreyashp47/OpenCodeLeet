CHALLENGE = {
    "id": "power-of-three",
    "title": "Power of Three",
    "difficulty": "Easy",
    "description": """<p>Given an integer <code>n</code>, return <em><code>true</code> if it is a power of three. Otherwise, return <code>false</code></em>.</p>
<p>An integer <code>n</code> is a power of three, if there exists an integer <code>x</code> such that <code>n == 3<sup>x</sup></code>.</p>

<h3 class="text-lg font-semibold mt-4 mb-2">Example 1:</h3>
<pre class="bg-gray-800 text-gray-100 p-3 rounded-lg font-mono text-sm mb-4">
<strong>Input:</strong> n = 27
<strong>Output:</strong> true
<strong>Explanation:</strong> 27 = 3<sup>3</sup>
</pre>

<h3 class="text-lg font-semibold mt-4 mb-2">Example 2:</h3>
<pre class="bg-gray-800 text-gray-100 p-3 rounded-lg font-mono text-sm mb-4">
<strong>Input:</strong> n = 0
<strong>Output:</strong> false
<strong>Explanation:</strong> There is no x where 3<sup>x</sup> = 0.
</pre>

<h3 class="text-lg font-semibold mt-4 mb-2">Example 3:</h3>
<pre class="bg-gray-800 text-gray-100 p-3 rounded-lg font-mono text-sm mb-4">
<strong>Input:</strong> n = -1
<strong>Output:</strong> false
<strong>Explanation:</strong> There is no x where 3<sup>x</sup> = -1.
</pre>

<h3 class="text-lg font-semibold mt-4 mb-2">Constraints:</h3>
<ul class="list-disc pl-5 space-y-1 text-gray-300">
  <li><code>-2<sup>31</sup> &lt;= n &lt;= 2<sup>31</sup> - 1</code></li>
</ul>

<h3 class="text-lg font-semibold mt-4 mb-2">Follow up:</h3>
<p class="text-gray-300">Could you solve it without loops/recursion?</p>""",
    "starter_code": {
        "python": """class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        pass
""",
        "kotlin": """class Solution {
    fun isPowerOfThree(n: Int): Boolean {
        // Write your code here
        return false
    }
}
""",
    },
    "solution_code": {
        "python": """class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n < 1:
            return False
        while n % 3 == 0:
            n //= 3
        return n == 1
""",
        "kotlin": """class Solution {
    fun isPowerOfThree(n: Int): Boolean {
        if (n < 1) return false
        var x = n
        while (x % 3 == 0) {
            x /= 3
        }
        return x == 1
    }
}
""",
    },
    "test_code": {
        "python": """
if __name__ == "__main__":
    try:
        sol = Solution()
        assert sol.isPowerOfThree(27) == True, "Test 1 failed. Expected True for 27"
        assert sol.isPowerOfThree(0) == False, "Test 2 failed. Expected False for 0"
        assert sol.isPowerOfThree(-1) == False, "Test 3 failed. Expected False for -1"
        assert sol.isPowerOfThree(1) == True, "Test 4 failed. Expected True for 1"
        assert sol.isPowerOfThree(9) == True, "Test 5 failed. Expected True for 9"
        assert sol.isPowerOfThree(45) == False, "Test 6 failed. Expected False for 45"
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
        require(sol.isPowerOfThree(27) == true) { "Test 1 failed. Expected true for 27" }
        require(sol.isPowerOfThree(0) == false) { "Test 2 failed. Expected false for 0" }
        require(sol.isPowerOfThree(-1) == false) { "Test 3 failed. Expected false for -1" }
        require(sol.isPowerOfThree(1) == true) { "Test 4 failed. Expected true for 1" }
        require(sol.isPowerOfThree(9) == true) { "Test 5 failed. Expected true for 9" }
        require(sol.isPowerOfThree(45) == false) { "Test 6 failed. Expected false for 45" }
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
