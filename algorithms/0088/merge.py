from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        index = m + n - 1
        while m > 0 and n > 0:
            if nums2[n-1] > nums1[m-1]:
                nums1[index] = nums2[n-1]
                n -= 1
            else:
                nums1[index] = nums1[m-1]
                m -= 1
            index -= 1
        while n > 0:
            nums1[index] = nums2[n-1]
            n -= 1
            index -= 1


if __name__ == "__main__":
    nums = [1, 2, 3, 0, 0, 0]
    Solution().merge(nums, 3, [2, 5, 6], 3)
    print(nums)
