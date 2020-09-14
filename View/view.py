import tkinter
import sqlite3
import tkinter.messagebox

import controller
conn=sqlite3.connect("MDBA.db")

#variables
rootB=None
rootE=None
var=None
P_id=None
rootR=None
rootAA=None


def inp():
    global e1,e2,e3,e4,e5,e6,e7,e8,e9,var
    e1=t1.get()
    e2=t2.get()
    e3=str(var.get())
    e4=t3.get()
    e5=lb.get(tkinter.ACTIVE)
    e6=t4.get()
    e7=t5.get()
    e8=t6.get()
    e9=t7.get()
    conn = sqlite3.connect("MDBA.db")
    conn.execute("INSERT INTO employee VALUES(?,?,?,?,?,?,?,?,?)",(e1,e2,e3,e4,e5,e6,e7,e8,e9,))
    conn.commit()
    tkinter.messagebox.showinfo("MEDANTA DATABASE SYSTEM", "EMPLOYEE DATA ADDED")

def ex():
    rootE.destroy()

def emp_screen():
    global rootE,t1,t2,r1,r2,t3,lb,t4,t5,t6,t7,var
    rootE=tkinter.Tk()
    rootE.title("Employee registration")
    rootE.geometry('400x400')
    var = tkinter.StringVar(master=rootE)
    H=tkinter.Label(rootE,text="EMPLOYEE REGISTRATION",fg='grey',font="Arial 10 bold")
    H.place(x=50,y=20)
    l1=tkinter.Label(rootE,text="EMPLOYEE ID")
    l1.place(x="50",y="50")
    t1=tkinter.Entry(rootE)
    t1.place(x='170',y='50')
    l2 = tkinter.Label(rootE, text="EMPLOYEE NAME")
    l2.place(x=50,y=80)
    t2 = tkinter.Entry(rootE)
    t2.place(x='170', y='80')
    l3 = tkinter.Label(rootE, text="SEX")
    l3.place(x=50,y=110)
    r1 = tkinter.Radiobutton(rootE, text="MALE", variable=var, value="Male")
    r1.place(x=80, y=110)
    r2 = tkinter.Radiobutton(rootE, text="FEMALE", variable=var, value="Female")
    r2.place(x=150, y=110)
    l4 = tkinter.Label(rootE, text="AGE")
    l4.place(x=50,y=140)
    t3=tkinter.Entry(rootE)
    t3.place(x=80,y=140)
    l5 = tkinter.Label(rootE, text="EMPLOYEE TYPE")
    l5.place(x=50,y=170)
    scrollbar = tkinter.Scrollbar(rootE, width=2)
    scrollbar.place(x=260, y=140)
    lb = tkinter.Listbox(rootE, selectmode='SINGLE', exportselection=0, height=1, width=15,yscrollcommand = scrollbar.set)
    lb.insert(tkinter.END, "DOCTOR")
    lb.insert(tkinter.END, "NURSE")
    lb.insert(tkinter.END, "RECEPTIONIST")
    lb.place(x=150, y=170)
    lb.config(yscrollcommand=scrollbar.set)
    scrollbar.configure(command=lb.yview)
    l6=tkinter.Label(rootE,text="SALARY")
    l6.place(x=50,y=200)
    t4=tkinter.Entry(rootE)
    t4.place(x=110,y=200)
    l7 = tkinter.Label(rootE, text="EXPERIENCE")
    l7.place(x=50,y=230)
    t5 = tkinter.Entry(rootE)
    t5.place(x=140,y=230)
    l8 = tkinter.Label(rootE, text="MOBILE NO")
    l8.place(x=50,y=260)
    t6 = tkinter.Entry(rootE)
    t6.place(x=140,y=260)
    l9 = tkinter.Label(rootE, text="EMAIL")
    l9.place(x=50,y=290)
    t7=tkinter.Entry(rootE)
    t7.place(x=90,y=290)
    b1=tkinter.Button(rootE,text="SAVE",command=inp)
    b1.place(x=60,y=320)
    b2=tkinter.Button(rootE,text="DELETE EMPLOYEE",command=delo)
    b2.place(x=110,y=320)
    b3=tkinter.Button(rootE,text="EXIT",command=ex)
    b3.place(x=230,y=320)
    rootE.mainloop()

