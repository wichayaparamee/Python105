from tkinter import *
from tkinter import ttk
from tkinter import messagebox

GUI = Tk()
GUI.title('โปรแกรมเตรียมตัวรายวัน')
GUI.geometry('600x800')

L1 = Label(GUI,text='การเตรียมตัวรายวัน',font=('Angsana New',26),fg='green')
L1.pack()

def Button1():
    text='run 7 km'
    messagebox.showinfo('programe',text)


FB1=LabelFrame(GUI,text='normal')
FB1.place(x=10,y=50)
B1 = ttk.Button(FB1,text='วันจันทร์',command=Button1) # หากใช้ ttk จะไม่สามารถกำหนดลักษณะ font ได้ 

B1.pack(ipadx=40,ipady=10)

def Button2():
    text='run 10 km'
    messagebox.showinfo('programe',text)

FB2=LabelFrame(GUI,text='normal')
FB2.place(x=10,y=150)
B2 = Button(FB2,text='วันอังคาร',font=('Angsana New',20),fg='pink',command=Button2)
B2.pack(ipadx=40,ipady=10)

def Button3():
    text='run 5 km'
    messagebox.showinfo('programe',text)
    
FB3=LabelFrame(GUI,text='normal')
FB3.place(x=10,y=250)
B3 = Button(FB3,text='วันพุธ',font=('Angsana New',20),fg='green',command=Button3)
B3.pack(ipadx=40,ipady=10)

FB4=LabelFrame(GUI,text='rest')
FB4.place(x=10,y=350)
B4 = Button(FB4,text='วันศุกร์นะ แก้ไข',font=('Angsana New',20),fg='orange')
B4.pack(ipadx=40,ipady=10)
