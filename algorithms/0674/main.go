package main

import "fmt"

func findLengthOfLCIS(nums []int) int {
	dp := make([]int, len(nums))
	for i := 0; i < len(dp); i++ {
		dp[i] = 1
	}
	res := 1
	for i := 0; i < len(nums) - 1; i++ {
		if nums[i+1] > nums[i] {
			dp[i+1] = dp[i] + 1
		}
		if dp[i+1] > res {
			res = dp[i+1]
		}
	}
	fmt.Println(dp)
	return res
}

func main() {
	fmt.Println(findLengthOfLCIS([]int{1, 3, 5, 4, 7}))
}
