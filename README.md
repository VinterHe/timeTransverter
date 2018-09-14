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
