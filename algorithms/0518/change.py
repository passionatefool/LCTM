from typing import List


class Solution:
    # def __init__(self):
    #     self.result = 0

    # def change(self, amount: int, coins: List[int]) -> int:
    #     def dfs(amount, index):
    #         if amount == 0:
    #             self.result += 1
    #             return
    #         for i in range(index, len(coins)):
    #             if amount - coins[i] >= 0:
    #                 dfs(amount - coins[i], i)
    #
    #     dfs(amount, 0)
    #     return self.result

    def change(self, amount: int, coins: List[int]) -> int:
        dp = [0] * (amount+1)
        dp[0] = 1
        for coin in coins:
            for i in range(coin, amount+1):
                dp[i] = dp[i] + dp[i - coin]
        return dp[-1]


if __name__ == "__main__":
    print(Solution().change(5, [1, 2, 5]))
