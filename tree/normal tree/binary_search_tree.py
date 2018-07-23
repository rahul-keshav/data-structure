from random import randint

class Node(object):
    def __init__(self,value=None):
        self.value=value
        self.left_child=None
        self.right_child=None
        self.parent=None

class Binary_search_tree(object):
    def __init__(self):
        self.root=None

    def __repr__(self):
        if self.root==None:
            return ''
        content='\n' # to hold final string
        cur_nodes=[self.root] # all nodes at current level
        cur_height=self.root.height # height of nodes at current level
        sep=' '*(2**(cur_height-1)) # variable sized separator between elements
        while True:
            cur_height+=-1 # decrement current height
            if len(cur_nodes)==0: break
            cur_row=' '
            next_row=''
            next_nodes=[]

            if all(n is None for n in cur_nodes):
                break

            for n in cur_nodes:

                if n==None:
                    cur_row+='   '+sep
                    next_row+='   '+sep
                    next_nodes.extend([None,None])
                    continue

                if n.value!=None:
                    buf=' '*int((5-len(str(n.value)))/2)
                    cur_row+='%s%s%s'%(buf,str(n.value),buf)+sep
                else:
                    cur_row+=' '*5+sep

                if n.left_child!=None:
                    next_nodes.append(n.left_child)
                    next_row+=' /'+sep
                else:
                    next_row+='  '+sep
                    next_nodes.append(None)

                if n.right_child!=None:
                    next_nodes.append(n.right_child)
                    next_row+='\ '+sep
                else:
                    next_row+='  '+sep
                    next_nodes.append(None)

            content+=(cur_height*'   '+cur_row+'\n'+cur_height*'   '+next_row+'\n')
            cur_nodes=next_nodes
            sep=' '*int(len(sep)/2) # cut separator size in half
        return content

    def insert(self,value):
        if self.root==None:
            self.root=Node(value)
        else:
            self._insert(value,self.root)

    def _insert(self,value,cur_node):
        if value<cur_node.value:
            if cur_node.left_child==None:
                cur_node.left_child=Node(value)
                cur_node.left_child.parent=cur_node
            else:
                self._insert(value,cur_node.left_child)
        elif value>cur_node.value:
            if cur_node.right_child==None:
                cur_node.right_child=Node(value)
                cur_node.right_child.parent=cur_node
            else:
                self._insert(value,cur_node.right_child)
        else:
            print ('value already exist')

    def print_tree(self):
        if self.root!=None:
            self._print_tree(self.root)

    def _print_tree(self,cur_node):
        if cur_node!=None:
            self._print_tree(cur_node.left_child)
            print (str(cur_node.value))
            self._print_tree(cur_node.right_child)

    def hight(self):
        cur_hight=-1
        if self.root==None:
            return('tree has no any hight')
        else:
            cur_hight=0
            self._hight(self.root,cur_hight)

    def _hight(self,cur_node,cur_hight):

        if cur_node==None: return cur_hight

        left_hight=self._hight(cur_node.left_child,cur_hight+1)

        right_hight=self._hight(cur_node.right_child,cur_hight+1)

        return (max(left_hight,right_hight))

    def search(self,value):
        if self.root!=None:
            found=self._search(self.root,value)
            if found:
                print('element is present')
            else:
                print('element not found')
        else:
            print('tree has no any element')

    def _search(self,node,value,found=False):
        if node!=None:
            if node.value==value:
                found=True
                return found
            elif self._search(node.left_child,value,found):
                found=True
                return found
            elif self._search(node.right_child,value,found):
                found=True
                return found
            else:
                return found

    def find(self,value):
        if self.root!=None:
            return self._find(value,self.root)
        else:
            return None

    def _find(self,value,cur_node):

        if value==cur_node.value:
            return cur_node
        elif value<cur_node.value and cur_node.left_child!=None:
            return self._find(value,cur_node.left_child)
        elif value>cur_node.value and cur_node.right_child!=None:
            return self._find(value,cur_node.right_child)

    def del_value(self,value):
        return self.del_node(self.find(value))

    def del_node(self,node):

        def min_value_node(n):
            current=n
            while current.left_child!=None:
                current=current.left_child
                return current
        def num_children(n):
            num_children=0
            if n.left_child!=None:
                num_children+=1
            if n.right_child!=None:
                num_children+=1
            return num_children

        node_parent=node.parent
        node_children=num_children(node)

        # case 1(node has no children)

        if node_children==0:
            if node_parent.left_child==node:
                node_parent.left_child=None
            else:
                node_parent.right_child=None

        # case 2 (node has one children)

        elif node_children==1:

            if node.left_child!=None:
                child=node.left_child
            else:
                child=node.right_child

            if node_parent.left_child==node:
                node_parent.left_child=child
            else:
                node_parent.right_child=child

            child.parent=node_parent
        elif node_children==2:

            successor=min_value_node(node.right_child)

            node.value=successor.value

            self.del_node(successor)



def fill_tree(tree,num_elem=100,max_int=1000):
    for _ in range(0,num_elem):
        integer=randint(0,max_int)
        tree.insert(integer)
    return tree


tree=Binary_search_tree()
tree=fill_tree(tree)
tree.print_tree()
