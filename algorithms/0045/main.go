package main

import "fmt"

func jump(nums []int) int {
	res := 0
	end := 0
	maxPos := 0
	for i := 0; i < len(nums)-1; i++ {
		maxPos = max(maxPos, i+nums[i])
		if i == end {
			end = maxPos
			res++
		}
	}
	return res
}

func max(x, y int) int {
	if x > y {
		return x
	}
	return y
}

func main() {
	fmt.Println(jump([]int{2, 3, 1, 1, 4}))
}
