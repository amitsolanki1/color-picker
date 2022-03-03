from tkinter import *

root =Tk()
root.title("Color Pickker")
root.geometry("380x200")

def change(value):
    R=s1.get()
    G=s2.get()  
    B=s3.get()
    # print(R,G,B)
    hexcol ="#%02x%02x%02x" % (R,G,B)
    # print(hexcol)
    textstore.set(hexcol)

    colorlabel=Label(root,text="",bg=hexcol).place(x=160,y=0,width=190,height=110)

    # colorlabel.config(bg=hexcol)
   

Label(root,text="R",fg="red").place(x=0)
s1=Scale(root,from_=0,to=255,orient=HORIZONTAL,command=change)
s1.place(x=10,y=10)
a=s1.get()
Label(root,text="G",fg="green").place(x=0,y=50)
s2=Scale(root,from_=0,to=255,orient=HORIZONTAL,command=change)
b=s2.place(x=10,y=50)
b=s2.get()
Label(root,text="B",fg="blue").place(x=0,y=90)
s3=Scale(root,from_=0,to=255,orient=HORIZONTAL,command=change)

s3.place(x=10,y=100)
c=s3.get()
colorlabel=Label(root,text="",bg="black").place(x=160,y=0,width=190,height=110)

def pickhex():
    import pyperclip as pc
    a=textstore.get()
    pc.copy(a)
    print(a)
    
  
f=Frame(root,bd=2,relief=SUNKEN).pack(pady=55)
Label(f,text="HEX COLOR",font="arial 10 bold").pack(padx=0,pady=10)
textstore=StringVar()
e=Entry(f,textvar=textstore,font="arial 15 bold",width=10).place(x=240,y=120)
textstore.set('#000000')
Button(f,text="Pick",command=pickhex).pack(padx=10)

root.mainloop()