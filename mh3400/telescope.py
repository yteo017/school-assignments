import random 
import time
import math

# this function checks if two tasks are conflicting. It assumes L is sorted according to starting time
def is_conflict(L):
    for i in range(len(L)-1):
        if L[i][1] > L[i+1][0]: return True
    return False

# this function makes a random search for assignments
def random_search(L):
    vec_assignment = [0]*len(L)
    
    while True:         
        non_conflicting_tasks = []
        for i,el in enumerate(L):
            if vec_assignment[i] == 0:
                vec_assignment[i] = 1
                assignment = [L[k] for k in range(len(L)) if vec_assignment[k]==1 ]
                if not is_conflict(assignment):
                    non_conflicting_tasks.append(i)
                vec_assignment[i] = 0                
                        
        if len(non_conflicting_tasks)==0:
            assignment = [L[k] for k in range(len(L)) if vec_assignment[k]==1 ]
            val = sum([k[2] for k in assignment])
            return (val,assignment)
        
        i = non_conflicting_tasks[random.randint(0,len(non_conflicting_tasks)-1)]
        vec_assignment[i] = 1        

# this function makes a brute force search for assignments
def brute_force(L):
    
    mylist = [] #create an empty vector to store the different combinations of the tuples
    subset = [] #create an empty vector to store the combis of tuples that do not overlap
    benefits = [] #create an empty vector to store the benefits of the tuples that do not overlap
    
    for i in range(2**len(L)):
        mylist.append(format(i,'020b')) #create a binary list of 0s and 1s to assign the tasks, 0 means not assigned and 1 is assigned
        mylist[i] = [int(x) for x in mylist[i]] #convert the binary form into a list of integers for easier referencing
        for j in range(1,len(mylist[i])+1): #running through all elements starting from the end of the list
            if mylist[i][-j] == 1: #check if the task is assigned
                mylist[i][-j] = L[-j] #if it is, update it to be the tuple of the task assigned
        for k in range(mylist[i].count(0)): #count the number of zeros
            mylist[i].remove(0) #and remove all the zeros from the list
    
        if mylist[i]!=[] and is_conflict(mylist[i]) == False: #check if the tuples overlap
            subset.append(mylist[i]) #if not, add to a new list for use later
        
    for l in range(len(subset)): #running through all the combis of tuples that do not overlap
        benefit = 0 #initialize benefit to 0
        for m in range(len(subset[l])): #running through all the tuples in the sublist
            benefit += subset[l][m][2] #calculate the total benefits of the tasks that do not overlap
        benefits.append(benefit) #add the total benefits of the different combinations of tasks to the list "benefits"
 
    maxben = max(benefits) #find the maximum benefit
    index = benefits.index(maxben) #find the index of the maximum benefit

    return (maxben,subset[index])
    
# this function makes a greedy force search for assignments
def greedy(L):
    subset = [] #create an empty vector to store the tuples 
    benefit = 0 #create a variable to calculate the benefits
    L_copy = L #create a copy of the list so that the original list is untouched
    
    while len(L_copy) > 0: #as long as there are elements in the list
        maxben = 0 #initialize the max benefit to be 0 first
        for i in range(len(L_copy)):  #find the tuple with the max benefit by checking each of the tuples
            if L_copy[i][2] > maxben: #if the benefit of the tuple is more than the maxben
                maxben = L_copy[i][2] #it is the max benefit, update maxben
                index = i #store the index of the tuple with the max benefit

        subset.append(L_copy[index]) #add the tuple with the max benefit to our list "subset"
        benefit += maxben            #calculate the total benefits
        del L_copy[index]            #delete the tuple so that it is not included again
        
        if is_conflict(sorted(subset)) == True: #check if there is conflict between the tasks
            subset.pop()        #if there is, do not include it in the list "subset"
            benefit -= maxben   #minus off the benefit
                    
    return (benefit,sorted(subset))

