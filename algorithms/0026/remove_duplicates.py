from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        slow = fast = 0
        while fast < len(nums):
            if nums[slow] != nums[fast]:
                slow += 1
                nums[slow] = nums[fast]
            fast += 1

        return slow + 1


if __name__ == "__main__":
    nums = [1, 1, 2]
    print(Solution().removeDuplicates(nums))
    print(nums)
