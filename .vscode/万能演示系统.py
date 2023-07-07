import tkinter as tk
from tkinter.scrolledtext import ScrolledText
from os import listdir,chdir
from tkinter.filedialog import askdirectory
main = tk.Tk()
howmanybuttonsarow = 5
buttonlist:list[tk.Button] =[]
main.attributes("-fullscreen", True)
main.update()
def clean():
    text.delete('1.0','end')
tk.Button(master=main,text="清除",command=clean).grid(column=1,row=0)
def newpathc():
    t =  len(buttonlist)
    for i in range(0,t):
        buttonlist[t-1-i].destroy()
        del buttonlist[t-1-i]
    main.update()
    frush(askdirectory())
    clean()
tk.Button(master=main, text="选取新路径",command=newpathc).grid(column=0, row=0)
def tkopen(filename):
    clean()
    print(filename)
    try:
        text.insert('1.0', open(filename, encoding='utf-8').read())
    except BaseException:
        try:
            text.insert('1.0', str(open(filename, encoding='gbk').read()))
        except BaseException:
            text.insert('1.0', str(open(filename, encoding='utf16').read()))
def frush(path):
    chdir(path)
    print(path)
    num = 0
    nowlinestr = 0
    dili = listdir()
    for i in dili:
        if (i[-4:-1] + i[-1] == ".cpp" or i[-4:-1] + i[-1] == ".txt" or i[-3:-1] + i[-1] == ".py"):
            buttonlist.append(tk.Button(master=main, text=i,font=("system",10),command=lambda x=i:tkopen(x)))
            buttonlist[num].grid(column=num % 5,row=int(num/5)+2)
            num += 1
text = ScrolledText(master=main,width=int(main.winfo_screenwidth() / 7.1))#,height=round(main.winfo_screenheight()/13.1)
text.grid(column=0, row=1, sticky='n',columnspan=5)#len(listdir())
frush(askdirectory())
tk.Button(main,text="exit",command=exit).grid(column=2,row=0)
main.mainloop()