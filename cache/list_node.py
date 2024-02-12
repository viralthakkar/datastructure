class ListNode:
    def __init__(self, key, value, priority, expiration=None):
        self.key = key
        self.value = value
        self.priority = priority
        self.expiration = expiration
        self.next = None
        self.prev = None