a = int(input("enter the value of a"))
b = int(input("enter the value of b"))
c = int(input("enter the value of c"))

d = b*b-4*a*c
r1 =-b+((b*b-4*a*c)**0.5)/2*a
r2 =-b-((b*b-4*a*c)**0.5)/2*a
if(d>0):
    r1 = (-b+d**0.5)/2*a
    r2 = (-b-d**0.5)/2*a
    print("root1 = ",r1 )
    print("root2 = ",r2)
elif(d==0):
    r1 = -b/2*a
    print("r1 =",r1 )
else:
    print("no real root")