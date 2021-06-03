from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if len(nums) <= 1:
            return True
        i, cover = 0, 0
        while i <= cover:
            cover = max(i + nums[i], cover)
            if cover >= len(nums) - 1:
                return True
            i += 1
        return False


if __name__ == "__main__":
    print(Solution().canJump([2, 3, 1, 1, 4]))
    print(Solution().canJump([3, 2, 1, 0, 4]))
