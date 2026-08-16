from math import *
n = int(input("Enter a number: "))
num = n
def count_num(num):
    return int(log10(num) +1)
count = count_num(num)
#count = len(str(num))
res = 0
while n != 0:
    dig = n %10
    res = res + dig**count
    n = n // 10
if res == num:
    print("AMSTRONG")
else:
    print("NOT AMSTRONG")
