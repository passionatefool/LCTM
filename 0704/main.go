package main

import "fmt"

func search(nums []int, target int) int {
	length := len(nums)
	if length == 1 && nums[0] != target {
		return -1
	}
	return s(nums, target, 0, len(nums)-1)
}

func s(nums []int, target int, start int, end int) int {
	mid := (start + end) / 2
	if start > end {
		return -1
	}
	if nums[mid] > target {
		return s(nums, target, 0, mid-1)
	} else if nums[mid] < target {
		return s(nums, target, mid+1, end)
	} else {
		return mid
	}
}

func main() {
	fmt.Println(search([]int{-1, 0, 3, 5, 9, 12}, 9))
	fmt.Println(search([]int{-1, 0, 3, 5, 9, 12}, 2))
	fmt.Println(search([]int{2, 5}, 5))
}
