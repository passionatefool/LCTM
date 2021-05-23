# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        result = []
        self.zigzagLevelOrderWithDepth(root, 1, result)
        return result

    def zigzagLevelOrderWithDepth(self, root: TreeNode, depth: int, result: List[List[int]]):
        if root is None:
            return
        if len(result) < depth:
            result.append([])
        r = result[depth - 1]
        if depth % 2 == 1:
            # left -> right
            r.append(root.val)
        else:
            r.insert(0, root.val)
        self.zigzagLevelOrderWithDepth(root.left, depth + 1, result)
        self.zigzagLevelOrderWithDepth(root.right, depth + 1, result)


if __name__ == "__main__":
    s = Solution()
    print(s.zigzagLevelOrder(TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))))
