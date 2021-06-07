from typing import List


class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        res = []
        for i in range(n):
            res.append([0] * n)

        left, right, top, bottom = 0, n-1, 0, n-1
        cur = 1
        while cur <= n * n:
            for i in range(left, right+1):
                res[top][i] = cur
                cur += 1
            top += 1

            for i in range(top, bottom+1):
                res[i][right] = cur
                cur += 1
            right -= 1

            for i in reversed(range(left, right+1)):
                res[bottom][i] = cur
                cur += 1
            bottom -= 1

            for i in reversed(range(top, bottom+1)):
                res[i][left] = cur
                cur += 1
            left += 1
        return res


if __name__ == "__main__":
    print(Solution().generateMatrix(3))
