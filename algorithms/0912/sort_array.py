from typing import List


class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        self.mergeSort(nums)
        return nums

    def mergeSort(self, nums: List[int]):
        if len(nums) <= 1:
            return
        mid = len(nums) // 2
        left, right = nums[:mid], nums[mid:]
        self.mergeSort(left)
        self.mergeSort(right)
        i = j = k = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                nums[k] = left[i]
                i += 1
            else:
                nums[k] = right[j]
                j += 1
            k += 1
        while i < len(left):
            nums[k] = left[i]
            i += 1
            k += 1
        while j < len(right):
            nums[k] = right[j]
            j += 1
            k += 1


if __name__ == "__main__":
    print(Solution().sortArray([5, 2, 3, 1]))
    print(Solution().sortArray([5, 1, 1, 2, 0, 0]))
