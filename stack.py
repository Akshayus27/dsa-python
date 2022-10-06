class Stack:
    def __init__(self, size):
        self.stack = []
        self.capacity = size
        self.head = -1

    def is_empty(self):
        return self.head == -1

    def is_full(self):
        return self.head == self.capacity - 1

    def push(self, item):
        if self.is_full():
            print('Stack is full');
            return
        
        self.head += 1
        self.stack.insert(self.head, item)

        return item

    def pop(self):
        if self.is_empty():
            print('Stack is empty')
            return

        self.head -= 1

        return self.stack[self.head + 1]

    def peek(self):
        if self.is_empty():
            print('Stack is empty to peek')
            return

        return self.stack[self.head]

    def _print(self):
        if self.is_empty():
            print('Stack is empty')
            return
        
        current_stack = []
        for idx in range(self.head, -1, -1):
            current_stack.append(self.stack[idx])

        print(current_stack)