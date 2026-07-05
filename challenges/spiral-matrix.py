CHALLENGE = {
    "id": "spiral-matrix",
    "title": "Spiral Matrix",
    "difficulty": "Medium",
    "description": """<p>Given an <code>m x n</code> <code>matrix</code>, return <em>all elements of the</em> <code>matrix</code> in spiral order.</p>

<h3 class="text-lg font-semibold mt-4 mb-2">Example 1:</h3>
<pre class="bg-gray-800 text-gray-100 p-3 rounded-lg font-mono text-sm mb-4">
<strong>Input:</strong> matrix = [[1,2,3],[4,5,6],[7,8,9]]
<strong>Output:</strong> [1,2,3,6,9,8,7,4,5]
</pre>

<h3 class="text-lg font-semibold mt-4 mb-2">Example 2:</h3>
<pre class="bg-gray-800 text-gray-100 p-3 rounded-lg font-mono text-sm mb-4">
<strong>Input:</strong> matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
<strong>Output:</strong> [1,2,3,4,8,12,11,10,9,5,6,7]
</pre>

<h3 class="text-lg font-semibold mt-4 mb-2">Constraints:</h3>
<ul class="list-disc pl-5 space-y-1 text-gray-300">
  <li><code>m == matrix.length</code></li>
  <li><code>n == matrix[0].length</code></li>
  <li><code>1 &lt;= m, n &lt;= 10</code></li>
  <li><code>-100 &lt;= matrix[i][j] &lt;= 100</code></li>
</ul>""",
    "starter_code": {
        "python": """class Solution:
    def spiralOrder(self, matrix: list[list[int]]) -> list[int]:
        pass
""",
        "kotlin": """class Solution {
    fun spiralOrder(matrix: Array<IntArray>): List<Int> {
        // Write your code here
        return listOf()
    }
}
""",
    },
    "solution_code": {
        "python": """class Solution:
    def spiralOrder(self, matrix: list[list[int]]) -> list[int]:
        res = []
        top, bottom = 0, len(matrix) - 1
        left, right = 0, len(matrix[0]) - 1
        while top <= bottom and left <= right:
            for j in range(left, right + 1):
                res.append(matrix[top][j])
            top += 1
            for i in range(top, bottom + 1):
                res.append(matrix[i][right])
            right -= 1
            if top <= bottom:
                for j in range(right, left - 1, -1):
                    res.append(matrix[bottom][j])
                bottom -= 1
            if left <= right:
                for i in range(bottom, top - 1, -1):
                    res.append(matrix[i][left])
                left += 1
        return res
""",
        "kotlin": """class Solution {
    fun spiralOrder(matrix: Array<IntArray>): List<Int> {
        val res = mutableListOf<Int>()
        var top = 0
        var bottom = matrix.size - 1
        var left = 0
        var right = matrix[0].size - 1
        while (top <= bottom && left <= right) {
            for (j in left..right) res.add(matrix[top][j])
            top++
            for (i in top..bottom) res.add(matrix[i][right])
            right--
            if (top <= bottom) {
                for (j in right downTo left) res.add(matrix[bottom][j])
                bottom--
            }
            if (left <= right) {
                for (i in bottom downTo top) res.add(matrix[i][left])
                left++
            }
        }
        return res
    }
}
""",
    },
    "test_code": {
        "python": """
if __name__ == "__main__":
    try:
        sol = Solution()
        res1 = sol.spiralOrder([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
        assert res1 is not None, "Test 1 failed. Returned None."
        assert res1 == [1, 2, 3, 6, 9, 8, 7, 4, 5], f"Test 1 failed. Got {res1}"
        res2 = sol.spiralOrder([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
        assert res2 is not None, "Test 2 failed. Returned None."
        assert res2 == [1, 2, 3, 4, 8, 12, 11, 10, 9, 5, 6, 7], f"Test 2 failed. Got {res2}"
        res3 = sol.spiralOrder([[1]])
        assert res3 is not None, "Test 3 failed. Returned None."
        assert res3 == [1], f"Test 3 failed. Got {res3}"
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
        val res1 = sol.spiralOrder(arrayOf(intArrayOf(1, 2, 3), intArrayOf(4, 5, 6), intArrayOf(7, 8, 9)))
        require(res1 == listOf(1, 2, 3, 6, 9, 8, 7, 4, 5)) { "Test 1 failed. Got $res1" }
        val res2 = sol.spiralOrder(arrayOf(intArrayOf(1, 2, 3, 4), intArrayOf(5, 6, 7, 8), intArrayOf(9, 10, 11, 12)))
        require(res2 == listOf(1, 2, 3, 4, 8, 12, 11, 10, 9, 5, 6, 7)) { "Test 2 failed. Got $res2" }
        val res3 = sol.spiralOrder(arrayOf(intArrayOf(1)))
        require(res3 == listOf(1)) { "Test 3 failed. Got $res3" }
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
