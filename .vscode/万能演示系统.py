import tkinter as tk
from os import listdir
from tkinter.messagebox import showerror
main = tk.Tk()


def tkopen(filename):
    
    t = tk.Toplevel()
    def Esc(event):
        if (event.keycode == 27):  # Esc
            t.destroy()
    t.bind("<Key>", Esc)
    t.attributes("-fullscreen",True)
    text = tk.Text(master=t)
    text.grid(column=0, row=0)
    escbutton = tk.Button(master=t, width=50,height=50,text="Esc")
    escbutton.grid(column=0, row=0)
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
    cur = 0
    for i in list_a:
        if (len(i) < 4):

            continue
        if (i[-4:-1] + i[-1] == ".txt"):  # and i[0:3] == "演示-"
            print(i)
            exec("temp"+str(cur)+" = tk.Button(master=main, text=\""+i +
                 "\",command=lambda:tkopen(\""+i+"\"))\ntemp"+str(cur)+".grid(row="+str(cur)+", column=0)")
            cur += 1


#frush()
main.attributes("-fullscreen",True)
main.update()
print(main.winfo_height)
print(main.winfo_width)
#main.mainloop()