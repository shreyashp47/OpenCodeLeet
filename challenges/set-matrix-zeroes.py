CHALLENGE = {
    "id": "set-matrix-zeroes",
    "title": "Set Matrix Zeroes",
    "difficulty": "Medium",
    "description": """<p>Given an <code>m x n</code> integer matrix <code>matrix</code>, if an element is <code>0</code>, set its entire row and column to <code>0</code>'s.</p>
<p>You must do it <strong>in place</strong>.</p>

<h3 class="text-lg font-semibold mt-4 mb-2">Example 1:</h3>
<pre class="bg-gray-800 text-gray-100 p-3 rounded-lg font-mono text-sm mb-4">
<strong>Input:</strong> matrix = [[1,1,1],[1,0,1],[1,1,1]]
<strong>Output:</strong> [[1,0,1],[0,0,0],[1,0,1]]
</pre>

<h3 class="text-lg font-semibold mt-4 mb-2">Example 2:</h3>
<pre class="bg-gray-800 text-gray-100 p-3 rounded-lg font-mono text-sm mb-4">
<strong>Input:</strong> matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
<strong>Output:</strong> [[0,0,0,0],[0,4,5,0],[0,3,1,0]]
</pre>

<h3 class="text-lg font-semibold mt-4 mb-2">Constraints:</h3>
<ul class="list-disc pl-5 space-y-1 text-gray-300">
  <li><code>m == matrix.length</code></li>
  <li><code>n == matrix[0].length</code></li>
  <li><code>1 &lt;= m, n &lt;= 200</code></li>
  <li><code>-2<sup>31</sup> &lt;= matrix[i][j] &lt;= 2<sup>31</sup> - 1</code></li>
</ul>""",
    "starter_code": {
        "python": """class Solution:
    def setZeroes(self, matrix: list[list[int]]) -> None:
        pass
""",
        "kotlin": """class Solution {
    fun setZeroes(matrix: Array<IntArray>): Unit {
        // Write your code here
    }
}
""",
    },
    "solution_code": {
        "python": """class Solution:
    def setZeroes(self, matrix: list[list[int]]) -> None:
        m, n = len(matrix), len(matrix[0])
        first_row = False
        first_col = False
        for j in range(n):
            if matrix[0][j] == 0:
                first_row = True
                break
        for i in range(m):
            if matrix[i][0] == 0:
                first_col = True
                break
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0
        if first_row:
            for j in range(n):
                matrix[0][j] = 0
        if first_col:
            for i in range(m):
                matrix[i][0] = 0
""",
        "kotlin": """class Solution {
    fun setZeroes(matrix: Array<IntArray>): Unit {
        val m = matrix.size
        val n = matrix[0].size
        var firstRow = false
        var firstCol = false
        for (j in 0 until n) {
            if (matrix[0][j] == 0) { firstRow = true; break }
        }
        for (i in 0 until m) {
            if (matrix[i][0] == 0) { firstCol = true; break }
        }
        for (i in 1 until m) {
            for (j in 1 until n) {
                if (matrix[i][j] == 0) {
                    matrix[i][0] = 0
                    matrix[0][j] = 0
                }
            }
        }
        for (i in 1 until m) {
            for (j in 1 until n) {
                if (matrix[i][0] == 0 || matrix[0][j] == 0) {
                    matrix[i][j] = 0
                }
            }
        }
        if (firstRow) for (j in 0 until n) matrix[0][j] = 0
        if (firstCol) for (i in 0 until m) matrix[i][0] = 0
    }
}
""",
    },
    "test_code": {
        "python": """
if __name__ == "__main__":
    try:
        sol = Solution()
        mat1 = [[1, 1, 1], [1, 0, 1], [1, 1, 1]]
        sol.setZeroes(mat1)
        assert mat1 == [[1, 0, 1], [0, 0, 0], [1, 0, 1]], f"Test 1 failed. Got {mat1}"
        mat2 = [[0, 1, 2, 0], [3, 4, 5, 2], [1, 3, 1, 5]]
        sol.setZeroes(mat2)
        assert mat2 == [[0, 0, 0, 0], [0, 4, 5, 0], [0, 3, 1, 0]], f"Test 2 failed. Got {mat2}"
        mat3 = [[1, 0], [2, 3]]
        sol.setZeroes(mat3)
        assert mat3 == [[0, 0], [2, 0]], f"Test 3 failed. Got {mat3}"
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
        val mat1 = arrayOf(intArrayOf(1, 1, 1), intArrayOf(1, 0, 1), intArrayOf(1, 1, 1))
        sol.setZeroes(mat1)
        require(mat1 contentDeepEquals arrayOf(intArrayOf(1, 0, 1), intArrayOf(0, 0, 0), intArrayOf(1, 0, 1))) { "Test 1 failed. Got ${mat1.contentDeepToString()}" }
        val mat2 = arrayOf(intArrayOf(0, 1, 2, 0), intArrayOf(3, 4, 5, 2), intArrayOf(1, 3, 1, 5))
        sol.setZeroes(mat2)
        require(mat2 contentDeepEquals arrayOf(intArrayOf(0, 0, 0, 0), intArrayOf(0, 4, 5, 0), intArrayOf(0, 3, 1, 0))) { "Test 2 failed. Got ${mat2.contentDeepToString()}" }
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
