from typing import List


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)
        max_dp = [0] * n
        min_dp = [0] * n
        res = max_dp[0] = min_dp[0] = nums[0]
        for i in range(1, n):
            ni = nums[i]
            max_dp[i] = max(max_dp[i - 1] * ni, min_dp[i - 1] * ni, ni)
            min_dp[i] = min(max_dp[i - 1] * ni, min_dp[i - 1] * ni, ni)
            res = max(res, max_dp[i])
        return res


if __name__ == "__main__":
    print(Solution().maxProduct([2, 3, -2, 4]))
