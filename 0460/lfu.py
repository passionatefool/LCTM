class ListNode:
    def __init__(self, key=0, val=0, prev=None, next=None):
        self.key = key
        self.val = val
        self.freq = 1
        self.prev = prev
        self.next = next


class LinkedList:
    def __init__(self, node: ListNode):
        self.head = ListNode()
        self.tail = ListNode()
        node.prev = self.head
        node.next = self.tail
        self.head.next = node
        self.tail.prev = node


class LFUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.minFreq = 1
        self.nm = {}
        self.fm = {}

    def get(self, key: int) -> int:
        if key in self.nm:
            node = self.nm[key]
            node.prev.next = node.next
            node.next.prev = node.prev

            ol = self.fm[node.freq]
            if self.minFreq == node.freq and ol.head.next == ol.tail:
                self.minFreq += 1

            node.freq += 1
            if node.freq in self.fm:
                l = self.fm[node.freq]
                node.prev = l.head
                node.next = l.head.next
                l.head.next.prev = node
                l.head.next = node
            else:
                self.fm[node.freq] = LinkedList(node)
            return node.val
        return -1

    def put(self, key: int, value: int) -> None:
        if self.capacity == 0:
            return
        if key in self.nm:
            self.nm[key].val = value
            self.get(key)
        else:
            node = ListNode(key, value)
            if self.capacity == len(self.nm):
                l = self.fm[self.minFreq]
                rn = l.tail.prev
                del self.nm[rn.key]
                l.tail.prev.prev.next = l.tail
                l.tail.prev = l.tail.prev.prev

            self.nm[key] = node
            self.minFreq = node.freq
            if node.freq in self.fm:
                l = self.fm[node.freq]
                node.prev = l.head
                node.next = l.head.next
                l.head.next.prev = node
                l.head.next = node
            else:
                self.fm[node.freq] = LinkedList(node)


if __name__ == "__main__":
    l = LFUCache(3)
    l.put(2, 2)
    l.put(1, 1)
    print(l.get(2))
    print(l.get(1))
    print(l.get(2))
    l.put(3, 3)
    l.put(4, 4)
    print(l.get(3))
    print(l.get(2))
    print(l.get(1))
    print(l.get(4))
