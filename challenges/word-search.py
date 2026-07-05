CHALLENGE = {
    "id": "word-search",
    "title": "Word Search",
    "difficulty": "Medium",
    "description": """<p>Given an <code>m x n</code> grid of characters <code>board</code> and a string <code>word</code>, return <code>true</code> <em>if <code>word</code> exists in the grid</em>.</p>
<p>The word can be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once.</p>

<h3 class="text-lg font-semibold mt-4 mb-2">Example 1:</h3>
<pre class="bg-gray-800 text-gray-100 p-3 rounded-lg font-mono text-sm mb-4">
<strong>Input:</strong> board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
<strong>Output:</strong> true
</pre>

<h3 class="text-lg font-semibold mt-4 mb-2">Example 2:</h3>
<pre class="bg-gray-800 text-gray-100 p-3 rounded-lg font-mono text-sm mb-4">
<strong>Input:</strong> board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "SEE"
<strong>Output:</strong> true
</pre>

<h3 class="text-lg font-semibold mt-4 mb-2">Example 3:</h3>
<pre class="bg-gray-800 text-gray-100 p-3 rounded-lg font-mono text-sm mb-4">
<strong>Input:</strong> board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCB"
<strong>Output:</strong> false
</pre>

<h3 class="text-lg font-semibold mt-4 mb-2">Constraints:</h3>
<ul class="list-disc pl-5 space-y-1 text-gray-300">
  <li><code>m == board.length</code></li>
  <li><code>n == board[i].length</code></li>
  <li><code>1 &lt;= m, n &lt;= 6</code></li>
  <li><code>1 &lt;= word.length &lt;= 15</code></li>
  <li><code>board</code> and <code>word</code> consist only of lowercase and uppercase English letters.</li>
</ul>""",
    "starter_code": {
        "python": """class Solution:
    def exist(self, board: list[list[str]], word: str) -> bool:
        pass
""",
        "kotlin": """class Solution {
    fun exist(board: Array<CharArray>, word: String): Boolean {
        // Write your code here
        return false
    }
}
""",
    },
    "solution_code": {
        "python": """class Solution:
    def exist(self, board: list[list[str]], word: str) -> bool:
        rows, cols = len(board), len(board[0])

        def dfs(r, c, i):
            if i == len(word):
                return True
            if r < 0 or r >= rows or c < 0 or c >= cols or board[r][c] != word[i]:
                return False
            tmp, board[r][c] = board[r][c], '#'
            found = (dfs(r + 1, c, i + 1) or
                     dfs(r - 1, c, i + 1) or
                     dfs(r, c + 1, i + 1) or
                     dfs(r, c - 1, i + 1))
            board[r][c] = tmp
            return found

        for r in range(rows):
            for c in range(cols):
                if dfs(r, c, 0):
                    return True
        return False
""",
        "kotlin": """class Solution {
    fun exist(board: Array<CharArray>, word: String): Boolean {
        val rows = board.size
        val cols = board[0].size

        fun dfs(r: Int, c: Int, i: Int): Boolean {
            if (i == word.length) return true
            if (r < 0 || r >= rows || c < 0 || c >= cols || board[r][c] != word[i]) return false
            val tmp = board[r][c]
            board[r][c] = '#'
            val found = dfs(r + 1, c, i + 1) ||
                        dfs(r - 1, c, i + 1) ||
                        dfs(r, c + 1, i + 1) ||
                        dfs(r, c - 1, i + 1)
            board[r][c] = tmp
            return found
        }

        for (r in 0 until rows) {
            for (c in 0 until cols) {
                if (dfs(r, c, 0)) return true
            }
        }
        return false
    }
}
""",
    },
    "test_code": {
        "python": """
if __name__ == "__main__":
    try:
        sol = Solution()
        board1 = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
        assert sol.exist(board1, "ABCCED") == True, "Test 1 failed."
        board2 = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
        assert sol.exist(board2, "SEE") == True, "Test 2 failed."
        board3 = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
        assert sol.exist(board3, "ABCB") == False, "Test 3 failed."
        board4 = [["a"]]
        assert sol.exist(board4, "a") == True, "Test 4 failed."
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
        val board1 = arrayOf(
            charArrayOf('A','B','C','E'),
            charArrayOf('S','F','C','S'),
            charArrayOf('A','D','E','E')
        )
        require(sol.exist(board1, "ABCCED")) { "Test 1 failed." }
        val board2 = arrayOf(
            charArrayOf('A','B','C','E'),
            charArrayOf('S','F','C','S'),
            charArrayOf('A','D','E','E')
        )
        require(sol.exist(board2, "SEE")) { "Test 2 failed." }
        val board3 = arrayOf(
            charArrayOf('A','B','C','E'),
            charArrayOf('S','F','C','S'),
            charArrayOf('A','D','E','E')
        )
        require(!sol.exist(board3, "ABCB")) { "Test 3 failed." }
        val board4 = arrayOf(charArrayOf('a'))
        require(sol.exist(board4, "a")) { "Test 4 failed." }
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
