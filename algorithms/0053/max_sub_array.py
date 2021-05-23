from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        result = nums[0]
        for i in range(1, len(nums)):
            nums[i] = max(nums[i - 1] + nums[i], nums[i])
            result = max(result, nums[i])
        return result


if __name__ == "__main__":
    print(Solution().maxSubArray([1, -2, 3, 5, -3, 2]))
