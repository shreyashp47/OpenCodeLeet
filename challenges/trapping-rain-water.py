CHALLENGE = {
    "id": "trapping-rain-water",
    "title": "Trapping Rain Water",
    "difficulty": "Hard",
    "description": """<p>Given <code>n</code> non-negative integers representing an elevation map where the width of each bar is <code>1</code>, compute how much water it can trap after raining.</p>

<h3 class="text-lg font-semibold mt-4 mb-2">Example 1:</h3>
<pre class="bg-gray-800 text-gray-100 p-3 rounded-lg font-mono text-sm mb-4">
<strong>Input:</strong> height = [0,1,0,2,1,0,1,3,2,1,2,1]
<strong>Output:</strong> 6
<strong>Explanation:</strong> The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water are trapped.
</pre>

<h3 class="text-lg font-semibold mt-4 mb-2">Example 2:</h3>
<pre class="bg-gray-800 text-gray-100 p-3 rounded-lg font-mono text-sm mb-4">
<strong>Input:</strong> height = [4,2,0,3,2,5]
<strong>Output:</strong> 9
</pre>

<h3 class="text-lg font-semibold mt-4 mb-2">Constraints:</h3>
<ul class="list-disc pl-5 space-y-1 text-gray-300">
  <li><code>n == height.length</code></li>
  <li><code>1 &lt;= n &lt;= 2 * 10<sup>4</sup></code></li>
  <li><code>0 &lt;= height[i] &lt;= 10<sup>5</sup></code></li>
</ul>""",
    "starter_code": {
        "python": """class Solution:
    def trap(self, height: list[int]) -> int:
        pass
""",
        "kotlin": """class Solution {
    fun trap(height: IntArray): Int {
        // Write your code here
        return 0
    }
}
""",
    },
    "solution_code": {
        "python": """class Solution:
    def trap(self, height: list[int]) -> int:
        left, right = 0, len(height) - 1
        left_max = right_max = water = 0
        while left < right:
            if height[left] < height[right]:
                if height[left] >= left_max:
                    left_max = height[left]
                else:
                    water += left_max - height[left]
                left += 1
            else:
                if height[right] >= right_max:
                    right_max = height[right]
                else:
                    water += right_max - height[right]
                right -= 1
        return water
""",
        "kotlin": """class Solution {
    fun trap(height: IntArray): Int {
        var left = 0
        var right = height.size - 1
        var leftMax = 0
        var rightMax = 0
        var water = 0
        while (left < right) {
            if (height[left] < height[right]) {
                if (height[left] >= leftMax) leftMax = height[left]
                else water += leftMax - height[left]
                left++
            } else {
                if (height[right] >= rightMax) rightMax = height[right]
                else water += rightMax - height[right]
                right--
            }
        }
        return water
    }
}
""",
    },
    "test_code": {
        "python": """
if __name__ == "__main__":
    try:
        sol = Solution()
        res1 = sol.trap([0,1,0,2,1,0,1,3,2,1,2,1])
        assert res1 == 6, f"Test 1 failed. Expected 6, got {res1}"
        res2 = sol.trap([4,2,0,3,2,5])
        assert res2 == 9, f"Test 2 failed. Expected 9, got {res2}"
        res3 = sol.trap([1,0,1])
        assert res3 == 1, f"Test 3 failed. Expected 1, got {res3}"
        res4 = sol.trap([5])
        assert res4 == 0, f"Test 4 failed. Expected 0 for single bar, got {res4}"
        res5 = sol.trap([0,0,0])
        assert res5 == 0, f"Test 5 failed. Expected 0, got {res5}"
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
        require(sol.trap(intArrayOf(0,1,0,2,1,0,1,3,2,1,2,1)) == 6) { "Test 1 failed" }
        require(sol.trap(intArrayOf(4,2,0,3,2,5)) == 9) { "Test 2 failed" }
        require(sol.trap(intArrayOf(1,0,1)) == 1) { "Test 3 failed" }
        require(sol.trap(intArrayOf(5)) == 0) { "Test 4 failed" }
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
