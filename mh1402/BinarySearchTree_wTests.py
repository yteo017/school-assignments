
class TreeNode:
    def __init__(self, initKey, initParent = None, initLeftChild = None, initRightChild = None):
        self.key = initKey
        self.parent = initParent
        self.leftChild = initLeftChild
        self.rightChild = initRightChild

    def search(self,k):
        """given a key value, search through the tree
        returns the node with such a 'key' value
        return None if not found"""
        
        if (self.key == k):                                                     #if the node has key value k
            return self                                                         #return the node
        
        elif self.key > k:                                                      #else if the key value k is less than the key value of the node
            if self.leftChild:                                                  #checking for existence of a leftChild
                return self.leftChild.search(k)                                 #do a recursive search of the subtree of the leftChild
            else:                                                               #if there is no leftChild
                return None                                                     #return None because the key value is not found
            
        else:                                                                   #else if the key value k is more than the key value of the node
            if self.rightChild:                                                 #checking for existence of a rightChild
                return self.rightChild.search(k)                                #do a recursive search of the subtree of the rightChild
            else:                                                               #if there is no rightChild
                return None                                                     #return None because the key value is not found
        
    def insert(self, k):
        """create a new node with 'key' value and insert it to teh tree
        first, search for the location where it should be inserted to"""
        
        if self.key == k:                                                       #if the node has key value k
            return None                                                         #it cannot be inserted as it is already present in the tree
        
        elif self.key > k:                                                      #else if the key value k is less than the key value of the node
            if self.leftChild:                                                  #checking for existence of a leftChild
                return self.leftChild.insert(k)                                 #insert a new node with the key value into the left subtree
            else:                                                               #if there is no leftChild
                self.leftChild = TreeNode(k)                                    #create a new subtree at the leftChild
                return True
        
        else:                                                                   #else if the key value k is more than the key value of the node
            if self.rightChild:                                                 #checking for existence of a rightChild
                return self.rightChild.insert(k)                                #insert a new node with the key value into the right subtree
            else:                                                               #if there is no rightChild
                self.rightChild = TreeNode(k)                                   #create a new subtree at the rightChild
                return True
    
    def minValueNode(self, parent):
        """finds the node with the minimum value"""
        
        if self.leftChild:                                                      #checking for existence of a leftChild
            return self.leftChild.minValueNode(self)                            #perform a recursive function
        else:                                                                   #if there is no leftChild
            return [parent, self]                                               #return a list with entries of the parent of the node and the node itself
            
        
    def delete(self, k):
        """delete the node with 'key' value
        no deletion if no such node is found"""
            
        if self.key == k:                                                       #if the node has key value k
                                                                                #it is the node we want to delete
            if self.rightChild is None and self.leftChild is None:              #if it has no children
                self = None                                                     #then just delete the node by setting it to None
            
            elif self.rightChild and self.leftChild is None:                    #if it has one child, the rightChild
                self = self.rightChild                                          #shift the rightChild and its subtree up one level
            
            elif self.rightChild is None and self.leftChild:                    #if it has one child, the leftChild
                self = self.leftChild                                           #shift the leftChild and its subtree up one level
            
            elif self.rightChild and self.leftChild:                            #if it has two children
                [parent, child] = self.rightChild.minValueNode(self)            #use the minValueNode function to find the leftmost node in the right subtree
                
                if parent.leftChild == child:                                   #if the node is the leftChild of its parent
                    parent.leftChild = child.rightChild                         #the node's rightChild becomes its parent's leftChild
                else:                                                           #if the node is the rightChild of its parent
                    parent.rightChild = child.rightChild                        #the node's rightChild is promoted to its parent's rightChild
                
                child.leftChild = self.leftChild                                #reset the children
                child.rightChild = self.rightChild
                
                return child

        else:                                                                   #if the node does not have key value k
            if self.key > k:                                                    #if k is less than the key value of the node, check the left subtree
                if self.leftChild:                                              #checking for existence of leftChild
                    self.leftChild = self.leftChild.delete(k)                   #use the recursive delete function to delete the node
                                                                                #else the key is not in the tree
            else:                                                               #if k is more than the key value of the node, check the right subtree
                if self.rightChild:                                             #checking for existence of rightChild
                    self.rightChild = self.rightChild.delete(k)                 #use the recursive delete function to delete the node
                    
        return self

        
