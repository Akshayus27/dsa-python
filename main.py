from stack import Stack
from queue import Queue
from deque import Deque

if __name__ == '__main__':
    queue = Deque(4)
    queue.insert_first(1)
    queue._print()
    queue.insert_first(2)
    queue._print()
    queue.insert_first(3)
    queue._print()
    queue.insert_first(4)
    queue._print()
    queue.remove_first()
    queue.insert_last(5)
    queue._print()