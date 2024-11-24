day = int(input("Enter the day no. "))
daye = int(input("enter the day no. of future"))

if(day == 1):
    print("sunday") #43
elif(day==2):
    print("monday")
elif(day==3):
    print("tuesday")
elif(day==4):
    print("wednesday")
elif(day ==5):
    print("thrusday")
elif(day==6):
    print("friday")
else:
    print("saturday")
    
future_day =(day+daye)%7

if(future_day == 1):
    print("sunday") #43
elif(future_day ==2 ):
    print("monday")
elif(future_day == 3):
    print("tuesday")
elif(future_day == 4):
    print("wednesday")
elif(future_day == 5):
    print("thrusday")
elif(future_day == 6):
    print("friday")
else:
    print("saturday")