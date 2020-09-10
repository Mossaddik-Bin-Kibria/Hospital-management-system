from view import Room_all
from view import BILLING
from view import emp_screen
from view import appo

import tkinter
import sqlite3
import tkinter.messagebox

# from PATDELSU import P_display
# from PATDELSU import D_display
# from PATDELSU import P_UPDATE


conn=sqlite3.connect("MDBA.db")
print("DATABASE CONNECTION SUCCESSFUL")

#variables
root1=None
rootp=None
pat_ID=None
pat_name=None
pat_dob=None
pat_address=None
pat_sex=None
pat_BG=None
pat_email=None
pat_contact=None
pat_contactalt=None
pat_CT=None

#variables
rootU=None
rootD=None
rootS=None
head=None
inp_s=None
searchB=None

inp_d=None
entry1=None
errorD=None
disd1=None

##variables for update

pat_ID=None
pat_name=None
pat_dob=None
pat_address=None
pat_sex=None
pat_BG=None
pat_email=None
pat_contact=None
pat_contactalt=None
pat_CT=None

labelu=None
bu1=None


#EXIT for MENU
def ex():
    global root1
    root1.destroy()

#MENU BUTTONS
def menu():
    global root1,button1,button2,button3,button4,button5,m,button6
    root1=tkinter.Tk()
    root1.geometry('545x400+0+0')
    root1.title("MAIN MENU")
    root1.wm_iconbitmap('C:/Users/BC/Downloads/Hospital management system/Hospital-management-python--master_3/Hospital-management-python--master/icon1.ico')
    m=tkinter.Label(root1,text="MENU",padx='230',pady=32,font='Times 20 bold italic',fg='#d77337',bg='white')
    button1=tkinter.Button(root1,text="1.PATIENT REGISTRATION",command=PAT,font='Times 12',padx='172',pady='10',bg='white',fg='#d77337')
    button2 = tkinter.Button(root1, text="2.ROOM ALLOCATION",font='Times 12',padx='185',pady='10',bg='white',fg='#d77337',command=Room_all)
    button3 = tkinter.Button(root1, text="3.EMPLOYEE REGISTRATION",font='Times 12',padx='163',pady='10',bg='white',fg='#d77337',command=emp_screen)
    button4 = tkinter.Button(root1, text="4.BOOK APPOINTMENT",font='Times 12',padx='181',pady='10',bg='white',fg='#d77337',command=appo)
    button5 = tkinter.Button(root1, text="5.PATIENT BILL",font='Times 12',padx='211',pady='10',bg='white',fg='#d77337',command=BILLING)
    button6 = tkinter.Button(root1, text="6.EXIT",command=ex,font='Times 12',padx='245',pady='10',bg='white',fg='#d77337')
    m.place(x=0,y=0,)
    button1.pack(side=tkinter.TOP)
    button1.place(x=1,y=100)
    button2.pack(side=tkinter.TOP)
    button2.place(x=1,y=150)
    button3.pack(side=tkinter.TOP)
    button3.place(x=1,y=200)
    button4.pack(side=tkinter.TOP)
    button4.place(x=1, y=250)
    button5.pack(side=tkinter.TOP)
    button5.place(x=1,y=300)
    button6.pack(side=tkinter.TOP)
    button6.place(x=1,y=350)
    root1.mainloop()

p=None
#input patient form
def IN_PAT():
    global pp1, pp2, pp3, pp4, pp5, pp6, pp7, pp8, pp9, pp10,ce1,conn
    conn=sqlite3.connect("MDBA.db")
    conn.cursor()
    pp1=pat_ID.get()
    pp2=pat_name.get()
    pp3=pat_sex.get()
    pp4=pat_BG.get()
    pp5=pat_dob.get()
    pp6=pat_contact.get()
    pp7=pat_contactalt.get()
    pp8=pat_address.get()
    pp9=pat_CT.get()
    pp10=pat_email.get()
    conn.execute('INSERT INTO PATIENT VALUES(?,?,?,?,?,?,?,?)',(pp1,pp2,pp3,pp4,pp5,pp8,pp9,pp10,))
    conn.execute('INSERT INTO CONTACT_NO VALUES (?,?,?)',(pp1,pp6,pp7,))
    tkinter.messagebox.showinfo("MEDANTA DATABSE SYSTEM","DETAILS INSERTED INTO DATABASE")
    conn.commit()


