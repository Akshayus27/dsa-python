from operator import le


class Node:
    def __init__(self, data):
        self.data = data
        self.previous = None
        self.next = None
  
class Circular_Linked_List:
    def __init__(self): 
        self.head = None
        self.tail = None

    def _set_cycle(self):
        self.head.previous = self.tail
        self.tail.next = self.head

    def insert_first(self, data): 
        node = Node(data)
        if not self.head:
            self.head = node
            self.tail = node
            self._set_cycle()
        else:
            node.next = self.head
            self.head.previous = node
            self.head = node
            self._set_cycle()

    def insert_last(self, data): 
        node = Node(data)
        if not self.head:
            self.head = node
            self.tail = node
            self._set_cycle()
        else:
            self.tail.next = node
            node.previous = self.tail
            self.tail = node
            self._set_cycle()

    def insert(self, data, index): 
        node = Node(data)
        current_idx = 0
        current_node = self.head

        while current_node.next != self.head.previous and current_idx != index - 1:
            current_node = current_node.next
            current_idx += 1 

        if current_idx == index - 1: 
            mid_node = current_node.next

            current_node.next = node
            node.previous = current_node

            mid_node.previous = node
            node.next = mid_node
        else:
            print('Index out of range')
            return
    
    def remove_first(self): 
        if not self.head:
            print('List is empty')
            return
        else:
            self.head = self.head.next
            self._set_cycle()
    
    def remove_last(self): 
        if not self.head: 
            print('List is empty')
            return
    
        previous_node = self.tail.previous
        self.tail = previous_node
        self._set_cycle()
  
    def remove(self, index): 
        current_idx = 0
        current_node = self.head

        while current_node.next != self.head.previous and current_idx != index:
            current_node = current_node.next
            current_idx += 1

        if current_idx == index:
            if current_node.next == self.head.previous:
                self.tail = current_node.previous
                self.tail.previous = current_node.previous.previous
                self._set_cycle()
            else:
                current_node.previous.next = current_node.next
                current_node.next.previous = current_node.previous
        else:
            print('Index out of range')
            return

    def get_string_to_print(self, node):
        next_data = node.next.data 
        previous_data = node.previous.data

        next_string = " %s ---> %s ," % (node.data, next_data)
        previous_string = " %s <--- %s ," % (previous_data, node.data)

        return previous_string  + next_string
    

    def _get_length(self, node):
        _length = 1
        current_node = node

        while current_node.next != self.head and _length != 0:
            current_node = current_node.next
            _length += 1

        return _length

    def _print_log(self, current_node, _length):
        print("[")
        while _length > 0:
            # " %s ---> %s ,"
            # " %s <--- %s ,"
            print(self.get_string_to_print(current_node))
            current_node = current_node.next
            _length -= 1
        print("]")


    def _print(self): 
        current_node = self.head
        _length = self._get_length(current_node)
        self._print_log(current_node, _length)
