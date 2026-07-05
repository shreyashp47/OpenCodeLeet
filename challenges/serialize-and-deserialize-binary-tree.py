CHALLENGE = {
    "id": "serialize-and-deserialize-binary-tree",
    "title": "Serialize and Deserialize Binary Tree",
    "difficulty": "Hard",
    "description": """<p>Serialization is the process of converting a data structure or object into a sequence of bits so that it can be stored in a file or memory buffer, or transmitted across a network connection link to be reconstructed later.</p>
<p>Design an algorithm to serialize and deserialize a binary tree. There is no restriction on how your serialization/deserialization algorithm should work. You just need to ensure that a binary tree can be serialized to a string and this string can be deserialized to the original tree structure.</p>
<p>The tree is represented as a list (level-order with <code>None</code> for null nodes). You need to implement both <code>serialize</code> and <code>deserialize</code> methods.</p>

<h3 class="text-lg font-semibold mt-4 mb-2">Example 1:</h3>
<pre class="bg-gray-800 text-gray-100 p-3 rounded-lg font-mono text-sm mb-4">
<strong>Input:</strong> root = [1,2,3,None,None,4,5]
<strong>Output:</strong> [1,2,3,None,None,4,5]
<strong>Explanation:</strong>
    1
   / \
  2   3
     / \
    4   5
</pre>

<h3 class="text-lg font-semibold mt-4 mb-2">Example 2:</h3>
<pre class="bg-gray-800 text-gray-100 p-3 rounded-lg font-mono text-sm mb-4">
<strong>Input:</strong> root = []
<strong>Output:</strong> []
</pre>

<h3 class="text-lg font-semibold mt-4 mb-2">Example 3:</h3>
<pre class="bg-gray-800 text-gray-100 p-3 rounded-lg font-mono text-sm mb-4">
<strong>Input:</strong> root = [1]
<strong>Output:</strong> [1]
</pre>

<h3 class="text-lg font-semibold mt-4 mb-2">Constraints:</h3>
<ul class="list-disc pl-5 space-y-1 text-gray-300">
  <li>The number of nodes in the tree is in the range <code>[0, 10<sup>4</sup>]</code>.</li>
  <li><code>0 &lt;= Node.val &lt;= 1000</code></li>
</ul>""",
    "starter_code": {
        "python": """class Solution:
    def serialize(self, root: list[int]) -> str:
        pass

    def deserialize(self, data: str) -> list[int]:
        pass
""",
        "kotlin": """class Solution {
    fun serialize(root: List<Int?>): String {
        // Write your code here
        return ""
    }

    fun deserialize(data: String): List<Int?> {
        // Write your code here
        return listOf()
    }
}
""",
    },
    "solution_code": {
        "python": """from collections import deque

class Solution:
    def serialize(self, root: list[int]) -> str:
        # root is already a level-order list with None markers
        # Convert to string: join with commas, None -> "null"
        parts = [str(x) if x is not None else "null" for x in root]
        return ",".join(parts)

    def deserialize(self, data: str) -> list[int]:
        if not data:
            return []
        parts = data.split(",")
        result: list[int] = []
        for p in parts:
            if p == "null":
                result.append(None)
            else:
                result.append(int(p))
        return result
""",
        "kotlin": """class Solution {
    fun serialize(root: List<Int?>): String {
        return root.joinToString(",") { it?.toString() ?: "null" }
    }

    fun deserialize(data: String): List<Int?> {
        if (data.isEmpty()) return listOf()
        return data.split(",").map {
            if (it == "null") null else it.toInt()
        }
    }
}
""",
    },
    "test_code": {
        "python": """
if __name__ == "__main__":
    try:
        sol = Solution()
        tree1 = [1,2,3,None,None,4,5]
        ser1 = sol.serialize(tree1)
        deser1 = sol.deserialize(ser1)
        assert ser1 == "1,2,3,null,null,4,5", f"Test 1 serialize failed. Got {ser1}"
        assert deser1 == tree1, f"Test 1 deserialize failed. Expected {tree1}, got {deser1}"
        tree2: list[int] = []
        ser2 = sol.serialize(tree2)
        deser2 = sol.deserialize(ser2)
        assert ser2 == "", f"Test 2 serialize failed. Got '{ser2}'"
        assert deser2 == tree2, f"Test 2 deserialize failed. Expected {tree2}, got {deser2}"
        tree3 = [1]
        ser3 = sol.serialize(tree3)
        deser3 = sol.deserialize(ser3)
        assert ser3 == "1", f"Test 3 serialize failed. Got {ser3}"
        assert deser3 == tree3, f"Test 3 deserialize failed. Expected {tree3}, got {deser3}"
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
        val tree1 = listOf(1, 2, 3, null, null, 4, 5)
        val ser1 = sol.serialize(tree1)
        val deser1 = sol.deserialize(ser1)
        require(ser1 == "1,2,3,null,null,4,5") { "Test 1 serialize failed. Got $ser1" }
        require(deser1 == tree1) { "Test 1 deserialize failed. Expected $tree1, got $deser1" }
        val tree2 = listOf<Int?>()
        val ser2 = sol.serialize(tree2)
        val deser2 = sol.deserialize(ser2)
        require(ser2 == "") { "Test 2 serialize failed. Got '$ser2'" }
        require(deser2 == tree2) { "Test 2 deserialize failed. Expected $tree2, got $deser2" }
        val tree3 = listOf<Int?>(1)
        val ser3 = sol.serialize(tree3)
        val deser3 = sol.deserialize(ser3)
        require(ser3 == "1") { "Test 3 serialize failed. Got $ser3" }
        require(deser3 == tree3) { "Test 3 deserialize failed. Expected $tree3, got $deser3" }
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
