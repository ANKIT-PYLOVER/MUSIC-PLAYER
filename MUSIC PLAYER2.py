from os import path
import tkinter as tk
from tkinter import StringVar,Label,Scrollbar
from tkinter import *
from typing import DefaultDict
from PIL import ImageTk
import random
from pygame import mixer
import os
from tkinter import messagebox
paths = "C:/Users/H1CK3R/Music/"
ank1 = []
ac=[]
ANK= [os.path.join(paths,f) for f in os.listdir(paths) if f.endswith(".mp3")]
for cl in os.listdir(paths):
    os.path.splitext(cl[0])
    ank1.append(cl)
mixer.init()
tk = tk.Tk()
tk.title("WELCOME TO MUSIC PLAYER ")
tk.geometry("800x500+270+100")
V = StringVar()
N = StringVar()
E = StringVar()
V.set("----")
N.set("-------")
photro = ImageTk.PhotoImage(file = r"aa.jpg") 
lab=Label(image=photro)
lab.place(x = 110, y = 30)

scrool= Scrollbar(tk)
scrool.pack(side=RIGHT,fill=BOTH)
mixer.music.set_volume(2)
def START():
    AC = random.choice(ANK)
    ac2.append(AC)
    mixer.music.load(AC)
    N.set(AC)
    mixer.music.play()
    V.set("PLAYING...")
def stop():
    V.set("STOPED!")
    mixer.music.stop()

def pause():
    V.set("PAUSED!")
    mixer.music.pause()
ac2 = []
def resume():
    V.set("PLAYING...")
    mixer.music.unpause()
def next():
    AC1 = random.choice(ANK)
    mixer.music.load(AC1)
    ac2.append(AC1)
    N.set(AC1)
    mixer.music.play()
    V.set("PLAYING...")
def pre():
    mixer.music.load(ac2[-2])
    N.set(ac2[-2])
    V.set("PLAYING...")
    mixer.music.play()
def vol(_=None):
    vol = w.get()
    c = vol/10
    mixer.music.set_volume(c)

vollis = LabelFrame(tk,width=70,height=110,text="VOL.")
vollis.place(x=375,y=335)
w = Scale(vollis,from_=20,to=0,bg="red",fg="black",command=vol)
w.set(20)
w.pack()
button = Button(text="PLAY",anchor=CENTER,command=START,width=7,height=1,bg="BLACK",fg="RED",font=("Bahnschrift SemiBold",14,"bold"))
button.place(x = 80,y =300)
button1 = Button(text="PAUSE",anchor=CENTER,command=pause,width=7,height=1,bg="BLACK",fg="RED",font=("Bahnschrift SemiBold",14,"bold"))
button1.place(x = 280,y =300)
button2 = Button(text="RESUME",anchor=CENTER,command=resume,width=7,height=1,bg="BLACK",fg="RED",font=("Bahnschrift SemiBold",14,"bold"))
button2.place(x=80, y= 450)
button3 = Button(text="STOP",anchor=CENTER,command=stop,width=7,height=1,bg="BLACK",fg="RED",font=("Bahnschrift SemiBold",14,"bold"))
button3.place(x=280,y=450)
button4 = Button(text="NEXT",anchor=CENTER,command=next,width=7,height=1,bg="BLACK",fg="RED",font=("Bahnschrift SemiBold",14,"bold"))
button4.place(x=180,y=300)
button4 = Button(text="PREVIOUS",anchor=CENTER,command=pre,width=7,height=1,bg="BLACK",fg="RED",font=("Bahnschrift SemiBold",14,"bold"))
button4.place(x=180,y=450)

scrol_y = Scrollbar(orient=VERTICAL)
lis = Listbox(tk,width=58,height=30,xscrollcommand=scrol_y)

for f1 in os.listdir(paths):
    lis.insert(END,f1)
    lis.config(yscrollcommand=scrool.set,bg="brown")
    scrool.config(command = lis.yview)
def A2(event):
    for f1 in lis.curselection():
        c = lis.get(f1)
        d = paths + c
        event.a=5
        try:
            N.set(c)
            V.set("PLAYING...")
            mixer.init()
            mixer.music.load(d)
            mixer.music.play()
            
        except:
            messagebox.showerror("ERROR","CAN'NT PLAY IT")
lis.bind('<Return>',A2)
lis.bind('<Double-Button-1>',A2)

frametk = LabelFrame(tk,text="song details",bg="red")
frametk.place(x =83,y=350,width=280,height=90)
label1 = Label(frametk,textvariable= V ,width=10,height=2,bg="WHITE",fg="BLACK",font=("Bahnschrift SemiBold",10,"bold"))
label1.place(x=100,y=40)
label2 = Label(frametk,textvariable=N,width=37,height=2,bg="WHITE",fg="BLACK",font=("Bahnschrift SemiBold",10,"bold"))
label2.place(x=9,y=1)

lis.place(x = 430,y=25)

tk.config(bg="black")

entry = Entry(tk,width=25,textvariable=E)
entry.place(x=530,y=3)
print("done")
def get1():
    c = entry.get()
    #print(ank1)
    if c !="":
        b = [x for  x in ank1 if x[0:4].lower()==c.lower()]
        
        lis.delete(0,END)
        for f in b :
            lis.insert(END,f)
    else:
        messagebox.showerror("none","enter starting 4 words of song")
    
    
def back():
    entry.delete(0,END)
    lis.delete(0,END)
    for f2 in os.listdir(paths): 
        lis.insert(END,f2)
buttons = Button(text="BACK",width=10,height=int(0.5),command=back,bg="BLACK",fg="RED",font=("Bahnschrift SemiBold",9,"bold"))
#print(ank1)
buttons.place(x=432,y=0)
buttons = Button(text="SEARCH",width=10,height=int(0.5),command=get1,bg="BLACK",fg="RED",font=("Bahnschrift SemiBold",9,"bold"))
#print(ank1)
buttons.place(x=700,y=0)
tk.mainloop()