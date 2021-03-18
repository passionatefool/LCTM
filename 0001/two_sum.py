from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        m = {}
        for i, num in enumerate(nums):
            if target - num in m:
                return [i, m.get(target - num)]
            else:
                m[num] = i

        return None


def main():
    s = Solution()
    print(s.twoSum([1, 2, 3, 4, 5], 7))


if __name__ == "__main__":
    main()
