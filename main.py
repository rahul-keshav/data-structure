from random import randint

class Node(object):
    def __init__(self,value=None):
        self.value=value
        self.left_child=None
        self.right_child=None
        self.parent=None
        self.height=1

class AVL_tree(object):
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
                # self._inspect_insertion(cur_node.left_child)
            else:
                self._insert(value,cur_node.left_child)
        elif value>cur_node.value:
            if cur_node.right_child==None:
                cur_node.right_child=Node(value)
                cur_node.right_child.parent=cur_node
                # self._inspect_insertion(cur_node.right_child)
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
            print ('%s,h=%s'%(str(cur_node.value),str(cur_node.height)))
            self._print_tree(cur_node.right_child)

    def height(self):
        cur_height=-1
        if self.root==None:
            return('tree has no any height')
        else:
            cur_height=0
            self._height(self.root,cur_height)

    def _height(self,cur_node,cur_height):

        if cur_node==None: return cur_height

        left_height=self._height(cur_node.left_child,cur_height+1)

        right_height=self._height(cur_node.right_child,cur_height+1)

        return (max(left_height,right_height))

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

            return

        if node_parent!=None:
            node_parent.height=1+max( self.get_height(node_parent.left_child),self.get_height(node_parent.right_child) )
            self._inspect_deletion(node_parent)

    def _inspect_insertion(self,cur_node,path=[]):
        if cur_node.parent==None:
            return
        path=[cur_node]+path
        left_height=self.get_height(cur_node.parent.left_child)
        right_height=self.get_height(cur_node.parent.right_child)
        if abs(left_height-right_height)>1:
            path=[cur_node.parent]+path
            self._rebalance_node(path[0],path[1],path[2])
            return
        new_hight=1+cur_node.height
        if new_hight>cur_node.parent.height:
            cur_node.parent.height=new_hight
        self._inspect_insertion(cur_node.parent,path)

    def _inspect_deletion(self,cur_node):
        if cur_node==None:
            return
        left_height=self.get_height(cur_node.left_child)
        right_height=self.get_height(cur_node.right_child)
        if abs(left_height-right_hight)>1:
            y=self.taller_child(cur_node)
            x=self.taller_child(y)
            self._rebalance_node(cur_node,y,x)
        self._inspect_deletion(cur_node.parent)

    def _rebalance_node(self,z,y,x):
        if y==z.left_child and x==y.left_child:
            self._right_rotate(z)
        elif y==z.left_child and x==y.right_child:
            self._left_rotate(y)
            self._right_rotate(z)
        elif y==z.right_child and x==y.right_child:
            self._left_rotate(z)
        elif y==z.right_child and x==y.left_child:
            self._right_rotate(y)
            self._left_rotate(z)
        else:
            raise Exception('z,y,x node not configured')
    def _right_rotate(self,z):
        sub_root=z.parent
        y=z.left_child
        t3=y.right_child
        y.right_child=z
        z.parent=y
        z.left_child=t3
        if t3!=None: t3.parent=z
        y.parent=sub_root
        if y.parent==None:
            self.root=y
        else:
            if y.parent.left_child==z:
                y.parent.left_child=y
            else:
                y.parent.right_child=y
        z.height=1+max(self.get_height(z.left_child),self.get_height(z.right_child))
        y.height=1+max(self.get_height(y.left_child),self.get_height(y.right_child))


    def _left_rotate(self,z):
        sub_root=z.parent
        y=z.right_child
        t2=y.left_child
        y.left_child=z
        z.parent=y
        z.right_child=t2
        if t2!=None: t2.parent=z
        y.parent=sub_root
        if y.parent==None:
            self.root=y
        else:
            if y.parent.left_child==z:
                y.parent.left_child=y
            else:
                y.parent.right_child=y
        z.height=1+max(self.get_height(z.left_child),self.get_height(z.right_child))
        y.height=1+max(self.get_height(y.left_child),self.get_height(y.right_child))

    def get_height(self,cur_node):
        if cur_node==None: return 0
        return cur_node.height

    def taller_child(self,cur_node):
        left=self.get_height(cur_node.left_child)
        right=self.get_height(cur_node.right_child)
        return cur_node.left_child if left>=right else cur_node.right_child




def fill_tree(tree,num_elem=100,max_int=1000):
    for _ in range(0,num_elem):
        integer=randint(0,max_int)
        tree.insert(integer)
    return tree


tree=AVL_tree()
tree=fill_tree(tree)
tree.print_tree()
