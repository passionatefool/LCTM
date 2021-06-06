from typing import List


class Solution:
    def jump(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0
        cur, result, dis = 0, 0, 0
        for i in range(len(nums)):
            dis = max(dis, nums[i] + i)
            if cur == i:
                if cur != len(nums) - 1:
                    result += 1
                    cur = dis
                    if dis >= len(nums) - 1:
                        return result
                else:
                    return result
        return result


if __name__ == "__main__":
    print(Solution().jump([2, 3, 1, 1, 4]))
