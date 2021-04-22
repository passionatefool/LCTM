from typing import List


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        start = total = 0
        m = len(nums) + 1
        result = m
        for i, num in enumerate(nums):
            total += num
            while total >= target:
                length = i - start + 1
                result = result if result < length else length
                total -= nums[start]
                start += 1
        return result if result != m else 0


if __name__ == "__main__":
    print(Solution().minSubArrayLen(7, [2, 3, 1, 2, 4, 3]))
