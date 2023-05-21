import tkinter as tk
from os import listdir,chdir
from tkinter.filedialog import askdirectory
main = tk.Tk()
buttonlist, howmanybuttonsarow = [], 5
main.attributes("-fullscreen", True)
main.update()
def newpathc():
    for i in buttonlist:
        i.destroy()
    frush(askdirectory())
tk.Button(master=main, text="选取新路径",command=newpathc).grid(column=0, row=0)
def tkopen(filename):
    text.delete('1.0', 'end')
    try:
        text.insert('1.0', str(open(filename, encoding='utf-8').read()))
    except BaseException:
        text.insert('1.0', str(open(filename, encoding='gbk').read()))
def frush(path):
    chdir(path)
    num = 0
    for i in listdir():
        if (i[-4:-1] + i[-1] == ".cpp" or i[-4:-1] + i[-1] == ".txt" or i[-3:-1] + i[-1] == ".py"):
            exec("temp"+str(num)+" = tk.Button(master=main, text=\""+i + "\",font=(\"等线\",10),command=lambda:tkopen(\""+i+"\"))\ntemp" +str(num)+".grid(column="+str(num % howmanybuttonsarow)+",row="+str(int(num/howmanybuttonsarow)+1)+")\nglobal buttonlist\nbuttonlist.append(temp" + str(num) + ")")
            num += 1
frush(askdirectory())
text = tk.Text(master=main, height=50)
text.grid(column=howmanybuttonsarow, row=0, rowspan=len(listdir()), sticky='n')
main.mainloop()