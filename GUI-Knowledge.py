from tkinter import *
from tkinter import ttk # theme of Tk
from tkinter import messagebox

GUI = Tk()
GUI.title('โปรแกรมบันทึกข้อมูล')
GUI.geometry('500x400')



L1 = Label(GUI,text='โปรแกรมบันทึกความรู้',font=('Angsana New',30),fg='green')
L1.place(x=30,y=20)

###########
def Button2():
    text = 'ตอนนี้มีเงินในบัญชีอยุ่ 300 บาท'
    messagebox.showwarning('เงินในบัญชี',text)

FB1 = Frame(GUI) #คล้ายกระดาษ
FB1.place(x=200,y=200)
B2 = ttk.Button(FB1,text='เงินมีอยุ่กี่่บาท',command=Button2)
B2.pack(ipadx=10,ipady=30)
###########

def Button3():
    text = 'python 101,Math'
    messagebox.showwarning('เรียนวิชาอะไร',text)




FB2 = LabelFrame(GUI,text='Frame') #คล้ายกระดาษ
FB2.place(x=10,y=100) # ตำแหน่ง
B3 = ttk.Button(FB2,text='วิชาที่กำลังเรียน',command=Button3)
B3.pack(ipadx=10,ipady=300) # ขนาดของเฟรม หรือป้ายข้อความ

GUI.mainloop()
