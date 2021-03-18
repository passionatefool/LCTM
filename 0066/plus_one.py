from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        for i in range(len(digits) - 1, -1, -1):
            digits[i] = digits[i] + 1
            if digits[i] < 10:
                return digits
            digits[i] = 0

        if digits[0] == 0:
            digits.insert(0, 1)
        return digits


def main():
    s = Solution()
    print(s.plusOne([9]))


if __name__ == "__main__":
    main()
