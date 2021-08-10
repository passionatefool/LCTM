package main

import "fmt"

func wiggleMaxLength(nums []int) int {
	var res, cur, pre int
	res = 1
	for i := 1; i < len(nums); i++ {
		cur = nums[i] - nums[i-1]
		if cur > 0 && pre <= 0 || cur < 0 && pre >= 0 {
			pre = cur
			res++
		}
	}
	return res
}

func main() {
	fmt.Println(wiggleMaxLength([]int{1, 7, 4, 9, 2, 5}))
}
