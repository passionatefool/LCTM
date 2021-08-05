from collections import deque
from typing import List


class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        n = len(nums)
        min_deque, max_deque = deque(), deque()
        left, right, result = 0, 0, 0
        while right < n:
            # inserted = False
            # for i in range(len(s)):
            #     if s[i] >= nums[right]:
            #         s.insert(i, nums[right])
            #         inserted = True
            #         break
            # if not inserted:
            #     s.append(nums[right])
            while min_deque and nums[right] <= nums[min_deque[-1]]:
                min_deque.pop()
            while max_deque and nums[right] >= nums[max_deque[-1]]:
                max_deque.pop()
            min_deque.append(right)
            max_deque.append(right)
            while nums[max_deque[0]] - nums[min_deque[0]] > limit:
                left += 1
                if left > min_deque[0]:
                    min_deque.popleft()
                if left > max_deque[0]:
                    max_deque.popleft()

            result = max(result, right - left + 1)
            right += 1
        return result


if __name__ == "__main__":
    print(Solution().longestSubarray([8, 2, 4, 7], 4))
