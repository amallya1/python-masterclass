class Node:
    def __init__(self, value):
        self.value = value
        self.lstree = None
        self.rstree = None
    
    def get_value(self):
        return self.value

class Tree:
    def __init__(self):
        self.root = None
    
    def add_node(self, value):
        if self.root is None:
            new_node = Node(value)
           # new_node.value = value
            self.root = new_node
        else:
            self.insert_child_node(self.root, value)
    

    def insert_child_node(self, curr_node, value):
        if(value <= curr_node.value):
            if(curr_node.lstree is None):
                curr_node.lstree = Node(value)
            else:
                self.insert_child_node(curr_node.lstree, value)
        elif(value > curr_node.value):
            if(curr_node.rstree is None):
                curr_node.rstree = Node(value)
            else:
                self.insert_child_node(curr_node.rstree, value)
    
    def preorder (self, curr_node):
        if curr_node:
            print (curr_node.value)
            self.preorder (curr_node.lstree)
            self.preorder (curr_node.rstree)
        

    def postorder (self, curr_node):
        if curr_node:
            self.postorder (curr_node.lstree)
            self.postorder (curr_node.rstree)
            print (curr_node.value)

                
t = Tree()

t.add_node(10)
t.add_node(3)
t.add_node(18)
t.add_node(1)
t.add_node(7)

print("PostOrder Traversals:")
t.postorder(t.root)

print("PreOrder Traversals")
t.preorder (t.root)


            
                