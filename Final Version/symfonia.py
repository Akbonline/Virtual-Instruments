from tkinter import *
def piano():
    import uprising

def drum():
    home.destroy()
    import drumsuit1
def bongo():
    home.destroy()
    import bongo

home=Tk()
home.configure(background="black")
img=PhotoImage(file="images\pianoimg.gif")
img1=PhotoImage(file="images\drumimg.gif")
img2=PhotoImage(file="images\congimg.gif")
heading=Label(home,text="Welcome to Symfonia",fg="white",bg="Black",font=("Times new roman",30,"bold"),bd=10,anchor=CENTER,cursor="star",relief="raised").grid(row=0,column=1)
pianomodule=Button(home,text="Piano",command=piano,image=img,height=400,width=400,bd=15,relief="groove").grid(row=1,column=0)
drummodule=Button(home,text="Drum",command=drum,image=img1,height=400,width=400,bd=15,relief="groove").grid(row=1,column=1)
bongo=Button(home,text="Bongo",image=img2,height=400,width=400,command=bongo,bd=15,relief="groove").grid(row=1,column=2)
home.mainloop()
