# timeTransverter
a tool can converts timestamps and dates
# 使用python制作时间戳转换工具 exe文件在bin目录下



python 时间戳转日期 日期转时间戳

---

> 前言：作为一个程序员一般情况下，json和时间戳是常用的两个工具，我咨询过很多个朋友，他们一般都是通过在线工具对json进行格式化，或者查询时间戳。这个方式也是我之前的使用方式，此种方式不足之处如下：
1.每次打开过程步骤繁琐，即使收藏了也要先打开浏览器，然后点击
2.如果打开的浏览器标签足够多的话，根本找不到（就是说的我这样的人）
3.等
后来我发现了hijson这个工具可以本地格式化json后，一直想找一个本地查找时间戳的小工具。奈何互联网大神们没有满足我的需求。于是我决定自己写一个。

##本文的环境

 - python 3.6
 - time 库
 - tkinter 库

 > 可选：可以使用pyinstaller打包成exe文件运行。程序大小大约8m，运行时内存占用15m左右。

先贴代码（因为时间有限，没有写的太工整，见谅）：

```python 

from tkinter import *
from time import *

'''
1、这个程序实现时间戳和日期格式的相互转换。
2、使用grid方法按照表格方式对组件位置进行安排
3、通过Button按钮进行转换和刷新操作。
4、通过Entry来获取用户输入。
'''
root = Tk()
root.title('时间戳转换')
root.resizable(0,0)#禁止拉伸 会变丑
# 对变量进行创建，和数据初始化
Label1 = Label(root, text='时间戳:').grid(row=0, column=0)
Label2 = Label(root, text='日期:').grid(row=1, column=0)
v1 = StringVar()
p1 = StringVar()
v1.set(int(time()))

Label3 = Label(root, text='日期:').grid(row=3, column=0)
Label4 = Label(root, text='时间戳').grid(row=4, column=0)
v2 = StringVar()
p2 = StringVar()
timeArray1 = localtime(int(time()))
v2.set(strftime("%Y-%m-%d %H:%M:%S", timeArray1))
p2.set(int(time()))
#时间戳转换成日期
def trans1():

    e1 = Entry(root, textvariable=v1)  # Entry 是 Tkinter 用来接收字符串等输入的控件.
    e2 = Entry(root, textvariable=p1)
    e1.grid(row=0, column=1, padx=10, pady=5)  # 设置输入框显示的位置，以及长和宽属性
    e2.grid(row=1, column=1, padx=10, pady=5)

    timeArray = localtime(int(e1.get()))
    p1.set(strftime("%Y-%m-%d %H:%M:%S", timeArray))
#日期转换为时间戳
def trans2():
    e3 = Entry(root, textvariable=v2)  # Entry 是 Tkinter 用来接收字符串等输入的控件.
    e4 = Entry(root, textvariable=p2)
    e3.grid(row=3, column=1, padx=10, pady=5)  # 设置输入框显示的位置，以及长和宽属性
    e4.grid(row=4, column=1, padx=10, pady=5)
    p2.set(int(mktime(strptime(e3.get(), "%Y-%m-%d %H:%M:%S"))))
#刷新第二个模组
def refresh():
    timeArray1 = localtime(int(time()))
    v2.set(strftime("%Y-%m-%d %H:%M:%S", timeArray1))
    p2.set(int(time()))



Button(root, text='转换', width=10, command=trans1) \
    .grid(row=2, column=0, sticky=W, padx=10, pady=5)
Button(root, text='转换', width=10, command=trans2) \
    .grid(row=5, column=0, sticky=W, padx=10, pady=5)
Button(root, text='刷新', width=10, command=refresh) \
    .grid(row=5, column=1, sticky=W, padx=10, pady=5)
Button(root, text='退出', width=10, command=root.quit) \
    .grid(row=6, column=1, sticky=E, padx=10, pady=5)
trans1()
trans2()
#设置窗口初始显示位置
sw = root.winfo_screenwidth()
sh = root.winfo_screenheight()
x = (sw) / 2
y = (sh) / 2
root.geometry("+%d+%d" %(x,y))
mainloop()


```

我一直信奉代码写的足够好不需要额外的太多解释。请看上面代码中的注释

## pyinstaller的安装和使用

### 安装

```python
pip install pyinsatller

#安装直接运行一下如下命令
pyinstaller
#如果能运行会提示选项
```

### 打包文件

```python
#打包的命令（在命令行中运行，如果不成功记得配置好环境变量）
pyinsatller -F -w D:\python\timeTran.py 
#选项介绍
#-F –onefile	产生一个文件用于部署 (参见XXXXX).
#-w,–windowed,–noconsole 使用Windows子系统执行.当程序启动的时候不会打开命令行(只对Windows有效) 
#						 就是不会显示一个黑窗口（太丑了，还要手动去关闭）如果不知道什么意思，可以自己去试试

```

生成成功后提示中会有一条INFO: Appending archive to EXE C:\Users\XXX\dist\timeTransverter.exe，里面放着你想要的exe文件。欢迎大家转载和使用，谢谢。
