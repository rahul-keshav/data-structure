class Node(object):

    def __init__(self,data,parentNode):
        self.data=data
        self.parentNode=parentNode
        self.left_child=None
        self.right_child=None
        self.balance=0

    def insert(self,data,parentNode):

        if data<self.data:
            if self.left_child==None:
                self.left_child=Node(data,self)
            else:
                self.insert(data,self.left_child)
        elif data>self.data:
            if self.right_child==None:
                self.right_child=Node(data,self)
            else:
                self.insert(data,self.right_child)
                
