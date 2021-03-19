package main

import "fmt"

func contains(s []int, i int) bool {
	for _, v := range s {
		if v == i {
			return true
		}
	}

	return false
}

func singleNumber(nums []int) int {
	d := map[int]int{}
	for _, v := range nums {
		if contains(nums, v) {
			d[v] += 1
		} else {
			d[v] = 1
		}
	}
	for k, v := range d {
		if v == 1 {
			return k
		}
	}
	return 0
}

func singleNumber2(nums []int) int {
	var res int
	for _, v := range nums {
		res ^= v
	}
	return res
}

func main() {
	fmt.Println(singleNumber([]int{4, 1, 2, 1, 2}))
}
