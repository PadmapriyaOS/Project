# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
from tkinter import *
top=Tk()
top.geometry("400x250")
uname=Label(top,text="USERNAME:").place(x=550,y=320)
password=Label(top,text="PASSWORD:").place(x=550,y=380)
sbtn=Button(top,text="SUBMIT",activebackground="black",activeforeground="white").place(x=650,y=450)
e1=Entry(top,width=20).place(x=700,y=320)
e2=Entry(top,width=20).place(x=700,y=380)
   
top.mainloop()
