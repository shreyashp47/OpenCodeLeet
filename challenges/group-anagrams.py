CHALLENGE = {
    "id": "group-anagrams",
    "title": "49. Group Anagrams",
    "difficulty": "Medium",
    "description": """<p>Given an array of strings <code>strs</code>, group <strong>the anagrams</strong> together. You can return the answer in <strong>any order</strong>.</p>
<p>An <strong>anagram</strong> is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.</p>

<h3 class="text-lg font-semibold mt-4 mb-2">Example 1:</h3>
<pre class="bg-gray-800 text-gray-100 p-3 rounded-lg font-mono text-sm mb-4">
<strong>Input:</strong> strs = ["eat","tea","tan","ate","nat","bat"]
<strong>Output:</strong> [["bat"],["nat","tan"],["ate","eat","tea"]]
</pre>

<h3 class="text-lg font-semibold mt-4 mb-2">Example 2:</h3>
<pre class="bg-gray-800 text-gray-100 p-3 rounded-lg font-mono text-sm mb-4">
<strong>Input:</strong> strs = [""]
<strong>Output:</strong> [[""]]
</pre>

<h3 class="text-lg font-semibold mt-4 mb-2">Example 3:</h3>
<pre class="bg-gray-800 text-gray-100 p-3 rounded-lg font-mono text-sm mb-4">
<strong>Input:</strong> strs = ["a"]
<strong>Output:</strong> [["a"]]
</pre>

<h3 class="text-lg font-semibold mt-4 mb-2">Constraints:</h3>
<ul class="list-disc pl-5 space-y-1 text-gray-300">
  <li><code>1 &lt;= strs.length &lt;= 10<sup>4</sup></code></li>
  <li><code>0 &lt;= strs[i].length &lt;= 100</code></li>
  <li><code>strs[i]</code> consists of lowercase English letters.</li>
</ul>""",
    "starter_code": """class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        pass
""",
    "solution_code": """class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        groups = {}
        for s in strs:
            key = "".join(sorted(s))
            if key in groups:
                groups[key].append(s)
            else:
                groups[key] = [s]
        return list(groups.values())
""",
    "test_code": """
if __name__ == "__main__":
    try:
        sol = Solution()
        res1 = sol.groupAnagrams(["eat","tea","tan","ate","nat","bat"])
        sorted_res1 = sorted([sorted(g) for g in res1])
        sorted_exp1 = sorted([["bat"],["nat","tan"],["ate","eat","tea"]])
        assert sorted_res1 == sorted_exp1, f"Test 1 failed. Got {res1}"
        res2 = sol.groupAnagrams([""])
        assert res2 == [[""]], f"Test 2 failed. Got {res2}"
        res3 = sol.groupAnagrams(["a"])
        assert res3 == [["a"]], f"Test 3 failed. Got {res3}"
        print("ALL_TESTS_PASSED")
    except AssertionError as ae:
        print(f"TEST_FAILED: {ae}")
    except Exception as e:
        print(f"ERROR: {e}")
""",
}
