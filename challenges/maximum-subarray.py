CHALLENGE = {
    "id": "maximum-subarray",
    "title": "Maximum Subarray",
    "difficulty": "Easy",
    "description": """<p>Given an integer array <code>nums</code>, find the <strong>subarray</strong> with the largest sum, and return <em>its sum</em>.</p>

<h3 class="text-lg font-semibold mt-4 mb-2">Example 1:</h3>
<pre class="bg-gray-800 text-gray-100 p-3 rounded-lg font-mono text-sm mb-4">
<strong>Input:</strong> nums = [-2,1,-3,4,-1,2,1,-5,4]
<strong>Output:</strong> 6
<strong>Explanation:</strong> The subarray [4,-1,2,1] has the largest sum 6.
</pre>

<h3 class="text-lg font-semibold mt-4 mb-2">Example 2:</h3>
<pre class="bg-gray-800 text-gray-100 p-3 rounded-lg font-mono text-sm mb-4">
<strong>Input:</strong> nums = [1]
<strong>Output:</strong> 1
</pre>

<h3 class="text-lg font-semibold mt-4 mb-2">Example 3:</h3>
<pre class="bg-gray-800 text-gray-100 p-3 rounded-lg font-mono text-sm mb-4">
<strong>Input:</strong> nums = [5,4,-1,7,8]
<strong>Output:</strong> 23
</pre>

<h3 class="text-lg font-semibold mt-4 mb-2">Constraints:</h3>
<ul class="list-disc pl-5 space-y-1 text-gray-300">
  <li><code>1 &lt;= nums.length &lt;= 10<sup>5</sup></code></li>
  <li><code>-10<sup>4</sup> &lt;= nums[i] &lt;= 10<sup>4</sup></code></li>
</ul>""",
    "starter_code": {
        "python": """class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        pass
""",
        "kotlin": """class Solution {
    fun maxSubArray(nums: IntArray): Int {
        // Write your code here
        return 0
    }
}
""",
    },
    "solution_code": {
        "python": """class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        max_ending_here = max_so_far = nums[0]
        for num in nums[1:]:
            max_ending_here = max(num, max_ending_here + num)
            max_so_far = max(max_so_far, max_ending_here)
        return max_so_far
""",
        "kotlin": """class Solution {
    fun maxSubArray(nums: IntArray): Int {
        var maxEndingHere = nums[0]
        var maxSoFar = nums[0]
        for (i in 1 until nums.size) {
            maxEndingHere = maxOf(nums[i], maxEndingHere + nums[i])
            maxSoFar = maxOf(maxSoFar, maxEndingHere)
        }
        return maxSoFar
    }
}
""",
    },
    "test_code": {
        "python": """
if __name__ == "__main__":
    try:
        sol = Solution()
        res1 = sol.maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4])
        assert res1 == 6, f"Test 1 failed. Expected 6, got {res1}"
        res2 = sol.maxSubArray([1])
        assert res2 == 1, f"Test 2 failed. Expected 1, got {res2}"
        res3 = sol.maxSubArray([5, 4, -1, 7, 8])
        assert res3 == 23, f"Test 3 failed. Expected 23, got {res3}"
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
        val res1 = sol.maxSubArray(intArrayOf(-2, 1, -3, 4, -1, 2, 1, -5, 4))
        require(res1 == 6) { "Test 1 failed. Expected 6, got $res1" }
        val res2 = sol.maxSubArray(intArrayOf(1))
        require(res2 == 1) { "Test 2 failed. Expected 1, got $res2" }
        val res3 = sol.maxSubArray(intArrayOf(5, 4, -1, 7, 8))
        require(res3 == 23) { "Test 3 failed. Expected 23, got $res3" }
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
