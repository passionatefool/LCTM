package main

import "fmt"

type MyQueue struct {
	stackIn, stackOut []int
}

/** Initialize your data structure here. */
func Constructor() MyQueue {
	return MyQueue{}
}

func (this *MyQueue) Dump() {
	if len(this.stackOut) == 0 {
		for len(this.stackIn) > 0 {
			this.stackOut = append(this.stackOut, this.stackIn[len(this.stackIn)-1])
			this.stackIn = this.stackIn[:len(this.stackIn)-1]
		}

	}
}

/** Push element x to the back of queue. */
func (this *MyQueue) Push(x int) {
	this.stackIn = append(this.stackIn, x)
}

/** Removes the element from in front of queue and returns that element. */
func (this *MyQueue) Pop() int {
	this.Dump()
	res := this.stackOut[len(this.stackOut)-1]
	this.stackOut = this.stackOut[:len(this.stackOut)-1]
	return res
}

/** Get the front element. */
func (this *MyQueue) Peek() int {
	this.Dump()
	return this.stackOut[len(this.stackOut)-1]
}

/** Returns whether the queue is empty. */
func (this *MyQueue) Empty() bool {
	return len(this.stackIn) == 0 && len(this.stackOut) == 0
}

func main() {
	obj := Constructor()
	obj.Push(1)
	obj.Push(2)
	fmt.Println(obj.Peek())
	fmt.Println(obj.Pop())
	fmt.Println(obj.Empty())
}
