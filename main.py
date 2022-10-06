from stack import Stack
from queue import Queue

if __name__ == '__main__':
    queue = Queue(4)
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    queue.enqueue(4)
    queue.dequeue()
    queue.enqueue(5)
    queue._print()