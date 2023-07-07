import tkinter as tk
from tkinter.scrolledtext import ScrolledText
from os import listdir,chdir
from tkinter.filedialog import askdirectory
from PIL import Image, ImageTk
main = tk.Tk()
howmanybuttonsarow = 5
buttonlist:list[tk.Button] =[]
main.attributes("-fullscreen", True)
main.update()
canva = tk.Canvas(main,width=main.winfo_screenwidth(),height=main.winfo_screenheight())
canva.grid(row=0, column=0, sticky=tk.NSEW,columnspan=howmanybuttonsarow+2,rowspan=100)
img = Image.open(fp="C:\\Users\\86156\\Documents\\GitHub\\python-Text-presentation-system\\.vscode\\view.png")
img = img.resize((main.winfo_screenwidth(), main.winfo_screenheight()), Image.LANCZOS)
img_tk = ImageTk.PhotoImage(img)
canva.create_image(0, 0, image=img_tk, anchor="nw")
background = tk.PhotoImage("view.png")
def clean():
    text.delete('1.0','end')
tk.Button(master=main,text="清除",command=clean).grid(column=1,row=0)
def newpathc():
    for i in buttonlist:i.destroy()
    frush(askdirectory())
    clean()
tk.Button(master=main, text="选取新路径",command=newpathc).grid(column=0, row=0)
def tkopen(filename):
    text.delete('1.0', 'end')
    try:text.insert('1.0', str(open(filename, encoding='utf-8').read()))
    except BaseException:
        try:text.insert('1.0', str(open(filename, encoding='gbk').read()))
        except BaseException:text.insert('1.0', str(open(filename, encoding='utf16').read()))
def frush(path):
    chdir(path)
    num = 0
    for i in listdir():
        if (i[-4:-1] + i[-1] == ".cpp" or i[-4:-1] + i[-1] == ".txt" or i[-3:-1] + i[-1] == ".py"):
            exec(f"temp{num} = tk.Button(master=main, text=\"{i}\",font=(\"等线\",10),command=lambda:tkopen(\"{i}\"))\ntemp{num}.grid(column={num % howmanybuttonsarow},row={int(num/howmanybuttonsarow)+1})\nglobal buttonlist\nbuttonlist.append(temp{num})")
            num += 1
#def chmbar():
#    top = tk.Toplevel(main)
#    entry = tk.Entry(top)
#    entry.grid(column=0, row=0)
    
text = ScrolledText(master=main,height=round(main.winfo_screenheight()/13.1))
frush(askdirectory())
text.grid(column=howmanybuttonsarow, row=0, rowspan=99, sticky='n')#len(listdir())
tk.Button(main,text="exit",command=exit).grid(column=2,row=0)
#tk.Button(main,text="更新行数",command=chmbar).grid(column=howmanybuttonsarow+1,row=2)
main.mainloop()