CHALLENGE = {
    "id": "rotate-image",
    "title": "Rotate Image",
    "difficulty": "Medium",
    "description": """<p>You are given an <code>n x n</code> 2D <code>matrix</code> representing an image, rotate the image by <strong>90</strong> degrees (clockwise).</p>
<p>You have to rotate the image <strong>in place</strong>, which means you have to modify the input 2D matrix directly.</p>

<h3 class="text-lg font-semibold mt-4 mb-2">Example 1:</h3>
<pre class="bg-gray-800 text-gray-100 p-3 rounded-lg font-mono text-sm mb-4">
<strong>Input:</strong> matrix = [[1,2,3],[4,5,6],[7,8,9]]
<strong>Output:</strong> [[7,4,1],[8,5,2],[9,6,3]]
</pre>

<h3 class="text-lg font-semibold mt-4 mb-2">Example 2:</h3>
<pre class="bg-gray-800 text-gray-100 p-3 rounded-lg font-mono text-sm mb-4">
<strong>Input:</strong> matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
<strong>Output:</strong> [[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]]
</pre>

<h3 class="text-lg font-semibold mt-4 mb-2">Constraints:</h3>
<ul class="list-disc pl-5 space-y-1 text-gray-300">
  <li><code>n == matrix.length == matrix[i].length</code></li>
  <li><code>1 &lt;= n &lt;= 20</code></li>
  <li><code>-1000 &lt;= matrix[i][j] &lt;= 1000</code></li>
</ul>""",
    "starter_code": {
        "python": """class Solution:
    def rotate(self, matrix: list[list[int]]) -> None:
        pass
""",
        "kotlin": """class Solution {
    fun rotate(matrix: Array<IntArray>): Unit {
        // Write your code here
    }
}
""",
    },
    "solution_code": {
        "python": """class Solution:
    def rotate(self, matrix: list[list[int]]) -> None:
        n = len(matrix)
        for i in range(n):
            for j in range(i, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        for i in range(n):
            matrix[i].reverse()
""",
        "kotlin": """class Solution {
    fun rotate(matrix: Array<IntArray>): Unit {
        val n = matrix.size
        for (i in 0 until n) {
            for (j in i until n) {
                val temp = matrix[i][j]
                matrix[i][j] = matrix[j][i]
                matrix[j][i] = temp
            }
        }
        for (i in 0 until n) {
            matrix[i].reverse()
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
        mat1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        sol.rotate(mat1)
        assert mat1 == [[7, 4, 1], [8, 5, 2], [9, 6, 3]], f"Test 1 failed. Got {mat1}"
        mat2 = [[5, 1, 9, 11], [2, 4, 8, 10], [13, 3, 6, 7], [15, 14, 12, 16]]
        sol.rotate(mat2)
        assert mat2 == [[15, 13, 2, 5], [14, 3, 4, 1], [12, 6, 8, 9], [16, 7, 10, 11]], f"Test 2 failed. Got {mat2}"
        mat3 = [[1]]
        sol.rotate(mat3)
        assert mat3 == [[1]], f"Test 3 failed. Got {mat3}"
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
        val mat1 = arrayOf(intArrayOf(1, 2, 3), intArrayOf(4, 5, 6), intArrayOf(7, 8, 9))
        sol.rotate(mat1)
        require(mat1 contentDeepEquals arrayOf(intArrayOf(7, 4, 1), intArrayOf(8, 5, 2), intArrayOf(9, 6, 3))) { "Test 1 failed. Got ${mat1.contentDeepToString()}" }
        val mat2 = arrayOf(intArrayOf(5, 1, 9, 11), intArrayOf(2, 4, 8, 10), intArrayOf(13, 3, 6, 7), intArrayOf(15, 14, 12, 16))
        sol.rotate(mat2)
        require(mat2 contentDeepEquals arrayOf(intArrayOf(15, 13, 2, 5), intArrayOf(14, 3, 4, 1), intArrayOf(12, 6, 8, 9), intArrayOf(16, 7, 10, 11))) { "Test 2 failed. Got ${mat2.contentDeepToString()}" }
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
