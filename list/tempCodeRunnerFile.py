number_of_element = int(input("Numbers of element : "))
list1= []
for i in range(number_of_element):
    element= int(input(f"Enter number {i+1} : "))
    list1.append(element)
print(list1)