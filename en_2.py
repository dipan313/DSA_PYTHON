from math import *
num = int(input("Enter a number: "))
def count_num(num):
    return int(log10(num) +1)
print(count_num(num))