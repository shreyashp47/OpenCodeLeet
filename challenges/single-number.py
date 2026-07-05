CHALLENGE = {
    "id": "single-number",
    "title": "Single Number",
    "difficulty": "Easy",
    "description": """<p>Given a <strong>non-empty</strong> array of integers <code>nums</code>, every element appears <strong>twice</strong> except for one. Find that single one.</p>
<p>You must implement a solution with a linear runtime complexity and use only constant extra space.</p>

<h3 class="text-lg font-semibold mt-4 mb-2">Example 1:</h3>
<pre class="bg-gray-800 text-gray-100 p-3 rounded-lg font-mono text-sm mb-4">
<strong>Input:</strong> nums = [2,2,1]
<strong>Output:</strong> 1
</pre>

<h3 class="text-lg font-semibold mt-4 mb-2">Example 2:</h3>
<pre class="bg-gray-800 text-gray-100 p-3 rounded-lg font-mono text-sm mb-4">
<strong>Input:</strong> nums = [4,1,2,1,2]
<strong>Output:</strong> 4
</pre>

<h3 class="text-lg font-semibold mt-4 mb-2">Example 3:</h3>
<pre class="bg-gray-800 text-gray-100 p-3 rounded-lg font-mono text-sm mb-4">
<strong>Input:</strong> nums = [1]
<strong>Output:</strong> 1
</pre>

<h3 class="text-lg font-semibold mt-4 mb-2">Constraints:</h3>
<ul class="list-disc pl-5 space-y-1 text-gray-300">
  <li><code>1 &lt;= nums.length &lt;= 3 * 10<sup>4</sup></code></li>
  <li><code>-3 * 10<sup>4</sup> &lt;= nums[i] &lt;= 3 * 10<sup>4</sup></code></li>
  <li>Each element appears <strong>twice</strong> except for one element which appears <strong>once</strong>.</li>
</ul>""",
    "starter_code": {
        "python": """class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        pass
""",
        "kotlin": """class Solution {
    fun singleNumber(nums: IntArray): Int {
        // Write your code here
        return 0
    }
}
""",
    },
    "solution_code": {
        "python": """class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        result = 0
        for num in nums:
            result ^= num
        return result
""",
        "kotlin": """class Solution {
    fun singleNumber(nums: IntArray): Int {
        var result = 0
        for (num in nums) {
            result = result xor num
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
        res1 = sol.singleNumber([2, 2, 1])
        assert res1 == 1, f"Test 1 failed. Expected 1, got {res1}"
        res2 = sol.singleNumber([4, 1, 2, 1, 2])
        assert res2 == 4, f"Test 2 failed. Expected 4, got {res2}"
        res3 = sol.singleNumber([1])
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
        val res1 = sol.singleNumber(intArrayOf(2, 2, 1))
        require(res1 == 1) { "Test 1 failed. Expected 1, got $res1" }
        val res2 = sol.singleNumber(intArrayOf(4, 1, 2, 1, 2))
        require(res2 == 4) { "Test 2 failed. Expected 4, got $res2" }
        val res3 = sol.singleNumber(intArrayOf(1))
        require(res3 == 1) { "Test 3 failed. Expected 1, got $res3" }
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
