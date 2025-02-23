f = open('file1.txt', 'w')  # Use consistent and valid file names
str = input("Enter string: ")
while str != '':
    f.write(str.upper() + ' ')  # Write input in uppercase with a space
    str = input("Enter string: ")
f.close()

f = open('file1.txt', 'r')  # Open the same file for reading
print(f.read())  # Display the contents of the file
f.close()
