CHALLENGE = {
    "id": "plus-one",
    "title": "Plus One",
    "difficulty": "Easy",
    "description": """<p>You are given a <strong>large integer</strong> represented as an integer array <code>digits</code>, where each <code>digits[i]</code> is the <code>i<sup>th</sup></code> digit of the integer. The digits are ordered from most significant to least significant in left-to-right order. The large integer does not contain any leading <code>0</code>'s.</p>
<p>Increment the large integer by one and return <em>the resulting array of digits</em>.</p>

<h3 class="text-lg font-semibold mt-4 mb-2">Example 1:</h3>
<pre class="bg-gray-800 text-gray-100 p-3 rounded-lg font-mono text-sm mb-4">
<strong>Input:</strong> digits = [1,2,3]
<strong>Output:</strong> [1,2,4]
<strong>Explanation:</strong> The array represents the integer 123. Incrementing by one gives 124.
</pre>

<h3 class="text-lg font-semibold mt-4 mb-2">Example 2:</h3>
<pre class="bg-gray-800 text-gray-100 p-3 rounded-lg font-mono text-sm mb-4">
<strong>Input:</strong> digits = [4,3,2,1]
<strong>Output:</strong> [4,3,2,2]
<strong>Explanation:</strong> The array represents the integer 4321. Incrementing by one gives 4322.
</pre>

<h3 class="text-lg font-semibold mt-4 mb-2">Example 3:</h3>
<pre class="bg-gray-800 text-gray-100 p-3 rounded-lg font-mono text-sm mb-4">
<strong>Input:</strong> digits = [9]
<strong>Output:</strong> [1,0]
<strong>Explanation:</strong> The array represents the integer 9. Incrementing by one gives 10.
</pre>

<h3 class="text-lg font-semibold mt-4 mb-2">Constraints:</h3>
<ul class="list-disc pl-5 space-y-1 text-gray-300">
  <li><code>1 &lt;= digits.length &lt;= 100</code></li>
  <li><code>0 &lt;= digits[i] &lt;= 9</code></li>
  <li><code>digits</code> does not contain any leading <code>0</code>'s.</li>
</ul>""",
    "starter_code": {
        "python": """class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        pass
""",
        "kotlin": """class Solution {
    fun plusOne(digits: IntArray): IntArray {
        // Write your code here
        return intArrayOf()
    }
}
""",
    },
    "solution_code": {
        "python": """class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        for i in range(len(digits) - 1, -1, -1):
            if digits[i] < 9:
                digits[i] += 1
                return digits
            digits[i] = 0
        return [1] + digits
""",
        "kotlin": """class Solution {
    fun plusOne(digits: IntArray): IntArray {
        val result = digits.toMutableList()
        for (i in result.indices.reversed()) {
            if (result[i] < 9) {
                result[i]++
                return result.toIntArray()
            }
            result[i] = 0
        }
        val newResult = mutableListOf(1)
        newResult.addAll(result)
        return newResult.toIntArray()
    }
}
""",
    },
    "test_code": {
        "python": """
if __name__ == "__main__":
    try:
        sol = Solution()
        res1 = sol.plusOne([1, 2, 3])
        assert res1 is not None, "Test 1 failed. Returned None."
        assert res1 == [1, 2, 4], f"Test 1 failed. Expected [1, 2, 4], got {res1}"
        res2 = sol.plusOne([4, 3, 2, 1])
        assert res2 is not None, "Test 2 failed. Returned None."
        assert res2 == [4, 3, 2, 2], f"Test 2 failed. Expected [4, 3, 2, 2], got {res2}"
        res3 = sol.plusOne([9])
        assert res3 is not None, "Test 3 failed. Returned None."
        assert res3 == [1, 0], f"Test 3 failed. Expected [1, 0], got {res3}"
        res4 = sol.plusOne([9, 9, 9])
        assert res4 is not None, "Test 4 failed. Returned None."
        assert res4 == [1, 0, 0, 0], f"Test 4 failed. Expected [1, 0, 0, 0], got {res4}"
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
        val res1 = sol.plusOne(intArrayOf(1, 2, 3))
        require(res1 contentEquals intArrayOf(1, 2, 4)) { "Test 1 failed. Expected [1, 2, 4], got ${res1.contentToString()}" }
        val res2 = sol.plusOne(intArrayOf(4, 3, 2, 1))
        require(res2 contentEquals intArrayOf(4, 3, 2, 2)) { "Test 2 failed. Expected [4, 3, 2, 2], got ${res2.contentToString()}" }
        val res3 = sol.plusOne(intArrayOf(9))
        require(res3 contentEquals intArrayOf(1, 0)) { "Test 3 failed. Expected [1, 0], got ${res3.contentToString()}" }
        val res4 = sol.plusOne(intArrayOf(9, 9, 9))
        require(res4 contentEquals intArrayOf(1, 0, 0, 0)) { "Test 4 failed. Expected [1, 0, 0, 0], got ${res4.contentToString()}" }
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
