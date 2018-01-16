def add():
    num=int(input("num1: "))
    num2=int(input("num2: "))
    result=num+num2
    print(result)

def sub():
    num=int(input("num1: "))
    num2=int(input("num2: "))
    result=num-num2
    print(result)

def multiple():
    num=int(input("num1: "))
    num2=int(input("num2: "))
    result=num*num2
    print(result)

def devide():
    num=int(input("num1: "))
    num2=int(input("num2: "))

    if num == 0 or num2 == 0:
        print("Error")
        return
    result=num/num2
    print(result)


while True:
    print("Menu")
    print("-----------")
    print("1.add")
    print("2.sub")
    print("3.multiple")
    print("4.devide")
    print("5.stop")
    sel=int(input(":"))

    if sel == 1:
        add()
    elif sel == 2:
        sub()
    elif sel == 3:
        multiple()
    elif sel == 4:
        devide()
    elif sel ==5:
        break
    else:
        print("Wrong input")
    

