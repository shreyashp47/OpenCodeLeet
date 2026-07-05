CHALLENGE = {
    "id": "product-of-array-except-self",
    "title": "Product of Array Except Self",
    "difficulty": "Medium",
    "description": """<p>Given an integer array <code>nums</code>, return <em>an array <code>answer</code> such that <code>answer[i]</code> is equal to the product of all the elements of <code>nums</code> except <code>nums[i]</code></em>.</p>
<p>The product of any prefix or suffix of <code>nums</code> is <strong>guaranteed</strong> to fit in a <strong>32-bit</strong> integer.</p>
<p>You must write an algorithm that runs in <code>O(n)</code> time and without using the division operation.</p>

<h3 class="text-lg font-semibold mt-4 mb-2">Example 1:</h3>
<pre class="bg-gray-800 text-gray-100 p-3 rounded-lg font-mono text-sm mb-4">
<strong>Input:</strong> nums = [1,2,3,4]
<strong>Output:</strong> [24,12,8,6]
</pre>

<h3 class="text-lg font-semibold mt-4 mb-2">Example 2:</h3>
<pre class="bg-gray-800 text-gray-100 p-3 rounded-lg font-mono text-sm mb-4">
<strong>Input:</strong> nums = [-1,1,0,-3,3]
<strong>Output:</strong> [0,0,9,0,0]
</pre>

<h3 class="text-lg font-semibold mt-4 mb-2">Constraints:</h3>
<ul class="list-disc pl-5 space-y-1 text-gray-300">
  <li><code>2 &lt;= nums.length &lt;= 10<sup>5</sup></code></li>
  <li><code>-30 &lt;= nums[i] &lt;= 30</code></li>
  <li>The product of any prefix or suffix fits in a <strong>32-bit</strong> integer.</li>
</ul>""",
    "starter_code": {
        "python": """class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        pass
""",
        "kotlin": """class Solution {
    fun productExceptSelf(nums: IntArray): IntArray {
        // Write your code here
        return intArrayOf()
    }
}
""",
    },
    "solution_code": {
        "python": """class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        n = len(nums)
        res = [1] * n
        prefix = 1
        for i in range(n):
            res[i] = prefix
            prefix *= nums[i]
        suffix = 1
        for i in range(n - 1, -1, -1):
            res[i] *= suffix
            suffix *= nums[i]
        return res
""",
        "kotlin": """class Solution {
    fun productExceptSelf(nums: IntArray): IntArray {
        val n = nums.size
        val res = IntArray(n) { 1 }
        var prefix = 1
        for (i in 0 until n) {
            res[i] = prefix
            prefix *= nums[i]
        }
        var suffix = 1
        for (i in n - 1 downTo 0) {
            res[i] *= suffix
            suffix *= nums[i]
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
        res1 = sol.productExceptSelf([1, 2, 3, 4])
        assert res1 is not None, "Test 1 failed. Returned None."
        assert res1 == [24, 12, 8, 6], f"Test 1 failed. Expected [24, 12, 8, 6], got {res1}"
        res2 = sol.productExceptSelf([-1, 1, 0, -3, 3])
        assert res2 is not None, "Test 2 failed. Returned None."
        assert res2 == [0, 0, 9, 0, 0], f"Test 2 failed. Expected [0, 0, 9, 0, 0], got {res2}"
        res3 = sol.productExceptSelf([2, 3, 5, 7])
        assert res3 is not None, "Test 3 failed. Returned None."
        assert res3 == [105, 70, 42, 30], f"Test 3 failed. Expected [105, 70, 42, 30], got {res3}"
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
        val res1 = sol.productExceptSelf(intArrayOf(1, 2, 3, 4))
        require(res1 contentEquals intArrayOf(24, 12, 8, 6)) { "Test 1 failed. Expected [24, 12, 8, 6], got ${res1.contentToString()}" }
        val res2 = sol.productExceptSelf(intArrayOf(-1, 1, 0, -3, 3))
        require(res2 contentEquals intArrayOf(0, 0, 9, 0, 0)) { "Test 2 failed. Expected [0, 0, 9, 0, 0], got ${res2.contentToString()}" }
        val res3 = sol.productExceptSelf(intArrayOf(2, 3, 5, 7))
        require(res3 contentEquals intArrayOf(105, 70, 42, 30)) { "Test 3 failed. Expected [105, 70, 42, 30], got ${res3.contentToString()}" }
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
