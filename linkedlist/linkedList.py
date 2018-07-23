from .import Node
class linkedList(object):
    def __init__(self):
        self.head=None;
        self.counter=0;
    def insertStart(self,data):
        self.counter+=1;
        newNode=Node(data)
        if not self.head:
            self.head=newNode;
        else:
            newNode.nextNode=self.head
            self.head=newNode;
    def insertEnd(self,data):
        newNode=Node();
        actualNode


