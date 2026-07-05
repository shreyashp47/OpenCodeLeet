CHALLENGE = {
    "id": "subarray-sum-equals-k",
    "title": "Subarray Sum Equals K",
    "difficulty": "Medium",
    "description": """<p>Given an array of integers <code>nums</code> and an integer <code>k</code>, return <em>the total number of subarrays whose sum equals to <code>k</code></em>.</p>
<p>A subarray is a contiguous <strong>non-empty</strong> sequence of elements within an array.</p>

<h3 class="text-lg font-semibold mt-4 mb-2">Example 1:</h3>
<pre class="bg-gray-800 text-gray-100 p-3 rounded-lg font-mono text-sm mb-4">
<strong>Input:</strong> nums = [1,1,1], k = 2
<strong>Output:</strong> 2
</pre>

<h3 class="text-lg font-semibold mt-4 mb-2">Example 2:</h3>
<pre class="bg-gray-800 text-gray-100 p-3 rounded-lg font-mono text-sm mb-4">
<strong>Input:</strong> nums = [1,2,3], k = 3
<strong>Output:</strong> 2
</pre>

<h3 class="text-lg font-semibold mt-4 mb-2">Constraints:</h3>
<ul class="list-disc pl-5 space-y-1 text-gray-300">
  <li><code>1 &lt;= nums.length &lt;= 2 * 10<sup>4</sup></code></li>
  <li><code>-1000 &lt;= nums[i] &lt;= 1000</code></li>
  <li><code>-10<sup>7</sup> &lt;= k &lt;= 10<sup>7</sup></code></li>
</ul>""",
    "starter_code": {
        "python": """class Solution:
    def subarraySum(self, nums: list[int], k: int) -> int:
        pass
""",
        "kotlin": """class Solution {
    fun subarraySum(nums: IntArray, k: Int): Int {
        // Write your code here
        return 0
    }
}
""",
    },
    "solution_code": {
        "python": """class Solution:
    def subarraySum(self, nums: list[int], k: int) -> int:
        prefix_sum = {0: 1}
        current = 0
        count = 0
        for num in nums:
            current += num
            if current - k in prefix_sum:
                count += prefix_sum[current - k]
            prefix_sum[current] = prefix_sum.get(current, 0) + 1
        return count
""",
        "kotlin": """class Solution {
    fun subarraySum(nums: IntArray, k: Int): Int {
        val prefixSum = mutableMapOf(0 to 1)
        var current = 0
        var count = 0
        for (num in nums) {
            current += num
            count += prefixSum.getOrDefault(current - k, 0)
            prefixSum[current] = prefixSum.getOrDefault(current, 0) + 1
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
        assert sol.subarraySum([1, 1, 1], 2) == 2, "Test 1 failed."
        assert sol.subarraySum([1, 2, 3], 3) == 2, "Test 2 failed."
        assert sol.subarraySum([1], 0) == 0, "Test 3 failed."
        assert sol.subarraySum([-1, -1, 1], 0) == 1, "Test 4 failed."
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
        require(sol.subarraySum(intArrayOf(1, 1, 1), 2) == 2) { "Test 1 failed." }
        require(sol.subarraySum(intArrayOf(1, 2, 3), 3) == 2) { "Test 2 failed." }
        require(sol.subarraySum(intArrayOf(1), 0) == 0) { "Test 3 failed." }
        require(sol.subarraySum(intArrayOf(-1, -1, 1), 0) == 1) { "Test 4 failed." }
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
