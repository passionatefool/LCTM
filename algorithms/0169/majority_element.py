from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count, candidate = 0, None
        for n in nums:
            if count == 0:
                candidate = n
            if n == candidate:
                count += 1
            else:
                count -= 1
        return candidate


if __name__ == "__main__":
    print(Solution().majorityElement([3, 2, 3]))
    print(Solution().majorityElement([2, 2, 1, 1, 1, 2, 2]))
