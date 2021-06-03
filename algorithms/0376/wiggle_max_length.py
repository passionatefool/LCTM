from typing import List


class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        if len(nums) <= 1:
            return len(nums)
        cur, pre = 0, 0
        result = 1
        for i in range(len(nums) - 1):
            cur = nums[i + 1] - nums[i]
            if (cur > 0 and pre <= 0) or (cur < 0 and pre >= 0):
                result += 1
                pre = cur
        return result


if __name__ == "__main__":
    print(Solution().wiggleMaxLength([1, 17, 5, 10, 13, 15, 10, 5, 16, 8]))
