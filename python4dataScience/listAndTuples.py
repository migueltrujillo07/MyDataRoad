# Tuples are an ordered sequence
# Tuples are expressed as comma-separated elements within parentheses
# Here is an example

ratings = (10,9,6,5,10,8,9,6.2)

# In python are different types: strings, integers, float
# They can all be contained in a tuple, but the type of the varible
# is a tuple

# The tuples are inmutable 
# The tuples can contain more tuples

# List are also ordered sequences
# A list is represented with square brackets
# List are mutable

li = ['Miguek', 10.1, 2011, [8,10],("a",1)]

# it can contain integers, string, float, other list or tuples.
l = ["Miguel", 10.19, 2023] 
print(l)
l.append(["Luis",7])
print(l)

# If we apply extend we can add new elements to the list
l.extend(["Michel", 10])
print(l)

# As list are mutable, we can change them 
a = ["disco", 10, 1.2]
print(a)
a[0]= "pop"
print(a)

# And we can delete elements from a list using "del" command
del(a[0])
print(a)

# split method help to split a sequence into a list
name = "Luis Miguel Lopez"
print(name)
name_s = name.split()
print(name_s)
# We can indicate the delimiter we would like to split
name_i = name.split("i")
print(name_i)

# We can clone a list
ls_a = ["Mike", 10, 1.2]
ls_b = ls_a[:]
print(ls_b)
ls_a[0] = "Luis"
print(ls_b)

