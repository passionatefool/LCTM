package main

import "fmt"

func combinationSum3(k int, n int) [][]int {
	var res [][]int
	var recursive func(start int, path []int)
	recursive = func(start int, path []int) {
		if len(path) == k {
			var sum int
			tmp := make([]int, len(path))
			copy(tmp, path)
			for _, v := range path {
				sum += v
			}
			if sum == n {
				res = append(res, tmp)
			}
			return
		}
		for i := start; i <= 9 - (k - len(path)) + 1; i++ {
			path = append(path, i)
			recursive(i+1, path)
			path = path[:len(path)-1]
		}
	}
	recursive(1, []int{})
	return res
}

func main() {
	fmt.Println(combinationSum3(3, 9))
}
