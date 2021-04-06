# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        result = []
        self.levelOrderWithDepth(root, 1, result)
        return result

    def levelOrderWithDepth(self, root: TreeNode, depth: int, result: List[int]):
        if root is None:
            return
        if len(result) < depth:
            result.append(root.val)
        else:
            result[depth - 1] = root.val
        self.levelOrderWithDepth(root.left, depth + 1, result)
        self.levelOrderWithDepth(root.right, depth + 1, result)


if __name__ == "__main__":
    s = Solution()
    print(s.rightSideView(TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))))
