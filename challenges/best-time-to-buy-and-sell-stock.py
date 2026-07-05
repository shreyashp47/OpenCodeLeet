CHALLENGE = {
    "id": "best-time-to-buy-and-sell-stock",
    "title": "Best Time to Buy and Sell Stock",
    "difficulty": "Easy",
    "description": """<p>You are given an array <code>prices</code> where <code>prices[i]</code> is the price of a given stock on the <code>i<sup>th</sup></code> day.</p>
<p>You want to maximize your profit by choosing a <strong>single day</strong> to buy one stock and choosing a <strong>different day in the future</strong> to sell that stock.</p>
<p>Return <em>the maximum profit you can achieve</em> from this transaction. If you cannot achieve any profit, return <code>0</code>.</p>

<h3 class="text-lg font-semibold mt-4 mb-2">Example 1:</h3>
<pre class="bg-gray-800 text-gray-100 p-3 rounded-lg font-mono text-sm mb-4">
<strong>Input:</strong> prices = [7,1,5,3,6,4]
<strong>Output:</strong> 5
<strong>Explanation:</strong> Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
</pre>

<h3 class="text-lg font-semibold mt-4 mb-2">Example 2:</h3>
<pre class="bg-gray-800 text-gray-100 p-3 rounded-lg font-mono text-sm mb-4">
<strong>Input:</strong> prices = [7,6,4,3,1]
<strong>Output:</strong> 0
<strong>Explanation:</strong> No transaction results in a positive profit.
</pre>

<h3 class="text-lg font-semibold mt-4 mb-2">Constraints:</h3>
<ul class="list-disc pl-5 space-y-1 text-gray-300">
  <li><code>1 &lt;= prices.length &lt;= 10<sup>5</sup></code></li>
  <li><code>0 &lt;= prices[i] &lt;= 10<sup>4</sup></code></li>
</ul>""",
    "starter_code": {
        "python": """class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        pass
""",
        "kotlin": """class Solution {
    fun maxProfit(prices: IntArray): Int {
        // Write your code here
        return 0
    }
}
""",
    },
    "solution_code": {
        "python": """class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        min_price = float('inf')
        max_profit = 0
        for price in prices:
            if price < min_price:
                min_price = price
            elif price - min_price > max_profit:
                max_profit = price - min_price
        return max_profit
""",
        "kotlin": """class Solution {
    fun maxProfit(prices: IntArray): Int {
        var minPrice = Int.MAX_VALUE
        var maxProfit = 0
        for (price in prices) {
            if (price < minPrice) {
                minPrice = price
            } else if (price - minPrice > maxProfit) {
                maxProfit = price - minPrice
            }
        }
        return maxProfit
    }
}
""",
    },
    "test_code": {
        "python": """
if __name__ == "__main__":
    try:
        sol = Solution()
        res1 = sol.maxProfit([7, 1, 5, 3, 6, 4])
        assert res1 == 5, f"Test 1 failed. Expected 5, got {res1}"
        res2 = sol.maxProfit([7, 6, 4, 3, 1])
        assert res2 == 0, f"Test 2 failed. Expected 0, got {res2}"
        res3 = sol.maxProfit([2, 4, 1])
        assert res3 == 2, f"Test 3 failed. Expected 2, got {res3}"
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
        val res1 = sol.maxProfit(intArrayOf(7, 1, 5, 3, 6, 4))
        require(res1 == 5) { "Test 1 failed. Expected 5, got $res1" }
        val res2 = sol.maxProfit(intArrayOf(7, 6, 4, 3, 1))
        require(res2 == 0) { "Test 2 failed. Expected 0, got $res2" }
        val res3 = sol.maxProfit(intArrayOf(2, 4, 1))
        require(res3 == 2) { "Test 3 failed. Expected 2, got $res3" }
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
