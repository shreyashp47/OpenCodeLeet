CHALLENGE = {
    "id": "intersection-of-two-arrays",
    "title": "Intersection of Two Arrays",
    "difficulty": "Easy",
    "description": """<p>Given two integer arrays <code>nums1</code> and <code>nums2</code>, return <em>an array of their intersection</em>. Each element in the result must be <strong>unique</strong> and you may return the result in <strong>any order</strong>.</p>

<h3 class="text-lg font-semibold mt-4 mb-2">Example 1:</h3>
<pre class="bg-gray-800 text-gray-100 p-3 rounded-lg font-mono text-sm mb-4">
<strong>Input:</strong> nums1 = [1,2,2,1], nums2 = [2,2]
<strong>Output:</strong> [2]
</pre>

<h3 class="text-lg font-semibold mt-4 mb-2">Example 2:</h3>
<pre class="bg-gray-800 text-gray-100 p-3 rounded-lg font-mono text-sm mb-4">
<strong>Input:</strong> nums1 = [4,9,5], nums2 = [9,4,9,8,4]
<strong>Output:</strong> [9,4]
<strong>Explanation:</strong> [4,9] is also accepted.
</pre>

<h3 class="text-lg font-semibold mt-4 mb-2">Constraints:</h3>
<ul class="list-disc pl-5 space-y-1 text-gray-300">
  <li><code>1 &lt;= nums1.length, nums2.length &lt;= 1000</code></li>
  <li><code>0 &lt;= nums1[i], nums2[i] &lt;= 1000</code></li>
</ul>""",
    "starter_code": {
        "python": """class Solution:
    def intersection(self, nums1: list[int], nums2: list[int]) -> list[int]:
        pass
""",
        "kotlin": """class Solution {
    fun intersection(nums1: IntArray, nums2: IntArray): IntArray {
        // Write your code here
        return intArrayOf()
    }
}
""",
    },
    "solution_code": {
        "python": """class Solution:
    def intersection(self, nums1: list[int], nums2: list[int]) -> list[int]:
        set1 = set(nums1)
        set2 = set(nums2)
        return list(set1 & set2)
""",
        "kotlin": """class Solution {
    fun intersection(nums1: IntArray, nums2: IntArray): IntArray {
        val set1 = nums1.toSet()
        val set2 = nums2.toSet()
        return set1.intersect(set2).toIntArray()
    }
}
""",
    },
    "test_code": {
        "python": """
if __name__ == "__main__":
    try:
        sol = Solution()
        res1 = sol.intersection([1, 2, 2, 1], [2, 2])
        assert res1 is not None, "Test 1 failed. Returned None."
        assert sorted(res1) == [2], f"Test 1 failed. Expected [2], got {res1}"
        res2 = sol.intersection([4, 9, 5], [9, 4, 9, 8, 4])
        assert res2 is not None, "Test 2 failed. Returned None."
        assert sorted(res2) == [4, 9], f"Test 2 failed. Expected [4, 9], got {res2}"
        res3 = sol.intersection([1, 2, 3], [4, 5, 6])
        assert res3 is not None, "Test 3 failed. Returned None."
        assert res3 == [], f"Test 3 failed. Expected [], got {res3}"
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
        val res1 = sol.intersection(intArrayOf(1, 2, 2, 1), intArrayOf(2, 2))
        require(res1.sorted().toList() == listOf(2)) { "Test 1 failed. Expected [2], got ${res1.contentToString()}" }
        val res2 = sol.intersection(intArrayOf(4, 9, 5), intArrayOf(9, 4, 9, 8, 4))
        require(res2.sorted().toList() == listOf(4, 9)) { "Test 2 failed. Expected [4, 9], got ${res2.contentToString()}" }
        val res3 = sol.intersection(intArrayOf(1, 2, 3), intArrayOf(4, 5, 6))
        require(res3.isEmpty()) { "Test 3 failed. Expected [], got ${res3.contentToString()}" }
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
