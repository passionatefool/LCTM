package main

import "fmt"

func isAnagram(s string, t string) bool {
	if len(s) != len(t) {
		return false
	}
	m := make(map[rune]int)

	for _, c := range s {
		m[c]++
	}

	for _, c := range t {
		if val, existed := m[c]; !existed || val == 0 {
			return false
		} else {
			m[c]--
		}
	}

	for _, v := range m {
		if v != 0 {
			return false
		}
	}
	return true
}

func main() {
	fmt.Println(isAnagram("anagram", "nagaram"))
}
