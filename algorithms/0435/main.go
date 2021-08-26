package main

import (
	"fmt"
	"sort"
)

func eraseOverlapIntervals(intervals [][]int) int {
	res := 0
	sort.Slice(intervals, func(i, j int) bool {
		if intervals[i][0] == intervals[j][0] {
			return intervals[i][1] < intervals[j][1]
		} else {
			return intervals[i][0] < intervals[j][0]
		}
	})
	for i := 1; i < len(intervals); i++ {
		if intervals[i][0] < intervals[i-1][1] {
			res++
			intervals[i][1] = min(intervals[i][1], intervals[i-1][1])
		}
	}
	return res
}

func min(x, y int) int {
	if x < y {
		return x
	}
	return y
}

func main() {
	fmt.Println(eraseOverlapIntervals([][]int{{1, 2}, {2, 3}, {3, 4}, {1, 3}})) // 1
	fmt.Println(eraseOverlapIntervals([][]int{{1, 2}, {1, 2}, {1, 2}})) // 2
	fmt.Println(eraseOverlapIntervals([][]int{{1, 2}, {2, 3}})) // 0
	fmt.Println(eraseOverlapIntervals([][]int{{1, 100}, {11, 22}, {1, 11}, {2, 12}})) // 2
	fmt.Println(eraseOverlapIntervals([][]int{{0, 2}, {1, 3}, {2, 4}, {3, 5}, {4, 6}})) // 2
}
