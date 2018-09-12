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
