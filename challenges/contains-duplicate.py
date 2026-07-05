CHALLENGE = {
    "id": "contains-duplicate",
    "title": "Contains Duplicate",
    "difficulty": "Easy",
    "description": """<p>Given an integer array <code>nums</code>, return <code>true</code> if any value appears <strong>at least twice</strong> in the array, and return <code>false</code> if every element is distinct.</p>

<h3 class="text-lg font-semibold mt-4 mb-2">Example 1:</h3>
<pre class="bg-gray-800 text-gray-100 p-3 rounded-lg font-mono text-sm mb-4">
<strong>Input:</strong> nums = [1,2,3,1]
<strong>Output:</strong> true
</pre>

<h3 class="text-lg font-semibold mt-4 mb-2">Example 2:</h3>
<pre class="bg-gray-800 text-gray-100 p-3 rounded-lg font-mono text-sm mb-4">
<strong>Input:</strong> nums = [1,2,3,4]
<strong>Output:</strong> false
</pre>

<h3 class="text-lg font-semibold mt-4 mb-2">Example 3:</h3>
<pre class="bg-gray-800 text-gray-100 p-3 rounded-lg font-mono text-sm mb-4">
<strong>Input:</strong> nums = [1,1,1,3,3,4,3,2,4,2]
<strong>Output:</strong> true
</pre>

<h3 class="text-lg font-semibold mt-4 mb-2">Constraints:</h3>
<ul class="list-disc pl-5 space-y-1 text-gray-300">
  <li><code>1 &lt;= nums.length &lt;= 10<sup>5</sup></code></li>
  <li><code>-10<sup>9</sup> &lt;= nums[i] &lt;= 10<sup>9</sup></code></li>
</ul>""",
    "starter_code": {
        "python": """class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        pass
""",
        "kotlin": """class Solution {
    fun containsDuplicate(nums: IntArray): Boolean {
        // Write your code here
        return false
    }
}
""",
    },
    "solution_code": {
        "python": """class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        seen = set()
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False
""",
        "kotlin": """class Solution {
    fun containsDuplicate(nums: IntArray): Boolean {
        val seen = mutableSetOf<Int>()
        for (num in nums) {
            if (num in seen) return true
            seen.add(num)
        }
        return false
    }
}
""",
    },
    "test_code": {
        "python": """
if __name__ == "__main__":
    try:
        sol = Solution()
        res1 = sol.containsDuplicate([1, 2, 3, 1])
        assert res1 == True, f"Test 1 failed. Expected True, got {res1}"
        res2 = sol.containsDuplicate([1, 2, 3, 4])
        assert res2 == False, f"Test 2 failed. Expected False, got {res2}"
        res3 = sol.containsDuplicate([1, 1, 1, 3, 3, 4, 3, 2, 4, 2])
        assert res3 == True, f"Test 3 failed. Expected True, got {res3}"
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
        val res1 = sol.containsDuplicate(intArrayOf(1, 2, 3, 1))
        require(res1 == true) { "Test 1 failed. Expected true, got $res1" }
        val res2 = sol.containsDuplicate(intArrayOf(1, 2, 3, 4))
        require(res2 == false) { "Test 2 failed. Expected false, got $res2" }
        val res3 = sol.containsDuplicate(intArrayOf(1, 1, 1, 3, 3, 4, 3, 2, 4, 2))
        require(res3 == true) { "Test 3 failed. Expected true, got $res3" }
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
