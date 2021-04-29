from math import trunc
import tkinter as tk
from tkinter import StringVar,Label,Scrollbar
from tkinter import *
from tkinter.filedialog import  askopenfilenames
from PIL import ImageTk
from pygame import mixer
import os
from tkinter import messagebox
import pygame 
import random  
paths = "C:/Users/H1CK3R/Music/"
ank = [os.path.join(paths,i) for i in os.listdir(paths) if i.endswith('.mp3')]
ank1 = random.choice(ank)
ank2 = []
ak3 = []
for cl in os.listdir(paths):
    os.path.splitext(cl[0])
    ank2.append(cl)

tk = tk.Tk()
tk.title("A DOT PLAYER")
tk.geometry("800x515+270+100")
V = StringVar()
N = StringVar()
V.set("----")
N.set("-------")
photro = ImageTk.PhotoImage(file = r"aa.jpg") 
lab=Label(image=photro)
lab.place(x = 110, y = 30)
photo = PhotoImage(file = r"12.png")
photo2 = PhotoImage(file = r"11.png")
photo3 = PhotoImage(file = r"download.png")
mixer.init()
pygame.init()
SONG_END = pygame.USEREVENT + 1
music_number = 0
rand = False
paused = True
aa = True
mixer.music.set_endevent(SONG_END)
playing = False
def PLAY():
    global playing
    if playing == False:
        global music_number
        mixer.music.load(ank[music_number])
        ak3.append((ank[music_number]))
        mixer.music.play()
        V.set("PLAYING...")
        N.set(ank[music_number])
        mixer.music.set_endevent(SONG_END)
        playing = True

a =True
def check():
    if a == True:
        for event in pygame.event.get():
            if event.type == SONG_END:

                next_song()
def next_song():
    global music_number
    if rand == True:
        ank1  =  random.choice(ank)
        mixer.music.load(ank1) 
        mixer.music.play()
        V.set("PLAYING...")
        N.set(ank1)
    else:
        global music_number
        music_number = music_number + 1
                            
        current_music = (ank[music_number])
        ak3.append(current_music)
        mixer.music.load(current_music) 
        mixer.music.play()
        V.set("PLAYING...")
        N.set(current_music) 

def pre():
    global music_number
    music_number = music_number - 1
    global current_music
    current_music = (ank[music_number])

    mixer.music.load(current_music) 
    mixer.music.play()
    V.set("PLAYING...")
    N.set(current_music)

def pause():
    mixer.music.pause()
    V.set("PAUSED!")
def pause2(event):
    global paused
    if paused:
        mixer.music.pause()
        V.set("PAUSED!")
        paused = False
    elif not paused:
        mixer.music.unpause()
        V.set("PLAYING...")
        paused=True

tk.bind('<space>',pause2)
def res():
    mixer.music.unpause()
    V.set("PLAYING...")
def stop():
    global a
    a = False
    mixer.music.stop()
    V.set("STOPED!")

def vol(_=None):
    vol = w.get()
    c = vol/10
    mixer.music.set_volume(c)

def suf():
    global paused
    global rand
    if paused:
        print("d1")
        rand = True
        paused = False
    elif  not paused :
        print("d")
        rand = False
        paused = True
asz = True
def rewind():
    global asz
    global a
    if asz:
        mixer.music.queue(ak3[-1])
        a = False
        asz = False
    elif not asz:
        a = True
list = list()

def adds():
    global aa
    aa = False
    dir  = askopenfilenames()
    lis.delete(0,END)
    for song in dir:
        list.append(song)
        print(list)        
    for i in list:
        lis.insert(END,i)  
vollis = LabelFrame(tk,width=70,height=110,text="VOL.")
vollis.place(x=375,y=335)
w = Scale(vollis,from_=20,to=0,bg="red",fg="black",command=vol)
w.set(20)
w.pack()
button = Button(text="PLAY",anchor=CENTER,command=PLAY,width=7,height=1,bg="BLACK",fg="RED",font=("Bahnschrift SemiBold",14,"bold"))
button.place(x = 80,y =300)
button1 = Button(text="PAUSE",anchor=CENTER,command=pause,width=7,height=1,bg="BLACK",fg="RED",font=("Bahnschrift SemiBold",14,"bold"))
button1.place(x = 280,y =300)
button2 = Button(text="RESUME",anchor=CENTER,command=res,width=7,height=1,bg="BLACK",fg="RED",font=("Bahnschrift SemiBold",14,"bold"))
button2.place(x=80, y= 450)
button3 = Button(text="STOP",anchor=CENTER,command=stop,width=7,height=1,bg="BLACK",fg="RED",font=("Bahnschrift SemiBold",14,"bold"))
button3.place(x=280,y=450)
button4 = Button(text="NEXT",anchor=CENTER,command=next_song,width=7,height=1,bg="BLACK",fg="RED",font=("Bahnschrift SemiBold",14,"bold"))
button4.place(x=180,y=300)
button4 = Button(text="PREVIOUS",anchor=CENTER,command=pre,width=7,height=1,bg="BLACK",fg="RED",font=("Bahnschrift SemiBold",14,"bold"))
button4.place(x=180,y=450)
button5 = Button(image=photo2,anchor=CENTER,command=rewind,bg="BLACK",fg="RED",font=("Bahnschrift SemiBold",14,"bold"),activebackground="red",foreground="white")
button5.place(x=160,y=265)
button56= Button(image=photo,anchor=CENTER,command=suf,bg="BLACK",fg="RED",font=("Bahnschrift SemiBold",14,"bold"),activebackground="red",background="black",foreground="white",highlightbackground="red")
button56.place(x=260,y=265)


lis = Listbox(tk,width=58,height=30)
scrool= Scrollbar(tk)
scrool.pack(side=RIGHT,fill=BOTH)
for f1 in os.listdir(paths):
    lis.insert(END,f1)
    lis.config(yscrollcommand=scrool.set,bg="brown")
    scrool.config(command = lis.yview)

button57= Button(lis,image=photo3,anchor=CENTER,command=adds,bg="BLACK",fg="RED",font=("Bahnschrift SemiBold",14,"bold"),activebackground="red",foreground="white")
button57.place(x=320,y=450)
def A2(event):
    global playing
    playing = True
    for f1 in lis.curselection():
        c = lis.get(f1)
        if aa==True:
            d = paths + c
            ak3.append(d)
            try:
                N.set(c)
                V.set("PLAYING...")
                mixer.init()
                mixer.music.load(d)
                mixer.music.play()
                
            except:
                N.set("ERROR")
                messagebox.showerror("ERROR","CAN'NT PLAY IT")
        elif aa == False:
            ak3.append(c)
            print(c)
            N.set(c)
            V.set("PLAYING...")
            mixer.init()
            mixer.music.load(c)
            mixer.music.play()


tk.bind('<Return>',A2)

tk.bind('<Double-Button-1>',A2)
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
    if c !="":
        b = [x for  x in ank2 if x[0:4].lower()==c.lower()]
        
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

buttons.place(x=432,y=0)

buttons = Button(text="SEARCH",width=10,height=int(0.5),command=get1,bg="BLACK",fg="RED",font=("Bahnschrift SemiBold",9,"bold"))

buttons.place(x=700,y=0)


while True:
    check()
    tk.update()