#要导入的库
import requests
import logging
import os
import time
import random
#定义函数部分
def power(a,b):#计算幂
    c=a**b
    print(c)
def powerpuls(a,b) :#计算特殊的幂
    c=1
    while c<=b:
        c+=1
        cab=a**c
        cab1=cab+cab
        print(cab1)
def echobin(a):#输出二进制
    print(bin(a)[2:])
def Calculators(a,b,co):#计算器
    # 检查输入类型
        if co=='+':
            d=a+b
            print(d)
        elif co=='-':
            d=a-b
            print(d)
        elif co=='*':
                d=a*b
                print(d)
        elif co=='/':
            if b == 0:
                raise ZeroDivisionError("不能用零做除数")
            else:
                d=a/b
                print(d)   
# 配置日志
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
def download_file(url, output_dir, filename):#下载文件部分
    """
    从指定的URL下载文件，并将其保存到指定的输出目录和文件名。
    """
    # 使用os.path.join来确保路径的正确性，不论在Windows还是Unix上
    output_path = os.path.join(output_dir, filename)
    
    try:
        response = requests.get(url, stream=True)  # 使用流模式下载大文件
        response.raise_for_status()  # 如果响应状态码不是200，就主动抛出异常
        
        # 确保输出目录存在
        os.makedirs(output_dir, exist_ok=True)
        
        # 打开文件以二进制写入模式
        with open(output_path, 'wb') as file:
            # 使用iter_content方法逐块读取内容，并写入文件
            for chunk in response.iter_content(chunk_size=8192):
                if chunk:  # 检查块是否为空，避免写入空块
                    file.write(chunk)
        
        logging.info(f'文件保存在 {output_path}')
        
    except requests.exceptions.RequestException as e:
        logging.error(f'下载错误: {e}')
    except IOError as e:
        logging.error(f'写入文件错误: {e}')
    except Exception as e:
        logging.error(f'未知错误: {e}')
def maketxt():#创建文本文件
    a=str(input("请输入保存文本的名字: "))
    try:
        with open(a, 'w') as f:
            f.write(a)
        print(f"成功创建"+a)
    except IOError:
        print("写入文件时出错")
def retxt():#读取文本文件
    readfile = input("要读取的文件名称: ")
    try:
        with open(readfile, 'r') as f:
            print(f.read())
            f.close()
    except FileNotFoundError:
        print("文件不存在")
def txt(filename=str, body=str):#写入文本文件
    try:
        with open(filename, 'a') as f:
            f.write(body)
        print(f"成功写入 {filename}.")
    except FileNotFoundError:
        print(f"文件不存在")
def rename(old_name, new_name):#重命名
    try:
        os.rename(old_name, new_name)
        print(f"成功把 '{old_name}' 改为 '{new_name}'.")
    except FileNotFoundError:
        print(f"指定的文件'{old_name}' 不存在.")
def makedir():#创建文件夹
    dirname = input("输入创建文件夹的名称")
    try:
        os.makedirs(dirname)
        print(f"'{dirname}' 已成功创建.")
    except OSError as e:
        print(f"目录创建 '{dirname}' 失败: {e}")
def remove():
    filename = input("输入要删除的文件/文件夹 ")
    try:
        os.remove(filename)
        print(f"{filename} 已成功删除.")
    except FileNotFoundError:
        print(f"指定的文件 '{filename}' 不存在")
# 示例用法
#url = 'http://example.com/somefile.zip'
#output_dir = 'downloads'  # 可以是相对路径或绝对路径
#filename = 'somefile.zip'
#download_file(url, output_dir, filename)
# 库部分（函数定义）保持不变
# ...
# 初始化变量以进入循环
running = True
a="0.0.0.2"
print("这是一个简单的工具箱")
print("本程序由haswell(Githud : leigong)制作")
print(a+"\n随机码\t"+str(random.randint(1,1000000)))
print("你好，用户.\n欢临你使用我的工具")
# 开始循环
while running:
    toolspower = str(input("/_ "))# 获取用户输入
    # 根据用户输入执行相应操作
    if toolspower == 'quit':
        print("关闭中\n再见!")
        running = False  # 设置条件为False以退出循环
    elif toolspower == 'help':
        print("time---显示时间\npower--计算a的b次方\npowerpuls--特殊的幂运算\nbin--二进制转换器\ncal\calculate--简单的计算器\nmktxt--创建新的文件\ntxt--编辑文件\nretxt--读取文件\ndownload\wget--下载文件\nmakedir--创建文件夹\nremove--删除文件/文件夹\nclear--清除上面的信息\nrename--重命名文件")
    elif toolspower == 'time':
        print(time.asctime(time.localtime(time.time())))
    elif toolspower == 'power':
        a = int(input("底数是: "))
        b = int(input("指数是: "))
        power(a, b)
    elif toolspower == 'powerpuls':
        a = int(input("底数是: "))
        b = int(input("最大指数是: "))
        powerpuls(a, b)
    elif toolspower == 'bin':
        a = int(input("要转换的数字是: "))
        echobin(a)
    elif toolspower == 'cal' or toolspower.lower() == 'calculator':
        a=int(input("这个计算器只能计算两个数\n第一个数是:"))
        b=int(input("第二个数是:"))
        co=str(input("运算符是(+,-,*,/):"))
        Calculators(a,b,co)
    elif toolspower == 'download' or toolspower.lower() == 'wget':
        url = input("下载链接: ")
        output_path = input("文件下载到什么地方(如d): ")
        filename = input("要下载文件的名字是(带后缀名): ")
        download_file(url, output_path, filename)
    elif toolspower == 'maketxt':
        maketxt()
    elif toolspower == 'retxt':
        retxt()
    elif toolspower == 'txt':
        filename=str(input("要写入的文件是:"))
        body=str(input("内容是:"))
        txt(filename, body)
    elif toolspower == 'rename':
        old_name = input("输入文件的旧名称: ")
        new_name = input("输入文件的新名称: ")
        rename(old_name, new_name)
    elif toolspower == 'makedir':
        makedir()
    elif toolspower == 'remove':
        remove()
    elif toolspower == 'clear':
        os.system('cls')
    else:
        print("未知命令，请重新输入.")