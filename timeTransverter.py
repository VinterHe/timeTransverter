from tkinter import *
from time import *
import win32clipboard as wincld
import win32con

'''
1、这个程序实现时间戳和日期格式的相互转换。
2、使用grid方法按照表格方式对组件位置进行安排
3、通过Button按钮进行转换和刷新操作。
4、通过Entry来获取用户输入。
'''
class timeTransverter:
    def __init__(self):
        self.tk = Tk()
        self.tk.title('时间戳转换')
        self.tk.resizable(0,0)#禁止拉伸
        self.ts1 = StringVar()
        self.date1 = StringVar()
        self.ts2 = StringVar()
        self.date2 = StringVar()
        self.initData()
        # self.timeToDateButton = ''
        # self.dateToTimeButton = ''
        # self.copyButton = ''
        # self.pasteButton = ''
        # self.exitButton = ''
        self.e3 = Entry(self.tk, textvariable=self.date2)  # Entry 是 Tkinter 用来接收字符串等输入的控件.
        self.e4 = Entry(self.tk, textvariable=self.ts2)
        self.e1 = Entry(self.tk, textvariable=self.ts1)  # Entry 是 Tkinter 用来接收字符串等输入的控件.
        self.e2 = Entry(self.tk, textvariable=self.date1)

        # 设置窗口初始显示位置
        sw = self.tk.winfo_screenwidth()
        sh = self.tk.winfo_screenheight()
        x = (sw) / 2
        y = (sh) / 2
        self.tk.geometry("+%d+%d" % (x, y))

    def initData(self):
        # 对数据进行初始化
        self.ts1.set(int(time()))
        # 对数据进行初始化
        timeArray1 = localtime(int(time()))
        self.date2.set(strftime("%Y-%m-%d %H:%M:%S", timeArray1))
        self.ts2.set(int(time()))

    def run(self):
        self.drawStampToDate()
        self.drawDateToStamp()
        self.drawButtons()

        self.tk.mainloop()

    def drawStampToDate(self):
        stampLabel = Label(self.tk, text = '时间戳')
        dateLabel = Label(self.tk, text = '日期')
        stampLabel.grid(row=0,column=0);
        dateLabel.grid(row=1,column=0);
        self.e1.grid(row=0, column=1, columnspan=2, padx=20, pady=5)  # 设置输入框显示的位置，以及长和宽属性
        self.e2.grid(row=1, column=1, columnspan=2, padx=20, pady=5)

        #调用转换功能
        self.stampToDate()

    def drawDateToStamp(self):
        dateLabel = Label(self.tk, text='日期:').grid(row=3, column=0)
        stampLabel = Label(self.tk, text='时间戳:').grid(row=4, column=0)
        self.e3.grid(row=3, column=1, columnspan=2, padx=20, pady=5)  # 设置输入框显示的位置，以及长和宽属性
        self.e4.grid(row=4, column=1, columnspan=2, padx=20, pady=5)
        #调用转换功能
        self.dateToStamp()
    def drawButtons(self):
        Button(self.tk, text='转换', width=8, command=self.stampToDate) \
            .grid(row=2, column=0, sticky=W, padx=8, pady=5)
        Button(self.tk, text=' 粘贴时间戳 ', width=8, command=self.paste) \
            .grid(row=2, column=2, sticky=W, padx=8, pady=5)
        Button(self.tk, text='转换', width=8, command=self.dateToStamp) \
            .grid(row=5, column=0, sticky=W, padx=8, pady=5)
        Button(self.tk, text='刷新', width=8, command=self.refresh) \
            .grid(row=5, column=1, sticky=W, padx=8, pady=5)
        Button(self.tk, text=' 复制时间戳 ', width=8, command=self.copy) \
            .grid(row=5, column=2, sticky=W, padx=8, pady=5)
        Button(self.tk, text='退出', width=8, command=self.tk.quit) \
            .grid(row=6, column=2, sticky=W, padx=8, pady=5)

    def stampToDate(self):
        timeArray = localtime(int(self.ts1.get()))
        self.date1.set(strftime("%Y-%m-%d %H:%M:%S", timeArray))

    def dateToStamp(self):
        self.ts2.set(int(mktime(strptime(self.e3.get(), "%Y-%m-%d %H:%M:%S"))))

    def refresh(self):
        timeArray1 = localtime(int(time()))
        self.date2.set(strftime("%Y-%m-%d %H:%M:%S", timeArray1))
        self.ts2.set(int(time()))

    # 复制时间戳
    def copy(self):
        wincld.OpenClipboard()
        wincld.EmptyClipboard()
        wincld.SetClipboardData(win32con.CF_UNICODETEXT, self.e4.get())
        wincld.CloseClipboard()

    # 粘贴时间戳
    def paste(self):
        wincld.OpenClipboard()
        text_result = wincld.GetClipboardData(win32con.CF_UNICODETEXT)
        wincld.CloseClipboard()
        self.ts1.set(int(text_result))

t = timeTransverter()
t.run()
