from typing import List


class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        def backtracking(cur: List[int], index_list: List[int]):
            if len(cur) == len(nums):
                res.append(cur.copy())
                return
            for i in range(0, len(nums)):
                if i in index_list:
                    continue
                if i != 0 and nums[i] == nums[i - 1] and i - 1 not in index_list:
                    continue
                cur.append(nums[i])
                index_list.append(i)
                backtracking(cur, index_list)
                cur.pop()
                index_list.pop()

        backtracking([], [])
        return res


if __name__ == "__main__":
    print(Solution().permuteUnique([1, 1, 2]))
    print(Solution().permuteUnique([1, 2, 3]))
