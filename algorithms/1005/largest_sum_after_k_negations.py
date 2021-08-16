from typing import List


class Solution:
    def largestSumAfterKNegations(self, nums: List[int], k: int) -> int:
        nums.sort(key=abs, reverse=True)
        for i in range(len(nums)):
            if nums[i] < 0 and k > 0:
                nums[i] *= -1
                k -= 1
        if k % 2 == 1:
            nums[-1] *= -1
        return sum(nums)


if __name__ == "__main__":
    print(Solution().largestSumAfterKNegations([4, 2, 3], 1))
    print(Solution().largestSumAfterKNegations([3, -1, 0, 2], 3))
    print(Solution().largestSumAfterKNegations([2, -3, -1, 5, -4], 2))
