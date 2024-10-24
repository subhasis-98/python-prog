x = int(input("Enter day number : "))
match x:
    case 1:
        print("Sunday")
    case 2:
        print("Monday")
    case 3:
        print("Tuesday")
    case 4:
        print("Wenesday")
    case 5:
        print("Thrusday")
    case 6:
        print("Friday")
    case 7:
        print("Saturday")
    case _:
        print("Invalid Entry")
        