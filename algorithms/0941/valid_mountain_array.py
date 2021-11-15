from typing import List


class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        if len(arr) < 3:
            return False
        pre, up, m = 0, True, 0
        for i in range(1, len(arr)):
            if up:
                if arr[i] < arr[pre]:
                    m = pre
                    up = False
                elif arr[i] == arr[pre]:
                    return False
            elif arr[i] >= arr[pre]:
                return False
            pre = i
        return m != 0


if __name__ == "__main__":
    print(Solution().validMountainArray([0, 3, 2, 1]))
    print(Solution().validMountainArray([3, 5, 5]))
    print(Solution().validMountainArray([9, 8, 7, 6, 5, 4, 3, 2, 1, 0]))
