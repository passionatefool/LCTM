from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> TreeNode:
        if len(nums) == 0:
            return None
        max_index = nums.index(max(nums))
        return TreeNode(nums[max_index], self.constructMaximumBinaryTree(nums[:max_index]),
                        self.constructMaximumBinaryTree(nums[max_index + 1:]))


if __name__ == "__main__":
    tree = Solution().constructMaximumBinaryTree([3, 2, 1, 6, 0, 5])
    s = [tree]
    while len(s) > 0:
        tn = s.pop()
        print(tn.val, end=' ')
        if tn.right:
            s.append(tn.right)
        else:
            print("None", end=' ')
        if tn.left:
            s.append(tn.left)
        else:
            print("None", end=' ')
