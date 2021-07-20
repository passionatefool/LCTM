import json


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__,
                          sort_keys=True, indent=4)


class Solution:
    def trimBST(self, root: TreeNode, L: int, R: int) -> TreeNode:
        if root is None:
            return root
        if root.val > R:
            return self.trimBST(root.left, L, R)
        if root.val < L:
            return self.trimBST(root.right, L, R)

        root.left = self.trimBST(root.left, L, R)
        root.right = self.trimBST(root.right, L, R)
        return root


if __name__ == "__main__":
    r = TreeNode(1)
    r.left = TreeNode(0)
    r.right = TreeNode(2)
    nr = Solution().trimBST(r, 1, 2)
    print(nr.toJSON())
