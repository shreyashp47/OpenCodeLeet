CHALLENGE = {
    "id": "remove-duplicates-from-sorted-array",
    "title": "Remove Duplicates from Sorted Array",
    "difficulty": "Easy",
    "description": """<p>Given an integer array <code>nums</code> sorted in <strong>non-decreasing order</strong>, remove the duplicates <strong><a href="https://en.wikipedia.org/wiki/In-place_algorithm" target="_blank">in-place</a></strong> such that each unique element appears only once. The <strong>relative order</strong> of the elements should be kept the <strong>same</strong>.</p>
<p>Since it is impossible to change the length of the array in some languages, you must instead have the result be placed in the <strong>first part</strong> of the array <code>nums</code>. More formally, if there are <code>k</code> elements after removing the duplicates, then the first <code>k</code> elements of <code>nums</code> should hold the final result. It does not matter what you leave beyond the first <code>k</code> elements.</p>
<p>Return <code>k</code> <em>after placing the final result in the first </em><code>k</code><em> slots of </em><code>nums</code>.</p>

<h3 class="text-lg font-semibold mt-4 mb-2">Example 1:</h3>
<pre class="bg-gray-800 text-gray-100 p-3 rounded-lg font-mono text-sm mb-4">
<strong>Input:</strong> nums = [1,1,2]
<strong>Output:</strong> 2, nums = [1,2,_]
<strong>Explanation:</strong> Your function should return k = 2, with the first two elements of nums being 1 and 2 respectively.
</pre>

<h3 class="text-lg font-semibold mt-4 mb-2">Example 2:</h3>
<pre class="bg-gray-800 text-gray-100 p-3 rounded-lg font-mono text-sm mb-4">
<strong>Input:</strong> nums = [0,0,1,1,1,2,2,3,3,4]
<strong>Output:</strong> 5, nums = [0,1,2,3,4,_,_,_,_,_]
<strong>Explanation:</strong> Your function should return k = 5, with the first five elements of nums being 0, 1, 2, 3, and 4 respectively.
</pre>

<h3 class="text-lg font-semibold mt-4 mb-2">Constraints:</h3>
<ul class="list-disc pl-5 space-y-1 text-gray-300">
  <li><code>1 &lt;= nums.length &lt;= 3 * 10<sup>4</sup></code></li>
  <li><code>-100 &lt;= nums[i] &lt;= 100</code></li>
  <li><code>nums</code> is sorted in <strong>non-decreasing</strong> order.</li>
</ul>""",
    "starter_code": {
        "python": """class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        pass
""",
        "kotlin": """class Solution {
    fun removeDuplicates(nums: IntArray): Int {
        // Write your code here
        return 0
    }
}
""",
    },
    "solution_code": {
        "python": """class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        if not nums:
            return 0
        k = 1
        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:
                nums[k] = nums[i]
                k += 1
        return k
""",
        "kotlin": """class Solution {
    fun removeDuplicates(nums: IntArray): Int {
        if (nums.isEmpty()) return 0
        var k = 1
        for (i in 1 until nums.size) {
            if (nums[i] != nums[i - 1]) {
                nums[k] = nums[i]
                k++
            }
        }
        return k
    }
}
""",
    },
    "test_code": {
        "python": """
if __name__ == "__main__":
    try:
        sol = Solution()
        nums1 = [1, 1, 2]
        k1 = sol.removeDuplicates(nums1)
        assert k1 == 2, f"Test 1 failed. Expected k=2, got {k1}"
        assert nums1[:k1] == [1, 2], f"Test 1 failed. First {k1} elements should be [1, 2], got {nums1[:k1]}"
        nums2 = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
        k2 = sol.removeDuplicates(nums2)
        assert k2 == 5, f"Test 2 failed. Expected k=5, got {k2}"
        assert nums2[:k2] == [0, 1, 2, 3, 4], f"Test 2 failed. First {k2} elements should be [0, 1, 2, 3, 4], got {nums2[:k2]}"
        nums3 = [1, 2, 3]
        k3 = sol.removeDuplicates(nums3)
        assert k3 == 3, f"Test 3 failed. Expected k=3, got {k3}"
        assert nums3[:k3] == [1, 2, 3], f"Test 3 failed. First {k3} elements should be [1, 2, 3], got {nums3[:k3]}"
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
        val nums1 = intArrayOf(1, 1, 2)
        val k1 = sol.removeDuplicates(nums1)
        require(k1 == 2) { "Test 1 failed. Expected k=2, got $k1" }
        require(nums1.take(k1).toList() == listOf(1, 2)) { "Test 1 failed. First $k1 elements should be [1, 2], got ${nums1.take(k1).toList()}" }
        val nums2 = intArrayOf(0, 0, 1, 1, 1, 2, 2, 3, 3, 4)
        val k2 = sol.removeDuplicates(nums2)
        require(k2 == 5) { "Test 2 failed. Expected k=5, got $k2" }
        require(nums2.take(k2).toList() == listOf(0, 1, 2, 3, 4)) { "Test 2 failed. First $k2 elements should be [0, 1, 2, 3, 4], got ${nums2.take(k2).toList()}" }
        val nums3 = intArrayOf(1, 2, 3)
        val k3 = sol.removeDuplicates(nums3)
        require(k3 == 3) { "Test 3 failed. Expected k=3, got $k3" }
        require(nums3.take(k3).toList() == listOf(1, 2, 3)) { "Test 3 failed. First $k3 elements should be [1, 2, 3], got ${nums3.take(k3).toList()}" }
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
