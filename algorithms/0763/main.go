package main

import "fmt"

func partitionLabels(s string) []int {
	maxPos := map[uint8]int{}
	for i := 0; i < len(s); i++ {
		maxPos[s[i]] = i
	}

	var res []int
	scannedMaxPos := 0
	start := 0
	for i := 0; i < len(s); i++ {
		curCharMaxPos := maxPos[s[i]]
		if curCharMaxPos > scannedMaxPos {
			scannedMaxPos = curCharMaxPos
		}
		if i == scannedMaxPos {
			res = append(res, i - start + 1)
			start = i + 1
		}
	}
	return res
}

func main() {
	fmt.Println(partitionLabels("ababcbacadefegdehijhklij"))
}
