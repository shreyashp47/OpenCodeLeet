CHALLENGE = {
    "id": "coin-change",
    "title": "Coin Change",
    "difficulty": "Medium",
    "description": """<p>You are given an integer array <code>coins</code> representing coins of different denominations and an integer <code>amount</code> representing a total amount of money.</p>
<p>Return <em>the fewest number of coins that you need to make up that amount</em>. If that amount of money cannot be made up by any combination of the coins, return <code>-1</code>.</p>
<p>You may assume that you have an infinite number of each kind of coin.</p>

<h3 class="text-lg font-semibold mt-4 mb-2">Example 1:</h3>
<pre class="bg-gray-800 text-gray-100 p-3 rounded-lg font-mono text-sm mb-4">
<strong>Input:</strong> coins = [1,2,5], amount = 11
<strong>Output:</strong> 3
<strong>Explanation:</strong> 11 = 5 + 5 + 1
</pre>

<h3 class="text-lg font-semibold mt-4 mb-2">Example 2:</h3>
<pre class="bg-gray-800 text-gray-100 p-3 rounded-lg font-mono text-sm mb-4">
<strong>Input:</strong> coins = [2], amount = 3
<strong>Output:</strong> -1
</pre>

<h3 class="text-lg font-semibold mt-4 mb-2">Example 3:</h3>
<pre class="bg-gray-800 text-gray-100 p-3 rounded-lg font-mono text-sm mb-4">
<strong>Input:</strong> coins = [1], amount = 0
<strong>Output:</strong> 0
</pre>

<h3 class="text-lg font-semibold mt-4 mb-2">Constraints:</h3>
<ul class="list-disc pl-5 space-y-1 text-gray-300">
  <li><code>1 &lt;= coins.length &lt;= 12</code></li>
  <li><code>1 &lt;= coins[i] &lt;= 2<sup>31</sup> - 1</code></li>
  <li><code>0 &lt;= amount &lt;= 10<sup>4</sup></code></li>
</ul>""",
    "starter_code": {
        "python": """class Solution:
    def coinChange(self, coins: list[int], amount: int) -> int:
        pass
""",
        "kotlin": """class Solution {
    fun coinChange(coins: IntArray, amount: Int): Int {
        // Write your code here
        return 0
    }
}
""",
    },
    "solution_code": {
        "python": """class Solution:
    def coinChange(self, coins: list[int], amount: int) -> int:
        dp = [amount + 1] * (amount + 1)
        dp[0] = 0
        for a in range(1, amount + 1):
            for c in coins:
                if a - c >= 0:
                    dp[a] = min(dp[a], 1 + dp[a - c])
        return dp[amount] if dp[amount] != amount + 1 else -1
""",
        "kotlin": """class Solution {
    fun coinChange(coins: IntArray, amount: Int): Int {
        val dp = IntArray(amount + 1) { amount + 1 }
        dp[0] = 0
        for (a in 1..amount) {
            for (c in coins) {
                if (a - c >= 0) {
                    dp[a] = minOf(dp[a], 1 + dp[a - c])
                }
            }
        }
        return if (dp[amount] != amount + 1) dp[amount] else -1
    }
}
""",
    },
    "test_code": {
        "python": """
if __name__ == "__main__":
    try:
        sol = Solution()
        res1 = sol.coinChange([1, 2, 5], 11)
        assert res1 is not None, "Test 1 failed. Returned None."
        assert res1 == 3, f"Test 1 failed. Expected 3, got {res1}"
        res2 = sol.coinChange([2], 3)
        assert res2 is not None, "Test 2 failed. Returned None."
        assert res2 == -1, f"Test 2 failed. Expected -1, got {res2}"
        res3 = sol.coinChange([1], 0)
        assert res3 is not None, "Test 3 failed. Returned None."
        assert res3 == 0, f"Test 3 failed. Expected 0, got {res3}"
        res4 = sol.coinChange([1, 5, 10, 25], 30)
        assert res4 is not None, "Test 4 failed. Returned None."
        assert res4 == 3, f"Test 4 failed. Expected 3, got {res4}"
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
        val res1 = sol.coinChange(intArrayOf(1, 2, 5), 11)
        require(res1 == 3) { "Test 1 failed. Expected 3, got $res1" }
        val res2 = sol.coinChange(intArrayOf(2), 3)
        require(res2 == -1) { "Test 2 failed. Expected -1, got $res2" }
        val res3 = sol.coinChange(intArrayOf(1), 0)
        require(res3 == 0) { "Test 3 failed. Expected 0, got $res3" }
        val res4 = sol.coinChange(intArrayOf(1, 5, 10, 25), 30)
        require(res4 == 3) { "Test 4 failed. Expected 3, got $res4" }
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
