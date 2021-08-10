package main

import (
	"fmt"
	"sort"
)

func findContentChildren(g []int, s []int) int {
	res := 0
	sort.Ints(g)
	sort.Ints(s)
	for i := 0; res < len(g) && i < len(s); i++ {
		if s[i] >= g[res] {
			res++
		}
	}
	return res
}

func main() {
	fmt.Println(findContentChildren([]int{1, 2}, []int{1, 2, 3}))
}
