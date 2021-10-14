# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        stack = [root]
        r = 0
        while stack:
            n = stack.pop()
            v = n.val
            if n.left:
                n.left.val = v * 2 + n.left.val
                stack.append(n.left)
            if n.right:
                n.right.val = v * 2 + n.right.val
                stack.append(n.right)
            if not n.left and not n.right:
                r += v
        return r


if __name__ == "__main__":
    t = TreeNode(1, TreeNode(0, TreeNode(0), TreeNode(1)), TreeNode(1, TreeNode(0), TreeNode(1)))
    print(Solution().sumRootToLeaf(t))
