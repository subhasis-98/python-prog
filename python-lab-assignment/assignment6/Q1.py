def remove_duplicates(input_list):
    unique_list = []
    for item in input_list:
        if item not in unique_list:
            unique_list.append(item)
    print(unique_list)
# values = [1, 2, 2, 3, 4, 4, 5, 6, 3, 1]

values =[]
for i in range(10):
    print("enter the element : ")
    el = int(input())
    values.append(el)


unique_values = remove_duplicates(values)
print("Original List:", values)
# print("List without duplicates:", unique_values)


