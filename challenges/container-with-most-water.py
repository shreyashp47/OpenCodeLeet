CHALLENGE = {
    "id": "container-with-most-water",
    "title": "Container With Most Water",
    "difficulty": "Medium",
    "description": """<p>You are given an integer array <code>height</code> of length <code>n</code>. There are <code>n</code> vertical lines drawn such that the two endpoints of the <code>i<sup>th</sup></code> line are <code>(i, 0)</code> and <code>(i, height[i])</code>.</p>
<p>Find two lines that together with the x-axis form a container, such that the container contains the most water.</p>
<p>Return <em>the maximum amount of water a container can store</em>.</p>

<h3 class="text-lg font-semibold mt-4 mb-2">Example 1:</h3>
<pre class="bg-gray-800 text-gray-100 p-3 rounded-lg font-mono text-sm mb-4">
<strong>Input:</strong> height = [1,8,6,2,5,4,8,3,7]
<strong>Output:</strong> 49
<strong>Explanation:</strong> The max area is between lines at indices 1 and 8 (height 8 and 7, width 7 => 7*7 = 49).
</pre>

<h3 class="text-lg font-semibold mt-4 mb-2">Example 2:</h3>
<pre class="bg-gray-800 text-gray-100 p-3 rounded-lg font-mono text-sm mb-4">
<strong>Input:</strong> height = [1,1]
<strong>Output:</strong> 1
</pre>

<h3 class="text-lg font-semibold mt-4 mb-2">Constraints:</h3>
<ul class="list-disc pl-5 space-y-1 text-gray-300">
  <li><code>n == height.length</code></li>
  <li><code>2 &lt;= n &lt;= 10<sup>5</sup></code></li>
  <li><code>0 &lt;= height[i] &lt;= 10<sup>4</sup></code></li>
</ul>""",
    "starter_code": {
        "python": """class Solution:
    def maxArea(self, height: list[int]) -> int:
        pass
""",
        "kotlin": """class Solution {
    fun maxArea(height: IntArray): Int {
        // Write your code here
        return 0
    }
}
""",
    },
    "solution_code": {
        "python": """class Solution:
    def maxArea(self, height: list[int]) -> int:
        l, r = 0, len(height) - 1
        res = 0
        while l < r:
            area = min(height[l], height[r]) * (r - l)
            res = max(res, area)
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        return res
""",
        "kotlin": """class Solution {
    fun maxArea(height: IntArray): Int {
        var l = 0
        var r = height.size - 1
        var res = 0
        while (l < r) {
            val area = minOf(height[l], height[r]) * (r - l)
            res = maxOf(res, area)
            if (height[l] < height[r]) l++ else r--
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
        res1 = sol.maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7])
        assert res1 is not None, "Test 1 failed. Returned None."
        assert res1 == 49, f"Test 1 failed. Expected 49, got {res1}"
        res2 = sol.maxArea([1, 1])
        assert res2 is not None, "Test 2 failed. Returned None."
        assert res2 == 1, f"Test 2 failed. Expected 1, got {res2}"
        res3 = sol.maxArea([4, 3, 2, 1, 4])
        assert res3 is not None, "Test 3 failed. Returned None."
        assert res3 == 16, f"Test 3 failed. Expected 16, got {res3}"
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
        val res1 = sol.maxArea(intArrayOf(1, 8, 6, 2, 5, 4, 8, 3, 7))
        require(res1 == 49) { "Test 1 failed. Expected 49, got $res1" }
        val res2 = sol.maxArea(intArrayOf(1, 1))
        require(res2 == 1) { "Test 2 failed. Expected 1, got $res2" }
        val res3 = sol.maxArea(intArrayOf(4, 3, 2, 1, 4))
        require(res3 == 16) { "Test 3 failed. Expected 16, got $res3" }
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
