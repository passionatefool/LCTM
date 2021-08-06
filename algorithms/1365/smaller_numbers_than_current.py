from typing import List


class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        ns = sorted(nums)
        n = len(nums)
        res = [0] * n
        h = {}
        for i in range(n - 1, -1, -1):
            h[ns[i]] = i
        for i in range(n):
            res[i] = h[nums[i]]
        return res


if __name__ == "__main__":
    print(Solution().smallerNumbersThanCurrent([8, 1, 2, 2, 3]))
