class Node:
    def __init__(self,data=None):
        self.data=data
        self.next=None

class LinkedList:
    def __init__(self):
        self.head=Node()

    def append(self,data):
        new_Node=Node(data)
        curr=self.head
        while curr.next!=None:
            curr=curr.next
        curr.next=new_Node

    def length(self):
        len=0
        curr=self.head
        while curr.next!=None:
            curr=curr.next
            len+=1
        return len


    def get(self,index):
        if index>=self.length():
            print("error index is out of range")
            return None
        curr_index=0
        curr_node=self.head

        while True:
            curr_node=curr_node.next
            if curr_index==index:
                return(curr_node.data)
            curr_index+=1

    def display(self):
        elems=[]
        curr_node=self.head
        while curr_node.next!=None:
            curr_node=curr_node.next
            elems.append(curr_node.data)
        print(elems)

    def erase(self,index):
        if index>=self.length() or index<0:
            print("'ERROR' index is out of range")
            return None
        curr_node=self.head
        curr_index=0
        while True:
            if curr_index==index:
                curr_node.next=curr_node.next.next
                print("index"+str(index)+"Erased")
                return(None)

            curr_node=curr_node.next
            curr_index+=1
