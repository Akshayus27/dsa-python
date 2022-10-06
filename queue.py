class Queue:
    def __init__(self, size):
        self.queue = []
        self.size = size
        self.front = -1
        self.rear = -1

    def is_empty(self):
        return self.front == self.rear

    def is_full(self):
        return self.front == (self.rear + 1) % self.size

    def enqueue(self, item):
        if self.is_full():
            print('Queue is full')
            return
        
        if (self.front == -1):
            self.front += 1

        self.rear = (self.rear + 1) % self.size
        self.queue.insert(self.rear, item)

        return item

    def dequeue(self):
        if self.is_empty():
            print('Queue is Empty')
            return

        self.front = (self.front + 1) % self.size

        return self.queue[self.front - 1]

    def peek(self):
        if self.is_empty():
            print('Queue is empty to peek')
            return

        return self.queue[self.front]
    
    def _print(self):
        if self.is_empty():
            print('Queue is empty')
            return
        
        current_queue = []
        for idx in range(self.front, self.size, 1):
            current_queue.append(self.queue[idx])
        
        for idx in range(self.rear, self.front, 1):
            current_queue.append(self.queue[idx])

        print(current_queue)