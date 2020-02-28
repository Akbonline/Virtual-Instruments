import pygame
import os
import sys
import time
from tkinter import *
pygame.init()
def a():
    sound=pygame.mixer.Sound("./drumsuite/a.wav")
    sound.play()
    return

def b():
    sound=pygame.mixer.Sound("./drumsuite/b.wav")
    sound.play()
    return

def c():
    sound=pygame.mixer.Sound("./drumsuite/c.wav")
    sound.play()
    return

def d():
    sound=pygame.mixer.Sound("./drumsuite/d.wav")
    sound.play()
    return

def e():
    sound=pygame.mixer.Sound("./drumsuite/e.wav")
    sound.play()
    return

def f():
    sound=pygame.mixer.Sound("drumsuite/f.wav")
    sound.play()
    return

def g():
    sound=pygame.mixer.Sound("drumsuite/g.wav")
    sound.play()
    return

def h():
    sound=pygame.mixer.Sound("drumsuite/h.wav")
    sound.play()
    return
def change():
    drumsuit1.destroy()
    import pygame
    import time
    import sys

    def a():
        sound=pygame.mixer.Sound("./drumsuite/i.wav")
        sound.play()
        return

    def b():
        sound=pygame.mixer.Sound("./drumsuite/j.wav")
        sound.play()
        return

    def c():
        sound=pygame.mixer.Sound("./drumsuite/k.wav")
        sound.play()
        return

    def d():
        sound=pygame.mixer.Sound("./drumsuite/l.wav")
        sound.play()
        return

    def e():
        sound=pygame.mixer.Sound("./drumsuite/m.wav")
        sound.play()
        return

    def f():
        sound=pygame.mixer.Sound("drumsuite/n.wav")
        sound.play()
        return

    def g():
        sound=pygame.mixer.Sound("drumsuite/o.wav")
        sound.play()
        return

    def h():
        sound=pygame.mixer.Sound("drumsuite/p.wav")
        sound.play()
        return

    def change():
        sroot.destroy()
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
            drumsuit3.destroy()
            import symfonia

        drumsuit3= Tk()
        topframe= Frame(drumsuit3)
        topframe.pack(side=TOP)
        img=PhotoImage(file="steel.gif")
        a=Button(topframe,image=img,height=300,width=300,bd=10,relief="raised",command=a).grid(row=0,column=0)
        b=Button(topframe,image=img,height=300,width=300,bd=10,relief="raised",command=b).grid(row=0,column=1)
        c=Button(topframe,image=img,height=300,width=300,bd=10,relief="raised",command=c).grid(row=0,column=2)
        d=Button(topframe,image=img,height=300,width=300,bd=10,relief="raised",command=d).grid(row=0,column=3)
        e=Button(topframe,image=img,height=300,width=300,bd=10,relief="raised",command=e).grid(row=1,column=0)
        f=Button(topframe,image=img,height=300,width=300,bd=10,relief="raised",command=f).grid(row=1,column=1)
        g=Button(topframe,image=img,height=300,width=300,bd=10,relief="raised",command=g).grid(row=1,column=2)
        h=Button(topframe,image=img,height=300,width=300,bd=10,relief="raised",command=h).grid(row=1,column=3)
        footer=Frame(drumsuit3)
        footer.pack(side=BOTTOM)
        main=Button(footer,text="Back to main menu",height=5,width=30,command=mainmenu).grid(row=0,column=0)
        change=Button(footer,text="Change",height=5,width=30,command=change).grid(row=0,column=1)
        drumsuit3.mainloop()

    def mainmenu():
        sroot.destroy()
        import symfonia


    sroot= Tk()
    topframe= Frame(sroot)
    topframe.pack(side=TOP)
    img=PhotoImage(file="steel.gif")
    a=Button(topframe,image=img,height=300,width=300,bd=10,relief="raised",command=a).grid(row=0,column=0)
    b=Button(topframe,image=img,height=300,width=300,bd=10,relief="raised",command=b).grid(row=0,column=1)
    c=Button(topframe,image=img,height=300,width=300,bd=10,relief="raised",command=c).grid(row=0,column=2)
    d=Button(topframe,image=img,height=300,width=300,bd=10,relief="raised",command=d).grid(row=0,column=3)
    e=Button(topframe,image=img,height=300,width=300,bd=10,relief="raised",command=e).grid(row=1,column=0)
    f=Button(topframe,image=img,height=300,width=300,bd=10,relief="raised",command=f).grid(row=1,column=1)
    g=Button(topframe,image=img,height=300,width=300,bd=10,relief="raised",command=g).grid(row=1,column=2)
    h=Button(topframe,image=img,height=300,width=300,bd=10,relief="raised",command=h).grid(row=1,column=3)
    footer=Frame(sroot)
    footer.pack(side=BOTTOM)
    main=Button(footer,text="Back to main menu",height=5,width=30).grid(row=0,column=0)
    change=Button(footer,text="Change",height=5,width=30,command=change).grid(row=0,column=2)
    sroot.mainloop()

def mainmenu():
    drumsuit1.destroy()
    import symfonia


drumsuit1= Tk()
drumsuit1.configure(background="black")
topframe= Frame(drumsuit1)
topframe.pack(side=TOP)
img=PhotoImage(file="steel.gif")
a=Button(topframe,image=img,height=300,width=300,bd=10,relief="raised",command=a).grid(row=0,column=0)
b=Button(topframe,image=img,height=300,width=300,bd=10,relief="raised",command=b).grid(row=0,column=1)
c=Button(topframe,image=img,height=300,width=300,bd=10,relief="raised",command=c).grid(row=0,column=2)
d=Button(topframe,image=img,height=300,width=300,bd=10,relief="raised",command=d).grid(row=0,column=3)
e=Button(topframe,image=img,height=300,width=300,bd=10,relief="raised",command=e).grid(row=1,column=0)
f=Button(topframe,image=img,height=300,width=300,bd=10,relief="raised",command=f).grid(row=1,column=1)
g=Button(topframe,image=img,height=300,width=300,bd=10,relief="raised",command=g).grid(row=1,column=2)
h=Button(topframe,image=img,height=300,width=300,bd=10,relief="raised",command=h).grid(row=1,column=3)
footer=Frame(drumsuit1)
footer.pack(side=BOTTOM)
main=Button(footer,text="Back to main menu",height=5,width=30).grid(row=0,column=0)
change=Button(footer,text="Change",height=5,width=30,command=change).grid(row=0,column=1)
drumsuit1.mainloop()
