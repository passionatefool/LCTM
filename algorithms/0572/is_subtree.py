# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        return self.isEqual(root, subRoot) or (root and (self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)))

    def isEqual(self, t1: TreeNode, t2: TreeNode) -> bool:
        if not t1 or not t2:
            return t1 == t2
        return t1.val == t2.val and self.isEqual(t1.left, t2.left) and self.isEqual(t1.right, t2.right)
