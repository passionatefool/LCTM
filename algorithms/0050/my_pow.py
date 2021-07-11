class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n < 0:
            return 1 / self.helper(x, -n)
        return self.helper(x, n)

    def helper(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        return (1 if n % 2 == 0 else x) * self.helper(x * x, int(n / 2))


if __name__ == "__main__":
    print(Solution().myPow(2.0, 10))
    print(Solution().myPow(2.0, -2))
