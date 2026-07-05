CHALLENGE = {
    "id": "climbing-stairs",
    "title": "Climbing Stairs",
    "difficulty": "Easy",
    "description": """<p>You are climbing a staircase. It takes <code>n</code> steps to reach the top.</p>
<p>Each time you can either climb <code>1</code> or <code>2</code> steps. In how many distinct ways can you climb to the top?</p>

<h3 class="text-lg font-semibold mt-4 mb-2">Example 1:</h3>
<pre class="bg-gray-800 text-gray-100 p-3 rounded-lg font-mono text-sm mb-4">
<strong>Input:</strong> n = 2
<strong>Output:</strong> 2
<strong>Explanation:</strong> There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps
</pre>

<h3 class="text-lg font-semibold mt-4 mb-2">Example 2:</h3>
<pre class="bg-gray-800 text-gray-100 p-3 rounded-lg font-mono text-sm mb-4">
<strong>Input:</strong> n = 3
<strong>Output:</strong> 3
<strong>Explanation:</strong> There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step
</pre>

<h3 class="text-lg font-semibold mt-4 mb-2">Constraints:</h3>
<ul class="list-disc pl-5 space-y-1 text-gray-300">
  <li><code>1 &lt;= n &lt;= 45</code></li>
</ul>""",
    "starter_code": {
        "python": """class Solution:
    def climbStairs(self, n: int) -> int:
        pass
""",
        "kotlin": """class Solution {
    fun climbStairs(n: Int): Int {
        // Write your code here
        return 0
    }
}
""",
    },
    "solution_code": {
        "python": """class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n
        prev2, prev1 = 1, 2
        for _ in range(3, n + 1):
            curr = prev1 + prev2
            prev2, prev1 = prev1, curr
        return prev1
""",
        "kotlin": """class Solution {
    fun climbStairs(n: Int): Int {
        if (n <= 2) return n
        var prev2 = 1
        var prev1 = 2
        for (i in 3..n) {
            val curr = prev1 + prev2
            prev2 = prev1
            prev1 = curr
        }
        return prev1
    }
}
""",
    },
    "test_code": {
        "python": """
if __name__ == "__main__":
    try:
        sol = Solution()
        res1 = sol.climbStairs(2)
        assert res1 == 2, f"Test 1 failed. Expected 2, got {res1}"
        res2 = sol.climbStairs(3)
        assert res2 == 3, f"Test 2 failed. Expected 3, got {res2}"
        res3 = sol.climbStairs(45)
        assert res3 == 1836311903, f"Test 3 failed. Expected 1836311903, got {res3}"
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
        val res1 = sol.climbStairs(2)
        require(res1 == 2) { "Test 1 failed. Expected 2, got $res1" }
        val res2 = sol.climbStairs(3)
        require(res2 == 3) { "Test 2 failed. Expected 3, got $res2" }
        val res3 = sol.climbStairs(45)
        require(res3 == 1836311903) { "Test 3 failed. Expected 1836311903, got $res3" }
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
