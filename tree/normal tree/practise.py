
class Node:
    def __init__(self,value=None):
        self.value=value
        self.left_child=None
        self.right_child=None

class Binary_search_tree(object):
    def __init__(self):
        self.root=None

    def insert(self,value):
        if self.root==None:
            self.root=Node(value)
        else:
            self._insert(value,self.root)

    def _insert(value,cur_node):
        if value<cur_node.value:
            if cur_node.left_child==None:
                cur_node.left_child=Node(value)
            else:
                self._insert(value,cur_node.left_child)
        elif value>cur_node.value:
            if cur_node.right_child==None:
                cur_node.right_child=Node(value)
            else:
                
