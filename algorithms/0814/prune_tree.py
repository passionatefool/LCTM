# Definition for a binary tree node.
from typing import Optional
import json


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__,
                          sort_keys=True, indent=4)


class Solution:
    def pruneTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        return None if self.dfs(root) else root

    def dfs(self, root: TreeNode) -> bool:
        if not root:
            return True
        l, r = self.dfs(root.left), self.dfs(root.right)
        if l:
            root.left = None
        if r:
            root.right = None
        return l and r and root.val == 0


if __name__ == "__main__":
    root = TreeNode(1, None, TreeNode(0, TreeNode(0), TreeNode(1)))
    print(Solution().pruneTree(root).toJSON())
