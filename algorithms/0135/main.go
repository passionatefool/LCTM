package main

import (
	"fmt"
)

func candy(ratings []int) int {
	res := 0
	left := make([]int, len(ratings))
	for i := range left {
		left[i] = 1
	}
	right := make([]int, len(ratings))
	copy(right, left)

	for i := 1; i < len(ratings); i++ {
		if ratings[i] > ratings[i-1] {
			left[i] = left[i-1] + 1
		}
	}
	for j := len(ratings) - 2; j >= 0; j-- {
		if ratings[j] > ratings[j+1] {
			right[j] = right[j+1] + 1
		}
	}

	for k := 0; k < len(ratings); k++ {
		res += max(left[k], right[k])
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
	fmt.Println(candy([]int{1, 2, 2}))
}
