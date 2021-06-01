class MyStack:

    def __init__(self):
        self.que = []

    def push(self, x: int) -> None:
        self.que.append(x)
        for i in range(0, len(self.que) - 1):
            self.que.append(self.que.pop(0))

    def pop(self) -> int:
        return self.que.pop(0)

    def top(self) -> int:
        return self.que[0]

    def empty(self) -> bool:
        return len(self.que) == 0


if __name__ == "__main__":
    obj = MyStack()
    obj.push(1)
    obj.push(2)
    param_2 = obj.pop()
    param_3 = obj.top()
    param_4 = obj.empty()
    print(param_2, param_3, param_4)
