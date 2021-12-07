from tkinter import *
from tkinter import ttk
klik=0
def klikker(event):
    global klik
    klik+=1
    lbl.configure(text=klik)

def klikker2(event):
    global klik
    if klik > 0:
        klik-=1
    else:
        klik=0
    lbl.configure(text = klik)

def text_to_lbl(event):
    text=ent.get()
    lbl.configure(text=text)
    ent.delete(0,END)

def valik():
    val=str(var.get())+", "
    ent.insert(END, var+", ")

def ava_pilt(ind:int):
    global tabs
    tabs.select(ind)

aken=Tk()
aken.title("Akna nimetus")
aken.geometry("600x400")

Menu=Menu(aken)
aken.config(menu=Menu)
m1=Menu(Menu)
Menu.add_cascade(label="Tabs", menu=m1)
m1.add_command(label="Tab1",acceleration="Command+A", command=lambda:ava_pilt(0))
m1.add_command(label="Tab2", command=lambda:uus_aken(1))
m1.add_command(label="Tab3", command=lambda:uus_aken(2))
m1.add_separator()


def uus_aken():
    uusaken=Toplevel()
    tabs=ttk.Notebook(uusaken)
    texts=["1.gif","2.gif","3.gif"]

    tab1=Frame(tabs)
    img1=PhotoImage(file=texts[0])
    tabs.add(tab1,text=texts[0])
    can1=Canvas(tab1,height=1000,width=1000,bg="red")
    can1.create_image(0,0,image=img1,anchor=NW)
    can1.pack()

    tab2=Frame(tabs)
    img2=PhotoImage(file=texts[1])
    tabs.add(tab2,text=texts[1])
    can2=Canvas(tab2,height=1000,width=1000,bg="red")
    can2.create_image(0,0,image=img2,anchor=NW)
    can2.pack()

    tab3=Frame(tabs)
    img3=PhotoImage(file=texts[2])
    tabs.add(tab3,text=texts[2])
    can3=Canvas(tab3,height=1000,width=1000,bg="red")
    can3.create_image(0,0,image=img3,anchor=NW)
    can3.pack()

    tabs.add(tab1,text=texts[0])
    tabs.add(tab2,text=texts[1]) 
    tabs.add(tab3,text=texts[2])
    tabs.grid(row=0,column=0)
    uusaken.mainloop()

btn=Button(aken,text="Vajuta siia",font="Arial 20",fg="green",bg="lightblue",width=20, height=3)
btn2=Button(aken,text="Veel aken",font="Arial 20",fg="green",bg="lightblue", command=uus_aken).pack()
lbl=Label(aken,text="...")
ent=Entry(aken,fg="BLue", width=20, font="Arial 20")
var=IntVar()
#var.set(2)
r1=Radiobutton(aken, text="Esimene", variable=var, value=1, command=valik)
r2=Radiobutton(aken, text="Teine", variable=var, value=2, command=valik)
r3=Radiobutton(aken, text="Kolmas", variable=var, value=3, command=valik)

btn.bind("<Button-1>", klikker) #LKM
btn.bind("<Button-3>", klikker2) #PKM
ent.bind("<Return>", text_to_lbl) #Enter
lbl.pack()
btn.pack()
ent.pack()
r1.pack(side=LEFT)
r2.pack(side=LEFT)
r3.pack(side=LEFT)
aken.mainloop()
