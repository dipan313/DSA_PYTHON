num1 = int(input("enter a number for num1: "))
num2 = int(input("enter a number for num2: "))

if num1<0 or num2<0:
    print("Invalid")
elif num1>num2:
    print ("Num1 is giving more profit")
elif num2> num1 :
    print("Num2 is giving more profit")
else:
    print("Both are giving same profit")