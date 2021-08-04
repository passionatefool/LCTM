package main

import (
	"fmt"
	"strconv"
	"strings"
)

var MAX = 255

func restoreIpAddresses(s string) []string {
	var res []string
	var dfs func(start int, subRes []string)
	dfs = func(start int, subRes []string) {
		if len(subRes) == 4 && start == len(s) {
			res = append(res, strings.Join(subRes, "."))
			return
		}
		// dose not fully use all of s
		if len(subRes) == 4 && start < len(s) {
			return
		}

		for i := 1; i < 4; i++ {
			if start+i-1 >= len(s) {
				return
			}
			if i != 1 && s[start] == '0' {
				return
			}
			str := s[start : start+i]
			converedStr, _ := strconv.Atoi(str)
			if converedStr > MAX {
				return
			}
			subRes = append(subRes, str)
			dfs(start+i, subRes)
			subRes = subRes[:len(subRes)-1]
		}
	}
	dfs(0, []string{})
	return res
}

func main() {
	fmt.Println(restoreIpAddresses("25525511135"))
}
