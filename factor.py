n = int(input("Enter a number: "))
num = n
fact = []
# while num > 0:
#     if n % num == 0:
#         fact.append(num)
#     num = num - 1
#     #print(num)
# print("The factors of ", n, "is :\n", fact)

#optimal sol

from math import sqrt
for i in range(1, int(sqrt(num))+1):
    if num % i == 0:
        fact.append(i)
        if num//i != i:
            fact.append(num//i)
fact.sort()
print("The factors of ", n, "is :\n", fact)