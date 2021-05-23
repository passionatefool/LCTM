class MyQueue:

    def __init__(self):
        self.stack_in = []
        self.stack_out = []

    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        self.stack_in.append(x)

    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        self.dump()
        return self.stack_out.pop()

    def peek(self) -> int:
        """
        Get the front element.
        """
        self.dump()
        return self.stack_out[-1]

    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        return len(self.stack_in) == 0 and len(self.stack_out) == 0

    def dump(self):
        if len(self.stack_out) == 0:
            while len(self.stack_in) != 0:
                self.stack_out.append(self.stack_in.pop())


if __name__ == "__main__":
    queue = MyQueue()
    queue.push(1)
    queue.push(2)
    queue.peek()
    queue.pop()
    queue.empty()
