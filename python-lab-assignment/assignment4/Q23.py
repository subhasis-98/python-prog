# 23. Observe carefully the below function 
# def fun(a=0, b=1):  
# return (a**2 + b**2) 
# What will be the output for each call made below?  
# a.) fun(2,a=3)  
# b.) fun(b=3,2) 
# c.) fun(3,b=2)  
# d.) fun(a=4,5) 
 
# def fun(a=0, b=1):  
#     return (a**2 + b**2)
# print(fun())


def fun(a=0, b=1):  
    return (a**2 + b**2)

print(fun(2,a=3))   #error
print(fun(b=3,2))   #error
print(fun(3,b=2))   #13
print(fun(a=4,5))     #error


