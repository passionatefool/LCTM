from typing import List


class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        if len(nums) < 4:
            return res
        nums.sort()

        for i in range(0, len(nums) - 3):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            if nums[i] + nums[len(nums) - 1] + nums[len(nums) - 2] + nums[len(nums) - 3] < target:
                continue
            if nums[i] + nums[i + 1] + nums[i + 2] + nums[i + 3] > target:
                return res

            for j in range(i + 1, len(nums) - 2):
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue
                if nums[i] + nums[j] + nums[len(nums) - 1] + nums[len(nums) - 2] < target:
                    continue
                if nums[i] + nums[j] + nums[j + 1] + nums[j + 2] > target:
                    break

                left, right = j + 1, len(nums) - 1
                while left < right:
                    four_sum = nums[i] + nums[j] + nums[left] + nums[right]
                    if four_sum == target:
                        res.append([nums[i], nums[j], nums[left], nums[right]])
                        while left < right and nums[left] == nums[left + 1]:
                            left += 1
                        while left < right and nums[right] == nums[right - 1]:
                            right -= 1
                        left += 1
                        right -= 1
                    elif four_sum > target:
                        right -= 1
                    else:
                        left += 1
        return res


if __name__ == "__main__":
    print(Solution().fourSum([1, 0, -1, 0, -2, 2], 0))
    print(Solution().fourSum([2, 2, 2, 2, 2], 8))
