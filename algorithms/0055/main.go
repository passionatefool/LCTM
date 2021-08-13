package main

import (
	"fmt"
	"math"
)

func canJump(nums []int) bool {
	cov := 0
	if len(nums) == 1 {
		return true
	}
	for i := 0; i < len(nums); i++ {
		// cannot covered
		if i > cov {
			return false
		}
		cov = int(math.Max(float64(cov), float64(i+nums[i])))
	}
	return true
}

func main() {
	fmt.Println(canJump([]int{3, 2, 1, 0, 4}))
	fmt.Println(canJump([]int{2, 3, 1, 1, 4}))
	fmt.Println(canJump([]int{2, 0}))
}
