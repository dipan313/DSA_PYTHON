s = input("enter a string ")
orS=s
left  = 0
right = len(s)-1

# def func(s, left, right):
#     if s[left] >= s[right]:
#         return True
#     else:
#         return False
#     func(s, left+1, right-1)
# val = func(s, left, right)
def func(s,left,right):
    while left<right:
        if s[left] != s[right]:
            return False
        left +=1
        right -=1
    return True
val = func(s,left,right)
if val is True:
    print("Palindrome")
else:
    print("Not Palindrome")