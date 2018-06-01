import pygame
import sys
import time
from Tkinter import *
list=[]
pygame.init()

def value_Cs(event=None):
    num1.set("C#")
    sound = pygame.mixer.Sound("piano\A2-61-1.wav")
    sound.play()
    return
def value_Ds1(event=None):
    num1.set("D#")
    sound = pygame.mixer.Sound("piano\d1s.wav")
    sound.play()
    return
def value_Fs(event=None):
    num1.set("F#")
    sound = pygame.mixer.Sound("piano\f1s.wav")
    sound.play()
    return
def value_Gs(event=None):
    num1.set("G#")
    sound = pygame.mixer.Sound("piano\g1s.wav")
    sound.play()
    return
def value_Bb(event=None):
    num1.set("Bb")
    sound = pygame.mixer.Sound("piano\b1.wav")
    sound.play()
    return
def value_Cs1(event=None):
    num1.set("C#1")
    sound = pygame.mixer.Sound("piano\c1s.wav")
    sound.play()
    return
def value_Ds(event=None):
    sound = pygame.mixer.Sound("piano\d1s.wav")
    sound.play()
    return
def value_C(event=None):
    sound = pygame.mixer.Sound("piano/a.wav")
    sound.play()
    list.append(1)
    return
def value_D(event=None):
    num1.set("D")
    sound = pygame.mixer.Sound("piano/b.wav")
    sound.play()
    list.append(2)
    return
def value_E(event=None):
    num1.set("E")
    sound = pygame.mixer.Sound("piano/c.wav")
    sound.play()
    list.append(3)
    return
def value_F(event=None):
    num1.set("F")
    sound = pygame.mixer.Sound("piano/d.wav")
    sound.play()
    list.append(4)
    return
def value_G(event=None):
    num1.set("G")
    sound = pygame.mixer.Sound("piano/e.wav")
    sound.play()
    list.append(5)
    return
def value_A(event=None):
    num1.set("A")
    sound = pygame.mixer.Sound("piano/f.wav")
    sound.play()
    list.append(6)
    return
def value_B(event=None):
    num1.set("B")
    sound = pygame.mixer.Sound("piano/g.wav")
    sound.play()
    list.append(7)
    return
def value_C1(event=None):
    num1.set("C1")
    sound = pygame.mixer.Sound("piano/h.wav")
    sound.play()
    list.append(8)
    return
def value_D1(event=None):
    num1.set("D1")
    sound = pygame.mixer.Sound("piano\i.wav")
    sound.play()
    list.append(9)
    return
def value_E1(event=None):
    num1.set("E1")
    sound = pygame.mixer.Sound("piano\j.wav")
    sound.play()
    list.append(10)
    return
def value_F1(event=None):
    num1.set("F1")
    sound = pygame.mixer.Sound("piano\k.wav")
    sound.play()
    list.append(11)
    return
def record(event=None):
    list[:]=[]
def tutorial(event=None):
    return

root= Tk()
frame = Frame(root)
frame.pack()
num1=StringVar()
topframe= Frame(root)
topframe.pack(side=TOP)
txtDisplay=Entry(frame,textvariable=num1,bd=20,insertwidth=1,font=30,justify="center",width=4)
txtDisplay.pack(side=TOP)

