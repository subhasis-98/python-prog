def cumulative_sum(input_list):
    cumulative_list = []
    current_sum = 0
    for num in input_list:
        current_sum += num
        cumulative_list.append(current_sum)
    return cumulative_list
numbers = list(map(int, input("Enter a list of numbers separated by spaces: ").split()))
result = cumulative_sum(numbers)
print("Original List:", numbers)
print("Cumulative List:", result)