class BinarySearchTree:
    def __init__(self, initRoot = None):
        if initRoot != None:
            self.root = TreeNode(initRoot)

    def search(self, k):
        """given a key value, search through the tree
        returns the node with such a 'key' value
        return None if not found"""
        
        if self.root:                                                           #check that the tree is not empty
            return self.root.search(k)                                          #call the search function of the TreeNode class
        else:                                                                   #if there is no self.root, then the tree is empty
            return None                                                         #then just return None because the key value cannot be found in an empty tree

    def insert(self, k):
        """create a new node with 'key' value and insert it to teh tree
        first, search for the location where it should be inserted to"""
        
        if self.root:                                                           #check that the tree is not empty
            return self.root.insert(k)                                          #call the insert function of the TreeNode class
        else:                                                                   #if there is no self.root the tree is empty
            self.root = TreeNode(k)                                             #create a new tree
            return True
    
    def delete(self, k):
        """delete the node with 'key' value
        no deletion if no such node is found"""
        
        if self.root:                                                           #if there is a self root
            self.root = self.root.delete(k)                                     #perform the recursive delete function on it                           
            
    def searchByRange(self, minimum, maximum):
        """return the list of nodes with key value in between [minimum,maximum]
        first, locate the node with the smallest possible key value such that
        key value >= minimum, then look for all elements by an in-order traversal
        until the key value of nodes are larger than minimum"""
        
        if self.root is None:                                                   #if there is no self root
            return None                                                         #return None
        else:                                                                   #else if there is a self root
            return self.searchRange(self.root, minimum, maximum)                #call another function to find the range query
    
    def searchRange(self, subtree, minimum, maximum, nodes = None):
        """aids the searchByRange function"""
        
        if subtree is None:
            return None
        if nodes is None:
            nodes = []                                                          #create an empty list to input the nodes whose keys are within the range
                                      
        if subtree.key > minimum:                                               #if the key of the subtree is more than the minimum
            self.searchRange(subtree.leftChild, minimum, maximum, nodes)        #search the leftChild of the subtree
        if minimum <= subtree.key <= maximum:                                   #if the key of the subtree is more than the minimum and less than the maximum
            nodes.append(subtree)                                               #append the subtree node to the list
        if subtree.key < maximum:                                               #if the key of the subtree is less than the maximum
            self.searchRange(subtree.rightChild, minimum, maximum, nodes)       #search the rightChild of the subtree
        
        return nodes                                                            #return the list to get the nodes
                    
                
            
# ------------- test code from here ------------------
    def printTree(self):
        x = [self.root]              
        print("--------- Tree begins here ----------")
        NonEmptyLevel = True
        while NonEmptyLevel == True:
            y = []
            NonEmptyLevel = False
            for i in range(len(x)):
                if x[i] != None:
                    print(x[i].key, end=' ')
                    NonEmptyLevel = True
                    y += [x[i].leftChild, x[i].rightChild]
                else:
                    print(' ', end=' ')
            x = y
            print()
        print("--------- Tree ends here -------------")

bst = BinarySearchTree('H')
print("Initializing the tree with 'H'")
bst.printTree()
bst.insert('B')
print("Inserting 'B'")
bst.printTree()
bst.insert('M')
print("Inserting 'M'")
bst.printTree()
bst.insert('A')
print("Inserting 'A'")
bst.printTree()
bst.insert('E')
print("Inserting 'E'")
bst.printTree()
bst.insert('C')
print("Inserting 'C'")
bst.printTree()
bst.insert('D')
print("Inserting 'D'")
bst.printTree()
bst.insert('L')
print("Inserting 'L'")
bst.printTree()
bst.insert('N')
print("Inserting 'N'")
bst.printTree()
found = bst.searchByRange('B', 'M')
print("Searching by the range (minimum = 'B', maximum='M')")
for i in range(len(found)):
    print(found[i].key, end=' ')
print()
bst.delete('B')
print("Deleting 'B'")
bst.printTree()
bst.delete('A')
print("Deleting 'A'")
bst.printTree()
bst.delete('H')
print("Deleting 'H'")
bst.printTree()
bst.delete('B')
print("Deleting 'B'")
bst.printTree()
bst.delete('L')
print("Deleting 'L'")
bst.printTree()
bst.delete('M')
print("Deleting 'M'")
bst.printTree()
bst.delete('C')
print("Deleting 'C'")
bst.printTree()
bst.delete('E')
print("Deleting 'E'")
bst.printTree()

# ------------- test output from here ------------------
'''
Initializing the tree with 'H'
--------- Tree begins here ----------
H 
    
--------- Tree ends here -------------
Inserting 'B'
--------- Tree begins here ----------
H 
B   
    
--------- Tree ends here -------------
Inserting 'M'
--------- Tree begins here ----------
H 
B M 
        
--------- Tree ends here -------------
Inserting 'A'
--------- Tree begins here ----------
H 
B M 
A       
    
--------- Tree ends here -------------
Inserting 'E'
--------- Tree begins here ----------
H 
B M 
A E     
        
--------- Tree ends here -------------
Inserting 'C'
--------- Tree begins here ----------
H 
B M 
A E     
    C   
    
--------- Tree ends here -------------
Inserting 'D'
--------- Tree begins here ----------
H 
B M 
A E     
    C   
  D 
    
--------- Tree ends here -------------
Inserting 'L'
--------- Tree begins here ----------
H 
B M 
A E L   
    C       
  D 
    
--------- Tree ends here -------------
Inserting 'N'
--------- Tree begins here ----------
H 
B M 
A E L N 
    C           
  D 
    
--------- Tree ends here -------------
Searching by the range (minimum = 'B', maximum='M')
B C D E H L M 
Deleting 'B'
--------- Tree begins here ----------
H 
C M 
A E L N 
    D           
    
--------- Tree ends here -------------
Deleting 'A'
--------- Tree begins here ----------
H 
C M 
  E L N 
D           
    
--------- Tree ends here -------------
Deleting 'H'
--------- Tree begins here ----------
L 
C M 
  E   N 
D       
    
--------- Tree ends here -------------
Deleting 'B'
--------- Tree begins here ----------
L 
C M 
  E   N 
D       
    
--------- Tree ends here -------------
Deleting 'L'
--------- Tree begins here ----------
M 
C N 
  E     
D   
    
--------- Tree ends here -------------
Deleting 'M'
--------- Tree begins here ----------
N 
C   
  E 
D   
    
--------- Tree ends here -------------
Deleting 'C'
--------- Tree begins here ----------
N 
E   
D   
    
--------- Tree ends here -------------
Deleting 'E'
--------- Tree begins here ----------
N 
D   
    
--------- Tree ends here -------------
'''
