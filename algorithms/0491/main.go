package main

import "fmt"

func findSubsequences(nums []int) [][]int {
	var res [][]int
	var dfs func(start int, path []int)
	dfs = func(start int, path []int) {
		if len(path) > 1 {
			tmp := make([]int, len(path))
			copy(tmp, path)
			res = append(res, tmp)
		}
		var pathSet [201]bool
		for i := start; i < len(nums); i++ {
			if len(path) > 0 && path[len(path)-1] > nums[i] {
				continue
			}
			if pathSet[nums[i]+100] {
				continue
			}
			pathSet[nums[i]+100] = true
			path = append(path, nums[i])
			dfs(i+1, path) //
			path = path[:len(path)-1]
		}
	}
	dfs(0, []int{})
	return res
}

func main() {
	//fmt.Println(findSubsequences([]int{4, 6, 7, 7}))
	fmt.Println(findSubsequences([]int{4, 4, 3, 2, 1}))
}
