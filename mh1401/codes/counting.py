def counting(intlist, my_integer):
    """ This function takes as inputs a sorted list of integers and an integer
    Format of call: (intlist,int)
    returns the number of times this integer is present in the list
    returns an integer"""
    intlist.sort() #sort the list of integers

    
    if len(intlist) > 1: #if there are more than 1 element in the list
        #we check the middle entry of the list, and depending on its value
        #we divide the current list into 2 halves, so as to only check
        #the appropriate half
        
        mid = int(len(intlist)/2) #finding the mid index of the list

        if intlist[mid] > my_integer: #if my_integer is less than mid element of intlist
            return counting(intlist[:mid],my_integer) #search in the left half of intlist using the counting function
        
        elif intlist[mid] < my_integer: #if my_integer is more than mid element of intlist
            return counting(intlist[mid+1:],my_integer) #search in the right half of intlist using the counting function
        
        else: #if intlist[mid] = my_integer
            counter = 0 #initialize counter to 0
            for i in range(len(intlist)): #goes through all elements in the list
                if intlist[i] == my_integer: #if the element in the i-th position is my_integer
                    counter += 1 #increase counter by 1
        return counter
    
    elif len(intlist) == 1: #if there is only 1 element in intlist
        if intlist[0] == my_integer: #and that element is my_integer
            return 1 #since there is only 1 element in the list
        else: #else if element is not my_integer
            return 0
    
    else: #if intlist = [], ie intlist is empty
        return 0

#the algorithm has an average asymptotic time complexity of O(log(n)), where n represents the input list size
#this is because we succesively divide the list in 2 until we reach a 1-element list
#we would have 1 = n/2^x, thus x = log2n = logn/log2 = O(log(n))