# this function makes a dynamic programming search for assignments
def dynamic_prog(L):
    
    mylist = L #create a copy of the list so that the original list is untouched
    mylist.sort(key=lambda x:x[1]) #sort the tuples according to the finish time
    accum_ben = [0]*len(mylist) #create a vector to store the accumulated benefits
    
    for i in range(len(mylist)): #running through the elements in mylist
        accum_ben[i] = mylist[i][2] #initialize the accumulated benefits with the original benefits of task i
    for j in range(1,len(mylist)): #set pointer j
        for k in range(len(mylist)-1): #and pointer k
            if mylist[k][1] <= mylist[j][0]: #if the end time of k does not overlap with the start time of j
                #and if the accumulated benefit of task k and the benefit of task j is bigger than the accum benefit of task j
                if accum_ben[k] + mylist[j][2] > accum_ben[j]:
                    #update the accumulated benefit of task j to be the sum of the accum benefit of k and the benefit of task j
                    accum_ben[j] = accum_ben[k] + mylist[j][2] 
                    
    maxben = max(accum_ben) #find the maximum benefit
    benefit = maxben #store it in "benefit"
    
    subset = [] #create an empty vector to store the tuples involved in the forming of the maximum benefit
    for m in reversed(range(len(mylist)-1)): #this for loop runs through all elements in mylist in reversed order
        if maxben == accum_ben[m]: #if the maximum benefit equals the accumulated benefit of task m
            subset.append(mylist[m]) #task m was involved, hence append it in "subset"
            maxben -= mylist[m][2]  #minus off the benefit of task m
                
    return (benefit,sorted(subset))

# this function prints the tasks
def print_tasks(L):
    for i,t in enumerate(L):
        print("task %2i (b=%2i):" %(i,t[2]),end="")
        print(" "*round(t[0]/10) + "-"*round((t[1]-t[0])/10))
        

# this function tests and times a telescope tasks assignment search
def test_telescope(algo,my_tab,display):
    tab = my_tab.copy()
    print("testing",algo,str(" "*(14-len(algo))),"... ",end='')
    t = time.time()
    (max_temp,assignment_temp) = eval(algo + "(tab)")
    print("done ! It took {:.2f} seconds".format(time.time() - t))
    if max_temp!=None:
        print("Solution with benefit = %i" %(max_temp),end='\n')
    if display: 
        if assignment_temp!=None:
            print_tasks(assignment_temp)
            print()
    

MAX_BENEFIT = 99
MAX_START_TIME = 500
MAX_DURATION = 250

NUMBER_OF_ELEMENTS = 10
print("\n ******** Testing to solve for %i events ********" %(NUMBER_OF_ELEMENTS))
val = [(random.randint(1, MAX_START_TIME),random.randint(1, MAX_DURATION),random.randint(1, MAX_BENEFIT)) for i in range(NUMBER_OF_ELEMENTS)] 
tab = sorted([(val[i][0],val[i][0]+val[i][1],val[i][2]) for i in range(NUMBER_OF_ELEMENTS)])
print("Problem instance: ")
print_tasks(tab)
print("")
test_telescope("random_search",tab,True)
test_telescope("brute_force",tab,True)
test_telescope("greedy",tab,True)
test_telescope("dynamic_prog",tab,True)


NUMBER_OF_ELEMENTS = 20
print("\n ******** Testing to solve for %i events ********" %(NUMBER_OF_ELEMENTS))
val = [(random.randint(1, MAX_START_TIME),random.randint(1, MAX_DURATION),random.randint(1, MAX_BENEFIT)) for i in range(NUMBER_OF_ELEMENTS)] 
tab = sorted([(val[i][0],val[i][0]+val[i][1],val[i][2]) for i in range(NUMBER_OF_ELEMENTS)])
test_telescope("random_search",tab,False)
test_telescope("brute_force",tab,False)
test_telescope("greedy",tab,False)
test_telescope("dynamic_prog",tab,False)

