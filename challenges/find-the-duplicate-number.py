CHALLENGE = {
    "id": "find-the-duplicate-number",
    "title": "Find the Duplicate Number",
    "difficulty": "Medium",
    "description": """<p>Given an array of integers <code>nums</code> containing <code>n + 1</code> integers where each integer is in the range <code>[1, n]</code> inclusive.</p>
<p>There is only <strong>one repeated number</strong> in <code>nums</code>, return <em>this repeated number</em>.</p>
<p>You must solve the problem <strong>without</strong> modifying the array <code>nums</code> and uses only constant extra space.</p>

<h3 class="text-lg font-semibold mt-4 mb-2">Example 1:</h3>
<pre class="bg-gray-800 text-gray-100 p-3 rounded-lg font-mono text-sm mb-4">
<strong>Input:</strong> nums = [1,3,4,2,2]
<strong>Output:</strong> 2
</pre>

<h3 class="text-lg font-semibold mt-4 mb-2">Example 2:</h3>
<pre class="bg-gray-800 text-gray-100 p-3 rounded-lg font-mono text-sm mb-4">
<strong>Input:</strong> nums = [3,1,3,4,2]
<strong>Output:</strong> 3
</pre>

<h3 class="text-lg font-semibold mt-4 mb-2">Constraints:</h3>
<ul class="list-disc pl-5 space-y-1 text-gray-300">
  <li><code>1 &lt;= n &lt;= 10<sup>5</sup></code></li>
  <li><code>nums.length == n + 1</code></li>
  <li><code>1 &lt;= nums[i] &lt;= n</code></li>
  <li>There is only <strong>one repeated number</strong> in <code>nums</code>.</li>
</ul>""",
    "starter_code": {
        "python": """class Solution:
    def findDuplicate(self, nums: list[int]) -> int:
        pass
""",
        "kotlin": """class Solution {
    fun findDuplicate(nums: IntArray): Int {
        // Write your code here
        return 0
    }
}
""",
    },
    "solution_code": {
        "python": """class Solution:
    def findDuplicate(self, nums: list[int]) -> int:
        slow = nums[0]
        fast = nums[0]
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
        slow = nums[0]
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]
        return slow
""",
        "kotlin": """class Solution {
    fun findDuplicate(nums: IntArray): Int {
        var slow = nums[0]
        var fast = nums[0]
        do {
            slow = nums[slow]
            fast = nums[nums[fast]]
        } while (slow != fast)
        slow = nums[0]
        while (slow != fast) {
            slow = nums[slow]
            fast = nums[fast]
        }
        return slow
    }
}
""",
    },
    "test_code": {
        "python": """
if __name__ == "__main__":
    try:
        sol = Solution()
        assert sol.findDuplicate([1, 3, 4, 2, 2]) == 2, "Test 1 failed."
        assert sol.findDuplicate([3, 1, 3, 4, 2]) == 3, "Test 2 failed."
        assert sol.findDuplicate([1, 1]) == 1, "Test 3 failed."
        assert sol.findDuplicate([1, 1, 2]) == 1, "Test 4 failed."
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
        require(sol.findDuplicate(intArrayOf(1, 3, 4, 2, 2)) == 2) { "Test 1 failed." }
        require(sol.findDuplicate(intArrayOf(3, 1, 3, 4, 2)) == 3) { "Test 2 failed." }
        require(sol.findDuplicate(intArrayOf(1, 1)) == 1) { "Test 3 failed." }
        require(sol.findDuplicate(intArrayOf(1, 1, 2)) == 1) { "Test 4 failed." }
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
