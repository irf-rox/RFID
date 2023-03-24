from tkinter import *
import customtkinter
import mysql.connector as mysql
from PIL import ImageTk,Image
from tkinter import ttk
from tkinter import messagebox
import os
import serial
import csv

def sup(*funcs):
    def combined_func(*args, **kwargs):
        for f in funcs:
            f(*args, **kwargs)

    return combined_func

mydb = mysql.connect(host="localhost",user="root",password="root")
cursor=mydb.cursor()
cursor.execute("create database if not exists rfid")
cursor.execute("use rfid")

cursor.execute("create table if not exists user1(name varchar(20),id varchar(20),password varchar(20))")
cursor.execute("create table if not exists vehicle(name varchar(20),vehicle_num varchar(20) primary key)")

customtkinter.set_appearance_mode("dark")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"

root = customtkinter.CTk()
root.geometry('1280x680')
root.resizable(width='False', height='False')
root.title("Vehicle Details Detector Pro")

def f5():
    frame_5 = customtkinter.CTkFrame(master=root)
    frame_5.pack(pady=20, padx=60, fill="both", expand=True)

    label_6 = customtkinter.CTkLabel(master=frame_5, justify=customtkinter.LEFT, text="Scan Successful",
                                     font=("Book Antiqua", 50))
    label_6.place(relx=0.25, rely=0.2)

    label_6 = customtkinter.CTkLabel(master=frame_5, justify=customtkinter.LEFT, text="Details:",
                                     font=("Book Antiqua", 50))
    label_6.place(relx=0.25, rely=0.35)

    button_5 = customtkinter.CTkButton(master=frame_5, text="FINISH", command=sup(frame_5.destroy, f3))
    button_5.place(relx=0.45, rely=0.85)

def rf_read():
    global l
    l=[]
    ser = serial.Serial('COM6', 9600)
    l=[]

    while True:
        data = ser.readline().decode().strip()
        l.append(data.split())
        x=(len(l)+1)

        if x%6==0:
            print("Vehicle number : ",l[x-2][0],"\nOwner Name : ",l[x-2][1])
            cursor.execute("insert ignore into vehicle values('{}','{}')".format(l[x-2][1], l[x-2][0]))
            mydb.commit()

        if x==30:
            break

def f4():
    global frame_4
    frame_4 = customtkinter.CTkFrame(master=root)
    frame_4.pack(pady=20, padx=60, fill="both", expand=True)

    label_5 = customtkinter.CTkLabel(master=frame_4, justify=customtkinter.LEFT, text="Ready to Scan", font=("Book Antiqua", 50))
    label_5.place(relx=0.15, rely=0.3)

    button_5 = customtkinter.CTkButton(master=frame_4, command=sup(frame_4.destroy, f3), text="Back")
    button_5.place(relx=0.85, rely=0.05)

    button_6 = customtkinter.CTkButton(master=frame_4, text="Start Scanning", command=sup(rf_read))
    button_6.place(relx=0.45, rely=0.5)

def fn():
    f5=Frame(root, width='1280', height='680', bg='#2B2B2B')
    f5.pack(pady=20, padx=60, fill="both", expand=True)


    back=Button(f5,bg='#1F6AA5',fg='white',relief='flat',text='Back',font=("Book Antiqua", 20),command=sup(f5.destroy,f3))
    back.place(relx=0.9,rely=0.05)

    f5x=Frame(f5,width='1280', height='580')
    f5x.place(relx=0.05, rely=0.2)

    my_canvas=Canvas(f5x,width=1280,height=500, bg="black")
    my_canvas.pack(side=LEFT,fill=BOTH,expand=0)
    
    my_scrollbar=ttk.Scrollbar(f5x,orient=VERTICAL,command=my_canvas.yview,)
    my_scrollbar.pack(side=RIGHT,fill=Y)
    
    my_canvas.configure(yscrollcommand=my_scrollbar.set)
    my_canvas.bind('<Configure>',lambda e: my_canvas.configure(scrollregion=my_canvas.bbox('all')))
    secondframe=Frame(my_canvas,bg="black")        
    my_canvas.create_window((0,0),window=secondframe,anchor='nw',)
        
    global rows
    cursor.execute("SELECT * FROM vehicle")
    
    l=[('Owner Name','Vehicle Number')]
    
    rows=cursor.fetchall()
   
    cl=l+rows
    
    trow=len(cl)
    tcolumn=len(cl[0])
    
    for i in range(trow):
        for j in range(tcolumn):
            a=Label(secondframe, width=90,fg='white',bg='black')
            a.grid(row=i, column=j)
            a.config(text=cl[i][j])
            a.grid_propagate(0)

def fx () :
    sl=[('Owner Name','Vehicle Number')]

    rslt ="SELECT * from vehicle"
    cursor.execute(rslt)
    result1 =sl + cursor.fetchall()
  
    with open('scanned_vehicle_det.csv', 'w') as file:
        writer = csv.writer(file)
        writer.writerows(result1)

    frame_31 = customtkinter.CTkFrame(master=root)
    frame_31.pack(pady=20, padx=60, fill="both", expand=True)

    label_5 = customtkinter.CTkLabel(master=frame_31, justify=customtkinter.LEFT, text="Successfully Exported",font=("Book Antiqua", 50))
    label_5.place(relx=0.31, rely=0.4)

    button_1z = customtkinter.CTkButton(master=frame_31, text="Done",height=50, width=100, font=("book antiqua", 20),command=sup(frame_31.destroy, f3))
    button_1z.place(relx=0.45, rely=0.8)

