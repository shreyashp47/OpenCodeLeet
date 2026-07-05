CHALLENGE = {
    "id": "word-ladder",
    "title": "Word Ladder",
    "difficulty": "Hard",
    "description": """<p>A transformation sequence from word <code>beginWord</code> to word <code>endWord</code> using a dictionary <code>wordList</code> is a sequence of words such that:</p>
<ul class="list-disc pl-5 space-y-1 text-gray-300">
  <li>The first word in the sequence is <code>beginWord</code>.</li>
  <li>The last word in the sequence is <code>endWord</code>.</li>
  <li>Only one letter is different between each adjacent pair of words.</li>
  <li>Every word in the sequence is in <code>wordList</code>.</li>
</ul>
<p>Return the <strong>length</strong> of the shortest transformation sequence from <code>beginWord</code> to <code>endWord</code>, or <code>0</code> if no such sequence exists.</p>

<h3 class="text-lg font-semibold mt-4 mb-2">Example 1:</h3>
<pre class="bg-gray-800 text-gray-100 p-3 rounded-lg font-mono text-sm mb-4">
<strong>Input:</strong> beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log","cog"]
<strong>Output:</strong> 5
<strong>Explanation:</strong> The shortest transformation is "hit" -&gt; "hot" -&gt; "dot" -&gt; "dog" -&gt; "cog" with length 5.
</pre>

<h3 class="text-lg font-semibold mt-4 mb-2">Example 2:</h3>
<pre class="bg-gray-800 text-gray-100 p-3 rounded-lg font-mono text-sm mb-4">
<strong>Input:</strong> beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log"]
<strong>Output:</strong> 0
<strong>Explanation:</strong> "cog" is not in wordList, so no transformation is possible.
</pre>

<h3 class="text-lg font-semibold mt-4 mb-2">Constraints:</h3>
<ul class="list-disc pl-5 space-y-1 text-gray-300">
  <li><code>1 &lt;= beginWord.length &lt;= 10</code></li>
  <li><code>endWord.length == beginWord.length</code></li>
  <li><code>1 &lt;= wordList.length &lt;= 5000</code></li>
  <li><code>wordList[i].length == beginWord.length</code></li>
  <li><code>beginWord</code>, <code>endWord</code>, and <code>wordList[i]</code> consist of lowercase English letters.</li>
  <li><code>beginWord != endWord</code></li>
  <li>All words in <code>wordList</code> are <strong>unique</strong>.</li>
</ul>""",
    "starter_code": {
        "python": """class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: list[str]) -> int:
        pass
""",
        "kotlin": """class Solution {
    fun ladderLength(beginWord: String, endWord: String, wordList: List<String>): Int {
        // Write your code here
        return 0
    }
}
""",
    },
    "solution_code": {
        "python": """from collections import deque

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: list[str]) -> int:
        wordSet = set(wordList)
        if endWord not in wordSet:
            return 0
        q = deque([(beginWord, 1)])
        while q:
            word, dist = q.popleft()
            if word == endWord:
                return dist
            for i in range(len(word)):
                for c in 'abcdefghijklmnopqrstuvwxyz':
                    nxt = word[:i] + c + word[i + 1:]
                    if nxt in wordSet:
                        if nxt == endWord:
                            return dist + 1
                        wordSet.remove(nxt)
                        q.append((nxt, dist + 1))
        return 0
""",
        "kotlin": """import java.util.*

class Solution {
    fun ladderLength(beginWord: String, endWord: String, wordList: List<String>): Int {
        val wordSet = wordList.toMutableSet()
        if (endWord !in wordSet) return 0
        val q: Queue<Pair<String, Int>> = LinkedList()
        q.add(Pair(beginWord, 1))
        while (q.isNotEmpty()) {
            val (word, dist) = q.poll()
            if (word == endWord) return dist
            val chars = word.toCharArray()
            for (i in chars.indices) {
                val orig = chars[i]
                for (c in 'a'..'z') {
                    chars[i] = c
                    val nxt = String(chars)
                    if (nxt in wordSet) {
                        if (nxt == endWord) return dist + 1
                        wordSet.remove(nxt)
                        q.add(Pair(nxt, dist + 1))
                    }
                }
                chars[i] = orig
            }
        }
        return 0
    }
}
""",
    },
    "test_code": {
        "python": """
if __name__ == "__main__":
    try:
        sol = Solution()
        res1 = sol.ladderLength("hit", "cog", ["hot","dot","dog","lot","log","cog"])
        assert res1 is not None, "Test 1 failed. Returned None."
        assert res1 == 5, f"Test 1 failed. Expected 5, got {res1}"
        res2 = sol.ladderLength("hit", "cog", ["hot","dot","dog","lot","log"])
        assert res2 is not None, "Test 2 failed. Returned None."
        assert res2 == 0, f"Test 2 failed. Expected 0, got {res2}"
        res3 = sol.ladderLength("a", "c", ["a","b","c"])
        assert res3 is not None, "Test 3 failed. Returned None."
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
        val res1 = sol.ladderLength("hit", "cog", listOf("hot","dot","dog","lot","log","cog"))
        require(res1 == 5) { "Test 1 failed. Expected 5, got $res1" }
        val res2 = sol.ladderLength("hit", "cog", listOf("hot","dot","dog","lot","log"))
        require(res2 == 0) { "Test 2 failed. Expected 0, got $res2" }
        val res3 = sol.ladderLength("a", "c", listOf("a","b","c"))
        require(res3 == 2) { "Test 3 failed. Expected 2, got $res3" }
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
