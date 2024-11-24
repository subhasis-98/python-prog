# num = int(input("enter number : "))
# count = 0
# for i in range(1,num):
#     if(i%3==0 or i%5==0):
#         print(i)
#         count+=i
# print(count)
N = int(input("Enter a number: "))
total_sum = 0

for i in range(N):
    if i % 3 == 0 or i % 5 == 0:
        total_sum += i

print("Sum:", total_sum)
