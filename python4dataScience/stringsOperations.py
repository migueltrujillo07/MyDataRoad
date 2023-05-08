# A string is sequence of characters. A string is contained within two quotes or single quotesd
# A string can be digits, spaces or special characters
# It's helpful to think of a string as an ordered sequence
# Each element in the sequence cab be accessed using an index

name = 'Miguel Trujillo'
# Where the first index is M and the last one is o
# We can also use negative index but the the -1 is the last element 
print(name[0]) # It prints M

print(name[-1]) # It prints o # It prints o

print(name[::2]) # It prints each pair element starting in 0

print(name[0:5:2]) # It prints eache element starting in 0 until element 5 with in pairs

# With the len function we can know how many elements are in the string
print(len(name)) # There are 15 element including the space

# So the element number 15 is the same as -1

# We can add string into other string
print(name + ' is fun') # It will print Miguel Trujillo is fun

# Or we can multiply the times of the name
print(name * 3) # It will print Miguel Trujillo 3 times

# Escape Sequences 
# \n are meant to proceed escape sequences
# Escape sequences are strings that are difficult to input
print("Miguel \n Trujillo")
print("Miguel \t Trujillo")

# Methods, when we apply a method to a string "A" we will get a new string "B"
# upper Method
string_a= "Thriller is the sixth studio albun"
string_b= string_a.upper()
print(string_b)
# As you can notice the string "B" is different from the string "A"
# The upper mothod makes all the character inside string uppercase

# replace Method
b = name.replace('Miguel','Luis')
print(b)
# The first argument we put the word that we want to replace and in the
# second argument we indicate with wich value we wanna to chage the first argument

# The find method find sub-strings.The argument is the sub-string
# you would like to find. And the output is the index of the sequence
print(b.find('Luis')) # --> It should print "0" that's because the string
# starts in the 0 value


