package main

import (
	"fmt"
	"sort"
)

func reconstructQueue(people [][]int) [][]int {
	var queue [][]int
	sort.Slice(people, func(i, j int) bool {
		if people[i][0] == people[j][0] {
			return people[i][1] < people[j][1]
		}
		return people[i][0] > people[j][0]
	})
	for _, v := range people {
		if len(queue) <= v[1] {
			queue = append(queue, v)
		} else {
			queue = append(queue, []int{})
			copy(queue[v[1]+1:], queue[v[1]:])
			queue[v[1]] = v
		}
	}
	return queue
}

func main() {
	fmt.Println(reconstructQueue([][]int{{7, 0}, {4, 4}, {7, 1}, {5, 0}, {6, 1}, {5, 2}}))
}
