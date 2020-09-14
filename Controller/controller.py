import sqlite3
import tkinter
from tkinter import *
from model import menu
from PIL import ImageTk
from tkinter import messagebox

class login:
    def __init__(self, root):
        self.root = root
        self.root.title("HOSPITAL MANAGEMENT SYSTEM")
        self.root.geometry('950x500+0+0')
        self.root.wm_iconbitmap('C:/Users/BC/Downloads/Hospital management system/Hospital-management-python--master_3/Hospital-management-python--master/icon1.ico')
        self.root.resizable(False,False)

        ###### BG IMAGE #########
        self.bg=ImageTk.PhotoImage(file="H:/SUMMER 2020/CSE 470/Project/Testing 3.0/hms.jpg")
        self.bg_image=Label(self.root,image=self.bg).place(x=0,y=0,relwidth=1,relheight=1)

        #######Login Frame
        Frame_login=Frame(self.root,bg="white")
        Frame_login.place(x=250,y=50,height=340,width=500)

        title=Label(Frame_login,text="Login Here",font=("times new roman",35,"bold"),fg='#d77337',bg="white").place(x=90,y=30)
        desc=Label(Frame_login,text="Database Employee Login Area",font=("times new roman",15,"bold"),fg='#d77337',bg="white").place(x=90,y=100)
        lbl_user=Label(Frame_login,text="Username",font=("times new roman",15,"bold"),fg='black',bg="white").place(x=90,y=140)
        self.txt_user=Entry(Frame_login,font=("times new roman",15),bg="lightgray")
        self.txt_user.place(x=90,y=170,width=350,height=35)

        lbl_pass=Label(Frame_login,text="Password",font=("times new roman",15,"bold"),fg='black',bg="white").place(x=90,y=210)
        self.txt_pass=Entry(Frame_login,font=("times new roman",15),bg="lightgray",show='*')
        self.txt_pass.place(x=90, y=240, width=350, height=35)

        forget_btn=Button(Frame_login,text="Forget password ?",bg="white",fg="#d77337",font=("times new roman",12)).place(x=90,y=280)
        reset_button = Button(Frame_login, command=self.reset_button,text="RESET", bg="white", fg="#d77337",font=("times new roman", 12)).place(x=220, y=280)
        login_btn = Button(self.root, command=self.login_function,text="Login", bg="#d77337", fg="white",font=("times new roman", 20)).place(x=450, y=370,width=150,height=40)

    def reset_button(self):
        self.txt_user.delete(0, END)
        self.txt_pass.delete(0, END)

    def login_function(self):
        if self.txt_pass.get == "12345" or self.txt_user.get() == "admin":
            menu()
            #messagebox.showinfo("Welcome", f"Welcome {self.txt_user.get()}\nYour Password: {self.txt_pass.get()}")
        elif self.txt_pass.get=="" or self.txt_user.get()=="":
            messagebox.showerror("Error"," All fields are required",parent=self.root)
        else:
            messagebox.showerror("Error", " Invalid Username/Password", parent=self.root)



root=Tk()
obj=login(root)
root.mainloop()







# Login part
# root=login page
# root1=menu
# rootp=patient form

# variables
# root = None
# userbox = None
# passbox = None
# topframe = None
# bottomframe = None
# frame3 = None
# login = None
#
#
# # command for login button
# def GET():
#     global userbox, passbox, error
#     S1 = userbox.get()
#     S2 = passbox.get()
#     if (S1 == 'admin1' and S2 == '1234'):
#         menu()
#     elif (S1 == 'admin2' and S2 == '1234'):
#         menu()
#     else:
#         error = tkinter.Label(bottomframe, text="Wrong Id / Password \n TRY AGAIN", fg="red", font="bold")
#         error.pack()
#
# def reset_button():
#     userbox.delete(0, END)
#     passbox.delete(0, END)
#
# # LOGIN PAGE WINDOW
# def Entry():
#     global userbox, passbox, login, topframe, bottomframe, image_1
#     root = tkinter.Tk()
#     root.geometry("950x550")
#     root.configure(bg='grey')
#
#     topframe = tkinter.Frame(root)
#     topframe.configure(bg='grey')
#     topframe.pack()
#
#     middleframe = tkinter.Frame(root)
#     middleframe.configure(bg='grey')
#     middleframe.place(x=150,y=150,height=340,width=500)
#     middleframe.pack()
#
#     bottomframe = tkinter.Frame(root)
#     bottomframe.configure(bg='grey')
#     bottomframe.pack()
#
#     heading = tkinter.Label(topframe, text="WELCOME TO HOSPITAL MANAGEMENT SYSTEM", bg='grey', fg='black',
#                             font='Times 16 bold italic')
#
#     username = tkinter.Label(topframe, padx=20, text="USERNAME", font='10', bg='grey', fg='black')
#     userbox = tkinter.Entry(topframe)
#
#     password = tkinter.Label(middleframe, padx=20, text="PASSWORD", font='10', bg='grey', fg='black')
#     passbox = tkinter.Entry(middleframe, show="*")
#
#     login = tkinter.Button(bottomframe, text="LOGIN", command=GET, font="arial 8 bold")
#     reset = tkinter.Button(bottomframe, text='RESET', font="arial 8 bold", command=reset_button)
#     heading.pack()
#     username.pack()
#     userbox.pack()
#     password.pack()
#     passbox.pack()
#     login.pack(side="left")
#     reset.pack(side="right")
#     # root.overrideredirect(True)
#     # title_bar = Frame(root, bg='white', relief='raised', bd=2)
#     # close_button = Button(title_bar, text='Close this Window', command=root.destroy)
#     # title_bar.pack(expand=1, fill="x")
#     # close_button.pack(side="right")
#     root.title("DATABASE LOGIN")
#     root.wm_iconbitmap(
#         'C:/Users/BC/Downloads/Hospital management system/Hospital-management-python--master_3/Hospital-management-python--master/icon1.ico')
#     root.mainloop()
#
#
# Entry()
