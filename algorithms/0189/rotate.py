from typing import List


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        k %= len(nums)
        nums.reverse()
        self.reverse(nums, 0, k - 1)
        self.reverse(nums, k, len(nums) - 1)

    def reverse(self, nums: List[int], i, j: int):
        while i < j:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
            j -= 1


if __name__ == "__main__":
    n = [1, 2, 3, 4, 5, 6, 7]
    Solution().rotate(n, 3)
    print(n)
