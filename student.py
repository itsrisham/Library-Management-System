import sqlite3
from tkinter import * 
from tkinter import ttk
import random
from subprocess import call
from datetime import datetime 
import tkinter.messagebox
import sqlite3
import LibBksDatabase
import LMS_verification
import tkinter as tk
import os
from subprocess import call
import sys
'''
CREATE TABLE "student" ( `student_id` INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE, `enrollment_no` INTEGER NOT NULL UNIQUE, `firstname` TEXT NOT NULL, `lastname` TEXT NOT NULL, `email` TEXT NOT NULL UNIQUE, `address` TEXT NOT NULL, `gender` TEXT NOT NULL, `dept_id` INTEGER NOT NULL, `phone` INTEGER NOT NULL UNIQUE , FOREIGN KEY(`dept_id`) REFERENCES `department`(`dept_id`))
'''
#root = Tk()
class student:


    """docstring for student"""
    def __init__(self, root):
        self.root = root

        self.root.title = "Library Management System"
        self.root.geometry("1350x750+0+0")
        self.root.configure(background='powder blue')
        tree = ttk.Treeview(root, column=("STUDENT_ID", "ENROLMENT NO.", "FIRSTNAME","LASTNAME", "EMAIL", "ADDRESS", "GENDER", "PHONE NO."), show='headings')
    
        tree.column("ENROLMENT NO.", width=150, anchor='center')
        tree.column("STUDENT_ID", width=70,  anchor='center')
        tree.column("FIRSTNAME", width=120,  anchor='center')
        tree.column("LASTNAME", width=120, anchor='center')
        tree.column("EMAIL", width=200,  anchor='center')
        tree.column("ADDRESS", width=200,  anchor='center')
        tree.column("GENDER", width=100,  anchor='center')
        tree.column("PHONE NO.", width=120,  anchor='center')

        tree.heading("#1", text="STUDENT_ID")
        tree.heading("#2", text="ENROLMENT NO.")
        tree.heading("#3", text="FIRSTNAME")
        tree.heading("#4", text="LASTNAME")
        tree.heading("#5", text="EMAIL")
        tree.heading("#6", text="ADDRESS")
        tree.heading("#7", text="GENDER")
        tree.heading("#8", text="PHONE NO.")
        tree.pack(side = BOTTOM, pady=30)



        '''def OnDoubleClick(self):
            print(self.tree.selection())
            print(self.tree.set(selected, '#1'))'''
        def OnDoubleClick(self):
            curItem = tree.focus()
            enr_no = tree.item(curItem)['values'][1]
            print(enr_no)
            UpdateData(enr_no)

        #self.tree.bind("<Double-1>", OnDoubleClick)
        tree.bind('<ButtonRelease-1>', OnDoubleClick)

        firstname= StringVar()
        lastname = StringVar()
        email = StringVar()
        address = StringVar()
        dept = StringVar()
        dept.set("Select") 
        gen = StringVar()
        phoneno = StringVar()

        def addDepartment():
            call(["python3", "department.py"])
            root.destroy()
            return

        def iExit():
            iExit = tkinter.messagebox.askyesno("Library Management System", "Are You Sure You Want to Exit?")
            if iExit>0:
                root.destroy()
                return

        def ClearData():
            self.txtFname.delete(0, END)
            self.txtLname.delete(0, END)
            self.txtEmail.delete(0, END)
            self.txtAddress.delete(0, END)
            self.txtPhoneno.delete(0, END)
            dept.set("Select")


        def DisplayData():
            conn = sqlite3.connect("libbooks.db")
            cur = conn.cursor()
            cur.execute("SELECT student_id, enrollment_no, firstname, lastname, email, address, gender, phone FROM student")
            for i in tree.get_children():
                tree.delete(i)
            rows = cur.fetchall()
            for row in rows:
                tree.insert("", tk.END, values=row)
            conn.close()
            
        def addData():
            
            if(len(firstname.get())==0):
                firstnamemsg = tkinter.messagebox.showinfo("Library Management System", "Please Enter Your Firstname!")
            elif (len(lastname.get())==0 ):
                lastnamemsg = tkinter.messagebox.showinfo("Library Management System", "Please Enter Your Lastname!")
            elif(len(email.get())==0):
                emailmsg = tkinter.messagebox.showinfo("Library Management System", "Please Enter Your Email!")
            elif (len(address.get())==0 ):
                addressmsf = tkinter.messagebox.showinfo("Library Management System", "Please Enter Your Address!")
            elif (len(phoneno.get())==0 ):
                phonenomsg = tkinter.messagebox.showinfo("Library Management System", "Please Enter Your Phone No-!")
            elif (len(phoneno.get())!=10 ):
                phonenomsg = tkinter.messagebox.showinfo("Library Management System", "Invalid Phone No-!")
            elif (len(dept.get())==0 or dept.get()=="Select"):
                deptmsg = tkinter.messagebox.showinfo("Library Management System", "Please Select Your Department!")
            elif (len(gen.get())==0 ):
                genmsg = tkinter.messagebox.showinfo("Library Management System", "Please Select Your Gender!")
           
            else:

                gender = LMS_verification.check_gender(gen.get())
                department,dept_id = LMS_verification.check_department(dept.get())
                
                enrolment_no = LMS_verification.check_enrollment_no(dept_id, department)

                email_check = LMS_verification.email_check(email.get())
                email_exist_for_student = LMS_verification.email_exist_for_student(email.get())
                
                phone_check = LMS_verification.phoneisValid(phoneno.get())
                phone_exist_for_student = LMS_verification.phone_exist_for_student(phoneno.get())
 
                if (phone_check==None):
                    phonenomsg = tkinter.messagebox.showinfo("Library Management System", "Invalid Phone No.!")
                else:
                    pass

                        
                if (email_exist_for_student==0 and email_check==0 and phone_check!=None and phone_exist_for_student==0):
                    if(len(firstname.get())!=0):
                        LibBksDatabase.addStudent(enrolment_no,firstname.get(),lastname.get(),email.get(),address.get(),gender ,dept_id, phoneno.get())
                        #booklist.delete(0, END)
                        #booklist.insert(END,(enrolment_no, firstname.get(),lastname.get(),email.get(),address.get(),gender,department, phoneno.get()))
                        tkinter.messagebox.showinfo("Library Management System", "Inserted Data Successfully!")
                        DisplayData()
                else:
                    pass

        def UpdateData(enr_no):
            conn = sqlite3.connect("libbooks.db")
            cur = conn.cursor()
            cur.execute("SELECT firstname, lastname, email, address, gender, phone, dept_id FROM student WHERE enrollment_no=?", [enr_no])
            rows = cur.fetchall()
            conn.close()
            firstname.set(rows[0][0])
            lastname.set(rows[0][1])
            email.set(rows[0][2])
            address.set(rows[0][3])
            phoneno.set(rows[0][5])


            if(rows[0][4]=="Male"):
                gen.set(1)
            elif (rows[0][4]=="Female"):
                gen.set(2)

            dept_to_update = LMS_verification.get_dept_for_update_books(rows[0][6])
            print(dept_to_update)
        

            dept.set(dept_to_update)



        def UpdateStudentsData():
            curItem = tree.focus()
            enr_no = tree.item(curItem)['values'][1]

            gender = LMS_verification.check_gender(gen.get())
            
            department,dept_id = LMS_verification.check_department(dept.get())
            
            email_check = LMS_verification.email_check(email.get())
            email_exist_for_update_student = LMS_verification.email_exist_for_update_student(email.get(), enr_no)
                
            phone_check = LMS_verification.phoneisValid(phoneno.get())
            if (len(phoneno.get())!=10 ):
                phonenomsg = tkinter.messagebox.showinfo("Library Management System", "Invalid Phone No-!")
            else:
                phone_exist_for_update_student = LMS_verification.phone_exist_for_update_student(phoneno.get(), enr_no)

                if (email_exist_for_update_student!=1 and phone_exist_for_update_student!=1):
                    conn = sqlite3.connect("libbooks.db")
                    cur = conn.cursor()
                    cur.execute("UPDATE student SET firstname=?, lastname=?, email=?, address=?, gender=?, dept_id=?, phone=? where enrollment_no=?", (firstname.get(),lastname.get(),email.get(),address.get(),gender ,dept_id, phoneno.get(), enr_no))
                    conn.commit()
                    conn.close()
                    tkinter.messagebox.showinfo("Library Management System", "Updated Data Successfully!")
                    DisplayData()
            

        MainFrame = Frame(self.root, padx=10, pady=0)
        MainFrame.pack(side=TOP)

        FrameDetail = Frame(MainFrame, bd=0, width=0,height=0, padx=0, relief=RIDGE)
        FrameDetail.pack(side=BOTTOM)

        DataFrame = Frame(MainFrame, bd=1, width=500,height=100, padx=50,pady=20)
        DataFrame.pack(side=LEFT)

        DataFrameLEFT = LabelFrame(DataFrame,  width=100,height=100, padx=100, pady=40 ,relief=RIDGE,font=('arial',12,'bold'), bg="Cadet blue")
        DataFrameLEFT.pack(side=TOP)

        ButtonFrame = Frame(MainFrame, width=1350, height=100, padx=30, pady=25, relief=RIDGE, bg="Cadet blue")
        ButtonFrame.pack(side=RIGHT)

        
        #========================widgets ==================

        self.studenttitle = Label(DataFrameLEFT, font=('arial',18,'bold'), text="Student Registration", bg = "Cadet blue")
        self.studenttitle.grid(row =0, column=0, columnspan=2)

        self.lblFname = Label(DataFrameLEFT, font=('arial',12,'bold'), text="Firstname", padx=10, pady=5 ,bg = "Cadet blue")
        self.lblFname.grid(row=1,column=0,sticky=W)
        self.txtFname = Entry(DataFrameLEFT, font=('arial',12,'bold'),textvariable=firstname, width=23)
        self.txtFname.grid(row=1,column=1)

        self.lblLname = Label(DataFrameLEFT, font=('arial',12,'bold'), text="Lastname", padx=10, pady=5,bg = "Cadet blue")
        self.lblLname.grid(row=3,column=0,sticky=W)
        self.txtLname = Entry(DataFrameLEFT, font=('arial',12,'bold'),textvariable=lastname, width=23)
        self.txtLname.grid(row=3,column=1)

        self.lblEmail = Label(DataFrameLEFT, font=('arial',12,'bold'), text="Email", padx=10, pady=5,bg = "Cadet blue")
        self.lblEmail.grid(row=4,column=0,sticky=W)
        self.txtEmail = Entry(DataFrameLEFT, font=('arial',12,'bold'),textvariable=email, width=23)
        self.txtEmail.grid(row=4,column=1)

        self.lblAddress = Label(DataFrameLEFT, font=('arial',12,'bold'), text="Address", padx=10, pady=5,bg = "Cadet blue")
        self.lblAddress.grid(row=5,column=0,sticky=W)
        self.txtAddress = Entry(DataFrameLEFT, font=('arial',12,'bold'),textvariable=address, width=23)
        self.txtAddress.grid(row=5,column=1)

        self.lblPhoneno = Label(DataFrameLEFT,font=('arial', 12, 'bold'), text="Phone No",padx=10,pady=5,bg = "Cadet blue")
        self.lblPhoneno.grid(row=6, column=0, sticky=W)
        self.txtPhoneno = Entry(DataFrameLEFT,font=('arial', 12, 'bold'),textvariable=phoneno, width=23)
        self.txtPhoneno.grid(row=6, column=1)
        

        def add_depts(evt):
            if (dept.get()=="Add_Department"):
                call(["python3", "department.py"])

        self.lblDepartment = Label(DataFrameLEFT,font=('arial', 12, 'bold'), text="Department",padx=10,pady=7,bg = "Cadet blue")
        self.lblDepartment.grid(row=7, column=0, sticky=W)

        depts = LMS_verification.get_departments()


        self.txtDepartment = OptionMenu(DataFrameLEFT, dept, *depts)
        self.txtDepartment.grid(row=7, column=1)

        self.txtDepartment.bind('<Button-1>', add_depts)
        self.txtDepartment.grid(row=7, column=1)

        self.btnAddDepartmentSpace = Label(DataFrameLEFT, text='', bg = "Cadet blue", padx=30)
        self.btnAddDepartmentSpace.grid(row=7, column=2)


        self.btnAddDepartment = Button(DataFrameLEFT, text='Add Department', font=('arial', 12), height=0, width=0, bd = 0, padx=10,  command=addDepartment)
        self.btnAddDepartment.grid(row=7, column=4)

        self.lblGender = Label(DataFrameLEFT,font=('arial', 12, 'bold'), text="Gender",padx=10,pady=5,bg = "Cadet blue")
        self.lblGender.grid(row=8, column=0, sticky=W)
        self.txtGender = tkinter.Radiobutton(DataFrameLEFT,text="Male", variable=gen, value=1, cursor="dot", )
        self.txtGender.grid(row=8, column=1)
        self.txtGender = tkinter.Radiobutton(DataFrameLEFT,text="Female", variable=gen, value=2, cursor="dot")
        self.txtGender.grid(row=9, column=1)

        #======================buttons=============================

        self.btnAddDate = Button(ButtonFrame, text='Add Data', font=('arial', 12, 'bold'), height=2, width=13, bd = 4, command=addData)
        self.btnAddDate.grid(row=0, column=0)

        self.btnDisplayData = Button(ButtonFrame, text=' Display Data', font=('arial', 12, 'bold'), height=2, width=13, bd = 4, command=DisplayData)
        self.btnDisplayData.grid(row=1, column=0)

        self.btnUpdateData = Button(ButtonFrame, text='Update Data', font=('arial', 12, 'bold'), height=2, width=13, bd = 4, command=UpdateStudentsData)
        self.btnUpdateData.grid(row=2, column=0)

        self.btnClearData = Button(ButtonFrame, text='Clear Data', font=('arial', 12, 'bold'), height=2, width=13, bd = 4, command=ClearData)
        self.btnClearData.grid(row=3, column=0)


        self.btnExit = Button(ButtonFrame, text='Exit', font=('arial', 12, 'bold'), height=2, width=13, bd = 4, command=iExit)
        self.btnExit.grid(row=4, column=0)
    
#application = student(root)
#root.mainloop()     


root =Tk()
application = student(root)
root.mainloop() 
//print hello world    