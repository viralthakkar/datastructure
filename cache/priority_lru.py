from collections import defaultdict

from cache.list_node import ListNode


class PriorityLRUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.used_capacity = 0
        self.mapping = {}
        self.priority_mapping = defaultdict(dict)

    def create_priority_head_tail(self, priority):
        head = ListNode(-1, -1, priority)
        tail = ListNode(-1, -1, priority)
        head.next = tail
        tail.prev = head

        self.priority_mapping[priority]['start'] = head
        self.priority_mapping[priority]['end'] = tail
        self.priority_mapping[priority]['count'] = 0

    def add(self, node, priority):
        priority_tail = self.priority_mapping[priority]['end']

        tail_of_left = priority_tail.prev

        tail_of_left.next = node
        node.prev = tail_of_left

        node.next = priority_tail
        priority_tail.prev = node

        self.priority_mapping[priority]['count'] += 1

    def remove(self, node, priority):
        node.prev.next = node.next
        node.next.prev = node.prev

        self.priority_mapping[priority]['count'] -= 1

    def get(self, key: int):
        if key in self.mapping:
            existing_node = self.mapping[key]

            priority = existing_node.priority

            self.remove(existing_node, priority)
            self.add(existing_node, priority)

            return existing_node.value
        return -1

    def put(self, key: int, value: int, priority: int):
        if priority not in self.priority_mapping:
            self.create_priority_head_tail(priority)

        if key in self.mapping:
            existing_node = self.mapping[key]
            self.remove(existing_node, priority)

        inserting_node = ListNode(key, value, priority)

        self.mapping[key] = inserting_node
        self.add(inserting_node, priority)

        if len(self.mapping) > self.capacity:
            lowest_priority = max(self.priority_mapping.keys())

            priority_head = self.priority_mapping[lowest_priority]['start']

            node_to_delete = priority_head.next

            self.remove(node_to_delete, lowest_priority)
            self.mapping.pop(node_to_delete.key)

            if self.priority_mapping[lowest_priority]['count'] == 0:
                self.priority_mapping.pop(lowest_priority)


if __name__ == '__main__':
    lc = PriorityLRUCache(5)
    lc.put(1, 15, 1)
    lc.put(2, 20, 2)
    lc.put(3, 25, 1)
    lc.put(4, 30, 2)
    lc.put(5, 10, 3)
    print(lc.get(5))
    lc.put(6, 10, 1)
    print(lc.priority_mapping)
    print(lc.get(5))
    print(lc.get(2))
    lc.put(8, 80, 3)
    print(lc.get(6))
    print(lc.get(3))

    print("Second Test Case")

    lc = PriorityLRUCache(2)
    lc.put(1, 1, 1)
    lc.put(2, 2, 2)
    print(lc.get(1))
    lc.put(3, 3, 1)
    print(lc.get(2))
    lc.put(4, 4, 3)
    print(lc.get(1))
    print(lc.get(3))
    print(lc.get(4))
    lc.put(5,5, 2)
    print(lc.get(4))

    print("Third Test Case")

    lc = PriorityLRUCache(1)
    lc.put(2, 1, 1)
    print(lc.get(2))
    lc.put(3, 2, 2)
    print(lc.get(2))
    print(lc.get(3))
