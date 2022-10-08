from stack import Stack
from queue import Queue
from deque import Deque

from singly_linked_list import Singly_Linked_List
from doubly_linked_list import Doubly_Linked_List
from circular_linked_list import Circular_Linked_List

from hash_table import Hash_Table

def _create_hash_table_mock(hash_t, arr):
    for idx in range(0, len(arr)):
        hash_t.insert(arr[idx])

if __name__ == '__main__':
    hash_t = Hash_Table(5)
    arr1 = [1, 2, 3, 4, 5]
    arr2 = [6, 7, 8, 9, 10]
    arr3 = [11, 12, 13, 14, 15]

    _create_hash_table_mock(hash_t, arr1)
    _create_hash_table_mock(hash_t, arr2)
    _create_hash_table_mock(hash_t, arr3)

    hash_t._print()