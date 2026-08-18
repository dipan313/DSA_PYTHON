num = int(input(" Enter a Number: "))
n = num
str = []
while n>0:
    dig = n % 10
    n = n//10
    print(dig)
    str.append(dig)
print(str)

