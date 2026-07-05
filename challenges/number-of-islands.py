CHALLENGE = {
    "id": "number-of-islands",
    "title": "Number of Islands",
    "difficulty": "Medium",
    "description": """<p>Given an <code>m x n</code> 2D binary grid <code>grid</code> which represents a map of <code>'1'</code>s (land) and <code>'0'</code>s (water), return <em>the number of islands</em>.</p>
<p>An <strong>island</strong> is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.</p>

<h3 class="text-lg font-semibold mt-4 mb-2">Example 1:</h3>
<pre class="bg-gray-800 text-gray-100 p-3 rounded-lg font-mono text-sm mb-4">
<strong>Input:</strong> grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
<strong>Output:</strong> 1
</pre>

<h3 class="text-lg font-semibold mt-4 mb-2">Example 2:</h3>
<pre class="bg-gray-800 text-gray-100 p-3 rounded-lg font-mono text-sm mb-4">
<strong>Input:</strong> grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
<strong>Output:</strong> 3
</pre>

<h3 class="text-lg font-semibold mt-4 mb-2">Constraints:</h3>
<ul class="list-disc pl-5 space-y-1 text-gray-300">
  <li><code>m == grid.length</code></li>
  <li><code>n == grid[i].length</code></li>
  <li><code>1 &lt;= m, n &lt;= 300</code></li>
  <li><code>grid[i][j]</code> is <code>'0'</code> or <code>'1'</code>.</li>
</ul>""",
    "starter_code": {
        "python": """class Solution:
    def numIslands(self, grid: list[list[str]]) -> int:
        pass
""",
        "kotlin": """class Solution {
    fun numIslands(grid: Array<CharArray>): Int {
        // Write your code here
        return 0
    }
}
""",
    },
    "solution_code": {
        "python": """class Solution:
    def numIslands(self, grid: list[list[str]]) -> int:
        if not grid:
            return 0
        rows, cols = len(grid), len(grid[0])
        count = 0

        def dfs(r, c):
            if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] == '0':
                return
            grid[r][c] = '0'
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '1':
                    count += 1
                    dfs(r, c)
        return count
""",
        "kotlin": """class Solution {
    fun numIslands(grid: Array<CharArray>): Int {
        if (grid.isEmpty()) return 0
        val rows = grid.size
        val cols = grid[0].size
        var count = 0

        fun dfs(r: Int, c: Int) {
            if (r < 0 || r >= rows || c < 0 || c >= cols || grid[r][c] == '0') return
            grid[r][c] = '0'
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)
        }

        for (r in 0 until rows) {
            for (c in 0 until cols) {
                if (grid[r][c] == '1') {
                    count++
                    dfs(r, c)
                }
            }
        }
        return count
    }
}
""",
    },
    "test_code": {
        "python": """
if __name__ == "__main__":
    try:
        sol = Solution()
        grid1 = [
            ["1","1","1","1","0"],
            ["1","1","0","1","0"],
            ["1","1","0","0","0"],
            ["0","0","0","0","0"]
        ]
        assert sol.numIslands(grid1) == 1, "Test 1 failed."
        grid2 = [
            ["1","1","0","0","0"],
            ["1","1","0","0","0"],
            ["0","0","1","0","0"],
            ["0","0","0","1","1"]
        ]
        assert sol.numIslands(grid2) == 3, "Test 2 failed."
        grid3 = [["1"]]
        assert sol.numIslands(grid3) == 1, "Test 3 failed."
        grid4 = [["0"]]
        assert sol.numIslands(grid4) == 0, "Test 4 failed."
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
        val grid1 = arrayOf(
            charArrayOf('1','1','1','1','0'),
            charArrayOf('1','1','0','1','0'),
            charArrayOf('1','1','0','0','0'),
            charArrayOf('0','0','0','0','0')
        )
        require(sol.numIslands(grid1) == 1) { "Test 1 failed." }
        val grid2 = arrayOf(
            charArrayOf('1','1','0','0','0'),
            charArrayOf('1','1','0','0','0'),
            charArrayOf('0','0','1','0','0'),
            charArrayOf('0','0','0','1','1')
        )
        require(sol.numIslands(grid2) == 3) { "Test 2 failed." }
        val grid3 = arrayOf(charArrayOf('1'))
        require(sol.numIslands(grid3) == 1) { "Test 3 failed." }
        val grid4 = arrayOf(charArrayOf('0'))
        require(sol.numIslands(grid4) == 0) { "Test 4 failed." }
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
