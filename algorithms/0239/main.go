package main

import (
	"fmt"
)

func maxSlidingWindow(nums []int, k int) []int {
	var res []int
	var queue []int

	if len(nums) == 1 {
		res = append(res, nums[0])
		return res
	}

	for i, v := range nums {
		// 维持队列递减
		for len(queue) > 0 && v > nums[queue[len(queue)-1]] {
			queue = queue[:len(queue)-1]
		}
		queue = append(queue, i)

		if i >= k-1 {
			res = append(res, nums[queue[0]])
			if queue[0] <= i-k+1 {
				queue = queue[1:]
			}
		}
	}
	return res
}

func main() {
	fmt.Println(maxSlidingWindow([]int{1, 3, -1, -3, 5, 3, 6, 7}, 3))
	fmt.Println(maxSlidingWindow([]int{1, -1}, 1))
	fmt.Println(maxSlidingWindow([]int{9, 11}, 2))
	fmt.Println(maxSlidingWindow([]int{4, -1}, 2))
	fmt.Println(maxSlidingWindow([]int{7, 4, 2}, 2))
}
