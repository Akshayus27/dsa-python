from stack import Stack
from queue import Queue
from deque import Deque

from singly_linked_list import Singly_Linked_List
from doubly_linked_list import Doubly_Linked_List
from circular_linked_list import Circular_Linked_List

if __name__ == '__main__':
    node = Circular_Linked_List()
    node.insert_last(2)
    node.insert_last(3)
    node.insert_last(5)
    node.insert_last(6)
    node.insert(3, 2)
    node.insert_first(1)
    node._print()
    node.remove_first()
    node._print()
    node.remove_last()
    node._print()