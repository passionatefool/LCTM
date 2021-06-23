# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def largestValues(self, root: TreeNode) -> List[int]:
        res = []
        self.handleLevel(root, 1, res)
        return res

    def handleLevel(self, root: TreeNode, depth: int, res: List[int]):
        if root is None:
            return
        if len(res) < depth:
            res.append(root.val)
        if root.val > res[depth - 1]:
            res[depth - 1] = root.val

        depth = depth + 1
        self.handleLevel(root.left, depth, res)
        self.handleLevel(root.right, depth, res)


if __name__ == "__main__":
    print(Solution().largestValues(TreeNode(1, TreeNode(3, TreeNode(5), TreeNode(3)), TreeNode(2, None, TreeNode(9)))))
