CHALLENGE = {
    "id": "two-sum",
    "title": "Two Sum",
    "difficulty": "Easy",
    "description": """<p>Given an array of integers <code>nums</code> and an integer <code>target</code>, return <em>indices of the two numbers such that they add up to <code>target</code></em>.</p>
<p>You may assume that each input would have <strong><em>exactly</em> one solution</strong>, and you may not use the <em>same</em> element twice.</p>
<p>You can return the answer in any order.</p>

<h3 class="text-lg font-semibold mt-4 mb-2">Example 1:</h3>
<pre class="bg-gray-800 text-gray-100 p-3 rounded-lg font-mono text-sm mb-4">
<strong>Input:</strong> nums = [2,7,11,15], target = 9
<strong>Output:</strong> [0,1]
<strong>Explanation:</strong> Because nums[0] + nums[1] == 9, we return [0, 1].
</pre>

<h3 class="text-lg font-semibold mt-4 mb-2">Example 2:</h3>
<pre class="bg-gray-800 text-gray-100 p-3 rounded-lg font-mono text-sm mb-4">
<strong>Input:</strong> nums = [3,2,4], target = 6
<strong>Output:</strong> [1,2]
</pre>

<h3 class="text-lg font-semibold mt-4 mb-2">Example 3:</h3>
<pre class="bg-gray-800 text-gray-100 p-3 rounded-lg font-mono text-sm mb-4">
<strong>Input:</strong> nums = [3,3], target = 6
<strong>Output:</strong> [0,1]
</pre>

<h3 class="text-lg font-semibold mt-4 mb-2">Constraints:</h3>
<ul class="list-disc pl-5 space-y-1 text-gray-300">
  <li><code>2 &lt;= nums.length &lt;= 10<sup>4</sup></code></li>
  <li><code>-10<sup>9</sup> &lt;= nums[i] &lt;= 10<sup>9</sup></code></li>
  <li><code>-10<sup>9</sup> &lt;= target &lt;= 10<sup>9</sup></code></li>
  <li><strong>Only one valid answer exists.</strong></li>
</ul>""",
    "starter_code": {
        "python": """class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        pass
""",
        "kotlin": """class Solution {
    fun twoSum(nums: IntArray, target: Int): IntArray {
        // Write your code here
        return intArrayOf()
    }
}
""",
    },
    "solution_code": {
        "python": """class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        lookup = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in lookup:
                return [lookup[complement], i]
            lookup[num] = i
""",
        "kotlin": """class Solution {
    fun twoSum(nums: IntArray, target: Int): IntArray {
        val map = mutableMapOf<Int, Int>()
        for ((i, num) in nums.withIndex()) {
            val complement = target - num
            if (complement in map) return intArrayOf(map[complement]!!, i)
            map[num] = i
        }
        return intArrayOf()
    }
}
""",
    },
    "test_code": {
        "python": """
if __name__ == "__main__":
    try:
        sol = Solution()
        res1 = sol.twoSum([2, 7, 11, 15], 9)
        assert res1 is not None, "Test 1 failed. Returned None."
        assert sorted(res1) == [0, 1], f"Test 1 failed. Expected [0, 1], got {res1}"
        res2 = sol.twoSum([3, 2, 4], 6)
        assert res2 is not None, "Test 2 failed. Returned None."
        assert sorted(res2) == [1, 2], f"Test 2 failed. Expected [1, 2], got {res2}"
        res3 = sol.twoSum([3, 3], 6)
        assert res3 is not None, "Test 3 failed. Returned None."
        assert sorted(res3) == [0, 1], f"Test 3 failed. Expected [0, 1], got {res3}"
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
        val res1 = sol.twoSum(intArrayOf(2, 7, 11, 15), 9)
        require(res1 contentEquals intArrayOf(0, 1)) { "Test 1 failed. Expected [0, 1], got ${res1.contentToString()}" }
        val res2 = sol.twoSum(intArrayOf(3, 2, 4), 6)
        require(res2 contentEquals intArrayOf(1, 2)) { "Test 2 failed. Expected [1, 2], got ${res2.contentToString()}" }
        val res3 = sol.twoSum(intArrayOf(3, 3), 6)
        require(res3 contentEquals intArrayOf(0, 1)) { "Test 3 failed. Expected [0, 1], got ${res3.contentToString()}" }
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
