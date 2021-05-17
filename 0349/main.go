package main

import "fmt"

func intersection(nums1 []int, nums2 []int) (intersection []int) {
	hash := map[int]bool{}
	res := []int{}

	for _, v := range nums1 {
		hash[v] = true
	}

	for _, v := range nums2 {
		if hash[v] == true {
			res = append(res, v)
			hash[v] = false
		}
	}
	return res
}

// python 重拳出击 🤜：`list(set(nums1) & set(nums2))`

func main() {
	fmt.Println(intersection([]int{1, 2, 2, 1}, []int{2, 2}))
}
