CHALLENGE = {
    "id": "unique-paths",
    "title": "Unique Paths",
    "difficulty": "Medium",
    "description": """<p>There is a robot on an <code>m x n</code> grid. The robot is initially located at the <strong>top-left corner</strong> (i.e., <code>grid[0][0]</code>). The robot tries to move to the <strong>bottom-right corner</strong> (i.e., <code>grid[m - 1][n - 1]</code>). The robot can only move either down or right at any point in time.</p>
<p>Given the two integers <code>m</code> and <code>n</code>, return <em>the number of possible unique paths that the robot can take to reach the bottom-right corner</em>.</p>

<h3 class="text-lg font-semibold mt-4 mb-2">Example 1:</h3>
<pre class="bg-gray-800 text-gray-100 p-3 rounded-lg font-mono text-sm mb-4">
<strong>Input:</strong> m = 3, n = 7
<strong>Output:</strong> 28
</pre>

<h3 class="text-lg font-semibold mt-4 mb-2">Example 2:</h3>
<pre class="bg-gray-800 text-gray-100 p-3 rounded-lg font-mono text-sm mb-4">
<strong>Input:</strong> m = 3, n = 2
<strong>Output:</strong> 3
<strong>Explanation:</strong> From the top-left corner, there are a total of 3 ways to reach the bottom-right corner:
1. Right -> Down -> Down
2. Down -> Down -> Right
3. Down -> Right -> Down
</pre>

<h3 class="text-lg font-semibold mt-4 mb-2">Constraints:</h3>
<ul class="list-disc pl-5 space-y-1 text-gray-300">
  <li><code>1 &lt;= m, n &lt;= 100</code></li>
</ul>""",
    "starter_code": {
        "python": """class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        pass
""",
        "kotlin": """class Solution {
    fun uniquePaths(m: Int, n: Int): Int {
        // Write your code here
        return 0
    }
}
""",
    },
    "solution_code": {
        "python": """class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        row = [1] * n
        for _ in range(m - 1):
            new_row = [1] * n
            for j in range(n - 2, -1, -1):
                new_row[j] = new_row[j + 1] + row[j]
            row = new_row
        return row[0]
""",
        "kotlin": """class Solution {
    fun uniquePaths(m: Int, n: Int): Int {
        var row = IntArray(n) { 1 }
        for (i in 1 until m) {
            val newRow = IntArray(n) { 1 }
            for (j in n - 2 downTo 0) {
                newRow[j] = newRow[j + 1] + row[j]
            }
            row = newRow
        }
        return row[0]
    }
}
""",
    },
    "test_code": {
        "python": """
if __name__ == "__main__":
    try:
        sol = Solution()
        res1 = sol.uniquePaths(3, 7)
        assert res1 is not None, "Test 1 failed. Returned None."
        assert res1 == 28, f"Test 1 failed. Expected 28, got {res1}"
        res2 = sol.uniquePaths(3, 2)
        assert res2 is not None, "Test 2 failed. Returned None."
        assert res2 == 3, f"Test 2 failed. Expected 3, got {res2}"
        res3 = sol.uniquePaths(1, 1)
        assert res3 is not None, "Test 3 failed. Returned None."
        assert res3 == 1, f"Test 3 failed. Expected 1, got {res3}"
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
        val res1 = sol.uniquePaths(3, 7)
        require(res1 == 28) { "Test 1 failed. Expected 28, got $res1" }
        val res2 = sol.uniquePaths(3, 2)
        require(res2 == 3) { "Test 2 failed. Expected 3, got $res2" }
        val res3 = sol.uniquePaths(1, 1)
        require(res3 == 1) { "Test 3 failed. Expected 1, got $res3" }
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
