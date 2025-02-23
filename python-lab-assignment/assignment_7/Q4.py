# Step 1: Write user input to file1
f1 = open('file1', 'w')
str = input("Enter string: ")
while str != '':
    f1.write(str + '\n')  # Write each string followed by a newline
    str = input("Enter string: ")
f1.close()

# Step 2: Read from file1 and write content to file2
f1 = open('file1', 'r')
f2 = open('file2', 'w')
str = f1.readline()
while str != '':
    f2.write(str)  # Write each line from file1 to file2
    f1.readline()
    str = f1.readline()
f2.close()
f1.close()

# Step 3: Display contents of file1 and file2
f1 = open('file1', 'r')
print("Content of file1:\n" + f1.read())
f1.close()

f2 = open('file2', 'r')
print("Content of file2:\n" + f2.read())
f2.close()
