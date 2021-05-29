from typing import List


class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        res = []
        self.handle(nums, 0, [], res)
        return res

    def handle(self, nums: List[int], index: int, cur: List[int], res: List[List[int]]):
        if len(cur) > 1:
            res.append(cur.copy())
        used = []
        for i in range(index, len(nums)):
            if nums[i] in used:
                continue
            if len(cur) > 0 and cur[-1] > nums[i]:
                continue
            used.append(nums[i])
            cur.append(nums[i])
            self.handle(nums, i + 1, cur, res)
            cur.pop()


if __name__ == "__main__":
    print(Solution().findSubsequences([4, 6, 7, 7]))
