def first():
    # Step 1: Write user input to file1
    datafile1 = open("file1", "w")
    str = input("Enter a string for datafile1: ")
    datafile1.write(str)
    datafile1.close()

    # Step 2: Read from file1 and write the content to file2
    datafile1 = open("file1", "r")
    datafile2 = open("file2", "w")
    str2 = datafile1.read()
    datafile2.write(str2)
    datafile2.close()
    datafile1.close()

    # Step 3: Read and display content from file2
    datafile2 = open("file2", "r")
    print("Content of file2: " + datafile2.read())
    datafile2.close()

first()
