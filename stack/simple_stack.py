class SimpleStack(object):
    def __init__(self, limit: int = 10):
        self.limit = limit
        self.stack = []

    def is_empty(self) -> int:
        return len(self.stack) <= 0

    def push(self, item: str):
        if len(self.stack) >= self.limit:
            print("Stack Overflow")
        else:
            self.stack.append(item)

    def pop(self):
        if self.is_empty():
            print("Stack Underflow")
        else:
            self.stack.pop()

    def top_and_pop(self):
        self.peek()
        self.pop()

    def peek(self):
        if self.is_empty():
            print("Stack Underflow")
        else:
            print(f"Element is : {self.stack[-1]}")

    def size(self) -> str:
        return f"Size is {len(self.stack)}"


if __name__ == '__main__':
    my_stack = SimpleStack(5)
    my_stack.push("1")
    my_stack.push("21")
    my_stack.push("14")
    my_stack.push("31")
    my_stack.push("19")
    my_stack.push("3")
    my_stack.push("99")
    my_stack.push("9")
    my_stack.peek()
    my_stack.pop()
    my_stack.pop()
    my_stack.peek()
    my_stack.pop()
    my_stack.peek()
    my_stack.pop()
    my_stack.peek()
    my_stack.pop()
    my_stack.pop()
    my_stack.push("99")
    print(my_stack.size())
    my_stack.peek()
    my_stack.top_and_pop()
