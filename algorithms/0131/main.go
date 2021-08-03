package main

import "fmt"

func partition(s string) [][]string {
	var res [][]string
	var dfs func(start int, path []string)
	dfs = func(start int, path []string) {
		if start == len(s) {
			tmp := make([]string, len(path))
			copy(tmp, path)
			res = append(res, tmp)
			return
		}
		for i := start; i < len(s); i++ {
			if isPartition(s, start, i) {
				path = append(path, s[start:i+1])
				dfs(i+1, path)
				path = path[:len(path)-1]
			}
		}
	}
	dfs(0, []string{})
	return res
}

func isPartition(s string, start int, end int) bool {
	for start < end {
		if s[start] != s[end] {
			return false
		} else {
			start++
			end--
		}
	}
	return true
}

func main() {
	fmt.Println(partition("aab"))
}
