# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.sum = 0

    def convertBST(self, root: TreeNode) -> TreeNode:
        self.dfs(root)
        return root

    def dfs(self, root: TreeNode):
        if root is None:
            return
        self.dfs(root.right)
        self.sum += root.val
        root.val = self.sum
        self.dfs(root.left)


if __name__ == "__main__":
    print(Solution().convertBST(TreeNode(4, TreeNode(1, TreeNode(0), TreeNode(2, None, TreeNode(3))),
                                         TreeNode(6, TreeNode(5), TreeNode(7, None, TreeNode(8))))))
