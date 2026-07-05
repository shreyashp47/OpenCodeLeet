CHALLENGE = {
    "id": "add-binary",
    "title": "Add Binary",
    "difficulty": "Easy",
    "description": """<p>Given two binary strings <code>a</code> and <code>b</code>, return <em>their sum as a binary string</em>.</p>

<h3 class="text-lg font-semibold mt-4 mb-2">Example 1:</h3>
<pre class="bg-gray-800 text-gray-100 p-3 rounded-lg font-mono text-sm mb-4">
<strong>Input:</strong> a = "11", b = "1"
<strong>Output:</strong> "100"
</pre>

<h3 class="text-lg font-semibold mt-4 mb-2">Example 2:</h3>
<pre class="bg-gray-800 text-gray-100 p-3 rounded-lg font-mono text-sm mb-4">
<strong>Input:</strong> a = "1010", b = "1011"
<strong>Output:</strong> "10101"
</pre>

<h3 class="text-lg font-semibold mt-4 mb-2">Constraints:</h3>
<ul class="list-disc pl-5 space-y-1 text-gray-300">
  <li><code>1 &lt;= a.length, b.length &lt;= 10<sup>4</sup></code></li>
  <li><code>a</code> and <code>b</code> consist only of <code>'0'</code> or <code>'1'</code> characters.</li>
  <li>Each string does not contain leading zeros except for the zero itself.</li>
</ul>""",
    "starter_code": {
        "python": """class Solution:
    def addBinary(self, a: str, b: str) -> str:
        pass
""",
        "kotlin": """class Solution {
    fun addBinary(a: String, b: String): String {
        // Write your code here
        return ""
    }
}
""",
    },
    "solution_code": {
        "python": """class Solution:
    def addBinary(self, a: str, b: str) -> str:
        i, j = len(a) - 1, len(b) - 1
        carry = 0
        result = []
        while i >= 0 or j >= 0 or carry:
            total = carry
            if i >= 0:
                total += int(a[i])
                i -= 1
            if j >= 0:
                total += int(b[j])
                j -= 1
            result.append(str(total % 2))
            carry = total // 2
        return "".join(reversed(result))
""",
        "kotlin": """class Solution {
    fun addBinary(a: String, b: String): String {
        val result = StringBuilder()
        var i = a.length - 1
        var j = b.length - 1
        var carry = 0
        while (i >= 0 || j >= 0 || carry > 0) {
            var sum = carry
            if (i >= 0) {
                sum += a[i] - '0'
                i--
            }
            if (j >= 0) {
                sum += b[j] - '0'
                j--
            }
            result.append(sum % 2)
            carry = sum / 2
        }
        return result.reverse().toString()
    }
}
""",
    },
    "test_code": {
        "python": """
if __name__ == "__main__":
    try:
        sol = Solution()
        res1 = sol.addBinary("11", "1")
        assert res1 is not None, "Test 1 failed. Returned None."
        assert res1 == "100", f"Test 1 failed. Expected \"100\", got {res1}"
        res2 = sol.addBinary("1010", "1011")
        assert res2 is not None, "Test 2 failed. Returned None."
        assert res2 == "10101", f"Test 2 failed. Expected \"10101\", got {res2}"
        res3 = sol.addBinary("0", "0")
        assert res3 is not None, "Test 3 failed. Returned None."
        assert res3 == "0", f"Test 3 failed. Expected \"0\", got {res3}"
        res4 = sol.addBinary("111", "111")
        assert res4 is not None, "Test 4 failed. Returned None."
        assert res4 == "1110", f"Test 4 failed. Expected \"1110\", got {res4}"
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
        val res1 = sol.addBinary("11", "1")
        require(res1 == "100") { "Test 1 failed. Expected \"100\", got $res1" }
        val res2 = sol.addBinary("1010", "1011")
        require(res2 == "10101") { "Test 2 failed. Expected \"10101\", got $res2" }
        val res3 = sol.addBinary("0", "0")
        require(res3 == "0") { "Test 3 failed. Expected \"0\", got $res3" }
        val res4 = sol.addBinary("111", "111")
        require(res4 == "1110") { "Test 4 failed. Expected \"1110\", got $res4" }
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
