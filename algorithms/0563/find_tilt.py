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

    def findTilt(self, root: Optional[TreeNode]) -> int:
        def dfs(n: TreeNode):
            if not n:
                return 0
            left, right = dfs(n.left), dfs(n.right)
            self.result += abs(left - right)
            return left + right + n.val

        dfs(root)
        return self.result


if __name__ == "__main__":
    print(Solution().findTilt(TreeNode(1, TreeNode(2), TreeNode(3))))
    print(Solution().findTilt(TreeNode(4, TreeNode(2, TreeNode(3), TreeNode(5)), TreeNode(9, None, TreeNode(7)))))
