import tkinter as tk
from os import listdir
from os import chdir
from tkinter.filedialog import askdirectory
from tkinter.messagebox import showerror
main = tk.Tk()
main.attributes("-fullscreen",True)
main.update()
h,w=main.winfo_height(),main.winfo_width()
buttonlist=[]
text = tk.Text(master=main)
num = 1
def newpathc():
    for i in buttonlist:
        i.destroy()
    frush(askdirectory())
tk.Button(master=main,text="NEW PATH",fg="orange",command=newpathc).grid(column=0,row=0)
def tkopen(filename):
    text.delete('1.0','end')
    for i in ["utf-8", "gbk","gb2312","ANSI","UTF16"]:
        try:
            text.insert('1.0', str(open(filename, encoding=i).read()))
        except BaseException:
            continue
        else:
            break
    if(text.get('1.0','end') == ""):showerror(title="错误!",message="这个文件可能不是正规txt?")
def frush(path):
    global main
    chdir(path)
    global num
    for i in listdir():
        if (i[-4:-1] + i[-1] == ".txt" or i[-3:-1] + i[-1] == ".py"):
            exec("temp"+str(num)+" = tk.Button(master=main, text=\""+i +"\",font=(\"等线\",10),command=lambda:tkopen(\""+i+"\"))\ntemp"+str(num)+".grid(column=0,row="+str(num)+")\nglobal buttonlist\nbuttonlist.append(temp" + str(num) + ")")
            num += 1
frush(askdirectory())
text.grid(column=1,row=0,rowspan=num+1)
main.mainloop()