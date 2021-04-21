import tkinter as tk
from tkinter import StringVar,Label,Scrollbar
from tkinter import *
from PIL import ImageTk
import random
from pygame import mixer
import os
from tkinter import messagebox

paths = "C:/Users/H1CK3R/Music/"

ANK= [os.path.join(paths,f) for f in os.listdir(paths) if f.endswith(".mp3")]

mixer.init()
tk = tk.Tk()
tk.title("MUSIC PLAYER ")
tk.geometry("800x500+400+100")
V = StringVar()
N = StringVar()
V.set("----")
N.set("-------")
photro = ImageTk.PhotoImage(file = r"aa.jpg") 
lab=Label(image=photro)
lab.place(x = 118, y = 30)

scrool= Scrollbar(tk)
scrool.pack(side=RIGHT,fill=BOTH)
#crool.place(x=700,y=0)

def START():
    V.set("PLAYING")
    AC = random.choice(ANK)
    ac2.append(AC)
    mixer.music.load(AC)
    N.set(AC)
    mixer.music.play()

def stop():
    V.set("STOPED")
    mixer.music.stop()

def pause():
    V.set("PAUSED")
    mixer.music.pause()
ac2 = []
def resume():
    V.set("PLAYING")
    mixer.music.unpause()
def next():
    AC1 = random.choice(ANK)
    mixer.music.load(AC1)
    ac2.append(AC1)
    N.set(AC1)
    mixer.music.play()
    V.set("PLAYING")
def pre():
    mixer.music.load(ac2[-2])
    N.set(ac2[-2])
    V.set("PLAYING")
    mixer.music.play()

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
lis = Listbox(tk,width=58,height=29,xscrollcommand=scrol_y)

for f in os.listdir(paths):
    lis.insert(END,f)
    lis.config(yscrollcommand=scrool.set,bg="brown")
    scrool.config(command = lis.yview)
lis.place(x = 430,y=1)
def A2():
    for f1 in lis.curselection():
        c = lis.get(f1)
        N.set(c)
        d = paths + c
        try:
            V.set("PLAYING")
            mixer.init()
            mixer.music.load(d)
            mixer.music.play()
            
        except:
            #messagebox.showinfo("error","it is not a song")
            messagebox.showerror("ERROR","CAN'NT PLAY IT")

frametk = LabelFrame(tk,text="song details",width=5,height=3,bg="red")
frametk.place(x =83,y=350,width=280,height=90)
label1 = Label(frametk,textvariable= V ,width=10,height=2,bg="WHITE",fg="BLACK",font=("Bahnschrift SemiBold",10,"bold"))
label1.place(x=100,y=40)
label2 = Label(frametk,textvariable=N,width=37,height=2,bg="WHITE",fg="BLACK",font=("Bahnschrift SemiBold",10,"bold"))
label2.place(x=9,y=1)
button4 = Button(text="PLAY FROM LIST",command=A2,bg="black",fg="white",activebackground="red")
button4.place(x =552,y =470)

tk.config(bg="black")
tk.mainloop()