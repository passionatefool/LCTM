package main

import "fmt"

func nextGreaterElements(nums []int) []int {
	n := len(nums)
	res := make([]int, n)
	for i := 0; i < n; i++ {
		res[i] = -1
	}
	var stack []int
	for i := 0; i < n*2-1; i++ {
		for len(stack) > 0 && nums[i%n] > nums[stack[len(stack)-1]] {
			tmp := stack[len(stack)-1]
			res[tmp] = nums[i%n]
			stack = stack[:len(stack)-1]
		}
		stack = append(stack, i%n)
	}
	return res
}

func main() {
	fmt.Println(nextGreaterElements([]int{1, 2, 1}))
}
