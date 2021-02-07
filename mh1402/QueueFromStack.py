
class Stack:
    def __init__(self):
        self.slist = [None] * 1000              # preset the maximum size of the list (named slist) to be 1000
        self.rear = 0                           # the index of next empty slot in the list
        self.push_count = 0                     # total number of calls to push() function
        self.pop_count = 0                      # total number of calls to pop() function

    def push(self, e):                          # push element e to the stack, push nothing if the slist is already full
        if (self.slist)[999] != None:
            print('the list is already full')
        else:
            for i in range(1000):
                if (self.slist)[i] == None:
                    (self.slist)[i] = e
                    self.push_count += 1
                    break
            
            
    def pop(self):                              # return None if the stack is empty, otherwise return the element last pushed 
        if (self.slist)[0] == None:
            return None
        else:
            for i in range(1000):
                if (self.slist)[i] == None:
                    i = i-1
                    y = (self.slist)[i]
                    (self.slist)[i] = None
                    self.pop_count += 1
                    return y
                    break
                
        
    def size(self):                             # return the number of elements in the stack
        if (self.slist)[0] == None:
            return 0
        elif (self.slist)[999] != None:
            return 1000
        else:
            for i in range(1000):
                if (self.slist)[i] == None:
                    return i
                    break
        
        
    def isEmpty(self):                          # return True if the stack is empty; False otherwise
        if (self.slist)[0] == None:
            return True
        else:
            return False


class Queue:
    def __init__(self):
        self.E = Stack()
        self.D = Stack()
        self.en_count = 0
        self.de_count = 0

    def enqueue(self,e):                        # enqueue the element e
        self.E.push(e)
        self.en_count += 1
        
        
    def dequeue(self):                          # remove and return the first element in the queue
        if self.D.isEmpty() == True:
            while self.E.isEmpty() == False:
                self.D.push(self.E.pop())
                
            self.de_count += 1
            return self.D.pop()

        else:
            self.de_count += 1
            return self.D.pop()


    def size(self):                             # return number of elements in the queue
        return self.E.size() + self.D.size()

    def total_enqueue(self):                    # return the number of calls to enqueue() function
        return self.en_count

    def total_dequeue(self):                    # return the number of calls to dequeue() function
        return self.de_count
    
    def total_stack_push(self):                 # return the total push() function calls in both stacks
        return self.E.push_count + self.D.push_count

    def total_stack_pop(self):                  # return the total pop() function calls in both stacks
        return self.E.pop_count + self.D.pop_count


# ----- test the functionalities of the queue implementation ----
test_q = Queue()
for i in reversed(range(200)):
    test_q.enqueue(i)
    
for i in range(100):
    test_q.dequeue()

print('size(): ', test_q.size(), 'dequeue(): ', test_q.dequeue())
print('Total stack push = ', test_q.total_stack_push(), ' total enqueue count = ', test_q.total_enqueue(), ', average stack push per enqueue = ', test_q.total_stack_push()/test_q.total_enqueue(), end='\n')
print('Total stack pop = ', test_q.total_stack_pop(), ' total dequeue count = ', test_q.total_dequeue(), ', average stack pop per dequeue = ', test_q.total_stack_pop()/test_q.total_dequeue(), end='\n')

for i in range(100):
    test_q.enqueue(i)

for i in range(190):
    test_q.dequeue()

print('size(): ', test_q.size(), 'dequeue(): ', test_q.dequeue())
print('Total stack push = ', test_q.total_stack_push(), ' total enqueue count = ', test_q.total_enqueue(), ', average stack push per enqueue = ', test_q.total_stack_push()/test_q.total_enqueue(), end='\n')
print('Total stack pop = ', test_q.total_stack_pop(), ' total dequeue count = ', test_q.total_dequeue(), ', average stack pop per dequeue = ', test_q.total_stack_pop()/test_q.total_dequeue(), end='\n')

for i in range(500):
    test_q.enqueue(i)
    test_q.dequeue()

print('size(): ', test_q.size(), 'dequeue(): ', test_q.dequeue())
print('Total stack push = ', test_q.total_stack_push(), ' total enqueue count = ', test_q.total_enqueue(), ', average stack push per enqueue = ', test_q.total_stack_push()/test_q.total_enqueue(), end='\n')
print('Total stack pop = ', test_q.total_stack_pop(), ' total dequeue count = ', test_q.total_dequeue(), ', average stack pop per dequeue = ', test_q.total_stack_pop()/test_q.total_dequeue(), end='\n')

# ----- end of test -----


'''
# output expected from above
size():  100 dequeue():  99
Total stack push =  400  total enqueue count =  200 , average stack push per enqueue =  2.0
Total stack pop =  301  total dequeue count =  101 , average stack pop per dequeue =  2.98019801980198
size():  9 dequeue():  91
Total stack push =  600  total enqueue count =  300 , average stack push per enqueue =  2.0
Total stack pop =  592  total dequeue count =  292 , average stack pop per dequeue =  2.0273972602739727
size():  8 dequeue():  492
Total stack push =  1595  total enqueue count =  800 , average stack push per enqueue =  1.99375
Total stack pop =  1588  total dequeue count =  793 , average stack pop per dequeue =  2.0025220680958387
'''
