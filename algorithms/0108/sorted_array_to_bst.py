# Definition for a binary tree node.
import json
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__,
                          sort_keys=True, indent=4)


class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        return self.helper(nums, 0, len(nums) - 1)

    def helper(self, nums: List[int], low, high: int) -> TreeNode:
        if low == high:
            return TreeNode(nums[low])
        if low > high:
            return None
        mid = (low + high) // 2
        n = TreeNode(nums[mid])
        n.left = self.helper(nums, low, mid - 1)
        n.right = self.helper(nums, mid + 1, high)
        return n


if __name__ == "__main__":
    node = Solution().sortedArrayToBST([-10, -3, 0, 5, 9])
    print(node.toJSON())
