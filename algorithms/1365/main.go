package main

import "fmt"

func smallerNumbersThanCurrent(nums []int) []int {
	res := make([]int, len(nums))
	tmp := make([]int, 101)
	for _, v := range nums {
		tmp[v]++
	}
	for i, v := range nums {
		res[i] = getCount(tmp[:v])
	}
	return res
}

func getCount(arr []int) int {
	res := 0
	for _, v := range arr {
		res += v
	}
	return res
}

func main() {
	fmt.Println(smallerNumbersThanCurrent([]int{8, 1, 2, 2, 3}))
}
