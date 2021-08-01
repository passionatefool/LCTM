package main

import "fmt"

func combinationSum(candidates []int, target int) [][]int {
	var res [][]int
	var recursive func(start int, sum int, path []int)
	recursive = func(start int, sum int, path []int) {
		if sum >= target {
			if sum == target {
				tmp := make([]int, len(path))
				copy(tmp, path)
				res = append(res, tmp)
			}
			return
		}
		for i := start; i < len(candidates); i++ {
			path = append(path, candidates[i])
			recursive(i, sum+candidates[i], path)
			path = path[:len(path)-1]
		}
	}
	recursive(0, 0, []int{})
	return res
}

func main() {
	fmt.Println(combinationSum([]int{2, 3, 6, 7}, 7))
}
