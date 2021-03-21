from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        m = {}
        result = 0
        for num in nums:
            if num in m:
                continue
            m[num] = 1
            left = right = 0
            if num - 1 in m:
                left = m[num - 1]
            if num + 1 in m:
                right = m[num + 1]
            lc = 1
            if left != 0:
                lc += m[num - left]
            if right != 0:
                lc += m[num + right]
            m[num - left] = m[num + right] = lc
            result = max(result, lc)
        return result


if __name__ == "__main__":
    print(Solution().longestConsecutive([100, 4, 200, 1, 3, 2]))