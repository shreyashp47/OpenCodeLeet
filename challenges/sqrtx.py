CHALLENGE = {
    "id": "sqrtx",
    "title": "Sqrt(x)",
    "difficulty": "Easy",
    "description": """<p>Given a non-negative integer <code>x</code>, return <em>the square root of </em><code>x</code><em> rounded down to the nearest integer</em>. The returned integer should be <strong>non-negative</strong> as well.</p>
<p>You <strong>must not use</strong> any built-in exponent function or operator.</p>

<h3 class="text-lg font-semibold mt-4 mb-2">Example 1:</h3>
<pre class="bg-gray-800 text-gray-100 p-3 rounded-lg font-mono text-sm mb-4">
<strong>Input:</strong> x = 4
<strong>Output:</strong> 2
<strong>Explanation:</strong> The square root of 4 is 2, so we return 2.
</pre>

<h3 class="text-lg font-semibold mt-4 mb-2">Example 2:</h3>
<pre class="bg-gray-800 text-gray-100 p-3 rounded-lg font-mono text-sm mb-4">
<strong>Input:</strong> x = 8
<strong>Output:</strong> 2
<strong>Explanation:</strong> The square root of 8 is 2.828..., and since we round it down, we return 2.
</pre>

<h3 class="text-lg font-semibold mt-4 mb-2">Constraints:</h3>
<ul class="list-disc pl-5 space-y-1 text-gray-300">
  <li><code>0 &lt;= x &lt;= 2<sup>31</sup> - 1</code></li>
</ul>""",
    "starter_code": {
        "python": """class Solution:
    def mySqrt(self, x: int) -> int:
        pass
""",
        "kotlin": """class Solution {
    fun mySqrt(x: Int): Int {
        // Write your code here
        return 0
    }
}
""",
    },
    "solution_code": {
        "python": """class Solution:
    def mySqrt(self, x: int) -> int:
        if x < 2:
            return x
        left, right = 1, x // 2
        while left <= right:
            mid = left + (right - left) // 2
            if mid * mid == x:
                return mid
            elif mid * mid < x:
                left = mid + 1
            else:
                right = mid - 1
        return right
""",
        "kotlin": """class Solution {
    fun mySqrt(x: Int): Int {
        if (x < 2) return x
        var left = 1
        var right = x / 2
        while (left <= right) {
            val mid = left + (right - left) / 2
            val sq = mid.toLong() * mid
            when {
                sq == x.toLong() -> return mid
                sq < x -> left = mid + 1
                else -> right = mid - 1
            }
        }
        return right
    }
}
""",
    },
    "test_code": {
        "python": """
if __name__ == "__main__":
    try:
        sol = Solution()
        res1 = sol.mySqrt(4)
        assert res1 is not None, "Test 1 failed. Returned None."
        assert res1 == 2, f"Test 1 failed. Expected 2, got {res1}"
        res2 = sol.mySqrt(8)
        assert res2 is not None, "Test 2 failed. Returned None."
        assert res2 == 2, f"Test 2 failed. Expected 2, got {res2}"
        res3 = sol.mySqrt(0)
        assert res3 is not None, "Test 3 failed. Returned None."
        assert res3 == 0, f"Test 3 failed. Expected 0, got {res3}"
        res4 = sol.mySqrt(1)
        assert res4 is not None, "Test 4 failed. Returned None."
        assert res4 == 1, f"Test 4 failed. Expected 1, got {res4}"
        res5 = sol.mySqrt(16)
        assert res5 is not None, "Test 5 failed. Returned None."
        assert res5 == 4, f"Test 5 failed. Expected 4, got {res5}"
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
        require(sol.mySqrt(4) == 2) { "Test 1 failed. Expected 2, got ${sol.mySqrt(4)}" }
        require(sol.mySqrt(8) == 2) { "Test 2 failed. Expected 2, got ${sol.mySqrt(8)}" }
        require(sol.mySqrt(0) == 0) { "Test 3 failed. Expected 0, got ${sol.mySqrt(0)}" }
        require(sol.mySqrt(1) == 1) { "Test 4 failed. Expected 1, got ${sol.mySqrt(1)}" }
        require(sol.mySqrt(16) == 4) { "Test 5 failed. Expected 4, got ${sol.mySqrt(16)}" }
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
