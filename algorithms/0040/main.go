package main

import (
	"fmt"
	"sort"
)

func combinationSum2(candidates []int, target int) [][]int {
	sort.Ints(candidates)
	var res [][]int
	var dfs func(start int, sum int, path []int)
	dfs = func(start int, sum int, path []int) {
		if sum >= target {
			if sum == target {
				tmp := make([]int, len(path))
				copy(tmp, path)
				res = append(res, tmp)
			}
			return
		}
		for i := start; i < len(candidates); i++ {
			if i > start && candidates[i-1] == candidates[i] {
				continue
			}
			path = append(path, candidates[i])
			dfs(i+1, sum+candidates[i], path)
			path = path[:len(path)-1]
		}
	}
	dfs(0, 0, []int{})
	return res
}

func main() {
	//fmt.Println(combinationSum2([]int{10, 1, 2, 7, 6, 1, 5}, 8))
	fmt.Println(combinationSum2([]int{14, 6, 25, 9, 30, 20, 33, 34, 28, 30, 16, 12, 31, 9, 9, 12, 34, 16, 25, 32, 8, 7, 30, 12, 33, 20, 21, 29, 24, 17, 27, 34, 11, 17, 30, 6, 32, 21, 27, 17, 16, 8, 24, 12, 12, 28, 11, 33, 10, 32, 22, 13, 34, 18, 12}, 27))
}
