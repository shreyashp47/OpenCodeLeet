CHALLENGE = {
    "id": "find-all-anagrams-in-a-string",
    "title": "Find All Anagrams in a String",
    "difficulty": "Medium",
    "description": """<p>Given two strings <code>s</code> and <code>p</code>, return <em>an array of all the start indices of </em><code>p</code><em>'s anagrams in </em><code>s</code>. You may return the answer in <strong>any order</strong>.</p>
<p>An <strong>Anagram</strong> is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.</p>

<h3 class="text-lg font-semibold mt-4 mb-2">Example 1:</h3>
<pre class="bg-gray-800 text-gray-100 p-3 rounded-lg font-mono text-sm mb-4">
<strong>Input:</strong> s = "cbaebabacd", p = "abc"
<strong>Output:</strong> [0,6]
<strong>Explanation:</strong>
The substring with start index = 0 is "cba", which is an anagram of "abc".
The substring with start index = 6 is "bac", which is an anagram of "abc".
</pre>

<h3 class="text-lg font-semibold mt-4 mb-2">Example 2:</h3>
<pre class="bg-gray-800 text-gray-100 p-3 rounded-lg font-mono text-sm mb-4">
<strong>Input:</strong> s = "abab", p = "ab"
<strong>Output:</strong> [0,1,2]
<strong>Explanation:</strong>
The substring with start index = 0 is "ab", which is an anagram of "ab".
The substring with start index = 1 is "ba", which is an anagram of "ab".
The substring with start index = 2 is "ab", which is an anagram of "ab".
</pre>

<h3 class="text-lg font-semibold mt-4 mb-2">Constraints:</h3>
<ul class="list-disc pl-5 space-y-1 text-gray-300">
  <li><code>1 &lt;= s.length, p.length &lt;= 3 * 10<sup>4</sup></code></li>
  <li><code>s</code> and <code>p</code> consist of lowercase English letters.</li>
</ul>""",
    "starter_code": {
        "python": """class Solution:
    def findAnagrams(self, s: str, p: str) -> list[int]:
        pass
""",
        "kotlin": """class Solution {
    fun findAnagrams(s: String, p: String): List<Int> {
        // Write your code here
        return listOf()
    }
}
""",
    },
    "solution_code": {
        "python": """class Solution:
    def findAnagrams(self, s: str, p: str) -> list[int]:
        if len(p) > len(s):
            return []
        p_count = [0] * 26
        s_count = [0] * 26
        for ch in p:
            p_count[ord(ch) - ord('a')] += 1
        result = []
        for i in range(len(s)):
            s_count[ord(s[i]) - ord('a')] += 1
            if i >= len(p):
                s_count[ord(s[i - len(p)]) - ord('a')] -= 1
            if s_count == p_count:
                result.append(i - len(p) + 1)
        return result
""",
        "kotlin": """class Solution {
    fun findAnagrams(s: String, p: String): List<Int> {
        if (p.length > s.length) return listOf()
        val pCount = IntArray(26)
        val sCount = IntArray(26)
        for (ch in p) pCount[ch - 'a']++
        val result = mutableListOf<Int>()
        for (i in s.indices) {
            sCount[s[i] - 'a']++
            if (i >= p.length) sCount[s[i - p.length] - 'a']--
            if (sCount.contentEquals(pCount)) result.add(i - p.length + 1)
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
        res1 = sol.findAnagrams("cbaebabacd", "abc")
        assert sorted(res1) == [0, 6], f"Test 1 failed. Got {res1}"
        res2 = sol.findAnagrams("abab", "ab")
        assert sorted(res2) == [0, 1, 2], f"Test 2 failed. Got {res2}"
        res3 = sol.findAnagrams("a", "a")
        assert sorted(res3) == [0], f"Test 3 failed. Got {res3}"
        res4 = sol.findAnagrams("a", "b")
        assert sorted(res4) == [], f"Test 4 failed. Got {res4}"
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
        val res1 = sol.findAnagrams("cbaebabacd", "abc")
        require(res1.sorted() == listOf(0, 6)) { "Test 1 failed. Got $res1" }
        val res2 = sol.findAnagrams("abab", "ab")
        require(res2.sorted() == listOf(0, 1, 2)) { "Test 2 failed. Got $res2" }
        val res3 = sol.findAnagrams("a", "a")
        require(res3 == listOf(0)) { "Test 3 failed. Got $res3" }
        val res4 = sol.findAnagrams("a", "b")
        require(res4 == listOf<Int>()) { "Test 4 failed. Got $res4" }
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
