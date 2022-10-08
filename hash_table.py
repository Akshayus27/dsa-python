from doubly_linked_list import Doubly_Linked_List

class Hash_Table:
    def __init__(self, size): 
        self.size = size
        self.buckets =  [None] * size
  
    def _hash_key(self, key):
        return key % self.size
  
    def _assign_table(self, hash_key):
        table = Doubly_Linked_List()
        self.buckets[hash_key] = table

    def insert(self, item):
        hash_key = self._hash_key(item)

        if self.buckets[hash_key] is None:
            self._assign_table(hash_key)
            self.buckets[hash_key].insert_last(item)
        else:
            self.buckets[hash_key].insert_last(item)
    
    def _print(self):
        for idx in range(0, self.size): 
            if (self.buckets[idx]):
                print(" key: %s " % (idx + 1))
                # print("""
                #          |
                #          |
                #          |
                #          """)
                print(" table:  ")
                self.buckets[idx]._print()
      

