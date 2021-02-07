class Node:
    def __init__(self,data): #initializing
        self.data = data
        self.next = None
        self.prev = None

class LinkedList:
    def __init__(self): #initializing
        self.head = None
        self.tail = None
        self.size = 0
    
    def first(self):
        """returns the position of the first element of L
        (or null if empty)"""
        if self.head == None: #check if first(head) node is empty
            return 'null' #if yes, then return null
        else: #if it is not empty
            return self.head.data #return the data of head node
    
    def last(self):
        """returns the position of the last element of L
        (or null if empty)"""
        if self.tail == None: #check if last(tail) node is empty
            return 'null' #if yes, then return null
        else: #if it is not empty
            return self.tail.data #return the data of tail node
        
    def before(self,p):
        """returns the position of L immediately before position p
        (or null if p is the first position)"""
        
        current = self.head #test from the head node
        
        if p == current: #if the head node = p
            return 'null' #there cannot be a node before it
        
        while current != p: #else keep checking the elements until it reaches p
            current = current.next
        return current.prev.data #now current = p, so return the node before p
        
    def after(self,p):
        """returns the position of L immediately after position p
        (or null if p is the last position)"""
        
        current = self.tail #test from the tail node
        
        if p == current: #if the tail node = p
            return 'null' #there cannot be a node after it
        
        while current !=p: #else keep cheking the elements until it reaches p
            current = current.prev
        return current.next.data #now current = p, so return the node after it
    
    def isEmpty(self):
        """returns true if list L does not contain any elements"""
        if self.size == 0:
            return True
        
    def size(self):
        """returns the number of elements in list L"""
        return self.size.data
    
    def insertBefore(self,p,e):
        """insert a new element e into L before position p in L"""
        
        if p == self.head: #if p is the head node
            e.next = p #link e to p
            p.prev = e #link p to e
            self.head = e #set e to be the 'new' head node
        
        else: 
            e.prev = p.prev #link e to prev node of p
            e.next = p #link e to p
            (p.prev).next = e #link prev node of p to e
            p.prev = e #link prev node to e
        
        self.size +=1 #increase length of linked list by 1
        
    def insertAfter(self,p,e):
        """insert a new element e into L after position p in L"""
        
        if p == self.tail: #if p is the tail node
            e.prev = p #link e to p
            p.next = e #link p to e
            self.tail = e #set e to be the 'new' tail node
            
        else:
            e.next = p.next #link e to next node of p
            e.prev = p #link e to p
            (p.next).prev = e #link next node of p to e
            p.next = e #link next node to e
        
        self.size +=1 #increase length of linked list by 1
            
    def remove(self,p):
        """remove from L the element at position p"""
        
        if p == self.head: #if p is the head node
            self.head = p.next #set the next node of p to be the 'new' head node
            (p.next).prev = None #remove the node at p
            p.next = None
            
        elif p == self.tail: #if p is the tail node
            self.tail = p.prev #set the prev node of p to be the 'new' tail node
            (p.prev).next = None #remove the node at p
            p.prev = None
            
        else:
            (p.prev).next = p.next #linking out p
            (p.next).prev = p.prev
            p.prev = None #invalidating the position p
            p.next = None

        self.size -=1 #decrease length of linked list by 1
        
    def insert(self,newNode):
        
        if self.head is None: #if there is no head node
            self.head = newNode #the newNode becomes the head node 
            self.tail = newNode #the newNode becomes the tail node as well
            #the newNode is inserted into an empty list
            #hence it is both the head node and the tail node
        else: #if there is a head node
            w = self.tail #let w be a temporary variable storing the current tail node
            w.next = newNode #link w to the newNode
            newNode.prev = w #link newNode to w
            self.tail = newNode #set newNode to be the 'new' tail node
            
        self.size +=1 #increase length of linked list by 1
            
    def printAllNodes(self):
        if self.head is None: #if there is no head node
            print('List is empty') #let the user know that it the list is empty
            return
        else:
            currentNode = self.head #let currentNode be the head node
            while True:
                if currentNode is None: # if there is no head node
                    break #can break the while loop
                print(currentNode.data) #print the data of the currentNode
                currentNode = currentNode.next #go on to the next node
                #and the while loop will repeat
                #allowing all the nodes to be printed