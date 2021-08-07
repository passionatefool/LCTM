package main

import "fmt"

func permute(nums []int) [][]int {
	var res [][]int
	var dfs func(path []int)
	dfs = func(path []int) {
		if len(path) == len(nums) {
			tmp := make([]int, len(nums))
			copy(tmp, path)
			res = append(res, tmp)
			return
		}
		for i := 0; i < len(nums); i++ {
			if contain(path, nums[i]) {
				continue
			}
			path = append(path, nums[i])
			dfs(path)
			path = path[:len(path)-1]
		}
	}
	dfs([]int{})
	return res
}

func contain(nums []int, v int) bool {
	for _, e := range nums {
		if e == v {
			return true
		}
	}
	return false
}

func main() {
	//fmt.Println(permute([]int{1, 2, 3}))
	fmt.Println(permute([]int{5, 4, 6, 2}))
}
