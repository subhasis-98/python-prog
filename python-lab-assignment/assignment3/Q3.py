# n =1000
# for i in range(1000,2000+1):
#     if(i%5==4):
#         print("\n")
#     print(" ",i,end="")
for i in range(1000, 2001):
    print(i, end=" ")
    if i % 5 == 4:  # Break the line after every 5 numbers
        print()