def delling():
    global d1,de
    de=str(d1.get())
    conn = sqlite3.connect("MDBA.db")
    p = list(conn.execute("select * from employee where EMP_ID=?", (de,)))
    if (len(p) != 0):
        conn.execute("DELETE from employee where EMP_ID=?", (de,))
        dme = tkinter.Label(rootDE, text="EMPLOYEE DELETED FROM DATABASE", fg="green")
        dme.place(x=20, y=100)
        conn.commit()
    else:
        error = tkinter.Label(rootDE, text="EMPLOYEE DOESN'T EXIST", fg="Red")
        error.place(x=20, y=100)

rootDE=None
def delo():
    global rootDE,d1
    rootDE=tkinter.Tk()
    rootDE.geometry("250x250")
    rootDE.title("EMPLOYEE DELETION")
    h1=tkinter.Label(rootDE,text="ENTER EMPLOYEE ID TO DELETE :")
    h1.place(x=20,y=10)
    d1=tkinter.Entry(rootDE)
    d1.place(x=20,y=40)
    B1=tkinter.Button(rootDE,text="DELETE",command=delling)
    B1.place(x=20,y=70)
    rootDE.mainloop()

def date_up():
    global b1,b2
    b1 = P_id.get()
    b2 = dd.get()
    conn.execute("UPDATE ROOM SET DATE_DISCHARGED=? where PATIENT_ID=?", (b2, b1,))
    conn.commit()
    tkinter.messagebox.showinfo("MEDANTA DATABASE SYSTEM", "DISCHARGE DATE UPDATED")

def up():
    global c1, b1, P_id, b3, b4, b5, b6, dd, treat_1, treat_2, cost_t, b7, b8, med, med_q, price, u
    conn = sqlite3.connect("MDBA.db")
    c1 = conn.cursor()
    b1 = P_id.get()
    b3 = treat_1.get(tkinter.ACTIVE)
    b4 = treat_2.get(tkinter.ACTIVE)
    b5 = cost_t.get()
    b6 = med.get(tkinter.ACTIVE)
    b7 = med_q.get(tkinter.ACTIVE)
    b8 = price.get()
    conn.execute("INSERT INTO TREATMENT VALUES(?,?,?,?)", (b1, b3, b4, b5,))
    conn.execute("INSERT INTO MEDICINE VALUES(?,?,?,?)", (b1, b6, b7, b8,))
    conn.commit()
    tkinter.messagebox.showinfo("MEDANTA DATABASE SYSTEM", "BILLING DATA SAVED")

def calci():
    global b1
    conn = sqlite3.connect("MDBA.db")
    u=conn.execute("Select sum(T_COST+ (M_COST*M_QTY) +(DATE_DISCHARGED-DATE_ADMITTED)*RATE) FROM ROOM NATURAL JOIN TREATMENT natural JOIN MEDICINE where PATIENT_ID=?",(b1,) )
    conn.commit()
    for ii in u:
        pp=tkinter.Label(rootB,text="TOTAL AMOUNT OUTSTANDING",fg='red',font='Arial 8 bold')
        pp.place(x="200", y='260')
        uu=tkinter.Label(rootB,text=ii[0])
        uu.place(x="230",y='290')

L1=None
L2=None
L3=None
L4=None

def exitt():
    rootB.destroy()

