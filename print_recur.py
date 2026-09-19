i = 0
n = 5
# def func(a,b):
#     if a>b:
#         return
#     print(a)
#     func(a+1,b)
# func(i,n)
def func(a,b):
    if a>b:
        return
    func(a+1,b)
    print(a)
func(i,n)