from typing import List


class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        count = {}
        result = []
        for num in nums1:
            count[num] = count.get(num, 0) + 1
        for num in nums2:
            if num in count and count[num] > 0:
                result.append(num)
                count[num] -= 1
        return result


if __name__ == "__main__":
    print(Solution().intersect([1, 2, 2, 1], [2, 2]))
    print(Solution().intersect([4, 9, 5], [9, 4, 9, 8, 4]))
