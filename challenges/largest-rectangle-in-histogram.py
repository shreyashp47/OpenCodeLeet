CHALLENGE = {
    "id": "largest-rectangle-in-histogram",
    "title": "Largest Rectangle in Histogram",
    "difficulty": "Hard",
    "description": """<p>Given an array of integers <code>heights</code> representing the histogram's bar height where the width of each bar is <code>1</code>, return the area of the largest rectangle in the histogram.</p>

<h3 class="text-lg font-semibold mt-4 mb-2">Example 1:</h3>
<pre class="bg-gray-800 text-gray-100 p-3 rounded-lg font-mono text-sm mb-4">
<strong>Input:</strong> heights = [2,1,5,6,2,3]
<strong>Output:</strong> 10
<strong>Explanation:</strong> The largest rectangle is formed by bars of heights [5,6] with width 2, area = 5*2 = 10.
</pre>

<h3 class="text-lg font-semibold mt-4 mb-2">Example 2:</h3>
<pre class="bg-gray-800 text-gray-100 p-3 rounded-lg font-mono text-sm mb-4">
<strong>Input:</strong> heights = [2,4]
<strong>Output:</strong> 4
</pre>

<h3 class="text-lg font-semibold mt-4 mb-2">Constraints:</h3>
<ul class="list-disc pl-5 space-y-1 text-gray-300">
  <li><code>1 &lt;= heights.length &lt;= 10<sup>5</sup></code></li>
  <li><code>0 &lt;= heights[i] &lt;= 10<sup>4</sup></code></li>
</ul>""",
    "starter_code": {
        "python": """class Solution:
    def largestRectangleArea(self, heights: list[int]) -> int:
        pass
""",
        "kotlin": """class Solution {
    fun largestRectangleArea(heights: IntArray): Int {
        // Write your code here
        return 0
    }
}
""",
    },
    "solution_code": {
        "python": """class Solution:
    def largestRectangleArea(self, heights: list[int]) -> int:
        stack = []
        max_area = 0
        heights.append(0)
        for i, h in enumerate(heights):
            while stack and heights[stack[-1]] > h:
                height = heights[stack.pop()]
                width = i if not stack else i - stack[-1] - 1
                max_area = max(max_area, height * width)
            stack.append(i)
        return max_area
""",
        "kotlin": """class Solution {
    fun largestRectangleArea(heights: IntArray): Int {
        val stack = ArrayDeque<Int>()
        var maxArea = 0
        val hs = heights + intArrayOf(0)
        for (i in hs.indices) {
            while (stack.isNotEmpty() && hs[stack.last()] > hs[i]) {
                val h = hs[stack.removeLast()]
                val w = if (stack.isEmpty()) i else i - stack.last() - 1
                maxArea = maxOf(maxArea, h * w)
            }
            stack.addLast(i)
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
        res1 = sol.largestRectangleArea([2,1,5,6,2,3])
        assert res1 is not None, "Test 1 failed. Returned None."
        assert res1 == 10, f"Test 1 failed. Expected 10, got {res1}"
        res2 = sol.largestRectangleArea([2,4])
        assert res2 is not None, "Test 2 failed. Returned None."
        assert res2 == 4, f"Test 2 failed. Expected 4, got {res2}"
        res3 = sol.largestRectangleArea([1])
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
        val res1 = sol.largestRectangleArea(intArrayOf(2,1,5,6,2,3))
        require(res1 == 10) { "Test 1 failed. Expected 10, got $res1" }
        val res2 = sol.largestRectangleArea(intArrayOf(2,4))
        require(res2 == 4) { "Test 2 failed. Expected 4, got $res2" }
        val res3 = sol.largestRectangleArea(intArrayOf(1))
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
