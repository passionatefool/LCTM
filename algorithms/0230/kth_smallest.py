# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        result = []
        self.rangeTree(root, result)
        return result[k-1]

    def rangeTree(self, root: TreeNode, result: List[int]):
        if root is None:
            return
        self.rangeTree(root.left, result)
        result.append(root.val)
        self.rangeTree(root.right, result)
