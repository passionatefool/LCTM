class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        if dividend == 0 or divisor == 0:
            return 0
        if dividend == pow(-2, 31) and divisor == -1:
            return pow(2, 31) - 1

        sign_diff = (dividend > 0) != (divisor > 0)
        i = j = total = 0
        while True:
            tmp = total - (divisor << j) if sign_diff else total + (divisor << j)
            if 0 < dividend < tmp or 0 > dividend > tmp:
                if j == 0:
                    break
                j -= 1
                continue
            total = tmp
            i += 1 << j
            j += 1
        return -i if sign_diff else i


if __name__ == "__main__":
    print(Solution().divide(10, 3))
    print(Solution().divide(-2147483648, 1))
    print(Solution().divide(-2147483648, -1))