#exit from patient form
def EXO():
    rootp.destroy()

#function for patient form help
def nothing():
    print("CONTACT DATABASE HEAD :921 ")

def nothing1():
    print("MADE BY BHAVIYA BATRA")

#PATIENT FORM
back=None
SEARCH=None
DELETE=None
UPDATE=None

def PAT():
    global pat_address, pat_BG, pat_contact, pat_contactalt, pat_CT, pat_dob, pat_email, pat_ID, pat_name, pat_sex
    global rootp,regform,id,name,dob,sex,email,ct,addr,c1,c2,bg,SUBMIT,menubar,filemenu,back,SEARCH,DELETE,UPDATE
    rootp=tkinter.Tk()
    rootp.title("MEDANTA PATIENT FORM")
    menubar=tkinter.Menu(rootp)
    filemenu=tkinter.Menu(menubar,tearoff=0)
    filemenu.add_command(label="NEW",command=PAT)
    filemenu.add_separator()
    filemenu.add_command(label="EXIT", command=EXO)
    helpmenu=tkinter.Menu(menubar,tearoff=0)
    helpmenu.add_command(label="HELP",command=nothing)
    helpmenu.add_command(label="ABOUT",command=nothing1)
    menubar.add_cascade(label="File", menu=filemenu)
    menubar.add_cascade(label="Help", menu=helpmenu)
    rootp.config(menu=menubar)
    regform=tkinter.Label(rootp,text="REGISTRATION FORM",font="Arial 16 bold")
    id=tkinter.Label(rootp,text="PATIENT ID")
    pat_ID=tkinter.Entry(rootp)
    name=tkinter.Label(rootp,text="PATIENT NAME")
    pat_name = tkinter.Entry(rootp)
    sex=tkinter.Label(rootp,text="SEX")
    pat_sex=tkinter.Entry(rootp)
    dob=tkinter.Label(rootp, text="DOB (YYYY-MM-DD)")
    pat_dob=tkinter.Entry(rootp)
    bg=tkinter.Label(rootp, text="BLOOD GROUP")
    pat_BG=tkinter.Entry(rootp)
    c1=tkinter.Label(rootp, text="CONTACT NUMBER")
    pat_contact=tkinter.Entry(rootp)
    c2=tkinter.Label(rootp, text="ALTERNATE CONTACT")
    pat_contactalt=tkinter.Entry(rootp)
    email=tkinter.Label(rootp, text="EMAIL")
    pat_email = tkinter.Entry(rootp)
    ct=tkinter.Label(rootp,text="CONSULTING TEAM / DOCTOR")
    pat_CT=tkinter.Entry(rootp)
    addr=tkinter.Label(rootp, text="ADDRESS")
    pat_address=tkinter.Entry(rootp)
    back=tkinter.Button(rootp,text="<< BACK",command=menu)
    SEARCH=tkinter.Button(rootp,text="  SEARCH >>  ",command=P_display)
    DELETE=tkinter.Button(rootp,text="  DELETE  ",command=D_display)
    UPDATE=tkinter.Button(rootp,text="  UPDATE  ",command=P_UPDATE)
    SUBMIT=tkinter.Button(rootp,text="  SUBMIT  ",command=IN_PAT,)
    regform.pack()
    id.pack()
    pat_ID.pack()
    name.pack()
    pat_name.pack()
    sex.pack()
    pat_sex.pack()
    dob.pack()
    pat_dob.pack()
    bg.pack()
    pat_BG.pack()
    c1.pack()
    pat_contact.pack()
    c2.pack()
    pat_contactalt.pack()
    email.pack()
    pat_email.pack()
    ct.pack()
    pat_CT.pack()
    addr.pack()
    pat_address.pack()
    SUBMIT.pack()
    back.pack(side=tkinter.LEFT)
    UPDATE.pack(side=tkinter.LEFT)
    DELETE.pack(side=tkinter.LEFT)
    SEARCH.pack(side=tkinter.LEFT)
    rootp.mainloop()


