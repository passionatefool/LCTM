from typing import List


class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack, h = [], {}
        for num in nums2:
            while stack and stack[-1] < num:
                h[stack.pop()] = num
            stack.append(num)
        for i in range(len(nums1)):
            nums1[i] = h.get(nums1[i], -1)
        return nums1


if __name__ == "__main__":
    print(Solution().nextGreaterElement([4, 1, 2], [1, 3, 4, 2]))
