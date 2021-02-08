import random 
import time
import math


def bubble_sort(my_list):       
    # do n passes on the list
    swapped = True
    while swapped:
       swapped = False   

	   # check neighbours and swap them if needed     
       for j in range(len(my_list)-1):
           if my_list[j] > my_list[j+1]:
               temp = my_list[j]
               my_list[j] = my_list[j+1]
               my_list[j+1] = temp     
               swapped = True


def selection_sort(my_list):  
    for i in range(len(my_list)-1): # perform n-1 passes
        
    	# find the minimum in the unsorted part of my_list 
        min_index = i
        for j in range(i+1,len(my_list)):
            if my_list[j]< my_list[min_index]:
                min_index = j
            
        # swap this min element with the first unsorted element from my_list 
        temp = my_list[i]
        my_list[i] = my_list[min_index]
        my_list[min_index] = temp 


def insertion_sort(my_list):
    i = 1                   # i is the size of the sorted list
    while i < len(my_list): # while the list is not sorted yet
    	j = i
    
    	# place the element j at the proper place in the sorted list
    	while j > 0 and my_list[j-1] > my_list[j]:
    	  # swap 
    	  temp = my_list[j]
    	  my_list[j] = my_list[j-1]
    	  my_list[j-1] = temp
    	  j = j - 1 
            
    	i = i + 1


def merge_sort(my_list):
    # if the list is empty or contains just one element, no need to sort 
    if len(my_list) <= 1: return my_list
     
    # we divide the work in two halves, and sort them recursively
    mid = int(len(my_list) / 2)
    left = merge_sort(my_list[:mid])      
    right = merge_sort(my_list[mid:])   
    
    # merge the two sorted halves, while keeping the list sorted
    my_sorted_list = []
    while left != [] or right != []: 
        if left == []: my_sorted_list.append(right.pop(0))  # left is empty
        elif right == []: my_sorted_list.append(left.pop(0)) # right is empty
        elif left[0] < right[0]: my_sorted_list.append(left.pop(0))
        else:  my_sorted_list.append(right.pop(0))
    
    return my_sorted_list



def quick_sort(my_list):
    if len(my_list) <= 1: #if there is only 1 element in the list
        return my_list    #return the list as it is already sorted
    
    left = []   #create empty lists to store elements
    right = []
    mid = []

    pivot = random.choice(my_list)      #choose a random element in my_list to be the pivot
    for i in range(len(my_list)):       #run through all elements in my_list
        if my_list[i] == pivot:         #if the element in the list equals the pivot
            mid.append(my_list[i])      #add it to the new list mid
        elif my_list[i] < pivot:        #if the element in the list is less than the pivot
            left.append(my_list[i])     #add it to the new list left
        else:                           #if the element in the list is more than the pivot
            right.append(my_list[i])    #add it to the new list right
    
    #we call the recursive function to continue sorting the left and right lists
    #we do not need to sort the mid list as it contains element(s) of the same value
    my_sorted_list = quick_sort(left) + mid + quick_sort(right) #we combine left mid and right to form the sorted list
    return my_sorted_list
    

def add_to_heap(heap,element):
    if heap == []:              #if the heap is empty
        heap.append(element)    #just append the element
    
    else:                       #if the heap has elements already
        heap.append(element)    #we append the element
        elem_index = len(heap)-1  #we know the index of the element as the element was just added to the end of the list
        parent_index = math.ceil(elem_index/2)-1 #we calculate the index of the parent of the element
        
        while heap[parent_index] > element and parent_index >= 0: #when the element at parent_index is more than the element we just added
            heap[parent_index],heap[elem_index] = heap[elem_index],heap[parent_index] #we swap the elements to make sure the parent is always less than the child
            
            element = heap[parent_index] #we update the element to continually check if the heap properties are maintained
            elem_index = parent_index    #we update the element index
            parent_index = math.ceil(elem_index/2)-1 #and the parent index
    
