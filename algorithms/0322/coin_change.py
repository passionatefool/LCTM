from typing import List


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [0] + [amount + 1] * amount
        for i in range(1, amount + 1):
            for coin in coins:
                if i - coin >= 0:
                    dp[i] = min(dp[i - coin] + 1, dp[i])
        return dp[-1] if dp[-1] != amount+1 else -1


if __name__ == "__main__":
    print(Solution().coinChange([1, 2, 5], 11))
