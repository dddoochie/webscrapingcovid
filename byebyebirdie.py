from  tkinter import *
from tkinter import ttk
bobert=Tk()
bobert.geometry("600x600")
import sqlite3

notebook=ttk.Notebook(bobert)
connection = sqlite3.connect('covidproject.db')
cursor = connection.cursor()

bobert.configure(bg='pink')

country_name=StringVar()

frame2=ttk.Frame(notebook, width=600,height=600)
frame1=ttk.Frame(notebook, width=600,height=600)
notebook.add(frame1,text="What is Covid?")
notebook.add(frame2,text="World Statistics")

notebook.pack()


intro2covid=Label(frame1,text="Basic Facts about Covid",fg="black",font=("sand script",20))
intro2covid.place(x=150,y=50)

intro2covid1=Label(frame1,text="-Coronavirus is an illness caused by a virus that can spread from ",fg="black",font=("sand script",15))
intro2covid1.place(x=10,y=80)

intro2covid2=Label(frame1,text="person to person.",fg="black",font=("sand script",15))
intro2covid2.place(x=15,y=110)

intro2covid3=Label(frame1,text="-The virus that causes COVID-19 is a new coronavirus that has",fg="black",font=("sand script",15))
intro2covid3.place(x=10,y=140)

intro2covid4=Label(frame1,text="spread throughout the world. ",fg="black",font=("sand script",15))
intro2covid4.place(x=15,y=170)

intro2covid5=Label(frame1,text="There is currently no cure for covid-19. If you think you may be",fg="black",font=("sand script",15))
intro2covid5.place(x=10,y=210)

intro2covid6=Label(frame1,text="experiencing symptoms, go to a local testing station to get tested.",fg="black",font=("sand script",15))
intro2covid6.place(x=10,y=240)

intro2covid6=Label(frame1,text="REMEMBER TO WEAR A ",fg="red",font=("sand script",30))
intro2covid6.place(x=40,y=280)

intro2covid7=Label(frame1,text="MASK WHEN OUTSIDE TO ",fg="red",font=("sand script",30))
intro2covid7.place(x=40,y=340)

intro2covid8=Label(frame1,text="PROTECT YOURSELF AND ",fg="red",font=("sand script",30))
intro2covid8.place(x=40,y=400)

intro2covid8=Label(frame1,text="OTHERS AROUND YOU!",fg="red",font=("sand script",30))
intro2covid8.place(x=40,y=460)
##******************************************************************************************
label1=Label(frame2,text="World Covid Stats",fg="black",font=("sand script",20))
label1.place(x=183,y=50)

label2=Label(frame2,text="Name of Country:",fg="black",font=("sand script",15))
label2.place(x=130,y=100)

country=Label(frame2,text="Country:",fg="black",font=("sand script",15))
country.place(x=40,y=190)

confirmed=Label(frame2,text="Confirmed:",fg="black",font=("sand script",15))
confirmed.place(x=40,y=230)

chtoday=Label(frame2,text="Changes today:",fg="black",font=("sand script",15))
chtoday.place(x=40,y=270)

dead=Label(frame2,text="Deceased:",fg="black",font=("sand script",15))
dead.place(x=40,y=310)

active=Label(frame2,text="Active:",fg="black",font=("sand script",15))
active.place(x=40,y=350)

recover=Label(frame2,text="Recovered:",fg="black",font=("sand script",15))
recover.place(x=40,y=390)

dec=Label(frame2,text="*all data web scraped from ncov2019.live",fg="black",font=("sand script",10))
dec.place(x=350,y=550)

n=Entry(frame2,textvariable=country_name)
n.place(x=310,y=108)
##***********************************************************************************
users0=StringVar()
users1=StringVar()
users2=StringVar()
users3=StringVar()
users4=StringVar()
users5=StringVar()
##***********************************************************************************
output0=Label(frame2,textvariable=users0,fg="black",font=("sand script",15))
output0.place(x=190,y=190)

output1=Label(frame2,textvariable=users1,fg="black",font=("sand script",15))
output1.place(x=190,y=230)

output2=Label(frame2,textvariable=users2,fg="black",font=("sand script",15))
output2.place(x=190,y=270)

output3=Label(frame2,textvariable=users3,fg="black",font=("sand script",15))
output3.place(x=190,y=310)

output4=Label(frame2,textvariable=users4,fg="black",font=("sand script",15))
output4.place(x=190,y=350)

output5=Label(frame2,textvariable=users5,fg="black",font=("sand script",15))
output5.place(x=190,y=390)
def subby():
    try:
        answer=country_name.get()
        l_answer = answer.capitalize()
        sql_command = "SELECT * FROM covid WHERE `name` = ?;"
        values = (l_answer,)
        cursor.execute(sql_command,values)
        data = cursor.fetchall()
        users0.set(data[0][0])
        users1.set(data[0][1])
        users2.set(data[0][2])
        users3.set(data[0][3])
        users4.set(data[0][4])
        users5.set(data[0][5])
    except:
        error=Label(frame2,text = "Error: no such country in database, try again",fg="red",font=("sand script",6))
        error.place(x=440,y=108)
        

submit=Button(frame2, text="SUBMIT", fg="black",font=("arial",13),command=subby)
submit.place(x=260,y=150)

bobert.mainloop()
