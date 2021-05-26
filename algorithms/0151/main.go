package main

import (
	"fmt"
	"strings"
)

func reverseWords(s string) string {
	res := strings.Fields(s)
	length := len(res)
	for i := 0; i < length/2; i++ {
		res[i], res[length-1-i] = res[length-1-i], res[i]
	}
	return strings.Join(res, " ")
}

func main() {
	fmt.Println(reverseWords("  hello world!  "))
}
