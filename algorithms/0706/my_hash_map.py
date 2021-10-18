class Node:
    def __init__(self, key, val: int, n=None):
        self.key = key
        self.val = val
        self.next = n


class MyHashMap:

    def __init__(self):
        self.size = 1000
        self.data = [None] * self.size

    def put(self, key: int, value: int) -> None:
        k = self.hashKey(key)
        head = self.data[k]
        if not head:
            self.data[k] = Node(key, value)
            return
        while head:
            if head.key == key:
                head.val = value
                return
            if not head.next:
                break
            head = head.next
        head.next = Node(key, value)

    def get(self, key: int) -> int:
        k = self.hashKey(key)
        head = self.data[k]
        while head:
            if head.key == key:
                return head.val
            head = head.next
        return -1

    def remove(self, key: int) -> None:
        k = self.hashKey(key)
        head = self.data[k]

        prev = None
        while head:
            if head.key == key:
                if prev:
                    prev.next = head.next
                else:
                    self.data[k] = head.next
                return
            prev = head
            head = head.next

    def hashKey(self, key: int) -> int:
        return key % self.size


if __name__ == "__main__":
    obj = MyHashMap()
    obj.put(1, 1)
    print(obj.get(1))
    obj.remove(1)
    print(obj.get(1))
