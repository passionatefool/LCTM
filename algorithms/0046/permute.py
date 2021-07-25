from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []

        def backtracking(cur: List[int]):
            if len(cur) == len(nums):
                res.append(cur.copy())
                return
            for num in nums:
                if num in cur:
                    continue
                cur.append(num)
                backtracking(cur)
                cur.pop()

        backtracking([])
        return res


if __name__ == "__main__":
    print(Solution().permute([1, 2, 3]))