def f3():
    frame_3 = customtkinter.CTkFrame(master=root)
    frame_3.pack(pady=20, padx=60, fill="both", expand=True)

    button_1 = customtkinter.CTkButton(master=frame_3, text="Scan Tag", width=400, height=400,font=("book antiqua", 30),command=sup(frame_3.destroy, f4))
    button_1.place(relx=0.1, rely=0.2)

    button_2 = customtkinter.CTkButton(master=frame_3, width=400, height=400, text="View scanned vehicles", font=("book antiqua", 30),command=sup(frame_3.destroy, fn))
    button_2.place(relx=0.6, rely=0.2)

    buttona= customtkinter.CTkButton(master=frame_3, text="Export", command=sup(frame_3.destroy, fx))
    buttona.place(relx=0.7, rely=0.04)

    button = customtkinter.CTkButton(master=frame_3, text="Log-Out", command=sup(frame_3.destroy, f1))
    button.place(relx=0.85, rely=0.04)

def f2():
    def check():
        if (entry_3x.get()==entry_4x.get()):
            cursor.execute("insert into user1 values('{}','{}','{}')".format(entry_1x.get(), entry_2x.get(), entry_3x.get()))
            mydb.commit()
            f3()

        else:
            messagebox.showerror('Error', "Passwords don't match")
            frame_2.destroy()
            f2()
            
    frame_2 = customtkinter.CTkFrame(master=root)
    frame_2.pack(pady=20, padx=60, fill="both", expand=True)

    label_1 = customtkinter.CTkLabel(master=frame_2, justify=customtkinter.LEFT, text="Name :")
    label_1.place(rely=0.3, relx=0.09)

    global entry_1x

    entry_1x = customtkinter.CTkEntry(master=frame_2, width=250)
    entry_1x.place(rely=0.3, relx=0.25)

    label_2 = customtkinter.CTkLabel(master=frame_2, justify=customtkinter.LEFT, text="User ID:")
    label_2.place(rely=0.4, relx=0.09)

    global entry_2x

    entry_2x = customtkinter.CTkEntry(master=frame_2, width=250)
    entry_2x.place(rely=0.4, relx=0.25)

    label_3 = customtkinter.CTkLabel(master=frame_2, justify=customtkinter.LEFT, text="Password :")
    label_3.place(rely=0.5, relx=0.09)

    global entry_3x
    entry_3x = customtkinter.CTkEntry(master=frame_2, width=250)
    entry_3x.place(rely=0.5, relx=0.25)
    passw=entry_3x.get()

    label_4 = customtkinter.CTkLabel(master=frame_2, justify=customtkinter.LEFT, text="Re-enter password :")
    label_4.place(rely=0.6, relx=0.09)

    global entry_4x
    entry_4x = customtkinter.CTkEntry(master=frame_2, width=250)
    entry_4x.place(rely=0.6, relx=0.25)

    button = customtkinter.CTkButton(master=frame_2, text="Create account", command=sup(check,frame_2.destroy))
    button.place(rely=0.8, relx=0.30)

def f1():
    def chpwd():
        cursor.execute("SELECT * FROM user1")
        r=cursor.fetchall()
        c=0
        for i in r:
            if entry_1.get()==i[1]:
                c+=1

        if c==0:
            messagebox.showerror('Error', "Account doesn't exist!")
            frame_1.destroy()
            f1()

        else:
            if entry_2.get()!=i[2]:
                messagebox.showerror('Error', "ID and password don't match!")
                frame_1.destroy()
                f1()

            else:
                frame_1.destroy()
                f3()

    frame_1 = customtkinter.CTkFrame(master=root)
    frame_1.pack(pady=30, padx=60, fill="both", expand=True)

    label_1 = customtkinter.CTkLabel(master=frame_1, justify=customtkinter.LEFT, text="USER LOGIN",
                                     font=("book antiqua", 50))
    label_1.place(relx=0.35, rely=0.1)

    global entry1, entry2

    entry_1 = customtkinter.CTkEntry(master=frame_1, placeholder_text="ID", width=200)
    entry_1.place(relx=0.38, rely=0.33)

    entry_2 = customtkinter.CTkEntry(master=frame_1, placeholder_text="PASSWORD", show="•", width=200)
    entry_2.place(relx=0.38, rely=0.44)

    button = customtkinter.CTkButton(master=frame_1, text="LOGIN", command=sup(frame_1.destroy, f3))#chpwd))
    button.place(relx=0.35, rely=0.58)

    button = customtkinter.CTkButton(master=frame_1, text="Sign-Up here", command=sup(frame_1.destroy, f2))
    button.place(relx=0.5, rely=0.58)


f1()
root.mainloop()
