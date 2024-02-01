class Node:
    def __init__(self, val):
        self.value = val
        self.next = None


class SingleLinkedList:
    def __init__(self, head=None):
        self.head = head

    def insert_at_beginning(self, value):
        new_node = Node(value)
        if not self.head:
            self.head = new_node
        else:
            temp = self.head
            new_node.next = temp
            self.head = new_node

    def delete_at_beginning(self):
        if not self.head:
            return

        if not self.head.next:
            self.head = None
            return

        temp = self.head
        self.head = temp.next
        temp = None

    def insert_at_end(self, value):
        new_node = Node(value)

        if not self.head:
            self.head = new_node

        temp = self.head
        while temp.next:
            temp = temp.next

        temp.next = new_node

    def delete_at_end(self):
        if not self.head:
            return

        if not self.head.next:
            self.head = None
            return

        temp = self.head
        prev = None
        while temp.next:
            prev = temp
            temp = temp.next

        prev.next = None
        temp = None

    def delete_at_pos(self, pos):
        if pos < 0:
            print("Pos is incorrect")
            return
        if pos == 1:
            self.delete_at_beginning()

        temp = self.head
        prev = None

        while temp.next and pos - 1 > 0:
            prev = temp
            temp = temp.next
            pos -= 1

        if temp.next is not None:
            prev.next = temp.next
        else:
            prev.next = None
        temp = None

    def insert_at_pos(self, value, pos):
        if pos < 0:
            print("Pos is incorrect")
            return
        if pos == 1:
            self.insert_at_beginning(value)

        temp = self.head
        prev = None
        while temp and pos-1 > 0:
            prev = temp
            temp = temp.next
            pos -= 1

        new_node = Node(value)
        prev.next = new_node

        if temp:
            new_node.next = temp

    def traverse(self):
        if not self.head:
            print("Linked List Empty")
        temp = self.head

        while temp:
            print(temp.value)
            temp = temp.next

    def reverse(self):
        prev = None
        curr = self.head

        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node

        self.head = prev


if __name__ == '__main__':
    s = SingleLinkedList()
    s.insert_at_beginning(1)
    s.insert_at_beginning(3)
    s.insert_at_end(4)
    s.insert_at_end(5)
    s.insert_at_pos(2, 2)
    s.insert_at_pos(6, 5)
    s.insert_at_pos(9, 10)
    # s.head.next = Node(2)
    # s.head.next.next = Node(3)
    s.traverse()
    print("Delete-1")
    s.delete_at_beginning()
    s.traverse()
    print("Delete-2")
    s.delete_at_end()
    s.traverse()
    print("Delete-3")
    s.delete_at_pos(4)
    s.traverse()
    print("Delete-4")
    s.delete_at_pos(2)
    s.traverse()
    s.insert_at_beginning(1)
    s.insert_at_pos(3, 3)
    s.insert_at_end(6)
    print("insert")
    s.traverse()
    s.delete_at_end()
    s.delete_at_pos(6)
    print("Delete-5")
    s.traverse()
    s.delete_at_beginning()
    s.delete_at_beginning()
    print("Delete-6")
    s.traverse()
    s.delete_at_pos(3)
    print("Delete-7")
    s.traverse()
    s.delete_at_beginning()
    s.delete_at_beginning()
    print("Delete-8")
    s.traverse()
    s.insert_at_beginning(11)
    s.insert_at_beginning(3)
    s.insert_at_end(4)
    s.insert_at_end(5)
    s.insert_at_pos(2, 2)
    s.insert_at_pos(6, 5)
    s.insert_at_pos(9, 10)
    print("New Insert")
    s.traverse()
    print("Reverse")
    s.reverse()
    s.traverse()