def BILLING():
    global rootB,L1,treat1,P_id,dd,cost,med,med_q,price,treat_1,treat_2,cost_t,j,jj,jjj,jjjj,L2,L3,L4
    rootB=tkinter.Tk()
    rootB.geometry("450x350")
    rootB.title("BILLING SYSTEM")
    head=tkinter.Label(rootB,text="PATIENT BILL",font="Arial 16 bold italic",fg='grey')
    head.place(x=100,y=10)
    id = tkinter.Label(rootB, text="PATIENT ID")
    id.place(x=20, y=60)
    P_id = tkinter.Entry(rootB)
    P_id.place(x=100, y=60)
    dd_l = tkinter.Label(rootB, text="DATE DISCHARGED")
    dd_l.place(x=20, y=100)
    dd = tkinter.Entry(rootB)
    dd.place(x=135, y=100)
    ddp=tkinter.Button(rootB,text="UPDATE DISCHARGE DATE",command=date_up)
    ddp.place(x=270,y=100)
    treat = tkinter.Label(rootB, text="SELECT TREATMENT")
    treat.place(x=20, y=140)
    L1 = ["CONSULATION","SURGERY","LAB TEST"]
    treat_1= tkinter.Listbox(rootB, width=15, height=1, selectmode='SINGLE', exportselection=0)
    for j in L1:
        treat_1.insert(tkinter.END, j)
    treat_1.place(x=140,y=140)
    treat_c = tkinter.Label(rootB, text="CODE")
    treat_c.place(x=240, y=140)
    L2 = ["C_1", "S_1", "L_1"]
    treat_2 = tkinter.Listbox(rootB, width=6, height=1, selectmode='SINGLE', exportselection=0)
    for jj in L2:
        treat_2.insert(tkinter.END, jj)
    treat_2.place(x=280, y=140)
    costl= tkinter.Label(rootB, text="COST ₹")
    costl.place(x=315, y=140)
    cost_t = tkinter.Entry(rootB,width=5)
    cost_t.place(x=350, y=140)
    med1 = tkinter.Label(rootB, text="SELECT MEDICINE")
    med1.place(x=20, y=180)
    L3 = ["NEURAL", "FANEKPLUS", "DISPRIN","DOLO+","BANDAGE","DIGENE"]
    med = tkinter.Listbox(rootB, width=15, height=1, selectmode='SINGLE', exportselection=0)
    for jjj in L3:
        med.insert(tkinter.END, jjj)
    med.place(x=140, y=180)
    med_ql = tkinter.Label(rootB, text="QUANTITY")
    med_ql.place(x=240, y=180)
    L4 = [1,2,3,4,5,6,7,8,9,10]
    med_q = tkinter.Listbox(rootB, width=4, height=1, selectmode='SINGLE', exportselection=0)
    for jjjj in L4:
        med_q.insert(tkinter.END, jjjj)
    med_q.place(x=280, y=180)
    pricel = tkinter.Label(rootB, text="PRICE ₹")
    pricel.place(x=315, y=180)
    price = tkinter.Entry(rootB, width=5)
    price.place(x=360, y=180)
    b1=tkinter.Button(rootB,text="GENERATE BILL",command=calci)
    b1.place(x="200",y="210")
    b2 = tkinter.Button(rootB, text="UPDATE DATA", command=up)
    b2.place(x="100", y="210")
    ee=tkinter.Button(rootB,text="EXIT",command=exitt)
    ee.place(x='310',y='210')
    rootB.mainloop()


##ROOM BUTTON
def room_button():
    global P_id,r1,r2,room_t,da,dd,rate,room_no,r3,r4,r5,r6,conn
    conn = sqlite3.connect("MDBA.db")
    r1=P_id.get()
    r2=room_t.get(tkinter.ACTIVE)
    r3=room_no.get(tkinter.ACTIVE)
    r4=rate.get()
    r5=da.get()
    r6=dd.get()
    conn.execute('INSERT INTO ROOM VALUES(?,?,?,?,?,?)',(r1,r3, r2, r4, r5, r6,))
    tkinter.messagebox.showinfo("MEDANTA DATABSE SYSTEM", "ROOM ALLOCATED")
    conn.commit()
    conn.close()

