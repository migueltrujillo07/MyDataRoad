# Before talking about loops, let's talk about the range function
# The range() function
#The range function outputs as an ordered sequence as a list
# When the input is just one positive value it starts from 0 to the current input

for i in range(10):
    print(i)# We will get from 0 to 10 

    # Lets change the next list with a for loop
colors = ["red", "yellow", "Blue", "green", "gray"]


print(len(colors))
print(colors)
for color in range(0,len(colors)):
    print(color)
    colors[color]= "white"

print(colors)

numbers = ["1","2","3"]

for i,number in enumerate(numbers):
   print(number) 
   print(i)

print(numbers)

countries = ["Mexico", "US","Brazil" ]
for index,countrie in enumerate(countries):
    countries[index] = "Canada"

print(countries)

# While looop

names = ["Jesus", "Jesus", "Lucas"]
newNames = []
i = 0
while (names[i] == 'Jesus'):
    newNames.append(names[i])
    i += 1

print(newNames)
