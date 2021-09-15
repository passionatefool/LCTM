import math
from typing import List


class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        m1 = m2 = m3 = -math.inf
        for num in nums:
            if num > m1:
                m1, m2, m3 = num, m1, m2
            elif m1 > num > m2:
                m2, m3 = num, m2
            elif m2 > num > m3:
                m3 = num
        return m3 if m3 != -math.inf else m1


if __name__ == "__main__":
    print(Solution().thirdMax([3, 2, 1]))
    print(Solution().thirdMax([1, 2, 2, 5, 3, 5]))
