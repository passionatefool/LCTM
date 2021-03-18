package main

import "fmt"

func twoSum(nums []int, target int) []int {
	m := map[int]int{}
	for i, num := range nums {
		diff := target - nums[i]
		if val, exist := m[diff]; exist {
			return []int{i, val}
		} else {
			m[num] = i
		}
	}
	return nil
}

func main() {
	nums := []int{1, 2, 3, 4, 5}
	fmt.Println(twoSum(nums, 7))
}

