n = int(input("Enter num "))
total = 0
a = 1
def sum(a,n):
    global total
    if a>n:
        return
    total=total+a
    return sum(a+1,n)
sum(a,n)
print(total)