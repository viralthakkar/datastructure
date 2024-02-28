import heapq
from collections import defaultdict


class Node:
    def __init__(self, key, value, priority, expiry):
        self.key = key
        self.value = value
        self.priority = priority
        self.expiry = expiry


class PECache:
    def __init__(self, max_capacity):
        self.max_capacity = max_capacity
        self.mapping = {}
        self.expiry_hp = []
        self.priority_mapping = defaultdict(list)

    def set(self, key, value, priority, expiry):
        if len(self.mapping) >= self.max_capacity:
            self.evict(expiry)

        heapq.heappush(self.expiry_hp, (expiry, key))
        self.priority_mapping[priority].append(key)
        inserting_node = Node(key, value, priority, expiry)
        self.mapping[key] = inserting_node

    def get(self, key):
        if key in self.mapping:
            inserting_node = self.mapping[key]
            return inserting_node.value
        return None

    def evict(self, barrier):
        if not self.mapping:
            return

        expiry, key_target = self.expiry_hp[0]
        if expiry <= barrier:
            heapq.heappop(self.expiry_hp)
        else:
            if self.priority_mapping:
                key_target = self.priority_mapping[min(self.priority_mapping)][0]

        inserting_node = self.mapping.pop(key_target)
        self.priority_mapping[inserting_node.priority].remove(key_target)
        if not self.priority_mapping[inserting_node.priority]:
            del self.priority_mapping[inserting_node.priority]


if __name__ == '__main__':
    cache = PECache(max_capacity=3)  # Set max capacity to 3
    cache.set('a', 1, priority=1, expiry=3)
    cache.set('b', 2, priority=2, expiry=12)
    cache.set('c', 3, priority=1, expiry=8)
    cache.set('d', 4, priority=3, expiry=20)  # Cache is full, 'a' will be evicted
    print(cache.get('a'))  # Output: None (evicted)
    print(cache.get('b'))  # Output: 2
    print(cache.get('c'))  # Output: 3
    print(cache.get('d'))  # Output: 4