
from tkinter import *
from tkinter.ttk import Combobox
from tkinter.messagebox import *
import datetime
import winsound

r = 423 # hz, change this as needed
g = 2 ** (1.0 / 12.0)
Sa = r
Re_k = r * g
Re = r * g ** 2
Ga_k = r * g ** 3
Ga = r * g ** 4
Ma = r * g ** 5
Ma_t = r * g ** 6
pa = r * g ** 7
Ni_K = r * g ** 8
Dha_K = r * g ** 9
Ma_t = r * g ** 10
Dha_K= r * g ** 11

song_list =[Ni_K,Dha_K,Ma_t,Dha_K,Dha_K,Dha_K,Dha_K,]

root=Tk()

def alarm():
    h=int(c.get())
    m=int(c1.get())
    #print(h,m)
    showinfo("Alarm Notification", "Alarm has been Set..")
    print(datetime.datetime.now())
    while True:
        if h==datetime.datetime.now().hour and m==datetime.datetime.now().minute:
            for j in range(2):
                for i in song_list:
                    #print(int(song_list[i]))
                    winsound.Beep(int(i),1000)
            break
       
root.title("My Alarm Clock")
l1=Label(root,text="set Alarm Hour")
l1.grid(row=0,column=0)
hour=list(range(1,25))
c=Combobox(root,values=hour)
c.grid(row=0,column=1)

l2=Label(root,text="set Alarm Minute")
l2.grid(row=1,column=0)
minute=list(range(1,61))
c1=Combobox(root,values=minute)
c1.grid(row=1,column=1)

btn=Button(root,text="Set Alarm",command=alarm)
btn.grid(row=2,columnspan=2)
root.mainloop()