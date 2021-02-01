# This scripts reads from the file salaries.dat
# and plots its data
import numpy as np
import matplotlib.pyplot as plt

try: #read the contents of this file
    my_file = open('salaries.dat','r')
except FileNotFoundError: #checking if the file exists
    print('This file does not exist!')
else:
    print('File found! Now processing your file')
    
# read from file and store it into a numpy matrix
my_data = np.loadtxt ('salaries.dat')

age = my_data [0,:] #age of the individuals, from the 1st row
experience = my_data [1,:] #years of experience, from the 2nd row
salary = my_data [2,:] #salary, from the 3rd row

#output the number of entries
x = np.size(age)
print('There are %d salaries in the file' %(x))


# plot the 1st graph in blue, solid line
plt.figure(1)
plt.plot (age,salary,'b-') #dependency of salary on age
# label axes and put title
plt.axis ([15,70,10000,100000])
plt.xlabel ('Age')
plt.ylabel ('Salary')
plt.title ('Dependency of the salary on the age')

#plot the 2nd graph in green, dashed line
plt.figure(2)
plt.plot (experience,salary, 'g--') #dependency of salary on experience
#label axes and put title
plt.axis ([-5,40,10000,100000])
plt.xlabel ('Experience')
plt.ylabel ('Salary')
plt.title ('Dependency of the salary on years of experience')

plt.show ()

