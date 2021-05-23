package main

import "fmt"

func fourSumCount(nums1 []int, nums2 []int, nums3 []int, nums4 []int) int {
	res := 0
	mapAB := map[int]int{}
	for _, a := range nums1 {
		for _, b := range nums2 {
			mapAB[a+b]++
		}
	}

	for _, c := range nums3 {
		for _, d := range nums4 {
			if val, ok := mapAB[-c-d]; ok {
				res+=val
			}
		}
	}
	return res
}

func main() {
	fmt.Println(fourSumCount([]int{1, 2}, []int{-2, -1}, []int{-1, 2}, []int{0, 2}))
}
