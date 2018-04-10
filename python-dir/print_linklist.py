class node:

   def __init__(self, next_node):
       self.value = next_node
       self.next = None

   def add_node(self, node_value, new_node):
       self.value = node_value
       self.next = new_node

   def iterate(self):
        while(self.next != NULL): 
            print node.value
            self.next = next.next
     

simple_list = node()
simple_list.add_node(4)
simple_list.iterate
