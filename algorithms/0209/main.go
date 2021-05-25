package main

import (
	"fmt"
	"math"
)

func minSubArrayLen(target int, nums []int) int {
	resLen := math.MaxInt32
	resSum := 0
	i, j := 0, 0
	for i < len(nums) {
		resSum += nums[i]
		for resSum >= target {
			subLen := i - j + 1
			if subLen < resLen {
				resLen = subLen
			}
			resSum -= nums[j]
			j++
		}
		i++
	}
	if resLen == math.MaxInt32 {
		return 0
	}
	return resLen
}

func main() {
	fmt.Println(minSubArrayLen(7, []int{2, 3, 1, 2, 4, 3}))
}