def Search_button():
    global inp_s,entry,errorS,t,i,q,dis1,dis2,dis3,dis4,dis5,dis6,dis7,dis8,dis9,dis10
    global l1,l2,l3,l4,l5,l6,l7,l8,l9,l10
    c1=conn.cursor()
    inp_s=entry.get()
    p=list(c1.execute('select * from PATIENT where PATIENT_ID=?',(inp_s,)))
    if (len(p)==0):
        errorS=tkinter.Label(rootS,text="PATIENT RECORD NOT FOUND")
        errorS.pack()
    else:
        t=c1.execute('SELECT * FROM PATIENT NATURAL JOIN CONTACT_NO where PATIENT_ID=?',(inp_s,));
        for i in t:
            l1=tkinter.Label(rootS,text="PATIENT ID",fg='blue')
            dis1=tkinter.Label(rootS,text=i[0])
            l2=tkinter.Label(rootS,text="PATIENT NAME",fg='blue')
            dis2=tkinter.Label(rootS,text=i[1])
            l3=tkinter.Label(rootS,text="PATIENT SEX",fg='blue')
            dis3=tkinter.Label(rootS,text=i[2])
            l4=tkinter.Label(rootS,text="PATIENT BLOOD GROUP",fg='blue')
            dis4=tkinter.Label(rootS,text=i[3])
            l5=tkinter.Label(rootS,text="PATIENT DATE OF BIRTH",fg='blue')
            dis5=tkinter.Label(rootS,text=i[4])
            l6=tkinter.Label(rootS,text="PATIENT ADDRESS",fg='blue')
            dis6=tkinter.Label(rootS,text=i[5])
            l7=tkinter.Label(rootS,text="PATIENT DOCTOR/TEAM",fg='blue')
            dis7=tkinter.Label(rootS,text=i[6])
            l8=tkinter.Label(rootS,text="PATIENT EMAIL",fg='blue')
            dis8=tkinter.Label(rootS,text=i[7])
            l9=tkinter.Label(rootS,text="PATEINT CONTACT NO",fg='blue')
            dis9=tkinter.Label(rootS,text=i[8])
            l10=tkinter.Label(rootS,text="PATIENT ALTERNATE CONTACT",fg='blue')
            dis10=tkinter.Label(rootS,text=i[9])
            l1.pack()
            dis1.pack()
            l2.pack()
            dis2.pack()
            l3.pack()
            dis3.pack()
            l4.pack()
            dis4.pack()
            l5.pack()
            dis5.pack()
            l6.pack()
            dis6.pack()
            l7.pack()
            dis7.pack()
            l8.pack()
            dis8.pack()
            l9.pack()
            dis9.pack()
            l10.pack()
            dis10.pack()
            conn.commit()


def eXO():
    rootS.destroy()

##search window
def P_display():
    global rootS,head,inp_s,entry,searchB
    rootS=tkinter.Tk()
    rootS.title("SEARCH WINDOW")
    head=tkinter.Label(rootS,text="ENTER PATIENT ID TO SEARCH",fg="red")
    entry=tkinter.Entry(rootS)
    searchB=tkinter.Button(rootS,text='SEARCH',command=Search_button)
    menubar= tkinter.Menu(rootS)
    filemenu = tkinter.Menu(menubar, tearoff=0)
    filemenu.add_command(label="NEW", command=P_display)
    filemenu.add_separator()
    filemenu.add_command(label="EXIT", command=eXO)
    menubar.add_cascade(label="File", menu=filemenu)
    rootS.config(menu=menubar)
    head.pack()
    entry.pack()
    searchB.pack()
    rootS.mainloop()


#DELTE BUTTON
def Delete_button():
    global inp_d,entry1,errorD,disd1
    c1= conn.cursor()
    inp_d = entry1.get()
    p=list(conn.execute("select * from PATIENT where PATIENT_ID=?", (inp_d,)))
    if (len(p)==0):
        errorD = tkinter.Label(rootD, text="PATIENT RECORD NOT FOUND")
        errorD.pack()
    else:
        conn.execute('DELETE FROM PATIENT where PATIENT_ID=?',(inp_d,))
        disd1=tkinter.Label(rootD,text="PATIENT RECORD DELETED",fg='green')
        disd1.pack()
        conn.commit()


## DELETE SCREEN
def D_display():
    global rootD,headD,inp_d,entry1,DeleteB
    rootD=tkinter.Tk()
    rootD.title("DELETE WINDOW")
    headD=tkinter.Label(rootD,text="ENTER PATIENT ID TO DELETE",fg="blue")
    entry1=tkinter.Entry(rootD)
    DeleteB=tkinter.Button(rootD,text="DELETE",command=Delete_button)
    headD.pack()
    entry1.pack()
    DeleteB.pack()
    rootD.mainloop()


