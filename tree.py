'''
Author: Yandi Xu

File: tree.py

'''

class Tree:
    ''' This class is ued to represent the nodes in the phylogenetic tree.

        Attributes: name: the the name of the node.
                         
                    left: references to the left subtrees of the node.
                    
                    right: references to the right subtrees of the node. '''

    def __init__(self, name):
        self._name = name
        #set side of subtrees to None.
        self._left = None
        self._right = None

    def id(self):
        ''' Get the name fo node. '''
        return str(self._name)

    def left(self):
        ''' Get left subtrees of node. '''
        return self._left

    def right(self):
        ''' Get right subtess of node. '''
        return self._right

    def is_leaf(self):
        '''check whether a node is leaf or nonleaf. '''
        return self._right == None and self._left == None

    def add_leaf(self):
        ''' Add a new leaf ot the tree. '''
        if self.is_leaf():
            return {self._name}

        else:
            if self._left != None and self._right != None:
                return {self._name} | self._left.add_leaf() | self._right.add_leaf()
            if self.is_leaf():
                return {self._name}
            if self._left != None:
                return {self._name} | self._left.add_leaf()
            if self._right != None:
                return {self._name} | self._right.add_leaf()
 
                
    def __str__(self):
        if self.is_leaf():
            return self.id()
        else:
            return "({}, {})".format(str(self.left()), str(self.right()))

    
