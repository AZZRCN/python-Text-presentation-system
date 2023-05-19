import tkinter as tk
from os import listdir
from os import chdir
from tkinter.filedialog import askdirectory
from tkinter.messagebox import showerror
main = tk.Tk()
main.attributes("-fullscreen",True)
namelist=[]
def Esc():
    global text
    text.destroy()
    text = tk.Text(master=main,width=200)
text = tk.Text(master=main,width=200)
def newpathc():
    global path
    path = askdirectory()
    for i in namelist:
        i.destory()
    frush(path)
newpath = tk.Button(master=main,text="NEW PATH",fg="orange",command=newpathc)
newpath.grid(column=0,row=0)
num = 1
def tkopen(filename):
    f = 0
    try:
        f = open(filename, encoding="utf-8")
    except BaseException:
        try:
            f = open(filename, encoding="gbk")
        except BaseException:
            try:
                f = open(filename, encoding="gb2312")
            except BaseException:
                try:
                    f = open(filename, encoding="Unicode")
                except BaseException:
                    try:
                        f = open(filename, encoding="ANSI")
                    except BaseException:
                        try:
                            f = open(filename, encoding="USC2")
                        except BaseException:
                            try:
                                f = open(filename, encoding="UTF16")
                            except BaseException:
                                showerror(title="错误!",message="这个文件可能不是正规txt?")
                                return
    global text
    text.grid(column=1,row=0,rowspan=num)
    text.insert('1.0', str(f.read()))
    f.close()

def frush(path):
    global main
    chdir(path)
    list_a = listdir()
    global num
    for i in list_a:
        if (len(i) < 4):

            continue
        if (i[-4:-1] + i[-1] == ".txt"):  # and i[0:3] == "演示-"
            print(i)
            exec("temp"+str(num)+" = tk.Button(master=main, text=\""+i +"\",command=lambda:tkopen(\""+i+"\"))\n\
                 temp"+str(num)+".grid(row="+str(num)+", column=0)\n\
                 global namelist\n\
                 namelist.append(temp)")
            num += 1

path = askdirectory()
if path != "":frush(path)
main.update()
h=main.winfo_height()
w=main.winfo_width()
main.mainloop()