# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        res = []
        self.handleTreePaths(root, res, "")
        return res

    def handleTreePaths(self, root: TreeNode, res: List[str], cur: str):
        cur += str(root.val)
        if root.left is None and root.right is None:
            res.append(cur)
            return
        cur += "->"
        if root.left:
            self.handleTreePaths(root.left, res, cur)
        if root.right:
            self.handleTreePaths(root.right, res, cur)


if __name__ == "__main__":
    print(Solution().binaryTreePaths(TreeNode(1, TreeNode(2, None, TreeNode(5)), TreeNode(3))))
