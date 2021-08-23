class Solution:
    def __init__(self):
        self.cache = {0: 0}

    def numSquares(self, n: int) -> int:
        if n in self.cache:
            return self.cache[n]
        i = 1
        res = float("inf")
        while i * i <= n:
            target = n - i * i
            res = min(res, self.numSquares(target) + 1)
            i += 1
        self.cache[n] = res
        return res


if __name__ == "__main__":
    print(Solution().numSquares(12))
    print(Solution().numSquares(13))
