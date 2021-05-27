package main

import "fmt"

func strStr(haystack string, needle string) int {
	if len(needle) == 0 {
		return 0
	}
	if len(haystack) < len(needle) {
		return -1
	}
	for i := 0; i < len(haystack); i++ {
		if haystack[i] == needle[0] {
			j := 0
			for j < len(needle) && i+j < len(haystack) {
				if haystack[i+j] != needle[j] {
					break
				}
				j++
			}
			if j == len(needle) {
				return i
			}
		}
	}
	return -1
}

func main() {
	fmt.Println(strStr("hello", "ll"))
	fmt.Println(strStr("aaaaa", "bba"))
	fmt.Println(strStr("", "a"))
	fmt.Println(strStr("aaa", "aaaa"))
	fmt.Println(strStr("a", "a"))
	fmt.Println(strStr("mississippi", "issip"))
	fmt.Println(strStr("mississippi", "issipi"))
}
