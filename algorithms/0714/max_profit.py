from typing import List


class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        buy, sell = -prices[0], 0
        for i in range(1, len(prices)):
            buy = max(buy, sell - prices[i])
            sell = max(sell, buy + prices[i] - fee)
        return sell


if __name__ == "__main__":
    print(Solution().maxProfit([1, 3, 2, 8, 4, 9], 2))
    print(Solution().maxProfit([1, 3, 7, 5, 10, 3], 3))
