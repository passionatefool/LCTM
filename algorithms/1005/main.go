package main

import (
	"fmt"
	"sort"
)

func largestSumAfterKNegations(nums []int, k int) int {
	res := 0
	sort.Ints(nums)
	for i := 0; i < len(nums); i++ {
		if k == 0 {
			break
		}
		if nums[i] < 0 {
			nums[i] *= -1
			k--
		}
	}
	// K still != 0, sort again and get the min num
	sort.Ints(nums)
	rest := k % 2
	if rest == 1 {
		nums[0] *= -1
	}
	for _, v := range nums {
		res += v
	}
	return res
}

func main() {
	fmt.Println(largestSumAfterKNegations([]int{4, 2, 3}, 1))
	fmt.Println(largestSumAfterKNegations([]int{3, -1, 0, 2}, 3))
	fmt.Println(largestSumAfterKNegations([]int{2, -3, -1, 5, -4}, 2))
	fmt.Println(largestSumAfterKNegations([]int{-8, 3, -5, -3, -5, -2}, 6))
}

/*
-8 -5 -5 -3 -2 3
*/
