package main

import (
	"fmt"
	"sort"
)

func merge(intervals [][]int) [][]int {
	var res [][]int
	sort.Slice(intervals, func(i, j int) bool {
		return intervals[i][0] < intervals[j][0]
	})
	for i := 0; i < len(intervals); i++ {
		if len(res) == 0 || res[len(res)-1][1] < intervals[i][0] {
			res = append(res, intervals[i])
		} else {
			res[len(res)-1][1] = max(res[len(res)-1][1], intervals[i][1])
		}
	}
	return res
}

func max(x, y int) int {
	if x > y {
		return x
	}
	return y
}

func main() {
	fmt.Println(merge([][]int{{1, 3}, {2, 6}, {8, 10}, {15, 18}}))
	fmt.Println(merge([][]int{{1, 4}, {4, 5}}))
}

/*
1 --- 3
   2 ------6
                8 ------ 10
                               15 ------18

1 --- 4
      4 ---- 5
*/
