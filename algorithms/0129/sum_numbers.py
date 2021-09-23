# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.result = 0

    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        self.dfs(root, 0)
        return self.result

    def dfs(self, root: TreeNode, cur: int):
        if not root:
            return

        cur = cur * 10 + root.val
        if not root.left and not root.right:
            self.result += cur
        else:
            self.dfs(root.left, cur)
            self.dfs(root.right, cur)


if __name__ == "__main__":
    print(Solution().sumNumbers(TreeNode(1, TreeNode(2), TreeNode(3))))
