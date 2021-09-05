package main

import "fmt"

func minCostClimbingStairs(cost []int) int {
	dp := make([]int, len(cost))
	dp[0] = cost[0]
	dp[1] = cost[1]
	for i := 2; i < len(cost); i++ {
		dp[i] = min(dp[i-1], dp[i-2]) + cost[i]
	}
	fmt.Println(dp)
	return min(dp[len(cost)-1], dp[len(cost)-2])
}

func min(x, y int) int {
	if x < y {
		return x
	}
	return y
}

func main() {
	//fmt.Println(minCostClimbingStairs([]int{10, 15, 20}))
	fmt.Println(minCostClimbingStairs([]int{1, 100, 1, 1, 1, 100, 1, 1, 100, 1}))
}
