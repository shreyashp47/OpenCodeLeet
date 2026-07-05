CHALLENGE = {
    "id": "house-robber",
    "title": "House Robber",
    "difficulty": "Medium",
    "description": """<p>You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security systems connected and <b>it will automatically contact the police if two adjacent houses were broken into on the same night</b>.</p>
<p>Given an integer array <code>nums</code> representing the amount of money of each house, return <em>the maximum amount of money you can rob tonight <strong>without alerting the police</strong></em>.</p>

<h3 class="text-lg font-semibold mt-4 mb-2">Example 1:</h3>
<pre class="bg-gray-800 text-gray-100 p-3 rounded-lg font-mono text-sm mb-4">
<strong>Input:</strong> nums = [1,2,3,1]
<strong>Output:</strong> 4
<strong>Explanation:</strong> Rob house 1 (money = 1) and then rob house 3 (money = 3). Total = 1 + 3 = 4.
</pre>

<h3 class="text-lg font-semibold mt-4 mb-2">Example 2:</h3>
<pre class="bg-gray-800 text-gray-100 p-3 rounded-lg font-mono text-sm mb-4">
<strong>Input:</strong> nums = [2,7,9,3,1]
<strong>Output:</strong> 12
<strong>Explanation:</strong> Rob house 1 (money = 2), rob house 3 (money = 9), then rob house 5 (money = 1). Total = 2 + 9 + 1 = 12.
</pre>

<h3 class="text-lg font-semibold mt-4 mb-2">Constraints:</h3>
<ul class="list-disc pl-5 space-y-1 text-gray-300">
  <li><code>1 &lt;= nums.length &lt;= 100</code></li>
  <li><code>0 &lt;= nums[i] &lt;= 400</code></li>
</ul>""",
    "starter_code": {
        "python": """class Solution:
    def rob(self, nums: list[int]) -> int:
        pass
""",
        "kotlin": """class Solution {
    fun rob(nums: IntArray): Int {
        // Write your code here
        return 0
    }
}
""",
    },
    "solution_code": {
        "python": """class Solution:
    def rob(self, nums: list[int]) -> int:
        prev2, prev1 = 0, 0
        for num in nums:
            curr = max(prev1, prev2 + num)
            prev2 = prev1
            prev1 = curr
        return prev1
""",
        "kotlin": """class Solution {
    fun rob(nums: IntArray): Int {
        var prev2 = 0
        var prev1 = 0
        for (num in nums) {
            val curr = maxOf(prev1, prev2 + num)
            prev2 = prev1
            prev1 = curr
        }
        return prev1
    }
}
""",
    },
    "test_code": {
        "python": """
if __name__ == "__main__":
    try:
        sol = Solution()
        assert sol.rob([1, 2, 3, 1]) == 4, "Test 1 failed."
        assert sol.rob([2, 7, 9, 3, 1]) == 12, "Test 2 failed."
        assert sol.rob([0]) == 0, "Test 3 failed."
        assert sol.rob([5, 1, 1, 5]) == 10, "Test 4 failed."
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
        require(sol.rob(intArrayOf(1, 2, 3, 1)) == 4) { "Test 1 failed." }
        require(sol.rob(intArrayOf(2, 7, 9, 3, 1)) == 12) { "Test 2 failed." }
        require(sol.rob(intArrayOf(0)) == 0) { "Test 3 failed." }
        require(sol.rob(intArrayOf(5, 1, 1, 5)) == 10) { "Test 4 failed." }
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
