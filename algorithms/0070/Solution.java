package main;

import java.util.Arrays;

public class Solution {
    public int climbStairs(int n) {
        int[] dp = new int[n + 1];
        for (int i = 0; i < n + 1; i++) {
            if (i <= 2) {
                dp[i] = i;
            } else {
                dp[i] = dp[i - 1] + dp[i - 2];
            }
        }
        return dp[n];
    }

    public static void main(String[] args) {
        Solution solution = new Solution();
        System.out.println(solution.climbStairs(3));
    }
}
