from tkinter import *
root =Tk()
root.geometry("500x500")
root['background']='turquoise'
root.title("Vashish Raja")
l1=Label(root,font=("Calibri",26,"bold"),text="Calculator",bg='turquoise')
l1.pack()
l2=Label(root,bg='turquoise')
l2.pack()

ex =""
def click (num):
    global ex
    ex = ex+ str(num)
    var.set(ex)

var= StringVar()
var1= StringVar()
def clr():
    global ex
    ex=""
    var.set(ex)

def eq():
    global ex
    var1.set(eval(ex))

f1= Frame(root)
f1.pack()
e1=Entry(f1,font=("Calibri",34,"bold"),textvariable=var)
e1.pack()

f2=Frame(root)
f2.pack()
b1=Button(f2,text="C",width=23,font=("Calibri",18,"bold"),bg='orange',command=clr)
b1.pack(side=LEFT)
b2=Button(f2,text="/",width=11,font=("Calibri",18,"bold"),bg='orange',command= lambda:click("/"))
b2.pack(side=LEFT)

f7=Frame(root)
f7.pack()
b15=Button(f7,text="=",width=23,font=("Calibri",18,"bold"),bg='green',command= eq)
b15.pack(side=LEFT)
b16=Button(f7,text="%",width=11,font=("Calibri",18,"bold"),bg='green',command= lambda:click("%"))
b16.pack(side=LEFT)


f3=Frame(root)
f3.pack()
b3=Button(f3,text="+",width=11,font=("Calibri",18,"bold"),bg='yellow',command= lambda:click("+"))
b3.pack(side=LEFT)
b4=Button(f3,text="-",width=11,font=("Calibri",18,"bold"),bg='yellow',command= lambda:click("-"))
b4.pack(side=LEFT)
b5=Button(f3,text="x",width=11,font=("Calibri",18,"bold"),bg='yellow',command= lambda:click("*"))
b5.pack(side=LEFT)

f4=Frame(root)
f4.pack()
b6=Button(f4,text="1",width=11,font=("Calibri",18,"bold"),bg='pink',command= lambda:click("1"))
b6.pack(side=LEFT)
b7=Button(f4,text="2",width=11,font=("Calibri",18,"bold"),bg='pink',command= lambda:click("2"))
b7.pack(side=LEFT)
b8=Button(f4,text="3",width=11,font=("Calibri",18,"bold"),bg='pink',command= lambda:click("3"))
b8.pack(side=LEFT)


f5=Frame(root)
f5.pack()
b9=Button(f5,text="4",width=11,font=("Calibri",18,"bold"),bg='blue',command= lambda:click("4"))
b9.pack(side=LEFT)
b10=Button(f5,text="5",width=11,font=("Calibri",18,"bold"),bg='blue',command= lambda:click("5"))
b10.pack(side=LEFT)
b11=Button(f5,text="6",width=11,font=("Calibri",18,"bold"),bg='blue',command= lambda:click("6"))
b11.pack(side=LEFT)

f6=Frame(root)
f6.pack()
b12=Button(f6,text="7",width=11,font=("Calibri",18,"bold"),bg='red',command= lambda:click("7"))
b12.pack(side=LEFT)
b13=Button(f6,text="8",width=11,font=("Calibri",18,"bold"),bg='red',command= lambda:click("8"))
b13.pack(side=LEFT)
b14=Button(f6,text="9",width=11,font=("Calibri",18,"bold"),bg='red',command= lambda:click("9"))
b14.pack(side=LEFT)

f8=Frame(root)
f8.pack()
e2=Entry(f8,font=("Calibri",34,"bold"),textvariable=var1)
e2.pack()

root.mainloop()