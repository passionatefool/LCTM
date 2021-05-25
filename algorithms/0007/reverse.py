class Solution:
    def reverse(self, x: int) -> int:
        is_minus = x < 0
        x = abs(x)
        i, result = 10, 0
        while i <= x * 10:
            result = result * 10 + int(x % i / (i / 10))
            i *= 10
        if is_minus:
            result = 0 - result
        if not (-2 ** 31 <= result <= 2 ** 31 - 1):
            return 0
        return result


if __name__ == "__main__":
    print(Solution().reverse(123))
