x = float(input("Enter the value of x : "))
y = float(input("Enter the value of y : "))

if(x>0 and y>0):
    print("Quadrant 1")
elif(x<0 and y>0):
    print("Quadrant 2")
elif(x<0 and y<0):
     print("Quadrant 3")
else:
     print("Quadrant 4")