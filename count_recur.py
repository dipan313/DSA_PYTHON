count = 0
def func():
    global count
    if count == 4:
        return
    # print("Dipan")
    count +=1
    func()
    print("Dipan")
func()