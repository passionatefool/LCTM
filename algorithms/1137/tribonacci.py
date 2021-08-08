class Solution:
    def __init__(self):
        self.results = None

    def tribonacci(self, n: int) -> int:
        if not self.results:
            if n <= 2:
                return 0 if n == 0 else 1
            self.results = [0] * (n + 1)
            self.results[0], self.results[1], self.results[2] = 0, 1, 1
        if n == 0 or self.results[n] != 0:
            return self.results[n]

        self.results[n] = self.tribonacci((n - 1)) + self.tribonacci(n - 2) + self.tribonacci(n - 3)
        return self.results[n]


if __name__ == "__main__":
    print(Solution().tribonacci(4))
