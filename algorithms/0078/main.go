package main

import "fmt"

func subsets(nums []int) [][]int {
	res := [][]int{}
	res = append(res, []int{})
	for _, v := range nums {
		tmpArr := [][]int{}
		for _, r := range res {
			tmp := []int{}
			tmp = append(tmp, r...)
			tmp = append(tmp, v)
			tmpArr = append(tmpArr, tmp)
		}
		for _, c := range tmpArr {
			res = append(res, c)
		}
	}
	return res
}

func main() {
	fmt.Println(subsets([]int{1,2,3}))
}
