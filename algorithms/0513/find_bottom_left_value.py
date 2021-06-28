from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def findBottomLeftValue(self, root: TreeNode) -> int:
        res = []
        self.handleLevel(root, 0, res)
        return res[-1].val

    def handleLevel(self, root: TreeNode, depth: int, res: List[TreeNode]):
        if root is None:
            return
        if len(res) <= depth:
            res.append(root)

        depth += 1
        self.handleLevel(root.left, depth, res)
        self.handleLevel(root.right, depth, res)
