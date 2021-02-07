import numpy as np

rows = int(input('Please input the number of rows for the matrix:'))
columns = int(input('Please input the number of columns for the matrix:'))
my_mat = np.random.rand(rows, columns) #generates a matrix of unknown size

#produce a function that calculates the sum of all the elements in the matrix
#and the product of all the elements in the matrix
def sum_and_prod(my_mat):
    my_sum = 0 #initializing my_sum
    my_product = 1 #initializing my_product
    for r in range(rows):
        for c in range(columns):
            my_sum += my_mat[r,c]
            my_product *= my_mat[r,c]
    return(my_sum,my_product)

#to call the function, print(sum_and_prod(my_mat))
print(sum_and_prod(my_mat))