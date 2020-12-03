class Node:
    def __init__(self, value):
        self._value = value
        self._parent = None 
        self._children = []

    @property
    def value(self):
        return self._value

    @property
    def children(self):
        return self._children
    
    @property
    def parent(self):
        return self._parent
    
    
    def add_child(self, node):
        if node not in self._children:
            self._children.append(node)
            node._parent = self

    def remove_child(self, node):
        if node in self._children:
            self._children.remove(node)
            node._parent = None

    @parent.setter
    def parent(self, node):
        self._parent = node
        node.add_child(self)
