package main

import (
	"container/heap"
	"fmt"
)

type IntHeap [][2]int

func (h IntHeap) Len() int {
	return len(h)
}

func (h IntHeap) Less(i, j int) bool {
	return h[i][1] < h[j][1]
}

func (h IntHeap) Swap(i, j int) {
	h[i], h[j] = h[j], h[i]
}

func (h *IntHeap) Push(x interface{}) {
	*h = append(*h, x.([2]int))
}

func (h *IntHeap) Pop() interface{} {
	tmp := *h
	x := tmp[len(tmp)-1]
	*h = tmp[:len(tmp)-1]
	return x
}

func topKFrequent(nums []int, k int) []int {
	maps := map[int]int{}
	for _, n := range nums {
		maps[n]++
	}
	h := &IntHeap{}
	heap.Init(h)

	for key, v := range maps {
		heap.Push(h, [2]int{key, v})
		if h.Len() > k {
			heap.Pop(h)
		}
	}

	res := make([]int, k)
	for i := 0; i < k; i++ {
		res[k-i-1] = heap.Pop(h).([2]int)[0]
	}
	return res
}

func main() {
	fmt.Println(topKFrequent([]int{1, 1, 1, 2, 2, 3}, 2))
}