def update_button():
    global P_id,r1,r2,room_t,da,dd,rate,room_no,r3,r4,r5,r6,conn
    r1=P_id.get()
    r2=room_t.get(tkinter.ACTIVE)
    r3=room_no.get(tkinter.ACTIVE)
    r4=rate.get()
    r5=da.get()
    r6=dd.get()
    p = list(conn.execute("Select * from ROOM where PATIENT_ID=?", (r1,)))
    if len(p) != 0:
        conn.execute('UPDATE ROOM SET ROOM_NO=?,ROOM_TYPE=?,RATE=?,DATE_ADMITTED=?,DATE_DISCHARGED=? where PATIENT_ID=?',(r3, r2, r4, r5, r6,r1,))
        tkinter.messagebox.showinfo("MEDANTA DATABSE SYSTEM", "ROOM DETAILS UPDATED")
        conn.commit()
    else:
        tkinter.messagebox.showinfo("MEDANTA DATABSE SYSTEM", "PATIENT IS NOT ALLOCATED A ROOM")
##ROOT FOR DISPLAY ROOM INFO
rootRD=None

##EXIT FOR ROOM_PAGE
def EXITT():
    global rootR
    rootR.destroy()

##FUNCTION FOR ROOM DISPLAY BUTTON
def ROOMD_button():
    global r1,lr1,dis1,lr2,dis2,c1,ii,conn,c1,P_iid
    conn = sqlite3.connect("MDBA.db")
    c1=conn.cursor()
    r1=P_iid.get()
    p=list(c1.execute('select * from  ROOM  where PATIENT_ID=?',(r1,)))
    if (len(p)==0):
        tkinter.messagebox.showinfo("MEDANTA DATABASE SYSTEM","PATIENT NOT ALLOCATED ROOM")
    else:
        t=c1.execute('SELECT NAME,ROOM_NO,ROOM_TYPE FROM ROOM NATURAL JOIN PATIENT where PATIENT_ID=?',(r1,));
        for ii in t:
            lr0=tkinter.Label(rootRD,text="PATIENT NAME",fg='blue')
            dis0=tkinter.Label(rootRD,text=ii[0])
            lr0.place(x=50,y=120)
            dis0.place(x=50,y=140)
            lr1=tkinter.Label(rootRD,text="ROOM NO",fg='blue')
            dis1=tkinter.Label(rootRD,text=ii[1])
            lr1.place(x=50,y=170)
            dis1.place(x=50,y=190)
            lr2=tkinter.Label(rootRD,text="ROOM TYPE",fg='blue')
            dis2=tkinter.Label(rootRD,text=ii[2])
            lr2.place(x=50,y=220)
            dis2.place(x=50,y=240)

def exittt():
    rootRD.destroy()

def roomDD():
    global rootRD,ra1,ss,P_iid
    rootRD=tkinter.Tk()
    rootRD.geometry("280x280")
    rootRD.title("ROOM INFO")
    ra1=tkinter.Label(rootRD,text="ENTER PATIENT ID")
    ra1.place(x=20,y=20)
    P_iid=tkinter.Entry(rootRD)
    ss=tkinter.Button(rootRD,text="SEARCH",command=ROOMD_button)
    ra1.place(x=50, y=20)
    P_iid.place(x=50, y=50)
    ss.place(x=70,y=80)
    e=tkinter.Button(rootRD,text="EXIT",command=exittt)
    e.place(x=150,y=80)
    rootRD.mainloop()

def exitt():
    rootR.destroy()

