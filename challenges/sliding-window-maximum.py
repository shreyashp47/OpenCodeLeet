CHALLENGE = {
    "id": "sliding-window-maximum",
    "title": "Sliding Window Maximum",
    "difficulty": "Hard",
    "description": """<p>You are given an array of integers <code>nums</code> and a sliding window of size <code>k</code> which moves from the very left to the very right. You can only see the <code>k</code> numbers in the window. Each time the sliding window moves right by one position.</p>
<p>Return the <em>max sliding window</em> (an array of the maximum values for each window).</p>

<h3 class="text-lg font-semibold mt-4 mb-2">Example 1:</h3>
<pre class="bg-gray-800 text-gray-100 p-3 rounded-lg font-mono text-sm mb-4">
<strong>Input:</strong> nums = [1,3,-1,-3,5,3,6,7], k = 3
<strong>Output:</strong> [3,3,5,5,6,7]
<strong>Explanation:</strong>
Window position                Max
---------------               -----
[1  3  -1] -3  5  3  6  7      3
 1 [3  -1  -3] 5  3  6  7      3
 1  3 [-1  -3  5] 3  6  7      5
 1  3  -1 [-3  5  3] 6  7      5
 1  3  -1  -3 [5  3  6] 7      6
 1  3  -1  -3  5 [3  6  7]     7
</pre>

<h3 class="text-lg font-semibold mt-4 mb-2">Example 2:</h3>
<pre class="bg-gray-800 text-gray-100 p-3 rounded-lg font-mono text-sm mb-4">
<strong>Input:</strong> nums = [1], k = 1
<strong>Output:</strong> [1]
</pre>

<h3 class="text-lg font-semibold mt-4 mb-2">Constraints:</h3>
<ul class="list-disc pl-5 space-y-1 text-gray-300">
  <li><code>1 &lt;= nums.length &lt;= 10<sup>5</sup></code></li>
  <li><code>-10<sup>4</sup> &lt;= nums[i] &lt;= 10<sup>4</sup></code></li>
  <li><code>1 &lt;= k &lt;= nums.length</code></li>
</ul>""",
    "starter_code": {
        "python": """class Solution:
    def maxSlidingWindow(self, nums: list[int], k: int) -> list[int]:
        pass
""",
        "kotlin": """class Solution {
    fun maxSlidingWindow(nums: IntArray, k: Int): List<Int> {
        // Write your code here
        return listOf()
    }
}
""",
    },
    "solution_code": {
        "python": """from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: list[int], k: int) -> list[int]:
        dq = deque()
        res = []
        for i, v in enumerate(nums):
            while dq and nums[dq[-1]] < v:
                dq.pop()
            dq.append(i)
            if dq[0] == i - k:
                dq.popleft()
            if i >= k - 1:
                res.append(nums[dq[0]])
        return res
""",
        "kotlin": """import java.util.*

class Solution {
    fun maxSlidingWindow(nums: IntArray, k: Int): List<Int> {
        val dq = ArrayDeque<Int>()
        val res = mutableListOf<Int>()
        for (i in nums.indices) {
            while (dq.isNotEmpty() && nums[dq.last()] < nums[i]) dq.removeLast()
            dq.addLast(i)
            if (dq.first() == i - k) dq.removeFirst()
            if (i >= k - 1) res.add(nums[dq.first()])
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
        res1 = sol.maxSlidingWindow([1,3,-1,-3,5,3,6,7], 3)
        assert res1 is not None, "Test 1 failed. Returned None."
        assert res1 == [3,3,5,5,6,7], f"Test 1 failed. Expected [3,3,5,5,6,7], got {res1}"
        res2 = sol.maxSlidingWindow([1], 1)
        assert res2 is not None, "Test 2 failed. Returned None."
        assert res2 == [1], f"Test 2 failed. Expected [1], got {res2}"
        res3 = sol.maxSlidingWindow([1,-1], 1)
        assert res3 is not None, "Test 3 failed. Returned None."
        assert res3 == [1,-1], f"Test 3 failed. Expected [1,-1], got {res3}"
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
        val res1 = sol.maxSlidingWindow(intArrayOf(1,3,-1,-3,5,3,6,7), 3)
        require(res1 == listOf(3,3,5,5,6,7)) { "Test 1 failed. Expected [3,3,5,5,6,7], got $res1" }
        val res2 = sol.maxSlidingWindow(intArrayOf(1), 1)
        require(res2 == listOf(1)) { "Test 2 failed. Expected [1], got $res2" }
        val res3 = sol.maxSlidingWindow(intArrayOf(1,-1), 1)
        require(res3 == listOf(1,-1)) { "Test 3 failed. Expected [1,-1], got $res3" }
        println("ALL_TESTS_PASSED")
    } catch (e: IllegalArgumentException) {
        println("TEST_FAILED: \${e.message}")
    } catch (e: Exception) {
        println("ERROR: \${e.message}")
    }
}
""",
    },
}
