class Solution:
    def isUgly(self, n: int) -> bool:
        if n <= 0:
            return False
        if n == 1:
            return True
        return (n % 2 == 0 and self.isUgly(int(n / 2))) or (n % 3 == 0 and self.isUgly(int(n / 3))) or (
                n % 5 == 0 and self.isUgly(int(n / 5)))


def main():
    s = Solution()
    print(s.isUgly(6), s.isUgly(8), s.isUgly(14))


if __name__ == "__main__":
    main()
