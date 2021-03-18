from typing import List


class Solution:
    def __init__(self):
        pass

    def maxProfit(self, prices: List[int]) -> int:
        result, lowest = 0, 0
        for i in range(1, len(prices), 1):
            if prices[i] < prices[lowest]:
                lowest = i
            else:
                result = max(result, prices[i] - prices[lowest])
        return result


def main():
    s = Solution()
    print(s.maxProfit([7, 1, 5, 3, 6, 4]))


if __name__ == "__main__":
    main()
