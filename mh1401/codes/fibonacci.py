def r_fibonacci(n):
    """This is the recursive implementation of the Fibonacci sequence
    This function returns the n-th Fibonacci number in the sequence
    Format of call: r_fibonacci(int)
    returns an integer"""
    
    #check the base cases
    if n == 0:
        return 0
    elif n == 1:
        return 1
    #otherwise just use recursive function
    else:
        return r_fibonacci(n-1) + r_fibonacci(n-2)

def i_fibonacci(n):
    """This is the iterative implementation of the Fibonacci sequence
    This function returns the n-th Fibonacci number in the sequence
    Format of call: i_fibonacci(int)
    returns an integer"""
    
    #check the base cases
    if n == 0:
        return 0
    elif n == 1:
        return 1
    #otherwise use iterative function
    else:
        F_i_2 = 0
        F_i_1 = 1
        #apply the formula (n-1) times to obtain F(n)
        for i in range((n-1)):
            x = F_i_1
            F_i_1 = F_i_1 + F_i_2
            F_i_2 = x
        return F_i_1

#call the function with n = 35
#and measure the timings
import time
start = time.clock() #start the clock
print(r_fibonacci(35))
print(time.clock()-start) #stop the clock

start = time.clock() #start the clock
print(i_fibonacci(35))
print(time.clock()-start) #stop the clock

#the recursive function is easier to write
#but the iterative function is faster to compute.
#for F(4), n=4, we compute F(n-1) + F(n-2) = F(3) + F(2)
#F(3) + F(2) = F(2) + F(1) + F(2)
# = F(1)+F(0)+F(1)+F(1)+F(0) = 1+0+1+1+0= 3
#this takes longer to compute as it has to keep calling itself
#even though it stimulates a loop and is similar to the iterative function in that sense