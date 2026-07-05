CHALLENGE = {
    "id": "candy",
    "title": "Candy",
    "difficulty": "Hard",
    "description": """<p>There are <code>n</code> children standing in a line. Each child is assigned a rating value given in the integer array <code>ratings</code>.</p>
<p>You are giving candies to these children subjected to the following requirements:</p>
<ul class="list-disc pl-5 space-y-1 text-gray-300">
  <li>Each child must have at least one candy.</li>
  <li>Children with a higher rating get more candies than their neighbors.</li>
</ul>
<p>Return the minimum number of candies you need to have to distribute.</p>

<h3 class="text-lg font-semibold mt-4 mb-2">Example 1:</h3>
<pre class="bg-gray-800 text-gray-100 p-3 rounded-lg font-mono text-sm mb-4">
<strong>Input:</strong> ratings = [1,0,2]
<strong>Output:</strong> 5
<strong>Explanation:</strong> You can allocate [2,1,2] candies respectively.
</pre>

<h3 class="text-lg font-semibold mt-4 mb-2">Example 2:</h3>
<pre class="bg-gray-800 text-gray-100 p-3 rounded-lg font-mono text-sm mb-4">
<strong>Input:</strong> ratings = [1,2,2]
<strong>Output:</strong> 4
<strong>Explanation:</strong> You can allocate [1,2,1] candies respectively. The third child gets 1 candy because it satisfies the above conditions.
</pre>

<h3 class="text-lg font-semibold mt-4 mb-2">Constraints:</h3>
<ul class="list-disc pl-5 space-y-1 text-gray-300">
  <li><code>n == ratings.length</code></li>
  <li><code>1 &lt;= n &lt;= 2 * 10<sup>4</sup></code></li>
  <li><code>0 &lt;= ratings[i] &lt;= 2 * 10<sup>4</sup></code></li>
</ul>""",
    "starter_code": {
        "python": """class Solution:
    def candy(self, ratings: list[int]) -> int:
        pass
""",
        "kotlin": """class Solution {
    fun candy(ratings: IntArray): Int {
        // Write your code here
        return 0
    }
}
""",
    },
    "solution_code": {
        "python": """class Solution:
    def candy(self, ratings: list[int]) -> int:
        n = len(ratings)
        candies = [1] * n
        for i in range(1, n):
            if ratings[i] > ratings[i - 1]:
                candies[i] = candies[i - 1] + 1
        for i in range(n - 2, -1, -1):
            if ratings[i] > ratings[i + 1]:
                candies[i] = max(candies[i], candies[i + 1] + 1)
        return sum(candies)
""",
        "kotlin": """class Solution {
    fun candy(ratings: IntArray): Int {
        val n = ratings.size
        val candies = IntArray(n) { 1 }
        for (i in 1 until n) {
            if (ratings[i] > ratings[i - 1]) candies[i] = candies[i - 1] + 1
        }
        for (i in n - 2 downTo 0) {
            if (ratings[i] > ratings[i + 1]) candies[i] = maxOf(candies[i], candies[i + 1] + 1)
        }
        return candies.sum()
    }
}
""",
    },
    "test_code": {
        "python": """
if __name__ == "__main__":
    try:
        sol = Solution()
        res1 = sol.candy([1,0,2])
        assert res1 is not None, "Test 1 failed. Returned None."
        assert res1 == 5, f"Test 1 failed. Expected 5, got {res1}"
        res2 = sol.candy([1,2,2])
        assert res2 is not None, "Test 2 failed. Returned None."
        assert res2 == 4, f"Test 2 failed. Expected 4, got {res2}"
        res3 = sol.candy([1])
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
        val res1 = sol.candy(intArrayOf(1,0,2))
        require(res1 == 5) { "Test 1 failed. Expected 5, got $res1" }
        val res2 = sol.candy(intArrayOf(1,2,2))
        require(res2 == 4) { "Test 2 failed. Expected 4, got $res2" }
        val res3 = sol.candy(intArrayOf(1))
        require(res3 == 1) { "Test 3 failed. Expected 1, got $res3" }
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
