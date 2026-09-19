x=38
n=4
def func(a,b):
    if b ==0:
        return
    print(a)
    func(a,b-1)
func(x,n)