CHALLENGE = {
    "id": "first-missing-positive",
    "title": "41. First Missing Positive",
    "difficulty": "Hard",
    "description": """<p>Given an unsorted integer array <code>nums</code>, return the <strong>smallest positive integer</strong> that is <strong>not present</strong> in <code>nums</code>.</p>
<p>You must implement an algorithm that runs in <code>O(n)</code> time and uses <code>O(1)</code> auxiliary space.</p>

<h3 class="text-lg font-semibold mt-4 mb-2">Example 1:</h3>
<pre class="bg-gray-800 text-gray-100 p-3 rounded-lg font-mono text-sm mb-4">
<strong>Input:</strong> nums = [1,2,0]
<strong>Output:</strong> 3
<strong>Explanation:</strong> The numbers in the range [1,2] are all in the array.
</pre>

<h3 class="text-lg font-semibold mt-4 mb-2">Example 2:</h3>
<pre class="bg-gray-800 text-gray-100 p-3 rounded-lg font-mono text-sm mb-4">
<strong>Input:</strong> nums = [3,4,-1,1]
<strong>Output:</strong> 2
<strong>Explanation:</strong> 1 is in the array but 2 is missing.
</pre>

<h3 class="text-lg font-semibold mt-4 mb-2">Example 3:</h3>
<pre class="bg-gray-800 text-gray-100 p-3 rounded-lg font-mono text-sm mb-4">
<strong>Input:</strong> nums = [7,8,9,11,12]
<strong>Output:</strong> 1
<strong>Explanation:</strong> The smallest positive integer 1 is missing.
</pre>

<h3 class="text-lg font-semibold mt-4 mb-2">Constraints:</h3>
<ul class="list-disc pl-5 space-y-1 text-gray-300">
  <li><code>1 &lt;= nums.length &lt;= 10<sup>5</sup></code></li>
  <li><code>-2<sup>31</sup> &lt;= nums[i] &lt;= 2<sup>31</sup> - 1</code></li>
</ul>""",
    "starter_code": """class Solution:
    def firstMissingPositive(self, nums: list[int]) -> int:
        pass
""",
    "solution_code": """class Solution:
    def firstMissingPositive(self, nums: list[int]) -> int:
        n = len(nums)
        for i in range(n):
            while 1 <= nums[i] <= n and nums[nums[i] - 1] != nums[i]:
                nums[nums[i] - 1], nums[i] = nums[i], nums[nums[i] - 1]
        for i in range(n):
            if nums[i] != i + 1:
                return i + 1
        return n + 1
""",
    "test_code": """
if __name__ == "__main__":
    try:
        sol = Solution()
        res1 = sol.firstMissingPositive([1,2,0])
        assert res1 == 3, f"Test 1 failed. Expected 3, got {res1}"
        res2 = sol.firstMissingPositive([3,4,-1,1])
        assert res2 == 2, f"Test 2 failed. Expected 2, got {res2}"
        res3 = sol.firstMissingPositive([7,8,9,11,12])
        assert res3 == 1, f"Test 3 failed. Expected 1, got {res3}"
        res4 = sol.firstMissingPositive([1,2,3])
        assert res4 == 4, f"Test 4 failed. Expected 4, got {res4}"
        res5 = sol.firstMissingPositive([-1,-2])
        assert res5 == 1, f"Test 5 failed. Expected 1 for all negatives, got {res5}"
        print("ALL_TESTS_PASSED")
    except AssertionError as ae:
        print(f"TEST_FAILED: {ae}")
    except Exception as e:
        print(f"ERROR: {e}")
""",
}
