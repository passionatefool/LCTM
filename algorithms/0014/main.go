package main

import "fmt"

func longestCommonPrefix(strs []string) string {
	prefix, length := strs[0], len(strs)
	for i := 1; i < length; i++ {
		prefix = makeLongest(prefix, strs[i])
	}
	return prefix
}

func makeLongest(str1 string, str2 string) string {
	index := 0
	length := min(len(str1), len(str2))
	for ; index < length && str1[index] == str2[index]; index++ {
	}
	return str1[:index]
}

func min(x, y int) int {
	if x < y {
		return x
	}
	return y
}

func main() {
	fmt.Println(longestCommonPrefix([]string{"flower", "flow", "flight"}))
}
