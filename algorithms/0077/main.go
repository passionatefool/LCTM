package main

import "fmt"

func combine(n int, k int) [][]int {
	var res [][]int
	var backtrack func(start int, subRes []int)
	backtrack = func(start int, subRes []int) {
		if len(subRes) == k {
			tmp := make([]int, len(subRes))
			copy(tmp, subRes)
			res = append(res, tmp)
			return
		}
		for i := start; i <= n; i++ {
			subRes = append(subRes, i)
			backtrack(i + 1, subRes)
			subRes = subRes[:len(subRes)-1]
		}
	}
	backtrack(1, []int{})
	return res
}

func main() {
	fmt.Println(combine(4, 2))
}
