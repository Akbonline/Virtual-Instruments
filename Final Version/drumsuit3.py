import pygame
import sys
import time
from tkinter import *
global i
i=1

pygame.init()
pygame.mixer.init()
def a():
    sound=pygame.mixer.Sound("./drumsuite/q.wav")
    sound.play()
    return

def b():
    sound=pygame.mixer.Sound("./drumsuite/r.wav")
    sound.play()
    return

def c():
    sound=pygame.mixer.Sound("./drumsuite/s.wav")
    sound.play()
    return

def d():
    sound=pygame.mixer.Sound("./drumsuite/t.wav")
    sound.play()
    return

def e():
    sound=pygame.mixer.Sound("./drumsuite/u.wav")
    sound.play()
    return

def f():
    sound=pygame.mixer.Sound("drumsuite/v.wav")
    sound.play()
    return

def g():
    sound=pygame.mixer.Sound("drumsuite/x.wav")
    sound.play()
    return

def h():
    sound=pygame.mixer.Sound("drumsuite/y.wav")
    sound.play()
    return

def change():
    import drumsuit1

def mainmenu():
    import symfonia
    topframe.destroy()


drumsuit3= Toplevel()
topframe= Frame(drumsuit3)
topframe.pack(side=TOP)
img=PhotoImage(file="steel.gif")
a=Button(topframe,image=img,height=300,width=300,command=a).grid(row=0,column=0)
b=Button(topframe,image=img,height=300,width=300,command=b).grid(row=0,column=1)
c=Button(topframe,image=img,height=300,width=300,command=c).grid(row=0,column=2)
d=Button(topframe,image=img,height=300,width=300,command=d).grid(row=0,column=3)
e=Button(topframe,image=img,height=300,width=300,command=e).grid(row=1,column=0)
f=Button(topframe,image=img,height=300,width=300,command=f).grid(row=1,column=1)
g=Button(topframe,image=img,height=300,width=300,command=g).grid(row=1,column=2)
h=Button(topframe,image=img,height=300,width=300,command=h).grid(row=1,column=3)
footer=Frame(drumsuit3)
footer.pack(side=BOTTOM)
main=Button(footer,text="Back to main menu",height=5,width=30,command=mainmenu).grid(row=0,column=0)
change=Button(footer,text="Change",height=5,width=30,command=change).grid(row=0,column=1)
drumsuit3.mainloop()
