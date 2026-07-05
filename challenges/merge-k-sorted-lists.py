CHALLENGE = {
    "id": "merge-k-sorted-lists",
    "title": "Merge k Sorted Lists",
    "difficulty": "Hard",
    "description": """<p>Given an array of <code>k</code> sorted lists, merge them into one sorted list and return it.</p>
<p>Each list is sorted in ascending order. Return a single list containing all elements in sorted order.</p>

<h3 class="text-lg font-semibold mt-4 mb-2">Example 1:</h3>
<pre class="bg-gray-800 text-gray-100 p-3 rounded-lg font-mono text-sm mb-4">
<strong>Input:</strong> lists = [[1,4,5],[1,3,4],[2,6]]
<strong>Output:</strong> [1,1,2,3,4,4,5,6]
</pre>

<h3 class="text-lg font-semibold mt-4 mb-2">Example 2:</h3>
<pre class="bg-gray-800 text-gray-100 p-3 rounded-lg font-mono text-sm mb-4">
<strong>Input:</strong> lists = []
<strong>Output:</strong> []
</pre>

<h3 class="text-lg font-semibold mt-4 mb-2">Example 3:</h3>
<pre class="bg-gray-800 text-gray-100 p-3 rounded-lg font-mono text-sm mb-4">
<strong>Input:</strong> lists = [[]]
<strong>Output:</strong> []
</pre>

<h3 class="text-lg font-semibold mt-4 mb-2">Constraints:</h3>
<ul class="list-disc pl-5 space-y-1 text-gray-300">
  <li><code>k == lists.length</code></li>
  <li><code>0 &lt;= k &lt;= 10<sup>4</sup></code></li>
  <li><code>0 &lt;= lists[i].length &lt;= 500</code></li>
  <li><code>-10<sup>4</sup> &lt;= lists[i][j] &lt;= 10<sup>4</sup></code></li>
  <li><code>lists[i]</code> is sorted in ascending order.</li>
  <li>The sum of all <code>lists[i].length</code> will not exceed <code>10<sup>4</sup></code>.</li>
</ul>""",
    "starter_code": {
        "python": """class Solution:
    def mergeKLists(self, lists: list[list[int]]) -> list[int]:
        pass
""",
        "kotlin": """class Solution {
    fun mergeKLists(lists: Array<IntArray>): List<Int> {
        // Write your code here
        return listOf()
    }
}
""",
    },
    "solution_code": {
        "python": """import heapq

class Solution:
    def mergeKLists(self, lists: list[list[int]]) -> list[int]:
        heap = []
        for i, lst in enumerate(lists):
            if lst:
                heapq.heappush(heap, (lst[0], i, 0))
        res = []
        while heap:
            val, i, j = heapq.heappop(heap)
            res.append(val)
            if j + 1 < len(lists[i]):
                heapq.heappush(heap, (lists[i][j + 1], i, j + 1))
        return res
""",
        "kotlin": """import java.util.*

class Solution {
    fun mergeKLists(lists: Array<IntArray>): List<Int> {
        val pq = PriorityQueue<Pair<Int, Pair<Int, Int>>>(compareBy { it.first })
        for (i in lists.indices) {
            if (lists[i].isNotEmpty()) pq.add(Pair(lists[i][0], Pair(i, 0)))
        }
        val res = mutableListOf<Int>()
        while (pq.isNotEmpty()) {
            val (val_, pair) = pq.poll()
            val (i, j) = pair
            res.add(val_)
            if (j + 1 < lists[i].size) pq.add(Pair(lists[i][j + 1], Pair(i, j + 1)))
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
        res1 = sol.mergeKLists([[1,4,5],[1,3,4],[2,6]])
        assert res1 is not None, "Test 1 failed. Returned None."
        assert res1 == [1,1,2,3,4,4,5,6], f"Test 1 failed. Expected [1,1,2,3,4,4,5,6], got {res1}"
        res2 = sol.mergeKLists([])
        assert res2 is not None, "Test 2 failed. Returned None."
        assert res2 == [], f"Test 2 failed. Expected [], got {res2}"
        res3 = sol.mergeKLists([[]])
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
        val res1 = sol.mergeKLists(arrayOf(intArrayOf(1,4,5), intArrayOf(1,3,4), intArrayOf(2,6)))
        require(res1 == listOf(1,1,2,3,4,4,5,6)) { "Test 1 failed. Expected [1,1,2,3,4,4,5,6], got $res1" }
        val res2 = sol.mergeKLists(emptyArray())
        require(res2 == listOf<Int>()) { "Test 2 failed. Expected [], got $res2" }
        val res3 = sol.mergeKLists(arrayOf(intArrayOf()))
        require(res3 == listOf<Int>()) { "Test 3 failed. Expected [], got $res3" }
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
