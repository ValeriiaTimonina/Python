from numpy import array
 
 
class Node:
    def __init__(self, value):
        self.value = value
        self.right = None
        self.left = None
 
 
class BinarySearchTree:
    def __init__(self):
        self.root = None
        self.count = 0
 
    def insert(self, value):
        if (self.root == None):
            self.root = Node(value)
            return
        temp = self.root
        while (True):
            if value < temp.value:
                if temp.left == None:
                    temp.left = Node(value)
                    return
                else:
                    temp = temp.left
            else:
                if temp.right == None:
                    temp.right = Node(value)
                    return
                else:
                    temp = temp.right
 
 
    def fromArray(self, array):
        for i in array:
            self.insert(i)
 
 
    def search(self, value):
        self.count = 0
        if (self.root == None):
            return False
        temp = self.root
        while (True):
            self.count = self.count + 1
            if value < temp.value:
                if temp.left == None:
                    return False
                else:
                    temp = temp.left
            elif value > temp.value:
                if temp.right == None:
                    return False
                else:
                    temp = temp.right
            else:
                return True
         
 
    def min(self):
        self.count = 0
        if (self.root == None):
            return None
        value = 100000
        temp = self.root
        while (True):
            self.count = self.count + 1
            if temp.value < value:
                if temp.left == None:
                    return temp.value
                else:
                    value = temp.value
                    temp = temp.left
            else:
                return temp.value
 
    def max(self):
        self.count = 0
        if (self.root == None):
            return None
        value = -100000
        temp = self.root
        while (True):
            self.count = self.count + 1
            if temp.value > value:
                if temp.right == None:
                    return temp.value
                else:
                    value = temp.value
                    temp = temp.right
            else:
                return temp.value
 
 
    def visitedNodes(self):
        return self.count
 
 
#bst = BinarySearchTree()
#root = Node(5)
 
#bst.fromArray([16, 9368, -731, 6792, 2414, -9299, -140, -6340, -2373, 9551])
 
#print(bst.min())
#print(bst.max())
 
#print(bst.search(16))
#print(bst.search(-9299))
#print(bst.min())
#print(bst.max())
#print(bst.search(100))
#print(bst.visitedNodes())