CHALLENGE = {
    "id": "fizz-buzz",
    "title": "Fizz Buzz",
    "difficulty": "Easy",
    "description": """<p>Given an integer <code>n</code>, return <em>a string array</em> <code>answer</code> (<strong>1-indexed</strong>) where:</p>
<ul class="list-disc pl-5 space-y-1 text-gray-300">
  <li><code>answer[i] == "FizzBuzz"</code> if <code>i</code> is divisible by <code>3</code> and <code>5</code>.</li>
  <li><code>answer[i] == "Fizz"</code> if <code>i</code> is divisible by <code>3</code>.</li>
  <li><code>answer[i] == "Buzz"</code> if <code>i</code> is divisible by <code>5</code>.</li>
  <li><code>answer[i] == i</code> (as a string) otherwise.</li>
</ul>

<h3 class="text-lg font-semibold mt-4 mb-2">Example 1:</h3>
<pre class="bg-gray-800 text-gray-100 p-3 rounded-lg font-mono text-sm mb-4">
<strong>Input:</strong> n = 3
<strong>Output:</strong> ["1","2","Fizz"]
</pre>

<h3 class="text-lg font-semibold mt-4 mb-2">Example 2:</h3>
<pre class="bg-gray-800 text-gray-100 p-3 rounded-lg font-mono text-sm mb-4">
<strong>Input:</strong> n = 5
<strong>Output:</strong> ["1","2","Fizz","4","Buzz"]
</pre>

<h3 class="text-lg font-semibold mt-4 mb-2">Example 3:</h3>
<pre class="bg-gray-800 text-gray-100 p-3 rounded-lg font-mono text-sm mb-4">
<strong>Input:</strong> n = 15
<strong>Output:</strong> ["1","2","Fizz","4","Buzz","Fizz","7","8","Fizz","Buzz","11","Fizz","13","14","FizzBuzz"]
</pre>

<h3 class="text-lg font-semibold mt-4 mb-2">Constraints:</h3>
<ul class="list-disc pl-5 space-y-1 text-gray-300">
  <li><code>1 &lt;= n &lt;= 10<sup>4</sup></code></li>
</ul>""",
    "starter_code": {
        "python": """class Solution:
    def fizzBuzz(self, n: int) -> list[str]:
        pass
""",
        "kotlin": """class Solution {
    fun fizzBuzz(n: Int): List<String> {
        // Write your code here
        return listOf()
    }
}
""",
    },
    "solution_code": {
        "python": """class Solution:
    def fizzBuzz(self, n: int) -> list[str]:
        result = []
        for i in range(1, n + 1):
            if i % 3 == 0 and i % 5 == 0:
                result.append("FizzBuzz")
            elif i % 3 == 0:
                result.append("Fizz")
            elif i % 5 == 0:
                result.append("Buzz")
            else:
                result.append(str(i))
        return result
""",
        "kotlin": """class Solution {
    fun fizzBuzz(n: Int): List<String> {
        val result = mutableListOf<String>()
        for (i in 1..n) {
            result.add(
                when {
                    i % 15 == 0 -> "FizzBuzz"
                    i % 3 == 0 -> "Fizz"
                    i % 5 == 0 -> "Buzz"
                    else -> i.toString()
                }
            )
        }
        return result
    }
}
""",
    },
    "test_code": {
        "python": """
if __name__ == "__main__":
    try:
        sol = Solution()
        res1 = sol.fizzBuzz(3)
        assert res1 is not None, "Test 1 failed. Returned None."
        assert res1 == ["1", "2", "Fizz"], f"Test 1 failed. Expected [\"1\",\"2\",\"Fizz\"], got {res1}"
        res2 = sol.fizzBuzz(5)
        assert res2 is not None, "Test 2 failed. Returned None."
        assert res2 == ["1", "2", "Fizz", "4", "Buzz"], f"Test 2 failed. Expected [\"1\",\"2\",\"Fizz\",\"4\",\"Buzz\"], got {res2}"
        res3 = sol.fizzBuzz(15)
        assert res3 is not None, "Test 3 failed. Returned None."
        assert len(res3) == 15, f"Test 3 failed. Expected length 15, got {len(res3)}"
        assert res3[14] == "FizzBuzz", f"Test 3 failed. Expected last element \"FizzBuzz\", got {res3[14]}"
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
        val res1 = sol.fizzBuzz(3)
        require(res1 == listOf("1", "2", "Fizz")) { "Test 1 failed. Expected [\"1\",\"2\",\"Fizz\"], got $res1" }
        val res2 = sol.fizzBuzz(5)
        require(res2 == listOf("1", "2", "Fizz", "4", "Buzz")) { "Test 2 failed. Expected [\"1\",\"2\",\"Fizz\",\"4\",\"Buzz\"], got $res2" }
        val res3 = sol.fizzBuzz(15)
        require(res3.size == 15) { "Test 3 failed. Expected size 15, got ${res3.size}" }
        require(res3[14] == "FizzBuzz") { "Test 3 failed. Expected last element \"FizzBuzz\", got ${res3[14]}" }
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
