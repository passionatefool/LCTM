from typing import List


class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        self.handle(nums, res, [], 0)
        return res

    def handle(self, nums: List[int], res: List[List[int]], cur: List[int], index: int):
        res.append(cur.copy())
        for i in range(index, len(nums)):
            if i > index and nums[i] == nums[i - 1]:
                continue
            cur.append(nums[i])
            self.handle(nums, res, cur, i + 1)
            cur.pop()


if __name__ == "__main__":
    print(Solution().subsetsWithDup([1, 2, 2]))
