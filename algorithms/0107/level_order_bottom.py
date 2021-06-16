# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        result = []
        self.levelOrderWithDepth(root, 1, result)
        return reversed(result)

    def levelOrderWithDepth(self, root: TreeNode, depth: int, result: List[List[int]]):
        if root is None:
            return
        if len(result) < depth:
            result.append([])
        r = result[depth - 1]
        r.append(root.val)
        self.levelOrderWithDepth(root.left, depth + 1, result)
        self.levelOrderWithDepth(root.right, depth + 1, result)


if __name__ == "__main__":
    s = Solution()
    print(s.levelOrderBottom(TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))))
    print(s.levelOrderBottom(TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5)), TreeNode(3))))
