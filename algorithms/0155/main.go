package main

import (
	"fmt"
	"math"
)

type MinStack struct {
	stack []int
	minStack []int
}

/** initialize your data structure here. */
func Constructor() MinStack {
	return MinStack{
		stack: []int{},
		minStack: []int{math.MaxInt64},
	}

}

func min(x, y int) int {
	if x < y {
		return x
	}
	return y
}

func (this *MinStack) Push(val int) {
	this.stack = append(this.stack, val)
	minVal := this.minStack[len(this.minStack)-1]
	this.minStack = append(this.minStack, min(val, minVal))
}

func (this *MinStack) Pop() {
	this.stack = this.stack[:len(this.stack)-1]
	this.minStack = this.minStack[:len(this.minStack)-1]
}

func (this *MinStack) Top() int {
	return this.stack[len(this.stack)-1]
}

func (this *MinStack) GetMin() int {
	return this.minStack[len(this.minStack)-1]
}

func main() {
	obj := Constructor()
	obj.Push(-2)
	obj.Push(0)
	obj.Push(-3)
	fmt.Println(obj.GetMin())
	obj.Pop()
	fmt.Println(obj.Top())
	fmt.Println(obj.GetMin())
}
