from typing import List


class Solution:
    def findLength(self, A: List[int], B: List[int]) -> int:
        la, lb = len(A) + 1, len(B) + 1
        dp = [[0 for _ in range(lb)] for _ in range(la)]
        result = 0
        for i in range(1, la):
            for j in range(1, lb):
                if A[i - 1] == B[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                    result = max(result, dp[i][j])
        return result


if __name__ == "__main__":
    print(Solution().findLength([1, 0, 0, 0, 1], [1, 0, 0, 1, 1]))
