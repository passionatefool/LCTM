from typing import List


class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        m = {}
        for i, num in enumerate(nums):
            if num in m and abs(m[num] - i) <= k:
                return True
            m[num] = i
        return False


if __name__ == "__main__":
    print(Solution().containsNearbyDuplicate([1, 2, 3, 1], 3))
    print(Solution().containsNearbyDuplicate([1, 2, 3, 1, 2, 3], 2))
