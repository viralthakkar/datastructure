from cache.list_node import ListNode


class LRUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.used_capacity = 0
        self.mapping = {}
        self.head = ListNode(-1, -1)
        self.tail = ListNode(-1, -1)
        self.head.next = self.tail
        self.tail.prev = self.head

    def add(self, node):
        tail_of_left = self.tail.prev

        tail_of_left.next = node
        node.prev = tail_of_left

        node.next = self.tail
        self.tail.prev = node

    def remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

    def get(self, key: int):
        if key in self.mapping:
            existing_node = self.mapping[key]

            self.remove(existing_node)
            self.add(existing_node)

            return existing_node.value
        return -1

    def put(self, key: int, value: int):
        if key in self.mapping:
            existing_node = self.mapping[key]
            self.remove(existing_node)

        inserting_node = ListNode(key, value)
        self.mapping[key] = inserting_node
        self.add(inserting_node)

        if len(self.mapping) > self.capacity:
            node_to_delete = self.head.next
            self.remove(node_to_delete)
            self.mapping.pop(node_to_delete.key)


if __name__ == '__main__':
    lc = LRUCache(5)
    lc.put(1, 15)
    lc.put(2, 20)
    lc.put(3, 25)
    lc.put(4, 30)
    lc.put(5, 10)
    print(lc.get(5))
    lc.put(6, 10)
    print(lc.get(2))
    print(lc.get(6))
    print(lc.get(2))

    print("Second Test Case")

    lc = LRUCache(2)
    lc.put(1, 1)
    lc.put(2, 2)
    print(lc.get(1))
    lc.put(3, 3)
    print(lc.get(2))
    lc.put(4, 4)
    print(lc.get(1))
    print(lc.get(3))
    print(lc.get(4))
    lc.put(4, 45)
    print(lc.get(4))

    print("Third Test Case")

    lc = LRUCache(1)
    lc.put(2, 1)
    print(lc.get(2))
    lc.put(3, 2)
    print(lc.get(2))
    print(lc.get(3))
