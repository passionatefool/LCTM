package main

import (
	"fmt"
	"sort"
)

func subsetsWithDup(nums []int) [][]int {
	var res [][]int
	sort.Ints(nums)
	var dfs func(start int, subRes []int)
	dfs = func(start int, subRes []int) {
		if start > len(nums) {
			return
		}
		tmp := make([]int, len(subRes))
		copy(tmp, subRes)
		res = append(res, tmp)
		for i := start; i < len(nums); i++ {
			if i > start && nums[i] == nums[i-1] {
				continue
			}
			subRes = append(subRes, nums[i])
			dfs(i+1, subRes)
			subRes = subRes[:len(subRes)-1]
		}
	}
	dfs(0, []int{})
	return res
}

func main() {
	fmt.Println(subsetsWithDup([]int{1, 1, 2}))
}