button1=Button(topframe,padx=8,height=6,pady=8,bd=8,text="C#",bg="black",fg="white",command=value_Cs)
button1.pack(side=LEFT)
button22=Button(topframe,state=DISABLED,height=7,width=1,padx=0,pady=0,relief=RIDGE)
button22.pack(side=LEFT)
button2=Button(topframe,padx=8,height=6,pady=8,bd=8,text="D#",bg="black",fg="white",command=value_Ds)
button2.pack(side=LEFT)
button22=Button(topframe,state=DISABLED,height=7,width=1,padx=0,pady=0,relief=RIDGE)
button22.pack(side=LEFT)
button3=Button(topframe,padx=8,height=6,pady=8,bd=8,text="F#",bg="black",fg="white",command=value_Fs)
button3.pack(side=LEFT)
button22=Button(topframe,state=DISABLED,height=7,width=1,padx=0,pady=0,relief=RIDGE)
button22.pack(side=LEFT)
button4=Button(topframe,padx=8,height=6,pady=8,bd=8,text="G#",bg="black",fg="white",command=value_Gs)
button4.pack(side=LEFT)
button22=Button(topframe,state=DISABLED,height=7,width=1,padx=0,pady=0,relief=RIDGE)
button22.pack(side=LEFT)

button2=Button(topframe,padx=8,height=6,pady=8,bd=8,text="Bb",bg="black",fg="white",command=value_Bb)
button2.pack(side=LEFT)
button22=Button(topframe,state=DISABLED,height=7,width=1,padx=0,pady=0,relief=RIDGE)
button22.pack(side=LEFT)
button3=Button(topframe,padx=8,height=6,pady=8,bd=8,text="C#1",bg="black",fg="white",command=value_Cs1)
button3.pack(side=LEFT)
button22=Button(topframe,state=DISABLED,height=7,width=1,padx=0,pady=0,relief=RIDGE)
button22.pack(side=LEFT)
button4=Button(topframe,padx=8,height=6,pady=8,bd=8,text="D#1",bg="black",fg="white",command=value_Ds1)
button4.pack(side=LEFT)

frame1=Frame(root)
frame1.pack(side=TOP)

button1=Button(frame1,padx=16,height=8,pady=16,bd=8,text="C",fg="black",command=value_C)
button1.pack(side=LEFT)
button2=Button(frame1,padx=16,height=8,pady=16,bd=8,text="D",fg="black",command=value_D)
button2.pack(side=LEFT)
button3=Button(frame1,padx=16,height=8,pady=16,bd=8,text="E",fg="black",command=value_E)
button3.pack(side=LEFT)
button4=Button(frame1,padx=16,height=8,pady=16,bd=8,text="F",fg="black",command=value_F)
button4.pack(side=LEFT)

button5=Button(frame1,padx=16,height=8,pady=16,bd=8,text="G",fg="black",command=value_G)
button5.pack(side=LEFT)
button6=Button(frame1,padx=16,height=8,pady=16,bd=8,text="A",fg="black",command=value_A)
button6.pack(side=LEFT)
button7=Button(frame1,padx=16,height=8,pady=16,bd=8,text="B",fg="black",command=value_B)
button7.pack(side=LEFT)
button8=Button(frame1,padx=16,height=8,pady=16,bd=8,text="C1",fg="black",command=value_C1)
button8.pack(side=LEFT)

button9=Button(frame1,padx=16,height=8,pady=16,bd=8,text="D1",fg="black",command=value_D1)
button9.pack(side=LEFT)
button10=Button(frame1,padx=16,height=8,pady=16,bd=8,text="E1",fg="black",command=value_E1)
button10.pack(side=LEFT)
button11=Button(frame1,padx=16,height=8,pady=16,bd=8,text="F1",fg="black",command=value_F1)
button11.pack(side=LEFT)
footer=Frame(root)
footer.pack(side=BOTTOM)
main=Button(footer,text="Go back to Main Menu",height=5,width=31).grid(row=0,column=0)
play=Button(footer,text="Tutorial",height=5,width=31,command=tutorial).grid(row=0,column=2)
root.bind('<a>',value_C)
root.bind('<s>',value_D)
root.bind('<d>',value_E)
root.bind('<f>',value_F)
root.bind('<g>',value_G)
root.bind('<h>',value_A)
root.bind('<j>',value_B)
root.bind('<k>',value_C1)
root.bind('<l>',value_D1)
root.bind('<;>',value_E1)
root.bind("<'>",value_F1)
root.mainloop()
