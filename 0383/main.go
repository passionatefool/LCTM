package main

import "fmt"

func canConstruct(ransomNote string, magazine string) bool {
	m := map[rune]int{}

	for _, v := range magazine {
		m[v]++
	}
	for _, v := range ransomNote {
		if val, ok := m[v]; ok && val>0 {
			m[v]--
		} else {
			return false
		}
	}
	return true
}

func main() {
	fmt.Println(canConstruct("aa", "ab"))
}
