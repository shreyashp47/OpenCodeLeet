CHALLENGE = {
    "id": "longest-increasing-subsequence",
    "title": "Longest Increasing Subsequence",
    "difficulty": "Medium",
    "description": """<p>Given an integer array <code>nums</code>, return <em>the length of the longest strictly increasing subsequence</em>.</p>

<h3 class="text-lg font-semibold mt-4 mb-2">Example 1:</h3>
<pre class="bg-gray-800 text-gray-100 p-3 rounded-lg font-mono text-sm mb-4">
<strong>Input:</strong> nums = [10,9,2,5,3,7,101,18]
<strong>Output:</strong> 4
<strong>Explanation:</strong> The longest increasing subsequence is [2,3,7,101], therefore the length is 4.
</pre>

<h3 class="text-lg font-semibold mt-4 mb-2">Example 2:</h3>
<pre class="bg-gray-800 text-gray-100 p-3 rounded-lg font-mono text-sm mb-4">
<strong>Input:</strong> nums = [0,1,0,3,2,3]
<strong>Output:</strong> 4
</pre>

<h3 class="text-lg font-semibold mt-4 mb-2">Example 3:</h3>
<pre class="bg-gray-800 text-gray-100 p-3 rounded-lg font-mono text-sm mb-4">
<strong>Input:</strong> nums = [7,7,7,7,7,7,7]
<strong>Output:</strong> 1
</pre>

<h3 class="text-lg font-semibold mt-4 mb-2">Constraints:</h3>
<ul class="list-disc pl-5 space-y-1 text-gray-300">
  <li><code>1 &lt;= nums.length &lt;= 2500</code></li>
  <li><code>-10<sup>4</sup> &lt;= nums[i] &lt;= 10<sup>4</sup></code></li>
</ul>""",
    "starter_code": {
        "python": """class Solution:
    def lengthOfLIS(self, nums: list[int]) -> int:
        pass
""",
        "kotlin": """class Solution {
    fun lengthOfLIS(nums: IntArray): Int {
        // Write your code here
        return 0
    }
}
""",
    },
    "solution_code": {
        "python": """class Solution:
    def lengthOfLIS(self, nums: list[int]) -> int:
        tails = []
        for x in nums:
            i = 0
            j = len(tails)
            while i < j:
                m = (i + j) // 2
                if tails[m] < x:
                    i = m + 1
                else:
                    j = m
            if i == len(tails):
                tails.append(x)
            else:
                tails[i] = x
        return len(tails)
""",
        "kotlin": """class Solution {
    fun lengthOfLIS(nums: IntArray): Int {
        val tails = mutableListOf<Int>()
        for (x in nums) {
            var i = 0
            var j = tails.size
            while (i < j) {
                val m = (i + j) / 2
                if (tails[m] < x) i = m + 1 else j = m
            }
            if (i == tails.size) tails.add(x) else tails[i] = x
        }
        return tails.size
    }
}
""",
    },
    "test_code": {
        "python": """
if __name__ == "__main__":
    try:
        sol = Solution()
        res1 = sol.lengthOfLIS([10, 9, 2, 5, 3, 7, 101, 18])
        assert res1 is not None, "Test 1 failed. Returned None."
        assert res1 == 4, f"Test 1 failed. Expected 4, got {res1}"
        res2 = sol.lengthOfLIS([0, 1, 0, 3, 2, 3])
        assert res2 is not None, "Test 2 failed. Returned None."
        assert res2 == 4, f"Test 2 failed. Expected 4, got {res2}"
        res3 = sol.lengthOfLIS([7, 7, 7, 7, 7, 7, 7])
        assert res3 is not None, "Test 3 failed. Returned None."
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
        val res1 = sol.lengthOfLIS(intArrayOf(10, 9, 2, 5, 3, 7, 101, 18))
        require(res1 == 4) { "Test 1 failed. Expected 4, got $res1" }
        val res2 = sol.lengthOfLIS(intArrayOf(0, 1, 0, 3, 2, 3))
        require(res2 == 4) { "Test 2 failed. Expected 4, got $res2" }
        val res3 = sol.lengthOfLIS(intArrayOf(7, 7, 7, 7, 7, 7, 7))
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
