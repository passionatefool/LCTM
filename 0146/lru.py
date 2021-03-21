class ListNode:
    def __init__(self, key=0, val=0, prev=None, next=None):
        self.key = key
        self.val = val
        self.prev = prev
        self.next = next


class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.m = {}
        self.head = ListNode()
        self.tail = ListNode()
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key: int) -> int:
        n = self.m.get(key)
        if n is not None:
            n.prev.next = n.next
            n.next.prev = n.prev

            n.next = self.head.next
            n.prev = self.head

            self.head.next.prev = n
            self.head.next = n
            return n.val
        return -1

    def put(self, key: int, value: int) -> None:
        n = self.m.get(key)
        if n is not None:
            self.m[key].val = value
            return

        n = ListNode(key, value, self.head, self.head.next)
        self.head.next.prev = n
        self.head.next = n
        self.m[key] = n

        if len(self.m) > self.capacity:
            del self.m[self.tail.prev.key]
            self.tail.prev = self.tail.prev.prev
            self.tail.prev.next = self.tail


if __name__ == "__main__":
    l = LRUCache(3)
    l.put(1, 1)
    l.put(2, 2)
    l.put(3, 3)
    print(l.get(1), l.get(2), l.get(3))
