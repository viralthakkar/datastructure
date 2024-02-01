class Queue:
    def __init__(self, capacity=5, resize_allowed=False):
        self.capacity = capacity
        self.queue = []
        self.front = None
        self.rear = None
        self.size = 0
        self.resize_allowed = resize_allowed

    def enqueue(self, value):
        if self.capacity <= self.size:
            if self.resize_allowed:
                self.resize()
            else:
                print(f"Queue is Full. {self.capacity}, {self.size}")

        if not self.queue:
            self.front = 0
            self.rear = 0
        else:
            self.rear += 1
        self.queue.append(value)
        self.size += 1

    def dequeue(self):
        if self.rear is not None:
            self.queue.pop(0)
            self.size -= 1
            if self.size > 0:
                self.rear -= 1
            else:
                self.rear = None
                self.front = None
        else:
            print("Queue is Empty")

    def front_and_dequeue(self):
        self.get_front_ele()
        self.dequeue()

    def is_queue_empty(self):
        if self.size == 0:
            return True
        return False

    def is_queue_full(self):
        if self.size >= self.capacity:
            return True
        return False

    def queue_size(self):
        print(f"Queue Size {self.size}")

    def get_front_ele(self):
        if self.front is not None:
            print(f"Front Element is: {self.queue[self.front]}")
        else:
            print("Queue is Empty")

    def get_rear_ele(self):
        if self.rear is not None:
            print(f"Rear Element is: {self.queue[self.rear]}")
        else:
            print("Queue is Empty")

    def is_empty(self):
        return self.size <= 0

    def resize(self):
        self.capacity = 2 * self.capacity


if __name__ == '__main__':
    q = Queue(capacity=3, resize_allowed=True)
    print(q.queue)
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    q.enqueue(4)
    q.enqueue(5)
    q.get_front_ele()
    q.front_and_dequeue()
    q.get_front_ele()
    q.dequeue()
    q.dequeue()
    q.get_front_ele()
    q.get_rear_ele()
    q.dequeue()
    q.dequeue()
    q.dequeue()
    q.get_front_ele()
    print(q.queue)
    q.dequeue()
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    q.enqueue(4)
    q.enqueue(5)
    q.enqueue(6)
    q.dequeue()
    q.enqueue(6)
    q.get_front_ele()
    q.get_rear_ele()
    q.enqueue(7)
    q.get_front_ele()
    q.get_rear_ele()
    q.enqueue(9)
    q.get_front_ele()
    q.get_rear_ele()
    q.queue_size()
    q.enqueue(10)
    q.queue_size()
