package main

import (
	"fmt"
	"sort"
)

func permuteUnique(nums []int) [][]int {
	var res [][]int
	used := make([]bool, len(nums))
	sort.Ints(nums)
	var dfs func(path []int, used []bool)
	dfs = func(path []int, used []bool) {
		if len(path) == len(nums) {
			tmp := make([]int, len(nums))
			copy(tmp, path)
			res = append(res, tmp)
			return
		}
		for i := 0; i < len(nums); i++ {
			if used[i] {
				continue
			}
			if i > 0 && nums[i-1] == nums[i] && used[i-1] == false {
				continue
			}
			path = append(path, nums[i])
			used[i] = true
			dfs(path, used)
			path = path[:len(path)-1]
			used[i] = false
		}
	}
	dfs([]int{}, used)
	return res
}

func main() {
	fmt.Println(permuteUnique([]int{1, 1, 2}))
}
