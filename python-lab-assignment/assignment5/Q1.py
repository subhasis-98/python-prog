import math
def area_of_triangle():
    s1 = int(input("enter length : "))
    s2 = int(input("enter width : "))
    s3 = int(input("enter width : "))
    s = (s1+s2+s3)/2
    area = math.sqrt(s*(s-s1)*(s-s2)*(s-s3))
    print("area = ",area)
area_of_triangle()