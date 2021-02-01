# This scripts reads from the file salaries_data.txt
# and plots its data
import numpy as np

try: #read the contents of this file
    my_file = open('salaries_data.txt','r')
except FileNotFoundError: #checking if the file exists
    print('This file does not exist!')
else:
    print('File found! Now processing your file')
    
# read from file and store it into a numpy matrix
my_data = np.loadtxt ('salaries_data.txt')

ID = my_data [: ,0] #ID of the employee, from the 1st column
salary_prev = my_data [: ,1] #salary/hour previous year, from the 2nd column
hours_prev = my_data [: ,2] #number of hours worked in previous year, from the 3rd column
salary_curr = my_data [: ,3] #salary/hour current year, from the 4th column
hours_curr = my_data [: ,4] #number of hours worked in current year, from the 5th column

salary1 = (salary_prev)*(hours_prev) #total salary in previous year
salary2 = (salary_curr)*(hours_curr) #total salary in current year

#calculate the percentage increase of the salaries
salary_increase = (salary2 - salary1)/salary1 * 100

#calculate the average percentage increase by summing all and dividing by size of the matrix
average_salary_increase = np.sum(salary_increase)/np.size(salary_increase)
print('The average total salary increase is %.4f percent' %(average_salary_increase))

#identify which employees got a total salary increase
#greater than 5% from previous to current year
x = my_data[:,0][np.where(salary_increase > 5 )]

print('The following employee IDs got a total salary increase greater than 5%:')
print(x)
