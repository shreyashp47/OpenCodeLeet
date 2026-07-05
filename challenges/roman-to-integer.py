CHALLENGE = {
    "id": "roman-to-integer",
    "title": "Roman to Integer",
    "difficulty": "Easy",
    "description": """<p>Roman numerals are represented by seven different symbols: <code>I</code>, <code>V</code>, <code>X</code>, <code>L</code>, <code>C</code>, <code>D</code> and <code>M</code>.</p>
<table class="table-auto bg-gray-800 text-gray-100 rounded-lg mb-4">
  <thead>
    <tr><th class="px-4 py-2">Symbol</th><th class="px-4 py-2">Value</th></tr>
  </thead>
  <tbody>
    <tr><td class="px-4 py-2">I</td><td class="px-4 py-2">1</td></tr>
    <tr><td class="px-4 py-2">V</td><td class="px-4 py-2">5</td></tr>
    <tr><td class="px-4 py-2">X</td><td class="px-4 py-2">10</td></tr>
    <tr><td class="px-4 py-2">L</td><td class="px-4 py-2">50</td></tr>
    <tr><td class="px-4 py-2">C</td><td class="px-4 py-2">100</td></tr>
    <tr><td class="px-4 py-2">D</td><td class="px-4 py-2">500</td></tr>
    <tr><td class="px-4 py-2">M</td><td class="px-4 py-2">1000</td></tr>
  </tbody>
</table>
<p>For example, <code>2</code> is written as <code>II</code> in Roman numeral, just two ones added together. <code>12</code> is written as <code>XII</code>, which is simply <code>X + II</code>. The number <code>27</code> is written as <code>XXVII</code>, which is <code>XX + V + II</code>.</p>
<p>Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not <code>IIII</code>. Instead, the number four is written as <code>IV</code>. Because the one is before the five we subtract it making four. The same principle applies to nine, written as <code>IX</code>. There are six instances where subtraction is used:</p>
<ul class="list-disc pl-5 space-y-1 text-gray-300">
  <li><code>I</code> can be placed before <code>V</code> (5) and <code>X</code> (10) to make 4 and 9.</li>
  <li><code>X</code> can be placed before <code>L</code> (50) and <code>C</code> (100) to make 40 and 90.</li>
  <li><code>C</code> can be placed before <code>D</code> (500) and <code>M</code> (1000) to make 400 and 900.</li>
</ul>
<p>Given a Roman numeral, convert it to an integer.</p>

<h3 class="text-lg font-semibold mt-4 mb-2">Example 1:</h3>
<pre class="bg-gray-800 text-gray-100 p-3 rounded-lg font-mono text-sm mb-4">
<strong>Input:</strong> s = "III"
<strong>Output:</strong> 3
</pre>

<h3 class="text-lg font-semibold mt-4 mb-2">Example 2:</h3>
<pre class="bg-gray-800 text-gray-100 p-3 rounded-lg font-mono text-sm mb-4">
<strong>Input:</strong> s = "LVIII"
<strong>Output:</strong> 58
<strong>Explanation:</strong> L = 50, V = 5, III = 3.
</pre>

<h3 class="text-lg font-semibold mt-4 mb-2">Example 3:</h3>
<pre class="bg-gray-800 text-gray-100 p-3 rounded-lg font-mono text-sm mb-4">
<strong>Input:</strong> s = "MCMXCIV"
<strong>Output:</strong> 1994
<strong>Explanation:</strong> M = 1000, CM = 900, XC = 90, IV = 4.
</pre>

<h3 class="text-lg font-semibold mt-4 mb-2">Constraints:</h3>
<ul class="list-disc pl-5 space-y-1 text-gray-300">
  <li><code>1 &lt;= s.length &lt;= 15</code></li>
  <li><code>s</code> contains only the characters <code>('I', 'V', 'X', 'L', 'C', 'D', 'M')</code>.</li>
  <li>It is <strong>guaranteed</strong> that <code>s</code> is a valid Roman numeral in the range <code>[1, 3999]</code>.</li>
</ul>""",
    "starter_code": {
        "python": """class Solution:
    def romanToInt(self, s: str) -> int:
        pass
""",
        "kotlin": """class Solution {
    fun romanToInt(s: String): Int {
        // Write your code here
        return 0
    }
}
""",
    },
    "solution_code": {
        "python": """class Solution:
    def romanToInt(self, s: str) -> int:
        values = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        total = 0
        prev = 0
        for ch in reversed(s):
            curr = values[ch]
            if curr < prev:
                total -= curr
            else:
                total += curr
            prev = curr
        return total
""",
        "kotlin": """class Solution {
    fun romanToInt(s: String): Int {
        val values = mapOf('I' to 1, 'V' to 5, 'X' to 10, 'L' to 50, 'C' to 100, 'D' to 500, 'M' to 1000)
        var total = 0
        var prev = 0
        for (ch in s.reversed()) {
            val curr = values[ch]!!
            if (curr < prev) total -= curr else total += curr
            prev = curr
        }
        return total
    }
}
""",
    },
    "test_code": {
        "python": """
if __name__ == "__main__":
    try:
        sol = Solution()
        res1 = sol.romanToInt("III")
        assert res1 == 3, f"Test 1 failed. Expected 3, got {res1}"
        res2 = sol.romanToInt("LVIII")
        assert res2 == 58, f"Test 2 failed. Expected 58, got {res2}"
        res3 = sol.romanToInt("MCMXCIV")
        assert res3 == 1994, f"Test 3 failed. Expected 1994, got {res3}"
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
        val res1 = sol.romanToInt("III")
        require(res1 == 3) { "Test 1 failed. Expected 3, got $res1" }
        val res2 = sol.romanToInt("LVIII")
        require(res2 == 58) { "Test 2 failed. Expected 58, got $res2" }
        val res3 = sol.romanToInt("MCMXCIV")
        require(res3 == 1994) { "Test 3 failed. Expected 1994, got $res3" }
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
