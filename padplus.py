import os
import shutil
import tkinter 
from tkinter import messagebox
import tkinter.font as tkfont
from random import randint

fontsize=10

top = tkinter.Tk()
top.geometry("630x500")
top.title("PlusPad")
s=tkinter.Scrollbar(top)
t=tkinter.Text(top,height=100,width=100)

t.insert("1.0","Enter name of your file with extention in next line")
t.tag_add("start", '1.0', '1.60')
t.tag_config("start",foreground="red")
t.configure(font=("", 20))

menubar=tkinter.Menu(top)

def save():
    fname = t.get('2.0','2.20') 
    f1 = open("F:/desktop/Practice/py/Project/2/Notes/"+fname, "w")
    thetext = t.get('3.0', 'end')
    
    f1.write(thetext)
    f1.close()
    # print(thetext)
    messagebox.showinfo("Save","Done Sucessfully")

def new():
    t.delete('2.0','end')
    # f2 = open("C:/Users/hp/Desktop/Practice/py/Project/2/Notes/myfile(2).txt", "w")
    # thetext = t.get('1.0', 'end')
    # f2.write(thetext)
    # f2.close()


def clear():
    t.delete('3.0','end')

def font():
    def arial():
        t.configure(font=("Arial", 25))

    def Bradley_Hand_ITC():
        t.configure(font=("Bradley Hand ITC", 25))
    
    def Algerian():
        t.configure(font=("Algerian", 25))

    def Comic_Sans_MS():
        t.configure(font=("Comic Sans MS", 25))

    def Monotype_Corsiva():
        t.configure(font=("Monotype Corsiva", 25))

    def Times_New_Roman():
        t.configure(font=("Times New Roman", 25))


    item2=tkinter.Menu(menubar,tearoff=0)
    item2.add_command(label="Algerian",command=Algerian)
    item2.add_command(label="Arial",command=arial)
    item2.add_command(label="Bradley Hand ITC",command=Bradley_Hand_ITC)
    item2.add_command(label="Comic Sans MS",command=Comic_Sans_MS)
    item2.add_command(label="Monotype Corsiva",command=Monotype_Corsiva)
    item2.add_command(label="Times New Roman",command=Times_New_Roman)
    

    menubar.add_cascade(label="Font",menu=item2)


def size():
    def _10():
        fontsize=10
        t.configure(font=("", fontsize))

    def _15():
        fontsize=15
        t.configure(font=("", fontsize))
    
    def _20():
        fontsize=20
        t.configure(font=("", fontsize))

    def _25():
        fontsize=25
        t.configure(font=("", fontsize))

    def _30():
        fontsize=30
        t.configure(font=("", fontsize))

    def _40():
        fontsize=40
        t.configure(font=("", fontsize))

    def _50():
        fontsize=70
        t.configure(font=("", fontsize))


    item2=tkinter.Menu(menubar,tearoff=0)
    item2.add_command(label="10",command=_10)
    item2.add_command(label="15",command=_15)
    item2.add_command(label="20",command=_20)
    item2.add_command(label="25",command=_25)
    item2.add_command(label="30",command=_30)
    item2.add_command(label="40",command=_40)
    item2.add_command(label="50",command=_50)
    

    menubar.add_cascade(label="Font Size",menu=item2)


def color():
    def violet():
        t.tag_add("start", '2.0', 'end')
        t.tag_config("start",foreground="violet")

    def indigo():
        t.tag_add("start", '2.0', 'end')
        t.tag_config("start",foreground="indigo")
    
    def blue():
        t.tag_add("start", '2.0', 'end')
        t.tag_config("start",foreground="blue")

    def green():
        t.tag_add("start", '2.0', 'end')
        t.tag_config("start",foreground="green")

    def yellow():
        t.tag_add("start", '2.0', 'end')
        t.tag_config("start",foreground="yellow")

    def orange():
        t.tag_add("start", '2.0', 'end')
        t.tag_config("start",foreground="orange")

    def red():
        t.tag_add("start", '2.0', 'end')
        t.tag_config("start",foreground="red")


    item2=tkinter.Menu(menubar,tearoff=0)
    item2.add_command(label="Violet",command=violet)
    item2.add_command(label="Indigo",command=indigo)
    item2.add_command(label="Blue",command=blue)
    item2.add_command(label="Green",command=green)
    item2.add_command(label="Yellow",command=yellow)
    item2.add_command(label="Orange",command=orange)
    item2.add_command(label="Red",command=red)
    

    menubar.add_cascade(label="Color",menu=item2)

    

# os.mkdir("C:/Users/hp/Desktop/Practice/py/Project/2/Notes")

item1=tkinter.Menu(menubar,tearoff=0)
item1.add_command(label="New File",command=new)
item1.add_command(label="Save",command=save)
item1.add_command(label="Clear",command=clear)
item1.add_separator()
item1.add_command(label="Exit",command=quit)



menubar.add_cascade(label="File",menu=item1)
font()
size()
color()

top.config(menu=menubar)

# def text():
#     f1 = open("C:/Users/hp/Desktop/Practice/py/Project/2/Notes/myfile.txt", "w")
#     thetext = t.get('1.0', 'end')
#     f1.write(thetext)
#     f1.close()

# def html():
#     f1 = open("C:/Users/hp/Desktop/Practice/py/Project/2/Notes/myfile.html", "w")
#     thetext = t.get('1.0', 'end')
#     f1.write(thetext)
#     f1.close()

# c1=tkinter.Checkbutton(top,text='Text File',command=text)
# c2=tkinter.Checkbutton(top,text='HTML File',command=html)
    
# # print(thetext)
# c1.pack()
# c2.pack()

s.pack(side=tkinter.RIGHT, fill=tkinter.Y)
t.pack(side=tkinter.LEFT, fill=tkinter.Y)
s.config(command=t.yview)
t.config(yscrollcommand=s.set)

top.mainloop()