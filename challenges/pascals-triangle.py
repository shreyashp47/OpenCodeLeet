CHALLENGE = {
    "id": "pascals-triangle",
    "title": "Pascals Triangle",
    "difficulty": "Easy",
    "description": """<p>Given an integer <code>numRows</code>, return the first numRows of <strong>Pascal's triangle</strong>.</p>
<p>In <strong>Pascal's triangle</strong>, each number is the sum of the two numbers directly above it.</p>

<h3 class="text-lg font-semibold mt-4 mb-2">Example 1:</h3>
<pre class="bg-gray-800 text-gray-100 p-3 rounded-lg font-mono text-sm mb-4">
<strong>Input:</strong> numRows = 5
<strong>Output:</strong> [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]
</pre>

<h3 class="text-lg font-semibold mt-4 mb-2">Example 2:</h3>
<pre class="bg-gray-800 text-gray-100 p-3 rounded-lg font-mono text-sm mb-4">
<strong>Input:</strong> numRows = 1
<strong>Output:</strong> [[1]]
</pre>

<h3 class="text-lg font-semibold mt-4 mb-2">Constraints:</h3>
<ul class="list-disc pl-5 space-y-1 text-gray-300">
  <li><code>1 &lt;= numRows &lt;= 30</code></li>
</ul>""",
    "starter_code": {
        "python": """class Solution:
    def generate(self, numRows: int) -> list[list[int]]:
        pass
""",
        "kotlin": """class Solution {
    fun generate(numRows: Int): List<List<Int>> {
        // Write your code here
        return listOf()
    }
}
""",
    },
    "solution_code": {
        "python": """class Solution:
    def generate(self, numRows: int) -> list[list[int]]:
        triangle = []
        for i in range(numRows):
            row = [1] * (i + 1)
            for j in range(1, i):
                row[j] = triangle[i - 1][j - 1] + triangle[i - 1][j]
            triangle.append(row)
        return triangle
""",
        "kotlin": """class Solution {
    fun generate(numRows: Int): List<List<Int>> {
        val triangle = mutableListOf<List<Int>>()
        for (i in 0 until numRows) {
            val row = MutableList(i + 1) { 1 }
            for (j in 1 until i) {
                row[j] = triangle[i - 1][j - 1] + triangle[i - 1][j]
            }
            triangle.add(row)
        }
        return triangle
    }
}
""",
    },
    "test_code": {
        "python": """
if __name__ == "__main__":
    try:
        sol = Solution()
        res1 = sol.generate(5)
        assert res1 is not None, "Test 1 failed. Returned None."
        assert res1 == [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]], f"Test 1 failed. Got {res1}"
        res2 = sol.generate(1)
        assert res2 is not None, "Test 2 failed. Returned None."
        assert res2 == [[1]], f"Test 2 failed. Expected [[1]], got {res2}"
        res3 = sol.generate(2)
        assert res3 is not None, "Test 3 failed. Returned None."
        assert res3 == [[1],[1,1]], f"Test 3 failed. Expected [[1],[1,1]], got {res3}"
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
        val res1 = sol.generate(5)
        require(res1.size == 5) { "Test 1 failed. Expected size 5, got ${res1.size}" }
        require(res1[4] == listOf(1, 4, 6, 4, 1)) { "Test 1 failed. Last row expected [1,4,6,4,1], got ${res1[4]}" }
        val res2 = sol.generate(1)
        require(res2 == listOf(listOf(1))) { "Test 2 failed. Expected [[1]], got $res2" }
        val res3 = sol.generate(2)
        require(res3 == listOf(listOf(1), listOf(1, 1))) { "Test 3 failed. Expected [[1],[1,1]], got $res3" }
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
