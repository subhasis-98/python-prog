def check_number_in_range(number, start, end):
    if start <= number <= end:
        return True
    else:
        return False

def main():
    number = float(input("Enter a number: "))
    start = float(input("Enter the start of the range: "))
    end = float(input("Enter the end of the range: "))
    if start > end:
        print("Invalid range. The start value should be less than the end value.")
        return
    
    if check_number_in_range(number, start, end):
        print(f"The number {number} is within the range {start} to {end}.")
    else:
        print(f"The number {number} is NOT within the range {start} to {end}.")

main()