L=None
L1=None
def Room_all():
    global rootR,r_head,P_id,id,room_tl,L,i,room_t,room_nol,room_no,L1,j,ratel,rate,da_l,da ,dd_l,dd,Submit,Update,cr
    rootR=tkinter.Tk()
    rootR.title("ROOM ALLOCATION")
    rootR.geometry("400x400")
    r_head=tkinter.Label(rootR,text="ROOM ALLOCATION",font='Times 13 bold',fg="dark grey")
    r_head.place(x=75,y=10)
    id=tkinter.Label(rootR,text="PATIENT ID")
    id.place(x=30,y=60)
    P_id=tkinter.Entry(rootR)
    P_id.place(x=100,y=60)
    room_tl=tkinter.Label(rootR,text="ROOM TYPE")
    room_tl.place(x=30, y=100)
    L=['SINGLE ROOM: Rs 4500','TWIN SHARING : Rs2500','TRIPLE SHARING: Rs2000']
    room_t= tkinter.Listbox(rootR, width=22, height=3, selectmode='SINGLE', exportselection=0)
    for i in L:
        room_t.insert(tkinter.END,i)
    room_t.place(x=105,y=100)
    room_nol=tkinter.Label(rootR,text="ROOM NUMBER")
    room_nol.place(x=30,y=180)
    L1=['101','102-AA','102-BB','103','104-AA','104-BB','105','206-AAA','206-BBB','206-CCC','207','208-AAA','208-BBB','208-CCC','210','211','302','304-AA','304-BB']
    room_no = tkinter.Listbox(rootR, width=8, height=1, selectmode='SINGLE', exportselection=0)
    for j in L1:
        room_no.insert(tkinter.END,j)
    room_no.place(x=135,y=180)
    ratel=tkinter.Label(rootR, text="ROOM CHARGES")
    ratel.place(x=30, y=220)
    rate=tkinter.Entry(rootR)
    rate.place(x=130, y=220)
    da_l = tkinter.Label(rootR, text="DATE ADMITTED")
    da_l.place(x=30,y=260)
    da=tkinter.Entry(rootR)
    da.place(x=140,y=260)
    dd_l = tkinter.Label(rootR, text="DATE DISCHARGED(0)")
    dd_l.place(x=30, y=300)
    dd =tkinter.Entry(rootR)
    dd.place(x=155, y=300)
    Submit=tkinter.Button(rootR,text="SUBMIT",command=room_button)
    Submit.place(x=30,y=340)
    Update=tkinter.Button(rootR,text="UPDATE",command=update_button)
    Update.place(x=130,y=340)
    cr=tkinter.Button(rootR,text='ROOM DETAILS',command=roomDD)
    cr.place(x=220,y=340)
    ee=tkinter.Button(rootR,text="EXIT",command=exitt)
    ee.place(x=330,y=340)
    rootR.mainloop()


def set():
    global e3,e1,e2,e4,e5,e6,conn
    p1=e1.get()
    p2=e2.get()
    p3=e3.get(tkinter.ACTIVE)
    p4=e4.get()
    p5=e5.get()
    p6=e6.get(1.0,tkinter.END)
    conn = sqlite3.connect("MDBA.db")
    conn.execute("Insert into appointment values(?,?,?,?,?,?)",(p1,p2,p3,p4,p5,p6,))
    conn.commit()
    tkinter.messagebox.showinfo("MEDANTA DATABASE SYSTEM", "APPOINTMENT SET SUCCSESSFULLY")


