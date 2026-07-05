CHALLENGE = {
    "id": "majority-element",
    "title": "Majority Element",
    "difficulty": "Easy",
    "description": """<p>Given an array <code>nums</code> of size <code>n</code>, return <em>the majority element</em>.</p>
<p>The majority element is the element that appears <strong>more than</strong> <code>&lfloor;n / 2&rfloor;</code> times. You may assume that the majority element always exists in the array.</p>

<h3 class="text-lg font-semibold mt-4 mb-2">Example 1:</h3>
<pre class="bg-gray-800 text-gray-100 p-3 rounded-lg font-mono text-sm mb-4">
<strong>Input:</strong> nums = [3,2,3]
<strong>Output:</strong> 3
</pre>

<h3 class="text-lg font-semibold mt-4 mb-2">Example 2:</h3>
<pre class="bg-gray-800 text-gray-100 p-3 rounded-lg font-mono text-sm mb-4">
<strong>Input:</strong> nums = [2,2,1,1,1,2,2]
<strong>Output:</strong> 2
</pre>

<h3 class="text-lg font-semibold mt-4 mb-2">Constraints:</h3>
<ul class="list-disc pl-5 space-y-1 text-gray-300">
  <li><code>n == nums.length</code></li>
  <li><code>1 &lt;= n &lt;= 5 * 10<sup>4</sup></code></li>
  <li><code>-10<sup>9</sup> &lt;= nums[i] &lt;= 10<sup>9</sup></code></li>
</ul>

<h3 class="text-lg font-semibold mt-4 mb-2">Follow up:</h3>
<p class="text-gray-300">Could you solve the problem in linear time and in O(1) space?</p>""",
    "starter_code": {
        "python": """class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        pass
""",
        "kotlin": """class Solution {
    fun majorityElement(nums: IntArray): Int {
        // Write your code here
        return 0
    }
}
""",
    },
    "solution_code": {
        "python": """class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        count = 0
        candidate = None
        for num in nums:
            if count == 0:
                candidate = num
            count += 1 if num == candidate else -1
        return candidate
""",
        "kotlin": """class Solution {
    fun majorityElement(nums: IntArray): Int {
        var count = 0
        var candidate = 0
        for (num in nums) {
            if (count == 0) {
                candidate = num
            }
            count += if (num == candidate) 1 else -1
        }
        return candidate
    }
}
""",
    },
    "test_code": {
        "python": """
if __name__ == "__main__":
    try:
        sol = Solution()
        res1 = sol.majorityElement([3, 2, 3])
        assert res1 is not None, "Test 1 failed. Returned None."
        assert res1 == 3, f"Test 1 failed. Expected 3, got {res1}"
        res2 = sol.majorityElement([2, 2, 1, 1, 1, 2, 2])
        assert res2 is not None, "Test 2 failed. Returned None."
        assert res2 == 2, f"Test 2 failed. Expected 2, got {res2}"
        res3 = sol.majorityElement([1])
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
        require(sol.majorityElement(intArrayOf(3, 2, 3)) == 3) { "Test 1 failed. Expected 3, got ${sol.majorityElement(intArrayOf(3, 2, 3))}" }
        require(sol.majorityElement(intArrayOf(2, 2, 1, 1, 1, 2, 2)) == 2) { "Test 2 failed. Expected 2, got ${sol.majorityElement(intArrayOf(2, 2, 1, 1, 1, 2, 2))}" }
        require(sol.majorityElement(intArrayOf(1)) == 1) { "Test 3 failed. Expected 1, got ${sol.majorityElement(intArrayOf(1))}" }
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
