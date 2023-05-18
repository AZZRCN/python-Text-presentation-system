import tkinter as tk
from os import listdir
from tkinter.messagebox import showerror
main = tk.Tk()

num = 0
def tkopen(filename):
    def Esc():
        text.destroy()
        escbutton.destroy()
    try:
        text.destroy()
        escbutton.destroy()
    except BaseException:
        None
    text = tk.Text(master=main,width=200)
    text.grid(column=1, row=0,rowspan=num)
    escbutton = tk.Button(master=main,text="ESC",command=Esc)
    escbutton.grid(column=0, row=num+1)
    try:
        with open(filename, encoding="utf-8") as f:
            text.insert('1.0', str(f.read()))
    except BaseException:
        try:
            with open(filename, encoding="gbk") as f:
                text.insert('1.0', str(f.read()))
        except BaseException:
            try:
                with open(filename, encoding="gb2312") as f:
                    text.insert('1.0', str(f.read()))
            except BaseException:
                try:
                    with open(filename, encoding="Unicode") as f:
                        text.insert('1.0', str(f.read()))
                except BaseException:
                    showerror(title="错误!",message="这个文件编码不太常见!")
    print(f)
    


def frush():
    global main
    list_a = listdir()
    global num
    for i in list_a:
        if (len(i) < 4):

            continue
        if (i[-4:-1] + i[-1] == ".txt"):  # and i[0:3] == "演示-"
            print(i)
            exec("temp"+str(num)+" = tk.Button(master=main, text=\""+i +
                 "\",command=lambda:tkopen(\""+i+"\"))\ntemp"+str(num)+".grid(row="+str(num)+", column=0)")
            num += 1


frush()
main.attributes("-fullscreen",True)
main.update()
h=main.winfo_height()
w=main.winfo_width()
main.mainloop()