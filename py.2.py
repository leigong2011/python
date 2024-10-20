def power(a,b):
    c=a**b
    print(c)
def powerpuls(a,b) :
    c=1
    while c<=b:
        c+=1
        cab=a**c
        cab1=cab+cab
        print(cab1)
        
def echobin(a):
    print(bin(a)[2:])
def Calculators(a,b):

    operation=str(input("What do you want to calculate? (pulse/minus/times/divide)"))
    if operation=="pulse":
        c=a+b
        print(c)
    elif operation=="minus":
        c=a-b
        print(c)
    elif operation=="times":
        c=a*b
        print(c)
    elif operation=="divide":
        c=a/b
        print(c)


import time
# 

# 库部分（函数定义）保持不变
# ...

# 初始化变量以进入循环
running = True

# 打印欢迎信息
print("This is a text tools shell.")
print("本程序由haswell制作")
print("ver:0.0.0.1")
print("Hello, user.\nWelcome to using my tools.")

# 开始循环
while running:
    toolspower = input("/_ ")
    if toolspower == 'quit':
        print("Exiting the shell.")
        running = False  # 设置条件为False以退出循环
    elif toolspower() == 'help':
        print("time---show current time\npower--calculate a to the power of b\npowerpuls--special power calculation\nbin--convert number to binary\ncal\calculate--simple calculator")
    elif toolspower == 'time':
        print(time.asctime(time.localtime(time.time())))
    elif toolspower == 'power':
        a = int(input("Base number is: "))
        b = int(input("Index is: "))
        power(a, b)
    elif toolspower == 'powerpuls':
        a = int(input("Base number is: "))
        b = int(input("Big index is: "))
        powerpuls(a, b)
    elif toolspower == 'bin':
        a = int(input("Number is: "))
        echobin(a)
    elif toolspower == 'cal' or toolspower.lower() == 'calculator':
        a=int(input("This calculator only supports two-number operations\nPlease enter your first number:"))
        b=int(input("Please enter your second number:"))
        Calculators(a,b)
    else:
        print("Unknown command. Please try again.")