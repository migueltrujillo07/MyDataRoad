# numpy is library for data science
# The basic and array creation 
# A numpy array is similiar to an array 

# Let's import the numpy library
import numpy as np

# a => an array

a = np.array([0,1,2,3,4])

print(a.size) # -> In this line we are printing the size of the array
print(a.ndim) # -> This line prints the number of the array dimentions
print(a.shape) # -> The attribute shape is a tuple of integers indicating the size of the array in each dimention

# Indexing and Slicing methods
# We can change the value of the array as follows
c = np.array([20,1,2,3,4])
print(c)
c[0] = 100
print(c)

c[0] = 0
print(c)
 # Just change the index value to indicate wich you want to change
b = np.array([7,7,8], )

d = c[1:4]
print(d)

# Play with vectors

u = [1,0]
v = [0,1]

z = []

for n,m in zip (u,v):
    z.append(n+m)
    
print(z)
 

