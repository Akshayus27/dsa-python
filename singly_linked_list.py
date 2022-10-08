class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Singly_Linked_List:
    def __init__(self):
        self.head = None
        self.tail = None
  
    def insert_first(self, data):
        node = Node(data)
        if not self.head:
            self.head = node
            self.tail = node
        else:
            node.next = self.head
            self.head = node

    def insert_last(self, data):
        node = Node(data)
        if not self.head:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            self.tail = node
    
    def insert(self, data, index):
        node = Node(data)
        current_idx = 0
        current_node = self.head

        while current_node.next is not None and current_idx != index - 1:
            current_node = current_node.next
            current_idx += 1
    
        if current_idx == index - 1:
            node.next = current_node.next
            current_node.next = node
        else:
            print('Index out of range')
            return
    
    def remove_first(self):
        if not self.head:
            print('List is empty')
            return
        else:
            self.head = self.head.next
    
    def remove_last(self):
        if not self.head:
            print('List is empty')
            return
        else:
            current_node = self.head
            previous_node = self.head

        while current_node.next is not None:
            previous_node = current_node
            current_node = current_node.next
      
        self.tail = previous_node
        self.tail.next = None
    
    def remove(self, index):
        current_idx = 0
        current_node = self.head

        while current_node.next != None and current_idx != index - 1:
            current_node = current_node.next
            current_idx += 1

        if current_idx == index - 1:
            current_node.next = current_node.next.next
        else:
            print('Index out of range')
            return
    
    def search(self, data):
        current_node = self.head
        current_idx = 0

        while current_node.next != None:
            if current_node.data == data:
                return current_idx
      
            current_idx += 1
            current_node = current_node.next
        
        return -1
  
    def get_string_to_print(self, node):
        next_data = node.next.data if node.next is not None else 'None'
        string = " %s ---> %s ," % (node.data, next_data)
        return string

    def _print(self):
        current_node = self.head
        idx = 0

        while current_node != None:
            if idx == 0:
                print("[")
                print(self.get_string_to_print(current_node))
            elif current_node.next == None:
                print(self.get_string_to_print(current_node))
                print("]")
            else:
                print(self.get_string_to_print(current_node))
      
            current_node = current_node.next
            idx += 1
    
  

