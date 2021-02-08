import matplotlib.pyplot as plt
import time
import random

# function that plots a points and hull in a new window
# it takes a cloud of points (pts) and a convex hull (hull) as inputs
def plot_hull(pts,hull,leftmost=None,rightmost=None):
    fig = plt.figure()
    ax = fig.add_subplot(111)
    my_hull = hull[:]
    my_hull.append(my_hull[0])
    ax.plot([x[0] for x in pts], [x[1] for x in pts], "ko")
    ax.plot([x[0] for x in my_hull], [x[1] for x in my_hull], "ro--")
    if leftmost!=None:
        ax.plot(hull[(leftmost)%len(hull)][0], hull[(leftmost)%len(hull)][1], "bo")
        plt.text(hull[(leftmost)%len(hull)][0]+0.015, hull[(leftmost)%len(hull)][1]+0.015, "l", fontsize=20)
    if rightmost!=None:
        ax.plot(hull[(rightmost)%len(hull)][0], hull[(rightmost)%len(hull)][1], "go")
        plt.text(hull[(rightmost)%len(hull)][0]+0.015, hull[(rightmost)%len(hull)][1]+0.015, "r", fontsize=20)
    

# function that checks if three points a,b,c are clockwise positioned 
def is_clockwise(a,b,c):
    if (c[1]-a[1])*(b[0]-a[0]) < (b[1]-a[1])*(c[0]-a[0]):
        return True
    else:
        return False


# compute with naive method the convex hull of the points cloud pts 
# and store it as a list of vectors
def convex_hull_2d_gift_wrapping(pts):

    a =  pts[0] #we set the first element of pts to be a
    index = 0 #we find the index of a , but since we know it's the first element
              #index is just 0
    
    l = index #we initialize l by letting l = index
    hull = [] #we create an empty vector hull to store the points which will form the convex hull
    hull.append(a) #since pts are already sorted by x coordinates
                   #we know that the first element in pts is the leftmost point and it is to be added to the hull

    for p in range(1,len(pts)): #we do not include 0 as pts[0] is already in the convex hull
        for q in range(len(pts)): #we run through all possible elements in pts
            if is_clockwise(pts[l], pts[q], pts[p]) == True:
                #when is_clockwise is False, p remains as it is and we run through q to check the other points
                #after checking all q, if is_clockwise is still False, p is the leftmost point
                #when is_clockwise is True, we set p to equal to q
                #so as to push p to be the leftmost point of pts after l
                p = q #p is the leftmost point after l
        l = p #we set p to be the new l 
        if l == index: #once we reach back to pts[0], we dont have to check anymore as a loop is formed already
            break
        hull.append(pts[p]) #we add p to the convex hull
    
    return hull  
    #the time complexity of this algorithm is O(n^2)

# define a new function merge to combine the points after dividing them 
def merge(left,right):
    l = max(left, key=lambda x: x[0]) #we find the rightmost point of l
    r = min(right, key=lambda x: x[0]) #we find the leftmost point of r
    
    l_1 = l #we create a copy of l
    r_1 = r #and a copy of r
    
    hull = [] #we create an empty vector to store the points which will form the convex hull
    
    #here we find the upper tangent of left and right
    for L in reversed(left): #we run through the points in left from the last point to the first
        if is_clockwise(r,l,L) == True: 
            #when is_clockwise is False, l remains as it is and we run through L to check the other points
            #after checking all L, if is_clockwise is still False, l is the leftmost point
            #when is_clockwise is True, we set l to equal to L
            #so as to push l to be the leftmost point
            l = L #we set L to be the new l
    hull.append(l) #we add l to the convex hull
    
    for R in right: #we run through the points in right 
        if is_clockwise(l,r,R) == False:
            #when is_clockwise is True, r remains as it is and we run through R to check the other points
            #after checking all R, if is_clockwise is still True, r is the leftmost point
            #when is_clockwise is False, we set r to equal to R
            #so as to push r to be the leftmost point
            r = R #we set R to be the new r
    hull.append(r)  #we add r to the convex hull

    #here we find the lower tangent of left and right using the same idea as above
    for R_1 in right: 
        if is_clockwise(l_1,r_1,R_1) == True:
            r_1 = R_1
    hull.append(r_1)
    
    for L_1 in reversed(left):
        if is_clockwise(r_1,l_1,L_1) == False:
            l_1 = L_1
    hull.append(l_1)
    
    #we want to add the points in right that is between r and r_1 to the convex hull
    for i in right:
        if right.index(i) > right.index(r) and right.index(i) < right.index(r_1):
            hull.insert(hull.index(r)+1,i)
            r = i
    #we want to add the points in left that is between l_1 and l to the convex hull
    for j in left:
        if left.index(j) < left.index(l) and left.index(j) > left.index(l_1):
            hull.insert(hull.index(l)-1,j)
            l = j
            
    return hull
        
# compute with divide and conquer method the convex hull of the points  
# cloud pts and store it as a list of vectors
def convex_hull_2d_divide_conquer(pts):
    
    if len(pts) == 1: #if there is only one point
        return pts    #it already forms the convex hull
    
    elif len(pts) <= 4: #if there is 4 points or less 
        return convex_hull_2d_gift_wrapping(pts) #we can do the gift wrapping algorithm
      
    else:
        mid = int(len(pts)/2) #we find the mid point of pts
        left = pts[0:mid] #then we split pts into 2 with left from index 0 to mid
        right = pts[mid:] #and right from index mid to the last element
        
        x = convex_hull_2d_divide_conquer(left) #we recursively run the function to split up pts until the length is 4 or lesser than 4
        y = convex_hull_2d_divide_conquer(right) #we do the same here 
        
        return merge(x,y) #then we merge the points to form the convex hull
        
    #the time complexity of this algorithm is O(nlogn)
    #for merge, it is O(n), for divide and conquer it is O(nlogn)
    
NUMBER_OF_POINTS = 20

# generate random points and sort them according to x coordinate
pts = []
for i in range(NUMBER_OF_POINTS): pts.append([random.random(),random.random()]) 
pts = sorted(pts, key=lambda x: x[0])

# compute the convex hulls
print("Computing convex hull using gift wrapping technique ... ",end="")
t = time.time()
hull_gift_wrapping = convex_hull_2d_gift_wrapping(pts)
print("done ! It took ",time.time() - t," seconds")

print("Computing convex hull using divide and conquer technique ... ",end="")
t = time.time()
hull_divide_conquer = convex_hull_2d_divide_conquer(pts)
print("done ! It took ",time.time() - t," seconds")

# close the convex hull for display
hull_gift_wrapping.append(hull_gift_wrapping[0])
hull_divide_conquer.append(hull_divide_conquer[0])

# display the convex hulls
if NUMBER_OF_POINTS<1000:
    fig = plt.figure()
    ax = fig.add_subplot(131)
    ax.plot([x[0] for x in pts], [x[1] for x in pts], "ko")
    ax.title.set_text('Points')
    ax = fig.add_subplot(132)
    ax.plot([x[0] for x in pts], [x[1] for x in pts], "ko")
    ax.plot([x[0] for x in hull_gift_wrapping], [x[1] for x in hull_gift_wrapping], "ro--")
    ax.title.set_text('Gift Wrapping')
    ax = fig.add_subplot(133)
    ax.plot([x[0] for x in pts], [x[1] for x in pts], "ko")
    ax.plot([x[0] for x in hull_divide_conquer], [x[1] for x in hull_divide_conquer], "ro--")
    ax.title.set_text('Divide/Conquer')
    plt.show(block=False)


    
