list = [1,2,3,4,3,5,5,55,20]
max = 0
for i in list:
    if i%2 == 0 and i>max:
        max=i
print(max)