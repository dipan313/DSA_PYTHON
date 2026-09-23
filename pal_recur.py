s = input("Enter a string ")
left=0
right = len(s)-1

def func(s, left, right):
    if left>=right:
        return True
    if s[left]!=s[right]:
        return False
    return func(s,left+1,right-1)
pal = func(s, left, right)

if pal is True:
    print("it is a palindrome number")
else:
    print("Not pal")