def up1():
    global u1, u2, u3, u4, u5, u6, u7, u8, u9, u10, ue1, conn
    conn.cursor()
    u1 = pat_ID.get()
    u2 = pat_name.get()
    u3 = pat_sex.get()
    u4 = pat_dob.get()
    u5 = pat_BG.get()
    u6 = pat_contact.get()
    u7 = pat_contactalt.get()
    u8 = pat_email.get()
    u9 = pat_CT.get()
    u10 = pat_address.get()
    conn = sqlite3.connect("MDBA.db")
    p = list(conn.execute("Select * from PATIENT where PATIENT_ID=?", (u1,)))
    if len(p) != 0:
        conn.execute('UPDATE PATIENT SET NAME=?,SEX=?,DOB=?,BLOOD_GROUP=?,ADDRESS=?,CONSULT_TEAM=?,EMAIL=? where PATIENT_ID=?', ( u2, u3, u4, u5, u10, u9, u8,u1,))
        conn.execute('UPDATE CONTACT_NO set CONTACTNO=?,ALT_CONTACT=? WHERE PATIENT_ID=?', ( u6, u7,u1,))
        tkinter.messagebox.showinfo("MEDANTA DATABSE SYSTEM", "DETAILS UPDATED INTO DATABASE")
        conn.commit()

    else:
        tkinter.messagebox.showinfo("MEDANTA DATABSE SYSTEM", "PATIENT IS NOT REGISTERED")

def EXITT():
    rootU.destroy()

##-----PATIENT UPDATE SCREEN -----##
def P_UPDATE():
    global pat_address, pat_BG, pat_contact, pat_contactalt, pat_CT, pat_dob, pat_email, pat_ID, pat_name, pat_sex
    global rootU, regform, id, name, dob, sex, email, ct, addr, c1, c2, bg, SUBMIT, menubar, filemenu, p1f, p2f,HEAD
    rootU = tkinter.Tk()
    rootU.title("UPDATE WINDOW")
    menubar = tkinter.Menu(rootU)
    filemenu = tkinter.Menu(menubar, tearoff=0)
    filemenu.add_command(label="NEW", command=P_UPDATE)
    filemenu.add_separator()
    filemenu.add_command(label="EXIT", command=EXITT)
    rootU.config(menu=menubar)
    menubar.add_cascade(label="File", menu=filemenu)
    HEAD=tkinter.Label(rootU,text="ENTER NEW DETAILS TO UPDATE",bg='black',fg='white')
    id = tkinter.Label(rootU, text="PATIENT ID")
    pat_ID = tkinter.Entry(rootU)
    name = tkinter.Label(rootU, text="PATIENT NAME")
    pat_name = tkinter.Entry(rootU)
    sex = tkinter.Label(rootU, text="SEX")
    pat_sex = tkinter.Entry(rootU)
    dob = tkinter.Label(rootU, text="DOB (YYYY-MM-DD)")
    pat_dob = tkinter.Entry(rootU)
    bg = tkinter.Label(rootU, text="BLOOD GROUP")
    pat_BG = tkinter.Entry(rootU)
    c1 = tkinter.Label(rootU, text="CONTACT NUMBER")
    pat_contact = tkinter.Entry(rootU)
    c2 = tkinter.Label(rootU, text="ALTERNATE CONTACT")
    pat_contactalt = tkinter.Entry(rootU)
    email = tkinter.Label(rootU, text="EMAIL")
    pat_email = tkinter.Entry(rootU)
    ct = tkinter.Label(rootU, text="CONSULTING TEAM / DOCTOR")
    pat_CT = tkinter.Entry(rootU)
    addr = tkinter.Label(rootU, text="ADDRESS")
    pat_address = tkinter.Entry(rootU)
    SUBMIT=tkinter.Button(rootU,text="SUBMIT",command=up1)
    HEAD.pack()
    id.pack()
    pat_ID.pack()
    name.pack()
    pat_name.pack()
    sex.pack()
    pat_sex.pack()
    dob.pack()
    pat_dob.pack()
    bg.pack()
    pat_BG.pack()
    c1.pack()
    pat_contact.pack()
    c2.pack()
    pat_contactalt.pack()
    email.pack()
    pat_email.pack()
    ct.pack()
    pat_CT.pack()
    addr.pack()
    pat_address.pack()
    SUBMIT.pack()
    rootU.mainloop()

