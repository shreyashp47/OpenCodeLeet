CHALLENGE = {
    "id": "jump-game",
    "title": "Jump Game",
    "difficulty": "Medium",
    "description": """<p>You are given an integer array <code>nums</code>. You are initially positioned at the array's <strong>first index</strong>, and each element in the array represents your maximum jump length at that position.</p>
<p>Return <code>true</code> if you can reach the last index, or <code>false</code> otherwise.</p>

<h3 class="text-lg font-semibold mt-4 mb-2">Example 1:</h3>
<pre class="bg-gray-800 text-gray-100 p-3 rounded-lg font-mono text-sm mb-4">
<strong>Input:</strong> nums = [2,3,1,1,4]
<strong>Output:</strong> true
<strong>Explanation:</strong> Jump 1 step from index 0 to 1, then 3 steps to the last index.
</pre>

<h3 class="text-lg font-semibold mt-4 mb-2">Example 2:</h3>
<pre class="bg-gray-800 text-gray-100 p-3 rounded-lg font-mono text-sm mb-4">
<strong>Input:</strong> nums = [3,2,1,0,4]
<strong>Output:</strong> false
<strong>Explanation:</strong> You will always arrive at index 3 no matter what. Its maximum jump length is 0, making it impossible to reach the last index.
</pre>

<h3 class="text-lg font-semibold mt-4 mb-2">Constraints:</h3>
<ul class="list-disc pl-5 space-y-1 text-gray-300">
  <li><code>1 &lt;= nums.length &lt;= 10<sup>4</sup></code></li>
  <li><code>0 &lt;= nums[i] &lt;= 10<sup>5</sup></code></li>
</ul>""",
    "starter_code": {
        "python": """class Solution:
    def canJump(self, nums: list[int]) -> bool:
        pass
""",
        "kotlin": """class Solution {
    fun canJump(nums: IntArray): Boolean {
        // Write your code here
        return false
    }
}
""",
    },
    "solution_code": {
        "python": """class Solution:
    def canJump(self, nums: list[int]) -> bool:
        goal = len(nums) - 1
        for i in range(len(nums) - 1, -1, -1):
            if i + nums[i] >= goal:
                goal = i
        return goal == 0
""",
        "kotlin": """class Solution {
    fun canJump(nums: IntArray): Boolean {
        var goal = nums.size - 1
        for (i in nums.size - 1 downTo 0) {
            if (i + nums[i] >= goal) goal = i
        }
        return goal == 0
    }
}
""",
    },
    "test_code": {
        "python": """
if __name__ == "__main__":
    try:
        sol = Solution()
        res1 = sol.canJump([2, 3, 1, 1, 4])
        assert res1 is not None, "Test 1 failed. Returned None."
        assert res1 == True, f"Test 1 failed. Expected True, got {res1}"
        res2 = sol.canJump([3, 2, 1, 0, 4])
        assert res2 is not None, "Test 2 failed. Returned None."
        assert res2 == False, f"Test 2 failed. Expected False, got {res2}"
        res3 = sol.canJump([0])
        assert res3 is not None, "Test 3 failed. Returned None."
        assert res3 == True, f"Test 3 failed. Expected True, got {res3}"
        res4 = sol.canJump([2, 0, 0])
        assert res4 is not None, "Test 4 failed. Returned None."
        assert res4 == True, f"Test 4 failed. Expected True, got {res4}"
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
        val res1 = sol.canJump(intArrayOf(2, 3, 1, 1, 4))
        require(res1 == true) { "Test 1 failed. Expected true, got $res1" }
        val res2 = sol.canJump(intArrayOf(3, 2, 1, 0, 4))
        require(res2 == false) { "Test 2 failed. Expected false, got $res2" }
        val res3 = sol.canJump(intArrayOf(0))
        require(res3 == true) { "Test 3 failed. Expected true, got $res3" }
        val res4 = sol.canJump(intArrayOf(2, 0, 0))
        require(res4 == true) { "Test 4 failed. Expected true, got $res4" }
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
