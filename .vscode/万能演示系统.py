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
        i.destroy()
    frush(path)
newpath = tk.Button(master=main,text="NEW PATH",fg="orange",command=newpathc)
newpath.grid(column=0,row=0)
num = 1

def tkopen(filename):
    f = 0
    encodinglist=["utf-8", "gbk","gb2312","ANSI","UTF16"]
    for i in encodinglist:
        try:
            f = open(filename, encoding=i)
        except BaseException:
            continue
        else:
            break
    try:
        f.read()
    except BaseException:
         showerror(title="错误!",message="这个文件可能不是正规txt?")
         return
    f.seek(0)
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
            exec("temp"+str(num)+" = tk.Button(master=main, text=\""+i +"\",command=lambda:tkopen(\""+i+"\"))\ntemp"+str(num)+".grid(column=0,row="+str(num)+")\nglobal namelist\nnamelist.append(temp" + str(num) + ")")
            num += 1

path = askdirectory()
if path != "":frush(path)
main.update()
h=main.winfo_height()
w=main.winfo_width()
main.mainloop()