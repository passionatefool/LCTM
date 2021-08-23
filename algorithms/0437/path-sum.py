# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        if root is None:
            return 0
        return self.dfs(root, targetSum) + self.pathSum(root.left, targetSum) + self.pathSum(root.right, targetSum)

    def dfs(self, root: Optional[TreeNode], targetSum: int) -> int:
        if root is None:
            return 0
        l = self.dfs(root.left, targetSum - root.val)
        r = self.dfs(root.right, targetSum - root.val)
        return l + r + (1 if targetSum == root.val else 0)


if __name__ == "__main__":
    s = Solution()
    print(s.pathSum(TreeNode(10, TreeNode(5, TreeNode(3, TreeNode(3), TreeNode(-2)), TreeNode(2, None, TreeNode(1))),
                             TreeNode(-3, None, TreeNode(11))), 3))
