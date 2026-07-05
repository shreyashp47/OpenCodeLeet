CHALLENGE = {
    "id": "top-k-frequent-elements",
    "title": "Top K Frequent Elements",
    "difficulty": "Medium",
    "description": """<p>Given an integer array <code>nums</code> and an integer <code>k</code>, return <em>the <code>k</code> most frequent elements</em>. You may return the answer in <strong>any order</strong>.</p>

<h3 class="text-lg font-semibold mt-4 mb-2">Example 1:</h3>
<pre class="bg-gray-800 text-gray-100 p-3 rounded-lg font-mono text-sm mb-4">
<strong>Input:</strong> nums = [1,1,1,2,2,3], k = 2
<strong>Output:</strong> [1,2]
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
  <li><code>k</code> is in the range <code>[1, the number of unique elements in the array]</code>.</li>
  <li>It is <strong>guaranteed</strong> that the answer is <strong>unique</strong>.</li>
</ul>""",
    "starter_code": {
        "python": """class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        pass
""",
        "kotlin": """class Solution {
    fun topKFrequent(nums: IntArray, k: Int): IntArray {
        // Write your code here
        return intArrayOf()
    }
}
""",
    },
    "solution_code": {
        "python": """class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        freq = {}
        for num in nums:
            freq[num] = freq.get(num, 0) + 1
        buckets = [[] for _ in range(len(nums) + 1)]
        for num, count in freq.items():
            buckets[count].append(num)
        result = []
        for i in range(len(buckets) - 1, 0, -1):
            for num in buckets[i]:
                result.append(num)
                if len(result) == k:
                    return result
        return result
""",
        "kotlin": """class Solution {
    fun topKFrequent(nums: IntArray, k: Int): IntArray {
        val freq = mutableMapOf<Int, Int>()
        for (num in nums) freq[num] = freq.getOrDefault(num, 0) + 1
        val buckets = Array<MutableList<Int>>(nums.size + 1) { mutableListOf() }
        for ((num, count) in freq) buckets[count].add(num)
        val result = mutableListOf<Int>()
        for (i in buckets.indices.reversed()) {
            for (num in buckets[i]) {
                result.add(num)
                if (result.size == k) return result.toIntArray()
            }
        }
        return result.toIntArray()
    }
}
""",
    },
    "test_code": {
        "python": """
if __name__ == "__main__":
    try:
        sol = Solution()
        res1 = sol.topKFrequent([1, 1, 1, 2, 2, 3], 2)
        assert res1 is not None, "Test 1 failed. Returned None."
        assert sorted(res1) == [1, 2], f"Test 1 failed. Expected [1, 2], got {res1}"
        res2 = sol.topKFrequent([1], 1)
        assert res2 is not None, "Test 2 failed. Returned None."
        assert sorted(res2) == [1], f"Test 2 failed. Expected [1], got {res2}"
        res3 = sol.topKFrequent([4, 1, -1, 2, -1, 2, 3], 2)
        assert res3 is not None, "Test 3 failed. Returned None."
        assert sorted(res3) == [-1, 2], f"Test 3 failed. Expected [-1, 2], got {res3}"
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
        val res1 = sol.topKFrequent(intArrayOf(1, 1, 1, 2, 2, 3), 2)
        require(res1.size == 2) { "Test 1 failed: wrong size" }
        require(res1.sorted() == listOf(1, 2)) { "Test 1 failed. Expected [1, 2], got ${res1.contentToString()}" }
        val res2 = sol.topKFrequent(intArrayOf(1), 1)
        require(res2 contentEquals intArrayOf(1)) { "Test 2 failed. Expected [1], got ${res2.contentToString()}" }
        val res3 = sol.topKFrequent(intArrayOf(4, 1, -1, 2, -1, 2, 3), 2)
        require(res3.sorted() == listOf(-1, 2)) { "Test 3 failed. Expected [-1, 2], got ${res3.contentToString()}" }
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
