class Deque:
    def __init__(self, size):
        self.deque = []
        self.size = size
        self.current_size = 0

    def is_empty(self):
        return self.current_size == 0

    def is_full(self):
        return self.current_size == self.size

    def insert_first(self, item):
        if self.is_full():
            print('Deque is full')
            return

        self.deque.insert(0, item)
        self.current_size += 1

    def insert_last(self, item):
        if self.is_full():
            print('Deque is full')
            return

        self.deque.append(item)
        self.current_size += 1

    def remove_first(self):
        if self.is_empty():
            print('Deque is Empty')
            return

        self.deque.pop(0)
        self.current_size -= 1

    def remove_last(self):
        if self.is_empty():
            print('Deque is Empty')
            return

        self.deque.pop()
        self.current_size -= 1

    def _print(self):
        if self.is_empty():
            print('Deque is empty')
            return
    
        print(self.deque)
