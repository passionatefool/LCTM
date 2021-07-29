package main

import (
	"fmt"
	"strconv"
	"strings"
)

var mapping = []string{"", "", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"}

func letterCombinations(digits string) []string {
	if len(digits) == 0 {
		return []string{}
	}
	var res []string
	strList := strings.Split(digits, "")
	var target []string
	for _, i := range strList {
		j, _ := strconv.Atoi(i)
		target = append(target, mapping[j])
	}
	var recursive func(start int, subRes string)
	recursive = func(start int, subRes string) {
		if len(subRes) == len(target) {
			res = append(res, subRes)
			return
		}
		letter := target[start]
		for _, j := range letter {
			subRes = subRes + string(j)
			recursive(start+1, subRes)
			subRes = subRes[:len(subRes)-1]
		}
	}
	recursive(0, "")
	return res
}

func main() {
	fmt.Println(letterCombinations("23"))
}
