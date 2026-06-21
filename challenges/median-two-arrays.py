CHALLENGE = {
    "id": "median-two-arrays",
    "title": "Median of Two Sorted Arrays",
    "difficulty": "Hard",
    "description": """<p>Given two sorted arrays <code>nums1</code> and <code>nums2</code> of size <code>m</code> and <code>n</code> respectively, return <strong>the median</strong> of the two sorted arrays.</p>
<p>The overall run time complexity should be <code>O(log (m+n))</code>.</p>

<h3 class="text-lg font-semibold mt-4 mb-2">Example 1:</h3>
<pre class="bg-gray-800 text-gray-100 p-3 rounded-lg font-mono text-sm mb-4">
<strong>Input:</strong> nums1 = [1,3], nums2 = [2]
<strong>Output:</strong> 2.00000
<strong>Explanation:</strong> Merged array = [1,2,3] and median is 2.
</pre>

<h3 class="text-lg font-semibold mt-4 mb-2">Example 2:</h3>
<pre class="bg-gray-800 text-gray-100 p-3 rounded-lg font-mono text-sm mb-4">
<strong>Input:</strong> nums1 = [1,2], nums2 = [3,4]
<strong>Output:</strong> 2.50000
<strong>Explanation:</strong> Merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.
</pre>

<h3 class="text-lg font-semibold mt-4 mb-2">Constraints:</h3>
<ul class="list-disc pl-5 space-y-1 text-gray-300">
  <li><code>0 &lt;= m, n &lt;= 1000</code></li>
  <li><code>1 &lt;= m + n &lt;= 2000</code></li>
  <li><code>-10<sup>6</sup> &lt;= nums1[i], nums2[i] &lt;= 10<sup>6</sup></code></li>
</ul>""",
    "starter_code": {
        "python": """class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        pass
""",
        "kotlin": """class Solution {
    fun findMedianSortedArrays(nums1: IntArray, nums2: IntArray): Double {
        // Write your code here
        return 0.0
    }
}
""",
    },
    "solution_code": {
        "python": """class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        m, n = len(nums1), len(nums2)
        total = m + n
        half = total // 2
        left, right = 0, m
        while left <= right:
            i = (left + right) // 2
            j = half - i
            left1 = nums1[i - 1] if i > 0 else float("-inf")
            right1 = nums1[i] if i < m else float("inf")
            left2 = nums2[j - 1] if j > 0 else float("-inf")
            right2 = nums2[j] if j < n else float("inf")
            if left1 <= right2 and left2 <= right1:
                if total % 2:
                    return min(right1, right2)
                return (max(left1, left2) + min(right1, right2)) / 2
            elif left1 > right2:
                right = i - 1
            else:
                left = i + 1
""",
        "kotlin": """class Solution {
    fun findMedianSortedArrays(nums1: IntArray, nums2: IntArray): Double {
        var a = nums1
        var b = nums2
        if (a.size > b.size) {
            val tmp = a; a = b; b = tmp
        }
        val m = a.size
        val n = b.size
        val total = m + n
        val half = total / 2
        var left = 0
        var right = m
        while (left <= right) {
            val i = (left + right) / 2
            val j = half - i
            val leftA = if (i > 0) a[i - 1].toDouble() else Double.NEGATIVE_INFINITY
            val rightA = if (i < m) a[i].toDouble() else Double.POSITIVE_INFINITY
            val leftB = if (j > 0) b[j - 1].toDouble() else Double.NEGATIVE_INFINITY
            val rightB = if (j < n) b[j].toDouble() else Double.POSITIVE_INFINITY
            if (leftA <= rightB && leftB <= rightA) {
                return if (total % 2 == 1) minOf(rightA, rightB)
                else (maxOf(leftA, leftB) + minOf(rightA, rightB)) / 2.0
            } else if (leftA > rightB) {
                right = i - 1
            } else {
                left = i + 1
            }
        }
        return 0.0
    }
}
""",
    },
    "test_code": {
        "python": """
if __name__ == "__main__":
    try:
        sol = Solution()
        res1 = sol.findMedianSortedArrays([1,3], [2])
        assert abs(res1 - 2.0) < 1e-5, f"Test 1 failed. Expected 2.0, got {res1}"
        res2 = sol.findMedianSortedArrays([1,2], [3,4])
        assert abs(res2 - 2.5) < 1e-5, f"Test 2 failed. Expected 2.5, got {res2}"
        res3 = sol.findMedianSortedArrays([0,0], [0,0])
        assert abs(res3 - 0.0) < 1e-5, f"Test 3 failed. Expected 0.0, got {res3}"
        res4 = sol.findMedianSortedArrays([], [1])
        assert abs(res4 - 1.0) < 1e-5, f"Test 4 failed. Expected 1.0, got {res4}"
        res5 = sol.findMedianSortedArrays([2], [])
        assert abs(res5 - 2.0) < 1e-5, f"Test 5 failed. Expected 2.0, got {res5}"
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
        require(kotlin.math.abs(sol.findMedianSortedArrays(intArrayOf(1,3), intArrayOf(2)) - 2.0) < 1e-5) { "Test 1 failed" }
        require(kotlin.math.abs(sol.findMedianSortedArrays(intArrayOf(1,2), intArrayOf(3,4)) - 2.5) < 1e-5) { "Test 2 failed" }
        require(kotlin.math.abs(sol.findMedianSortedArrays(intArrayOf(0,0), intArrayOf(0,0)) - 0.0) < 1e-5) { "Test 3 failed" }
        require(kotlin.math.abs(sol.findMedianSortedArrays(intArrayOf(), intArrayOf(1)) - 1.0) < 1e-5) { "Test 4 failed" }
        require(kotlin.math.abs(sol.findMedianSortedArrays(intArrayOf(2), intArrayOf()) - 2.0) < 1e-5) { "Test 5 failed" }
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
