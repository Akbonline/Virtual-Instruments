from Tkinter import *
import pygame
import sys
def pad1():
    sound=pygame.mixer.Sound("bongosuite\a.wav")
    sound.play()
    return

def pad2():
    sound=pygame.mixer.Sound("bongosuite\b.wav")
    sound.play()
    return

def pad3():
    sound=pygame.mixer.Sound("bongosuite\c.wav")
    sound.play()
    return
def mainmenu():
    bongo.destroy()
    import symfonia

bongo=Tk()
img=PhotoImage(file="bongo.gif")
heading=Label(bongo,text="Bongos").grid(row=0,column=1)
a=Button(bongo,image=img,height=500,width=250,command=pad1).grid(row=1,column=0)
b=Button(bongo,image=img,height=500,width=250,command=pad2).grid(row=1,column=1)
c=Button(bongo,image=img,height=500,width=250,command=pad3).grid(row=1,column=2)
main=Button(bongo,text="Back to Main Menu",height=10,width=20,command=mainmenu).grid(row=2,column=1)
bongo.bind('<a>',pad1)
bongo.bind('<s>',pad2)
bongo.bind('<d>',pad3)

bongo.mainloop()
