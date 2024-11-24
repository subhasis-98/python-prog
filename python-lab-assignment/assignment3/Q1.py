# Get inputs from the user
start = int(input("From : "))
end = int(input("to : "))
step = int(input("step by : "))

# Check if the step is valid
if step == 0:
    print("Increment value cannot be zero.")
else:
    print("Counting:")
    for i in range(start, end, step):
        print(i, end=" ")
    # print()
