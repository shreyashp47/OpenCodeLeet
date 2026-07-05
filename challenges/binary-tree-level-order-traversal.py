CHALLENGE = {
    "id": "binary-tree-level-order-traversal",
    "title": "Binary Tree Level Order Traversal",
    "difficulty": "Medium",
    "description": """<p>Given the <code>root</code> of a binary tree, return <em>the level order traversal of its nodes' values</em>. (i.e., from left to right, level by level).</p>

<h3 class="text-lg font-semibold mt-4 mb-2">Example 1:</h3>
<pre class="bg-gray-800 text-gray-100 p-3 rounded-lg font-mono text-sm mb-4">
<strong>Input:</strong> root = [3,9,20,null,null,15,7]
<strong>Output:</strong> [[3],[9,20],[15,7]]
</pre>

<h3 class="text-lg font-semibold mt-4 mb-2">Example 2:</h3>
<pre class="bg-gray-800 text-gray-100 p-3 rounded-lg font-mono text-sm mb-4">
<strong>Input:</strong> root = [1]
<strong>Output:</strong> [[1]]
</pre>

<h3 class="text-lg font-semibold mt-4 mb-2">Example 3:</h3>
<pre class="bg-gray-800 text-gray-100 p-3 rounded-lg font-mono text-sm mb-4">
<strong>Input:</strong> root = []
<strong>Output:</strong> []
</pre>

<h3 class="text-lg font-semibold mt-4 mb-2">Constraints:</h3>
<ul class="list-disc pl-5 space-y-1 text-gray-300">
  <li>The number of nodes in the tree is in the range <code>[0, 2000]</code>.</li>
  <li><code>-1000 &lt;= Node.val &lt;= 1000</code></li>
</ul>""",
    "starter_code": {
        "python": """from typing import Optional, List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        pass
""",
        "kotlin": """class TreeNode(var `val`: Int) {
    var left: TreeNode? = null
    var right: TreeNode? = null
}

class Solution {
    fun levelOrder(root: TreeNode?): List<List<Int>> {
        // Write your code here
        return listOf()
    }
}
""",
    },
    "solution_code": {
        "python": """from typing import Optional, List
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        result = []
        q = deque([root])
        while q:
            level = []
            for _ in range(len(q)):
                node = q.popleft()
                level.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            result.append(level)
        return result
""",
        "kotlin": """class TreeNode(var `val`: Int) {
    var left: TreeNode? = null
    var right: TreeNode? = null
}

class Solution {
    fun levelOrder(root: TreeNode?): List<List<Int>> {
        if (root == null) return listOf()
        val result = mutableListOf<List<Int>>()
        val q = ArrayDeque<TreeNode>()
        q.addLast(root)
        while (q.isNotEmpty()) {
            val level = mutableListOf<Int>()
            repeat(q.size) {
                val node = q.removeFirst()
                level.add(node.`val`)
                node.left?.let { q.addLast(it) }
                node.right?.let { q.addLast(it) }
            }
            result.add(level)
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

        def build_tree(values):
            if not values:
                return None
            root = TreeNode(values[0])
            q = [root]
            i = 1
            while q and i < len(values):
                node = q.pop(0)
                if values[i] is not None:
                    node.left = TreeNode(values[i])
                    q.append(node.left)
                i += 1
                if i < len(values) and values[i] is not None:
                    node.right = TreeNode(values[i])
                    q.append(node.right)
                i += 1
            return root

        res1 = sol.levelOrder(build_tree([3, 9, 20, None, None, 15, 7]))
        assert res1 == [[3], [9, 20], [15, 7]], f"Test 1 failed. Got {res1}"
        res2 = sol.levelOrder(build_tree([1]))
        assert res2 == [[1]], f"Test 2 failed. Got {res2}"
        res3 = sol.levelOrder(build_tree([]))
        assert res3 == [], f"Test 3 failed. Got {res3}"
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

        fun buildTree(values: List<Int?>): TreeNode? {
            if (values.isEmpty() || values[0] == null) return null
            val root = TreeNode(values[0]!!)
            val q = ArrayDeque<TreeNode>()
            q.addLast(root)
            var i = 1
            while (q.isNotEmpty() && i < values.size) {
                val node = q.removeFirst()
                if (i < values.size && values[i] != null) {
                    node.left = TreeNode(values[i]!!)
                    q.addLast(node.left!!)
                }
                i++
                if (i < values.size && values[i] != null) {
                    node.right = TreeNode(values[i]!!)
                    q.addLast(node.right!!)
                }
                i++
            }
            return root
        }

        val res1 = sol.levelOrder(buildTree(listOf(3, 9, 20, null, null, 15, 7)))
        require(res1 == listOf(listOf(3), listOf(9, 20), listOf(15, 7))) { "Test 1 failed. Got $res1" }
        val res2 = sol.levelOrder(buildTree(listOf(1)))
        require(res2 == listOf(listOf(1))) { "Test 2 failed. Got $res2" }
        val res3 = sol.levelOrder(buildTree(listOf()))
        require(res3 == listOf<List<Int>>()) { "Test 3 failed. Got $res3" }
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
