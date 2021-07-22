# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def searchBST(self, root: TreeNode, val: int) -> TreeNode:
        if root is None or root.val == val:
            return root

        return self.searchBST(root.left, val) if root.val > val else self.searchBST(root.right, val)


if __name__ == "__main__":
    r = TreeNode(4, TreeNode(2, TreeNode(1), TreeNode(3)), TreeNode(7))
    nr = Solution().searchBST(r, 2)
    print(nr.val)
