number = 72958476 
a, b = 0, 0  
while (number > 0):  
    digit = number % 10 
if(digit % 2 != 0):  
    a += digit 
else:  
    b += digit  
number /= 10  
print(a,b) 