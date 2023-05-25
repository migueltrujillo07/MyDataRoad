file1 = open("example2.txt", "w")
# first argument => the path of the file
# The second argument is the mode where r => reading and w => writing a => appending
print(file1.name)

with open("example2.txt", "w") as file1:
    file1.write("This is the line A\n")
    file1.write("This is the line B")


forlines = open("forlines.txt", "w")
lines = ["This is the line A\n", "This is the line B \n", "This is the line C\n"  ]
with open("forlines.txt", "w") as forlines:
    for line in lines:
        forlines.write(line)

with open("forlines.txt", "r") as readfile:
    with open("example3.txt","w") as writefile:
        for line in readfile:
            writefile.write(line)
