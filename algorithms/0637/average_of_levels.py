# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def averageOfLevels(self, root: TreeNode) -> List[float]:
        res = []
        self.handleLevel(root, 0, res)
        result = []
        for item in res:
            result.append(item[1] / item[0])
        return result

    def handleLevel(self, root: TreeNode, depth: int, res: List[List[float]]):
        if root is None:
            return
        if len(res) <= depth:
            res.append([0, 0])
        res[depth][0] += 1
        res[depth][1] += root.val

        depth += 1
        self.handleLevel(root.left, depth, res)
        self.handleLevel(root.right, depth, res)


if __name__ == "__main__":
    print(Solution().averageOfLevels(TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))))
