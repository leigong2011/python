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
import requests

import logging

# 配置日志
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

import requests
import logging
import os

# 配置日志
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def download_file(url, output_dir, filename):
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
        
        logging.info(f'文件下载完成，已保存到 {output_path}')
        
    except requests.exceptions.RequestException as e:
        logging.error(f'下载文件时发生错误: {e}')
    except IOError as e:
        logging.error(f'写入文件时发生错误: {e}')
    except Exception as e:
        logging.error(f'发生未知错误: {e}')
def maketxt():
    a=str(input("Please enter the text you want to save: "))
    with open('text.txt', 'a') as f:
        f.close()
def retxt()



# 示例用法
url = 'http://example.com/somefile.zip'
output_dir = 'downloads'  # 可以是相对路径或绝对路径
filename = 'somefile.zip'
download_file(url, output_dir, filename)

import platform
import os


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
    toolspower = str(input("/_ "))
    if toolspower == 'quit':
        print("Exiting the shell.")
        running = False  # 设置条件为False以退出循环
    elif toolspower == 'help':
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
    elif toolspower == 'download' or toolspower.lower() == 'wget':
        url = input("Enter the URL of the file to be downloaded: ")
        output_path = input("Enter the path where the file should be saved: ")
        filename = input("Enter the name of the file to be saved: ")
        download_file(url, output_path, filename)
    
    else:
        print("Unknown command. Please try again.")