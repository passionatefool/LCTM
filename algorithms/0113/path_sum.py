# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def pathSum(self, root: TreeNode, targetSum: int) -> List[List[int]]:
        res = []
        self.dfs(root, targetSum, [], res)
        return res

    def dfs(self, root: TreeNode, target_sum: int, cur: List[int], res: List[List[int]]):
        if root is None:
            return

        cur.append(root.val)
        if root.val == target_sum and root.left is None and root.right is None:
            res.append(cur)
        else:
            target_sum -= root.val
            self.dfs(root.left, target_sum, cur.copy(), res)
            self.dfs(root.right, target_sum, cur.copy(), res)


if __name__ == "__main__":
    print(Solution().pathSum(TreeNode(5, TreeNode(4, TreeNode(11, TreeNode(7), TreeNode(2))),
                                      TreeNode(8, TreeNode(13), TreeNode(4, TreeNode(5), TreeNode(1)))), 22))
