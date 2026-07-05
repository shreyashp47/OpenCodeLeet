CHALLENGE = {
    "id": "happy-number",
    "title": "Happy Number",
    "difficulty": "Easy",
    "description": """<p>Write an algorithm to determine if a number <code>n</code> is happy.</p>
<p>A <strong>happy number</strong> is a number defined by the following process:</p>
<ul class="list-disc pl-5 space-y-1 text-gray-300">
  <li>Starting with any positive integer, replace the number by the sum of the squares of its digits.</li>
  <li>Repeat the process until the number equals 1 (where it will stay), or it <strong>loops endlessly in a cycle</strong> which does not include 1.</li>
  <li>Those numbers for which this process <strong>ends in 1</strong> are happy.</li>
</ul>
<p>Return <code>true</code> <em>if</em> <code>n</code> <em>is a happy number, and</em> <code>false</code> <em>if not</em>.</p>

<h3 class="text-lg font-semibold mt-4 mb-2">Example 1:</h3>
<pre class="bg-gray-800 text-gray-100 p-3 rounded-lg font-mono text-sm mb-4">
<strong>Input:</strong> n = 19
<strong>Output:</strong> true
<strong>Explanation:</strong>
1<sup>2</sup> + 9<sup>2</sup> = 82
8<sup>2</sup> + 2<sup>2</sup> = 68
6<sup>2</sup> + 8<sup>2</sup> = 100
1<sup>2</sup> + 0<sup>2</sup> + 0<sup>2</sup> = 1
</pre>

<h3 class="text-lg font-semibold mt-4 mb-2">Example 2:</h3>
<pre class="bg-gray-800 text-gray-100 p-3 rounded-lg font-mono text-sm mb-4">
<strong>Input:</strong> n = 2
<strong>Output:</strong> false
</pre>

<h3 class="text-lg font-semibold mt-4 mb-2">Constraints:</h3>
<ul class="list-disc pl-5 space-y-1 text-gray-300">
  <li><code>1 &lt;= n &lt;= 2<sup>31</sup> - 1</code></li>
</ul>""",
    "starter_code": {
        "python": """class Solution:
    def isHappy(self, n: int) -> bool:
        pass
""",
        "kotlin": """class Solution {
    fun isHappy(n: Int): Boolean {
        // Write your code here
        return false
    }
}
""",
    },
    "solution_code": {
        "python": """class Solution:
    def isHappy(self, n: int) -> bool:
        def sum_squares(num: int) -> int:
            total = 0
            while num:
                total += (num % 10) ** 2
                num //= 10
            return total

        seen = set()
        while n != 1 and n not in seen:
            seen.add(n)
            n = sum_squares(n)
        return n == 1
""",
        "kotlin": """class Solution {
    fun isHappy(n: Int): Boolean {
        fun sumSquares(num: Int): Int {
            var x = num
            var total = 0
            while (x > 0) {
                val d = x % 10
                total += d * d
                x /= 10
            }
            return total
        }

        val seen = mutableSetOf<Int>()
        var current = n
        while (current != 1 && current !in seen) {
            seen.add(current)
            current = sumSquares(current)
        }
        return current == 1
    }
}
""",
    },
    "test_code": {
        "python": """
if __name__ == "__main__":
    try:
        sol = Solution()
        assert sol.isHappy(19) == True, "Test 1 failed. Expected True for 19"
        assert sol.isHappy(2) == False, "Test 2 failed. Expected False for 2"
        assert sol.isHappy(1) == True, "Test 3 failed. Expected True for 1"
        assert sol.isHappy(7) == True, "Test 4 failed. Expected True for 7"
        assert sol.isHappy(4) == False, "Test 5 failed. Expected False for 4"
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
        require(sol.isHappy(19) == true) { "Test 1 failed. Expected true for 19" }
        require(sol.isHappy(2) == false) { "Test 2 failed. Expected false for 2" }
        require(sol.isHappy(1) == true) { "Test 3 failed. Expected true for 1" }
        require(sol.isHappy(7) == true) { "Test 4 failed. Expected true for 7" }
        require(sol.isHappy(4) == false) { "Test 5 failed. Expected false for 4" }
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
