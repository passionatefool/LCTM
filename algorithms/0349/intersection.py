from typing import List


class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        m = {}
        for num in nums1:
            m[num] = True
        result = []
        for num in nums2:
            if num in m:
                result.append(num)
                del m[num]
        return result


if __name__ == "__main__":
    print(Solution().intersection([1, 2, 2, 1], [2, 2]))
