CHALLENGE = {
    "id": "missing-number",
    "title": "Missing Number",
    "difficulty": "Easy",
    "description": """<p>Given an array <code>nums</code> containing <code>n</code> distinct numbers in the range <code>[0, n]</code>, return <em>the only number in the range that is missing from the array.</em></p>

<h3 class="text-lg font-semibold mt-4 mb-2">Example 1:</h3>
<pre class="bg-gray-800 text-gray-100 p-3 rounded-lg font-mono text-sm mb-4">
<strong>Input:</strong> nums = [3,0,1]
<strong>Output:</strong> 2
<strong>Explanation:</strong> n = 3 since there are 3 numbers, so all numbers are in the range [0,3]. 2 is the missing number.
</pre>

<h3 class="text-lg font-semibold mt-4 mb-2">Example 2:</h3>
<pre class="bg-gray-800 text-gray-100 p-3 rounded-lg font-mono text-sm mb-4">
<strong>Input:</strong> nums = [0,1]
<strong>Output:</strong> 2
<strong>Explanation:</strong> n = 2 since there are 2 numbers, so all numbers are in the range [0,2]. 2 is the missing number.
</pre>

<h3 class="text-lg font-semibold mt-4 mb-2">Example 3:</h3>
<pre class="bg-gray-800 text-gray-100 p-3 rounded-lg font-mono text-sm mb-4">
<strong>Input:</strong> nums = [9,6,4,2,3,5,7,0,1]
<strong>Output:</strong> 8
<strong>Explanation:</strong> n = 9 since there are 9 numbers, so all numbers are in the range [0,9]. 8 is the missing number.
</pre>

<h3 class="text-lg font-semibold mt-4 mb-2">Constraints:</h3>
<ul class="list-disc pl-5 space-y-1 text-gray-300">
  <li><code>n == nums.length</code></li>
  <li><code>1 &lt;= n &lt;= 10<sup>4</sup></code></li>
  <li><code>0 &lt;= nums[i] &lt;= n</code></li>
  <li>All the numbers of <code>nums</code> are <strong>unique</strong>.</li>
</ul>""",
    "starter_code": {
        "python": """class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        pass
""",
        "kotlin": """class Solution {
    fun missingNumber(nums: IntArray): Int {
        // Write your code here
        return 0
    }
}
""",
    },
    "solution_code": {
        "python": """class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        n = len(nums)
        result = n
        for i, num in enumerate(nums):
            result ^= i ^ num
        return result
""",
        "kotlin": """class Solution {
    fun missingNumber(nums: IntArray): Int {
        val n = nums.size
        var result = n
        for ((i, num) in nums.withIndex()) {
            result = result xor i xor num
        }
        return result
    }
}
""",
    },
    "test_code": {
        "python": """
if __name__ == "__main__":
    try:
        sol = Solution()
        res1 = sol.missingNumber([3, 0, 1])
        assert res1 == 2, f"Test 1 failed. Expected 2, got {res1}"
        res2 = sol.missingNumber([0, 1])
        assert res2 == 2, f"Test 2 failed. Expected 2, got {res2}"
        res3 = sol.missingNumber([9, 6, 4, 2, 3, 5, 7, 0, 1])
        assert res3 == 8, f"Test 3 failed. Expected 8, got {res3}"
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
        val res1 = sol.missingNumber(intArrayOf(3, 0, 1))
        require(res1 == 2) { "Test 1 failed. Expected 2, got $res1" }
        val res2 = sol.missingNumber(intArrayOf(0, 1))
        require(res2 == 2) { "Test 2 failed. Expected 2, got $res2" }
        val res3 = sol.missingNumber(intArrayOf(9, 6, 4, 2, 3, 5, 7, 0, 1))
        require(res3 == 8) { "Test 3 failed. Expected 8, got $res3" }
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
