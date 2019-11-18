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
CREATE TABLE "student" ( `student_id` INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE, `faculty_id` INTEGER NOT NULL UNIQUE, `firstname` TEXT NOT NULL, `lastname` TEXT NOT NULL, `email` TEXT NOT NULL UNIQUE, `address` TEXT NOT NULL, `gender` TEXT NOT NULL, `dept_id` INTEGER NOT NULL, `phone` INTEGER NOT NULL UNIQUE , FOREIGN KEY(`dept_id`) REFERENCES `department`(`dept_id`))
'''
#root = Tk()
class student:


    """docstring for student"""
    def __init__(self, root):
        self.root = root

        self.root.title = "Library Management System"
        self.root.geometry("1350x750+0+0")
        self.root.configure(background='powder blue')
        tree = ttk.Treeview(root, column=("FACULTY ID", "BOOK TITLE",  "BOOK ID", "ISSUE DATE", "RETURN DATE" ,"ACTUAL RETURN DATE", "STATUS" ), show='headings')
    
       
        tree.column("FACULTY ID", width=150, anchor='center')
        tree.column("BOOK ID", width=170, anchor='center')
        tree.column("BOOK TITLE", width=170, anchor='center')
        tree.column("ISSUE DATE", width=170, anchor='center')
        tree.column("RETURN DATE", width=170, anchor='center')
        tree.column("ACTUAL RETURN DATE", width=170, anchor='center')
        tree.column("STATUS", width=170, anchor='center')
        

        tree.heading("#1", text="FACULTY ID")
        tree.heading("#2", text="BOOK TITLE")
        tree.heading("#3", text="BOOK ID")
        tree.heading("#4", text="ISSUE DATE")
        tree.heading("#5", text="RETURN DATE")
        tree.heading("#6", text="ACTUAL RETURN DATE")
        tree.heading("#7", text="STATUS")
         
        tree.pack(side = BOTTOM, pady=30)



        '''def OnDoubleClick(self):
            print(self.tree.selection())
            print(self.tree.set(selected, '#1'))'''
        def OnDoubleClick(self):
            curItem = tree.focus()
            dept_id = tree.item(curItem)['values'][0]
            UpdateData(dept_id)

        #self.tree.bind("<Double-1>", OnDoubleClick)
        tree.bind('<ButtonRelease-1>', OnDoubleClick)

        faculty_id = StringVar()
        

        def iExit():
            iExit = tkinter.messagebox.askyesno("Library Management System", "Are You Sure You Want to Exit?")
            if iExit>0:
                root.destroy()
                return
        
        def ClearData():
            self.txtDept.delete(0, END)
                 
        def searchData():
            if(len(faculty_id.get())<=0):
                deptmsg = tkinter.messagebox.showinfo("Library Management System", "Please Enter Faculty ID!")
            else:
                faculty_is_valid = LMS_verification.faculty_idIsValid(faculty_id.get())
                if (faculty_is_valid!=1):
                    msg = tkinter.messagebox.showinfo("Library Management System", "Invalid Faculty ID")
                else:
                    getFacultyBookRecords = LMS_verification.getFacultyBookRecords(faculty_id.get())
                    data = [list(elem) for elem in getFacultyBookRecords]
                    print(data)

                    for  i in range(0, len(data)):
                        getBookId = LMS_verification.getBookId(data[i][2])
                        print("id ", getBookId)

                        getBookTitle = LMS_verification.getBookTitle(getBookId)
                        print("title ", getBookTitle)

                        data[i][1] = getBookTitle

                    for row in data:
                        tree.insert("", tk.END, values=row)

        MainFrame = Frame(self.root, padx=10, pady=0)
        MainFrame.pack(side=TOP)

        FrameDetail = Frame(MainFrame, bd=0, width=0,height=0, padx=0, relief=RIDGE )
        FrameDetail.pack(side=BOTTOM)

        DataFrame = Frame(MainFrame, bd=1, width=500,height=100, padx=100,pady=100)
        DataFrame.pack(side=LEFT)

        DataFrameLEFT = LabelFrame(DataFrame,  width=100,height=100, padx=100, pady=40 ,relief=RIDGE,font=('arial',12,'bold'), bg="Cadet blue")
        DataFrameLEFT.pack(side=TOP)

        ButtonFrame = Frame(MainFrame, width=1350, height=100, padx=30, pady=25, relief=RIDGE, bg="Cadet blue")
        ButtonFrame.pack(side=RIGHT)

        
        #========================widgets ==================

        self.deptTitle = Label(DataFrameLEFT, font=('arial',18,'bold'), text="Search Faculty Records", bg = "Cadet blue")
        self.deptTitle.grid(row =0, column=0, columnspan=2)

        self.extraspacelbl = Label(DataFrameLEFT, font=('arial',12,'bold'), text="", padx=10, pady=5,bg = "Cadet blue")
        self.extraspacelbl.grid(row=1,column=0,sticky=W)
        
        self.lblDept = Label(DataFrameLEFT, font=('arial',12,'bold'), text="Faculty ID", padx=10, pady=5,bg = "Cadet blue")
        self.lblDept.grid(row=2,column=0,sticky=W)
        self.txtDept = Entry(DataFrameLEFT, font=('arial',12,'bold'),textvariable=faculty_id, width=23)
        self.txtDept.grid(row=2,column=1)

        
        #======================buttons=============================

        self.btnAddDate = Button(ButtonFrame, text='Search', font=('arial', 12, 'bold'), height=2, width=13, bd = 4, command=searchData)
        self.btnAddDate.grid(row=0, column=0)

        '''self.btnDisplayData = Button(ButtonFrame, text=' Display Data', font=('arial', 12, 'bold'), height=2, width=13, bd = 4, command=DisplayData)
        self.btnDisplayData.grid(row=1, column=0)

        self.btnUpdateData = Button(ButtonFrame, text='Update Data', font=('arial', 12, 'bold'), height=2, width=13, bd = 4, command=UpdatDepartmentData)
        self.btnUpdateData.grid(row=2, column=0)

        self.btnClearData = Button(ButtonFrame, text='Clear Data', font=('arial', 12, 'bold'), height=2, width=13, bd = 4, command=ClearData)
        self.btnClearData.grid(row=3, column=0)'''

        self.btnExit = Button(ButtonFrame, text='Exit', font=('arial', 12, 'bold'), height=2, width=13, bd = 4, command=iExit)
        self.btnExit.grid(row=4, column=0)
    
#application = student(root)
#root.mainloop()     


root =Tk()
application = student(root)
root.mainloop()     