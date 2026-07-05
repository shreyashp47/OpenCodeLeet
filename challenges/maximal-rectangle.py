CHALLENGE = {
    "id": "maximal-rectangle",
    "title": "Maximal Rectangle",
    "difficulty": "Hard",
    "description": """<p>Given a rows x cols binary <code>matrix</code> filled with <code>0</code>'s and <code>1</code>'s, find the largest rectangle containing only <code>1</code>'s and return its area.</p>

<h3 class="text-lg font-semibold mt-4 mb-2">Example 1:</h3>
<pre class="bg-gray-800 text-gray-100 p-3 rounded-lg font-mono text-sm mb-4">
<strong>Input:</strong> matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
<strong>Output:</strong> 6
<strong>Explanation:</strong> The largest rectangle containing only 1's has area 6 (rows 1-2, columns 2-4).
</pre>

<h3 class="text-lg font-semibold mt-4 mb-2">Example 2:</h3>
<pre class="bg-gray-800 text-gray-100 p-3 rounded-lg font-mono text-sm mb-4">
<strong>Input:</strong> matrix = [["0"]]
<strong>Output:</strong> 0
</pre>

<h3 class="text-lg font-semibold mt-4 mb-2">Example 3:</h3>
<pre class="bg-gray-800 text-gray-100 p-3 rounded-lg font-mono text-sm mb-4">
<strong>Input:</strong> matrix = [["1"]]
<strong>Output:</strong> 1
</pre>

<h3 class="text-lg font-semibold mt-4 mb-2">Constraints:</h3>
<ul class="list-disc pl-5 space-y-1 text-gray-300">
  <li><code>rows == matrix.length</code></li>
  <li><code>cols == matrix[i].length</code></li>
  <li><code>1 &lt;= rows, cols &lt;= 200</code></li>
  <li><code>matrix[i][j]</code> is <code>'0'</code> or <code>'1'</code>.</li>
</ul>""",
    "starter_code": {
        "python": """class Solution:
    def maximalRectangle(self, matrix: list[list[str]]) -> int:
        pass
""",
        "kotlin": """class Solution {
    fun maximalRectangle(matrix: Array<CharArray>): Int {
        // Write your code here
        return 0
    }
}
""",
    },
    "solution_code": {
        "python": """class Solution:
    def maximalRectangle(self, matrix: list[list[str]]) -> int:
        if not matrix or not matrix[0]:
            return 0
        heights = [0] * len(matrix[0])
        max_area = 0
        for row in matrix:
            for i, v in enumerate(row):
                heights[i] = heights[i] + 1 if v == '1' else 0
            stack = []
            for i, h in enumerate(heights + [0]):
                while stack and heights[stack[-1]] > h:
                    height = heights[stack.pop()]
                    width = i if not stack else i - stack[-1] - 1
                    max_area = max(max_area, height * width)
                stack.append(i)
        return max_area
""",
        "kotlin": """class Solution {
    fun maximalRectangle(matrix: Array<CharArray>): Int {
        if (matrix.isEmpty() || matrix[0].isEmpty()) return 0
        val cols = matrix[0].size
        val heights = IntArray(cols)
        var maxArea = 0
        for (row in matrix) {
            for (i in 0 until cols) {
                heights[i] = if (row[i] == '1') heights[i] + 1 else 0
            }
            val stack = ArrayDeque<Int>()
            val hs = heights + intArrayOf(0)
            for (i in hs.indices) {
                while (stack.isNotEmpty() && hs[stack.last()] > hs[i]) {
                    val h = hs[stack.removeLast()]
                    val w = if (stack.isEmpty()) i else i - stack.last() - 1
                    maxArea = maxOf(maxArea, h * w)
                }
                stack.addLast(i)
            }
        }
        return maxArea
    }
}
""",
    },
    "test_code": {
        "python": """
if __name__ == "__main__":
    try:
        sol = Solution()
        res1 = sol.maximalRectangle([["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]])
        assert res1 is not None, "Test 1 failed. Returned None."
        assert res1 == 6, f"Test 1 failed. Expected 6, got {res1}"
        res2 = sol.maximalRectangle([["0"]])
        assert res2 is not None, "Test 2 failed. Returned None."
        assert res2 == 0, f"Test 2 failed. Expected 0, got {res2}"
        res3 = sol.maximalRectangle([["1"]])
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
        val res1 = sol.maximalRectangle(arrayOf(
            charArrayOf('1','0','1','0','0'),
            charArrayOf('1','0','1','1','1'),
            charArrayOf('1','1','1','1','1'),
            charArrayOf('1','0','0','1','0')
        ))
        require(res1 == 6) { "Test 1 failed. Expected 6, got $res1" }
        val res2 = sol.maximalRectangle(arrayOf(charArrayOf('0')))
        require(res2 == 0) { "Test 2 failed. Expected 0, got $res2" }
        val res3 = sol.maximalRectangle(arrayOf(charArrayOf('1')))
        require(res3 == 1) { "Test 3 failed. Expected 1, got $res3" }
        println("ALL_TESTS_PASSED")
    } catch (e: IllegalArgumentException) {
        println("TEST_FAILED: \${e.message}")
    } catch (e: Exception) {
        println("ERROR: \${e.message}")
    }
}
""",
    },
}
