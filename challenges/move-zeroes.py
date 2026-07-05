CHALLENGE = {
    "id": "move-zeroes",
    "title": "Move Zeroes",
    "difficulty": "Easy",
    "description": """<p>Given an integer array <code>nums</code>, move all <code>0</code>'s to the end of it while maintaining the relative order of the non-zero elements.</p>
<p><strong>Note:</strong> You must do this <strong>in-place</strong> without making a copy of the array.</p>

<h3 class="text-lg font-semibold mt-4 mb-2">Example 1:</h3>
<pre class="bg-gray-800 text-gray-100 p-3 rounded-lg font-mono text-sm mb-4">
<strong>Input:</strong> nums = [0,1,0,3,12]
<strong>Output:</strong> [1,3,12,0,0]
</pre>

<h3 class="text-lg font-semibold mt-4 mb-2">Example 2:</h3>
<pre class="bg-gray-800 text-gray-100 p-3 rounded-lg font-mono text-sm mb-4">
<strong>Input:</strong> nums = [0]
<strong>Output:</strong> [0]
</pre>

<h3 class="text-lg font-semibold mt-4 mb-2">Constraints:</h3>
<ul class="list-disc pl-5 space-y-1 text-gray-300">
  <li><code>1 &lt;= nums.length &lt;= 10<sup>4</sup></code></li>
  <li><code>-2<sup>31</sup> &lt;= nums[i] &lt;= 2<sup>31</sup> - 1</code></li>
</ul>""",
    "starter_code": {
        "python": """class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        pass
""",
        "kotlin": """class Solution {
    fun moveZeroes(nums: IntArray): Unit {
        // Write your code here
    }
}
""",
    },
    "solution_code": {
        "python": """class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        non_zero_idx = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[non_zero_idx], nums[i] = nums[i], nums[non_zero_idx]
                non_zero_idx += 1
""",
        "kotlin": """class Solution {
    fun moveZeroes(nums: IntArray): Unit {
        var nonZeroIdx = 0
        for (i in nums.indices) {
            if (nums[i] != 0) {
                val temp = nums[nonZeroIdx]
                nums[nonZeroIdx] = nums[i]
                nums[i] = temp
                nonZeroIdx++
            }
        }
    }
}
""",
    },
    "test_code": {
        "python": """
if __name__ == "__main__":
    try:
        sol = Solution()
        nums1 = [0, 1, 0, 3, 12]
        sol.moveZeroes(nums1)
        assert nums1 == [1, 3, 12, 0, 0], f"Test 1 failed. Got {nums1}"
        nums2 = [0]
        sol.moveZeroes(nums2)
        assert nums2 == [0], f"Test 2 failed. Got {nums2}"
        nums3 = [0, 0, 1]
        sol.moveZeroes(nums3)
        assert nums3 == [1, 0, 0], f"Test 3 failed. Got {nums3}"
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
        val nums1 = intArrayOf(0, 1, 0, 3, 12)
        sol.moveZeroes(nums1)
        require(nums1 contentEquals intArrayOf(1, 3, 12, 0, 0)) { "Test 1 failed. Got ${nums1.contentToString()}" }
        val nums2 = intArrayOf(0)
        sol.moveZeroes(nums2)
        require(nums2 contentEquals intArrayOf(0)) { "Test 2 failed. Got ${nums2.contentToString()}" }
        val nums3 = intArrayOf(0, 0, 1)
        sol.moveZeroes(nums3)
        require(nums3 contentEquals intArrayOf(1, 0, 0)) { "Test 3 failed. Got ${nums3.contentToString()}" }
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
