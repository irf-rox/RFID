from tkinter import *
import customtkinter
import mysql.connector as mysql
from PIL import ImageTk,Image
from tkinter import ttk
from tkinter import messagebox
from functools import partial
import os
from tkinter.filedialog import askopenfilename
import serial
import csv

def sup(*funcs):
    def combined_func(*args, **kwargs):
        for f in funcs:
            f(*args, **kwargs)

    return combined_func


customtkinter.set_appearance_mode("dark")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"

root = customtkinter.CTk()
root.geometry('1280x680')
root.resizable(width='False', height='False')
root.title("Vehicle Details Detector Pro")


def f8():
    frame_8 = customtkinter.CTkFrame(master=root)
    frame_8.pack(pady=20, padx=60, fill="both", expand=True)

    button_1 = customtkinter.CTkButton(master=frame_8, text="Done", command=sup(frame_8.destroy, f3))
    button_1.place(relx=0.45, rely=0.8)


def f7():
    frame_7 = customtkinter.CTkFrame(master=root)
    frame_7.pack(pady=20, padx=60, fill="both", expand=True)

    label_5 = customtkinter.CTkLabel(master=frame_7, justify=customtkinter.LEFT, text="Tap your RFID tag now",
                                     font=("Book Antiqua", 50))
    label_5.place(relx=0.15, rely=0.3)

    button_1 = customtkinter.CTkButton(master=frame_7, text="Back", command=sup(frame_7.destroy, f3))
    button_1.place(relx=0.86, rely=0.04)
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


def f4():
    frame_4 = customtkinter.CTkFrame(master=root)
    frame_4.pack(pady=20, padx=60, fill="both", expand=True)

    label_5 = customtkinter.CTkLabel(master=frame_4, justify=customtkinter.LEFT, text="Scanning for Vehicle",
                                     font=("Book Antiqua", 50))
    label_5.place(relx=0.15, rely=0.3)

    button_5 = customtkinter.CTkButton(master=frame_4, command=sup(frame_4.destroy, f3), text="Back")
    button_5.place(relx=0.85, rely=0.05)


def f3():
    frame_3 = customtkinter.CTkFrame(master=root)
    frame_3.pack(pady=20, padx=60, fill="both", expand=True)

    button_1 = customtkinter.CTkButton(master=frame_3, text="Scan Tag", font=("book antiqua", 30),
                                       command=sup(frame_3.destroy, f4))
    button_1.place(relx=0.4, rely=0.45)

    '''button_2 = customtkinter.CTkButton(master=frame_3, text="Load Tag", font=("book antiqua", 30),
                                       command=sup(frame_3.destroy, f6))
    button_2.place(relx=0.3, rely=0.45)'''

    button = customtkinter.CTkButton(master=frame_3, text="Log-Out", command=sup(frame_3.destroy, f1))
    button.place(relx=0.47, rely=0.8)

def f2():
    def check():
        if (entry_3x.get()==entry_4x.get()):
            f3()
        else:
            messagebox.showerror('Error', "Passwords don't match")
            frame_2.destroy()
            f2()
            
    frame_2 = customtkinter.CTkFrame(master=root)
    frame_2.pack(pady=20, padx=60, fill="both", expand=True)

    label_1 = customtkinter.CTkLabel(master=frame_2, justify=customtkinter.LEFT, text="Name :")
    label_1.place(rely=0.3, relx=0.09)

    entry_1 = customtkinter.CTkEntry(master=frame_2, width=250)
    entry_1.place(rely=0.3, relx=0.25)
    name=entry_1.get()

    label_2 = customtkinter.CTkLabel(master=frame_2, justify=customtkinter.LEFT, text="User ID:")
    label_2.place(rely=0.4, relx=0.09)

    entry_2 = customtkinter.CTkEntry(master=frame_2, width=250)
    entry_2.place(rely=0.4, relx=0.25)
    id=entry_2.get()

    label_3 = customtkinter.CTkLabel(master=frame_2, justify=customtkinter.LEFT, text="Password :")
    label_3.place(rely=0.5, relx=0.09)

    global entry_3x
    entry_3x = customtkinter.CTkEntry(master=frame_2, width=250)
    entry_3x.place(rely=0.5, relx=0.25)

    label_4 = customtkinter.CTkLabel(master=frame_2, justify=customtkinter.LEFT, text="Re-enter password :")
    label_4.place(rely=0.6, relx=0.09)

    global entry_4x
    entry_4x = customtkinter.CTkEntry(master=frame_2, width=250)
    entry_4x.place(rely=0.6, relx=0.25)

    button = customtkinter.CTkButton(master=frame_2, text="Create account", command=sup(check,frame_2.destroy))
    button.place(rely=0.8, relx=0.30)



def f1():
    frame_1 = customtkinter.CTkFrame(master=root)
    frame_1.pack(pady=30, padx=60, fill="both", expand=True)

    label_1 = customtkinter.CTkLabel(master=frame_1, justify=customtkinter.LEFT, text="USER LOGIN",
                                     font=("book antiqua", 50))
    label_1.place(relx=0.35, rely=0.1)

    button = customtkinter.CTkButton(master=frame_1, text="LOGIN", command=sup(frame_1.destroy, f3))
    button.place(relx=0.35, rely=0.58)

    entry_1 = customtkinter.CTkEntry(master=frame_1, placeholder_text="ID", width=200)
    entry_1.place(relx=0.38, rely=0.33)

    entry_1 = customtkinter.CTkEntry(master=frame_1, placeholder_text="PASSWORD", show="•", width=200)
    entry_1.place(relx=0.38, rely=0.44)

    button = customtkinter.CTkButton(master=frame_1, text="Sign-Up here", command=sup(frame_1.destroy, f2))
    button.place(relx=0.5, rely=0.58)

'''mydb=mysql.connect(host="localhost",username="",password="")
cursor=mydb.cursor()
cursor.execute("create database rfid")
cursor.execute("create table user1(name varchar2(20),id varchar2(20,password varchar2(20))")'''
f1()  # function call
root.mainloop()