def remove_min_from_heap(heap):
    if heap == []:              #if the heap is empty
        return None             #there is nothing to remove
    else:                       #if the heap has elements already
        minvalue = heap[0]      #set the minvalue to be the first element in the heap
        
        heap[0] = heap[-1]      #move the last element in the heap to be the new first element
        del heap[-1]            #remove the last element in the heap
        
        index = 0               #initialize the index to be 0
        
        leftchild_index = 2*index+1     #we calculate the indexes of the 2 children 
        rightchild_index = 2*index+2
        #the indexes of the elements must be less than the length of the tree
        #to ensure we are referencing within the tree
        while leftchild_index <= len(heap)-1 and rightchild_index <= len(heap)-1 and index <= len(heap)-1:
            if heap[leftchild_index] <= heap[rightchild_index]: #if the element at the leftchild is less than the element at the rightchild
                if heap[index] > heap[leftchild_index]: #check if the element at index is more than the element at the leftchild index
                    heap[index],heap[leftchild_index] = heap[leftchild_index],heap[index] #we swap the elements to make sure the parent is always less than the child
                    
                    index = leftchild_index #we update the index to continually check if the heap properties are maintained
                    leftchild_index = 2*index+1 #we update the leftchild index
                    rightchild_index = 2*index+2 #and the rightchild index
                    
                else: #if the element at the index is less than or equal the element at the chidren indexes
                    break #we can stop swapping the elements
                
            elif heap[rightchild_index] < heap[leftchild_index]: #if the element at the rightchild is less than the element at the leftchild
                if heap[index] > heap[rightchild_index]: #if the element at index is more than the element at the rightchild index
                    heap[index],heap[rightchild_index] = heap[rightchild_index],heap[index] #we swap the elements to make sure the parent is always less than the child
                    
                    index = rightchild_index #we update the index to continually check if the heap properties are maintained
                    leftchild_index = 2*index+1 #we update the leftchild index
                    rightchild_index = 2*index+2 #and the rightchild index
                    
                else: #if the element at the index is less than or equal the element at the chidren indexes
                    break #we can stop swapping the elements
        
        if leftchild_index <= len(heap)-1 and rightchild_index >= len(heap)-1: #if there is no rightchild but there is a leftchild, just check the leftchild
            if heap[index] > heap[leftchild_index]: #check if the element at index is more than the element at the leftchild index
                heap[index],heap[leftchild_index] = heap[leftchild_index],heap[index] #we swap the elements to make sure the parent is always less than the child
                #we do not need to update the indexes as we have reached the end of the heap
    
    return minvalue

def heap_sort(my_list): 
    heap = [] #create empty list to store the elements in the heap
    for i in my_list: #for all the elements in the list
        add_to_heap(heap,i) #add the elements to the heap, maintaining the heap properties
    
    my_sorted_list = [] #create empty list to store the sorted elements
    while heap != []:   #as long as the heap still contains elements
        my_sorted_list.append(remove_min_from_heap(heap)) #we remove the minimum value from it to append to our sorted list
    return my_sorted_list

def test_sorting(algo,my_tab,display):
    tab = my_tab.copy()
    print("testing",algo,str(" "*(14-len(algo))),"... ",end='')
    t = time.time()
    temp = eval(algo + "(tab)")
    if temp != None: tab = temp
    print("done ! It took {:.2f} seconds".format(time.time() - t))
    if display: print(tab,end='\n\n')
    

print("\n ******** Testing to sort a small table of 30 elements ********")
NUMBER_OF_ELEMENTS = 30
tab = [random.randint(1, 40) for i in range(NUMBER_OF_ELEMENTS)] 
#tab = list(set([random.randint(1, 40) for i in range(NUMBER_OF_ELEMENTS)]))
print("Original table: ")
print(tab,end='\n\n')
test_sorting("bubble_sort",tab,True)
test_sorting("selection_sort",tab,True)
test_sorting("insertion_sort",tab,True)
test_sorting("merge_sort",tab,True)
test_sorting("quick_sort",tab,True)
test_sorting("heap_sort",tab,True)

print("\n ******** Testing to sort a big table of 5000 elements ********")
NUMBER_OF_ELEMENTS = 5000
tab = list(set([random.random() for i in range(NUMBER_OF_ELEMENTS)]))
test_sorting("bubble_sort",tab,False)
test_sorting("selection_sort",tab,False)
test_sorting("insertion_sort",tab,False)
test_sorting("merge_sort",tab,False)
test_sorting("quick_sort",tab,False)
test_sorting("heap_sort",tab,False)
