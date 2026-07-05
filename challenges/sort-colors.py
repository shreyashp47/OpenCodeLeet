CHALLENGE = {
    "id": "sort-colors",
    "title": "Sort Colors",
    "difficulty": "Medium",
    "description": """<p>Given an array <code>nums</code> with <code>n</code> objects colored red, white, or blue, sort them <strong><a href="https://en.wikipedia.org/wiki/In-place_algorithm" target="_blank">in-place</a></strong> so that objects of the same color are adjacent, with the colors in the order red, white, and blue.</p>
<p>We will use the integers <code>0</code>, <code>1</code>, and <code>2</code> to represent the color red, white, and blue, respectively.</p>
<p>You must solve this problem <strong>without</strong> using the library's sort function.</p>

<h3 class="text-lg font-semibold mt-4 mb-2">Example 1:</h3>
<pre class="bg-gray-800 text-gray-100 p-3 rounded-lg font-mono text-sm mb-4">
<strong>Input:</strong> nums = [2,0,2,1,1,0]
<strong>Output:</strong> [0,0,1,1,2,2]
</pre>

<h3 class="text-lg font-semibold mt-4 mb-2">Example 2:</h3>
<pre class="bg-gray-800 text-gray-100 p-3 rounded-lg font-mono text-sm mb-4">
<strong>Input:</strong> nums = [2,0,1]
<strong>Output:</strong> [0,1,2]
</pre>

<h3 class="text-lg font-semibold mt-4 mb-2">Constraints:</h3>
<ul class="list-disc pl-5 space-y-1 text-gray-300">
  <li><code>n == nums.length</code></li>
  <li><code>1 &lt;= n &lt;= 300</code></li>
  <li><code>nums[i]</code> is either <code>0</code>, <code>1</code>, or <code>2</code>.</li>
</ul>""",
    "starter_code": {
        "python": """class Solution:
    def sortColors(self, nums: list[int]) -> None:
        pass
""",
        "kotlin": """class Solution {
    fun sortColors(nums: IntArray): Unit {
        // Write your code here
    }
}
""",
    },
    "solution_code": {
        "python": """class Solution:
    def sortColors(self, nums: list[int]) -> None:
        low, mid, high = 0, 0, len(nums) - 1
        while mid <= high:
            if nums[mid] == 0:
                nums[low], nums[mid] = nums[mid], nums[low]
                low += 1
                mid += 1
            elif nums[mid] == 1:
                mid += 1
            else:
                nums[mid], nums[high] = nums[high], nums[mid]
                high -= 1
""",
        "kotlin": """class Solution {
    fun sortColors(nums: IntArray): Unit {
        var low = 0
        var mid = 0
        var high = nums.size - 1
        while (mid <= high) {
            when (nums[mid]) {
                0 -> {
                    val tmp = nums[low]
                    nums[low] = nums[mid]
                    nums[mid] = tmp
                    low++
                    mid++
                }
                1 -> mid++
                else -> {
                    val tmp = nums[mid]
                    nums[mid] = nums[high]
                    nums[high] = tmp
                    high--
                }
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
        arr1 = [2, 0, 2, 1, 1, 0]
        sol.sortColors(arr1)
        assert arr1 == [0, 0, 1, 1, 2, 2], f"Test 1 failed. Got {arr1}"
        arr2 = [2, 0, 1]
        sol.sortColors(arr2)
        assert arr2 == [0, 1, 2], f"Test 2 failed. Got {arr2}"
        arr3 = [0]
        sol.sortColors(arr3)
        assert arr3 == [0], f"Test 3 failed. Got {arr3}"
        arr4 = [1, 2, 0]
        sol.sortColors(arr4)
        assert arr4 == [0, 1, 2], f"Test 4 failed. Got {arr4}"
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
        val arr1 = intArrayOf(2, 0, 2, 1, 1, 0)
        sol.sortColors(arr1)
        require(arr1 contentEquals intArrayOf(0, 0, 1, 1, 2, 2)) { "Test 1 failed. Got ${arr1.contentToString()}" }
        val arr2 = intArrayOf(2, 0, 1)
        sol.sortColors(arr2)
        require(arr2 contentEquals intArrayOf(0, 1, 2)) { "Test 2 failed. Got ${arr2.contentToString()}" }
        val arr3 = intArrayOf(0)
        sol.sortColors(arr3)
        require(arr3 contentEquals intArrayOf(0)) { "Test 3 failed. Got ${arr3.contentToString()}" }
        val arr4 = intArrayOf(1, 2, 0)
        sol.sortColors(arr4)
        require(arr4 contentEquals intArrayOf(0, 1, 2)) { "Test 4 failed. Got ${arr4.contentToString()}" }
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
