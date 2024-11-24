row = 10
col = 10

for i in range (1,row+1):
    # print("*")
    for j in range(1,col+1):
        if(i%j == 0 or j%i==0):
            print("*",end="")
        else:
            print(" ",end="")
    print(i)        
    # print()        