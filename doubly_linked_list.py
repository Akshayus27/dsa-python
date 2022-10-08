class Node:
    def __init__(self, data):
        self.data = data
        self.previous = None
        self.next = None
  
class Doubly_Linked_List:
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
            node.previous = None
            self.head.previous = node
            self.head = node

    def insert_last(self, data): 
        node = Node(data)
        if not self.head:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            node.previous = self.tail
            self.tail = node

    def insert(self, data, index): 
        node = Node(data)
        current_idx = 0
        current_node = self.head

        while current_node.next != None and current_idx != index - 1:
            current_node = current_node.next
            current_idx += 1 

        if current_idx == index - 1: 
            nextNode = current_node.next

            current_node.next = node
            node.previous = current_node

            nextNode.previous = node
            node.next = nextNode
        else:
            print('Index out of range')
            return
    
    def remove_first(self): 
        if not self.head:
            print('List is empty')
            return
        else:
            self.head = self.head.next
            self.head.previous = None
    
    def remove_last(self): 
        if not self.head: 
            print('List is empty')
            return
    
        previous_node = self.tail.previous
        self.tail = previous_node
        self.tail.next = None
  
    def remove(self, index): 
        current_idx = 0
        current_node = self.head

        while current_node.next != None and current_idx != index:
            current_node = current_node.next
            current_idx += 1

        if current_idx == index:
            if current_node.next == None:
                self.tail = current_node.previous
                self.tail.previous = current_node.previous.previous
                self.tail.next = None
            else:
                current_node.previous.next = current_node.next
                current_node.next.previous = current_node.previous
        else:
            print('Index out of range')
            return

    def get_string_to_print(self, node):
        next_data = node.next.data if node.next is not None else 'None'
        previous_data = node.previous.data if node.previous is not None else 'None'

        next_string = " %s ---> %s ," % (node.data, next_data)
        previous_string = " %s <--- %s ," % (previous_data, node.data)

        return previous_string  + next_string
    
    def _print(self): 
        current_node = self.head
        idx = 0

        while current_node is not None: 
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
