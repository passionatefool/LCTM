package main

import "fmt"

func fib(n int) int {
	if n == 0 {
		return 0
	}
	dp := make([]int, n+1)
	dp[0], dp[1] = 0, 1
	for i := 2; i <= n; i++ {
		dp[i] = dp[i-1] + dp[i-2]
	}
	fmt.Println(dp)
	return dp[n]
}

func main() {
	fmt.Println(fib(2))
	fmt.Println(fib(0))
}
