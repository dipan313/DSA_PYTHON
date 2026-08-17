num = int(input(" Enter a Number: "))
n = num
res = 0
while n>0:
    dig = n % 10
    res = res * 10 + dig
    n = n // 10
print(res)

if num == res:
    print("The number is a palindrome")