n = int(input("enter a number "))

def fac(n):
    if n==0 or n==1:
        return 1
    return (n*fac(n-1))
facto = fac(n)
print(facto)