from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums:
            return [-1, -1]

        def find_first(l, r: int):
            while l <= r:
                mid = (l + r) // 2
                if nums[mid] >= target:
                    r = mid - 1
                else:
                    l = mid + 1
            return l

        def find_last(l, r: int):
            while l <= r:
                mid = (l + r) // 2
                if nums[mid] > target:
                    r = mid - 1
                else:
                    l = mid + 1
            return r

        left, right = find_first(0, len(nums) - 1), find_last(0, len(nums) - 1)
        if left > right:
            return [-1, -1]
        return [left, right]


if __name__ == "__main__":
    print(Solution().searchRange([5, 7, 7, 8, 8, 10], 8))