def appo():
    global rootAA,L,e1,e2,e3,e4,e5,e6
    rootAA=tkinter.Tk()
    rootAA.geometry("500x550")
    rootAA.title("APPOINTMENTS")
    H=tkinter.Label(rootAA,text="APOINTMENTS",fg="blue",font="Arial 10 bold")
    H.place(x=55,y=5)
    l1=tkinter.Label(rootAA,text="PATIENT ID")
    l1.place(x=20,y=30)
    e1=tkinter.Entry(rootAA)
    e1.place(x=100,y=30)
    l2 = tkinter.Label(rootAA,text="DOCTOR ID")
    l2.place(x=20,y=60)
    e2 = tkinter.Entry(rootAA)
    e2.place(x=110, y=60)
    l3 = tkinter.Label(rootAA,text="APPOINTMENT NO")
    l3.place(x=20,y=90)
    L=['A1','A2','A3','A4','A5','A6','A7','A8','A9','A10','A11','A12','A13','A14','A15','A16','A17','A18','A19','A20','A21','A22','A23','A24','A25','A26','A27','A28','A29','A30','A31','A32','A33','A34','A35','A36','A37','A38','A39','A40','A41','A42','A43','A44','A45','A46','A47','A48','A49','A50']
    e3=tkinter.Listbox(rootAA, width=15, height=1, selectmode='SINGLE', exportselection=0)
    for jjj in L:
        e3.insert(tkinter.END, jjj)
    e3.place(x=140,y=90)
    l4 = tkinter.Label(rootAA,text="APPOINTMENT TIME(HH:MM:SS)")
    l4.place(x=20,y=120)
    e4=tkinter.Entry(rootAA)
    e4.place(x=20,y=145)
    l5 = tkinter.Label(rootAA,text="APPOINTMENT DATE(YYYY-MM-DD)")
    l5.place(x=20,y=170)
    e5=tkinter.Entry(rootAA)
    e5.place(x=20,y=195)
    l6=tkinter.Label(rootAA,text="DESCRIPTION")
    l6.place(x=20,y=220)
    e6=tkinter.Text(rootAA,width=20,height=3)
    e6.place(x=20,y=240)
    scrollbar = tkinter.Scrollbar(rootAA,orient=tkinter.HORIZONTAL)
    scrollbar.place(x=235, y=90)
    e3.config(yscrollcommand=scrollbar.set)
    scrollbar.configure(command=e3.yview)
    b1=tkinter.Button(rootAA,text="SET APPOINTMENT",command=set)
    b1.place(x=20,y=310)
    b2=tkinter.Button(rootAA,text="Delete Appointment",command=dela)
    b2.place(x=180,y=310)
    b4=tkinter.Button(rootAA,text="TODAYS APPOINTMENTS",command=va)
    b4.place(x=320,y=310)
    rootAA.mainloop()

def remove():
    global e7,edd
    edd=str(e7.get())
    v=list(conn.execute("select * from appointment where AP_NO=?", (edd,)))
    if (len(v)==0):
        errorD = tkinter.Label(rootAA, text="PATIENT APPOINTMENT NOT FIXED",fg="red")
        errorD.place(x=20,y=420)
    else:
        conn.execute('DELETE FROM PATIENT where PATIENT_ID=?',(edd,))
        disd1=tkinter.Label(rootAA,text="PATIENT APPOINTMENT DELETED",fg='green')
        disd1.place(x=20,y=420)
        conn.commit()



def dela():
    global e1,e7
    l3 = tkinter.Label(rootAA, text="ENTER APPOINTMENT NO TO DELETE")
    l3.place(x=20, y=340)
    e7=tkinter.Entry(rootAA)
    e7.place(x=20,y=360)
    b3=tkinter.Button(rootAA,text="Delete",command=remove)
    b3.place(x=50,y=380)

rootAP=None

def viewappointment():
    global e8
    ap=str(e8.get())
    vv = list(conn.execute("select * from appointment where AP_DATE=?", (ap,)))
    if (len(vv) == 0):
        errorD = tkinter.Label(rootAA, text="NO APPOINTMENT FOR TODAY", fg="red")
        errorD.place(x=20, y=420)
    else:
        s=conn.execute("Select PATIENT_ID,NAME,AP_NO,EMP_NAME,AP_DATE,AP_TIME from PATIENT NATURAL JOIN employee NATURAL JOIN appointment where AP_DATE=?",(ap,))
        for i in s:
            s1=tkinter.Label(rootAP,text=i,fg='green')
            s1.place(x=10,y=85)


def va():
    global rootAP,e8
    rootAP=tkinter.Tk()
    rootAP.geometry("500x550")
    rootAP.title("TODAYS APPOINTMENTS")
    h1=tkinter.Label(rootAP,text="ENTER DATE TO VIEW APPOINTMENTS")
    h1.place(x=20,y=20)
    e8=tkinter.Entry(rootAP)
    e8.place(x=20,y=40)
    b5=tkinter.Button(rootAP,text="SEARCH",command=viewappointment)
    b5.place(x=30,y=65)
    rootAP.mainloop()




