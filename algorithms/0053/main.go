package main

import "fmt"

func maxSubArray(nums []int) int {
	maxSum, curSum := nums[0], 0
	for i := range nums {
		if nums[i] < 0 {
			if curSum > -nums[i] {
				// 不会减成负数，可接受
				curSum += nums[i]
			} else {
				// 重新计算
				curSum = nums[i]
			}
		} else {
			// 只要当前和大于 0，就可以加进来
			if curSum > 0 {
				curSum += nums[i]
			} else {
				// 当前和小于 0，不如重新计算
				curSum = nums[i]
			}
		}
		if curSum > maxSum {
			maxSum = curSum
		}
	}
	return maxSum
}


func maxSubArray2(nums []int) int {
	if len(nums) == 0 {
		return 0
	}
	dp := make([]int, len(nums))
	dp[0] = nums[0]
	res := dp[0]
	for i := 1; i < len(nums); i++ {
		dp[i] = max(dp[i-1]+nums[i], nums[i])
		if dp[i] > res {
			res = dp[i]
		}
	}
	return res
}

func max(a, b int) int {
	if a > b {
		return a
	}
	return b
}

func main() {
	fmt.Println(maxSubArray([]int{-2, 1, -3, 4, -1, 2, 1, -5, 4}))
	fmt.Println(maxSubArray2([]int{-2, 1, -3, 4, -1, 2, 1, -5, 4}))
}
