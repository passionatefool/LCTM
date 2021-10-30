package main

import "fmt"

func nextGreaterElement(nums1 []int, nums2 []int) []int {
	res := make([]int, 0, len(nums1))
	dict := make(map[int]int, len(nums2))

	var stack []int
	for _, n := range nums2 {
		for len(stack) > 0 && n > stack[len(stack)-1] {
			tmp := stack[len(stack)-1]
			dict[tmp] = n
			stack = stack[:len(stack)-1]
		}
		stack = append(stack, n)
	}
	for i := 0; i < len(nums1); i++ {
		if v, ok := dict[nums1[i]]; ok {
			res = append(res, v)
		} else {
			res = append(res, -1)
		}
	}
	return res
}

func main() {
	fmt.Println(nextGreaterElement([]int{4, 1, 2}, []int{1, 3, 4, 2}))
}
