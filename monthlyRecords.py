import sqlite3
from tkinter import * 
from tkinter import ttk
import random
from subprocess import call
from datetime import datetime 
from datetime import timedelta  
import tkinter.messagebox
import sqlite3
import LibBksDatabase
import LMS_verification
import tkinter as tk
import os
from subprocess import call
import sys
import cal
from datetime import date

class student:
    """docstring for student"""
    def __init__(self, root):
        self.root = root

        self.root.title = "Library Management System"
        self.root.geometry("1350x1350+0+0")
        self.root.configure(background='powder blue')
        tree = ttk.Treeview(root, column=("ID", "STUDENT_ID", "F_ID", "UNIQUE_BOOK_ID", "ISSUE_DATE", "RETURN_DATE", "ACTUAL_DATE", "STATUS"), show='headings')

        tree.column("ID", width=60, anchor=W)
        tree.column("STUDENT_ID", width=160, anchor='center')
        tree.column("F_ID", width=60, anchor='center')
        tree.column("UNIQUE_BOOK_ID", width=140, anchor='center')
        tree.column("ISSUE_DATE", width=175, anchor='center')
        tree.column("RETURN_DATE", width=175, anchor='center')
        tree.column("ACTUAL_DATE", width=175, anchor='center')
        tree.column("STATUS", width=100, anchor='center')

        tree.heading("#1", text="ID")
        tree.heading("#2", text="STUDENT_ID")
        tree.heading("#3", text="F_ID")
        tree.heading("#4", text="UNIQUE_BOOK_ID")
        tree.heading("#5", text="ISSUE_DATE")
        tree.heading("#6", text="RETURN_DATE")
        tree.heading("#7", text="ACTUAL_DATE")
        tree.heading("#8", text="STATUS")
        
        tree.pack(side = BOTTOM, pady=30)


        '''def OnDoubleClick(self):
            print(self.tree.selection())
            print(self.tree.set(selected, '#1'))'''

        def OnDoubleClick(self):
            curItem = tree.focus()
            issue_return_id = tree.item(curItem)['values'][0]
            UpdateData(issue_return_id)

        #self.tree.bind("<Double-1>", OnDoubleClick)
        tree.bind('<ButtonRelease-1>', OnDoubleClick)

        enrollment_no = StringVar()
        isbn = StringVar()
        faculty_id = StringVar()
        book_id = StringVar()
        

        def iExit():
            iExit = tkinter.messagebox.askyesno("Library Management System", "Are You Sure You Want to Exit?")
            if iExit>0:
                root.destroy()
                return
        
        def ClearData():
            self.txtenrollmentno.delete(0, END)
            self.txtfaculty.delete(0, END)
            self.txtunqbkid.delete(0, END)


        def DisplayData():
            conn = sqlite3.connect("libbooks.db")
            cur = conn.cursor()
            cur.execute("SELECT * FROM issue_return")
            for i in tree.get_children():
                tree.delete(i)
            rows = cur.fetchall()

            data = [list(elem) for elem in rows]
     
            for row in data:
                tree.insert("", tk.END, values=row)
            conn.close()

        MainFrame = Frame(self.root, padx=30, pady=50)
        MainFrame.pack(side=TOP)

        
        '''FrameDetail = Frame(MainFrame, bd=0, width=0,height=0, padx=0, relief=RIDGE)
        FrameDetail.pack(side=BOTTOM)

        ButtonFrameLeft = Frame(MainFrame, width=200, height=335, padx=0, pady=0, relief=RIDGE, bg="Cadet blue")
        ButtonFrameLeft.pack(side=LEFT)

        DataFrame = Frame(MainFrame, bd=1, width=900,height=100, padx=50,pady=20)
        DataFrame.pack(side=LEFT)
        
        DataFrameLEFT = LabelFrame(DataFrame,  width=100,height=100, padx=100, pady=40 ,relief=RIDGE,font=('arial',12,'bold'), bg="Cadet blue")
        DataFrameLEFT.pack(side=TOP)'''

        ButtonFrameRight = Frame(MainFrame, width=500, height=100, padx=30, pady=25, relief=RIDGE, bg="Cadet blue")
        ButtonFrameRight.pack(side=RIGHT)

        
        #========================widgets ==================

        '''self.issuereturnTitle = Label(DataFrameLEFT, font=('arial',18,'bold'), text="Issue/Return Book", bg = "Cadet blue")
        self.issuereturnTitle.grid(row =0, column=0, columnspan=2)

        self.extraspacelbl = Label(DataFrameLEFT, font=('arial',12,'bold'), text="", padx=10, pady=5,bg = "Cadet blue")
        self.extraspacelbl.grid(row=1,column=0,sticky=W)
        
        self.lblenrollmentno = Label(DataFrameLEFT, font=('arial',12,'bold'), text=" Enrollment No.", padx=10, pady=5,bg = "Cadet blue")
        self.lblenrollmentno.grid(row=3,column=0,sticky=W)
        self.txtenrollmentno = Entry(DataFrameLEFT, font=('arial',11,'bold'),textvariable=enrollment_no, width=20)
        self.txtenrollmentno.grid(row=3,column=1)
        self.txtenrollmentno.config(width=22)

        self.lblforstudent = Label(DataFrameLEFT, font=('arial',11,'bold'), text="  For Student", padx=0, pady=0,bg = "Cadet blue")
        self.lblforstudent.grid(row=3,column=2,sticky=W)

        self.txtor = Label(DataFrameLEFT, font=('arial',12,'bold'), text="OR", padx=10, pady=5,bg = "Cadet blue")
        self.txtor.grid(row=4,column=1)

        self.lblfaculty = Label(DataFrameLEFT, font=('arial',12,'bold'), text=" Faculty ID", padx=10, pady=5,bg = "Cadet blue")
        self.lblfaculty.grid(row=5,column=0,sticky=W)
        self.txtfaculty = Entry(DataFrameLEFT, font=('arial',12,'bold'),textvariable=faculty_id, width=20)
        self.txtfaculty.grid(row=5,column=1)

        self.lblforfaculty = Label(DataFrameLEFT, font=('arial',11,'bold'), text="For Faculty", padx=10, pady=5,bg = "Cadet blue")
        self.lblforfaculty.grid(row=5,column=2,sticky=W)

        self.lblunqbkid = Label(DataFrameLEFT, font=('arial',12,'bold'), text=" Book ID", padx=10, pady=5,bg = "Cadet blue")
        self.lblunqbkid.grid(row=2,column=0,sticky=W)
        self.txtunqbkid = Entry(DataFrameLEFT, font=('arial',12,'bold'), textvariable=book_id, width=20)
        self.txtunqbkid.grid(row=2 ,column=1)'''

        #========================================buttons===============================

        '''self.btnReturnBook = Button(ButtonFrameLeft, text='Return Book', font=('arial', 12, 'bold'), height=2, width=10, bd = 4, command=returnBook)
        self.btnReturnBook.grid(row=0, column=0)'''

        self.btnAddDate = Button(ButtonFrameRight, text='Display Records', font=('arial', 12, 'bold'), height=2, width=13, bd = 4, command=DisplayData)
        self.btnAddDate.grid(row=0, column=0)

        '''self.btnDisplayData = Button(ButtonFrameRight, text =' Display Data', font=('arial', 12, 'bold'), height=2, width=13, bd = 4, command=DisplayData)
        self.btnDisplayData.grid(row=1, column=0)

        self.btnUpdateData = Button(ButtonFrameRight, text='Update Data', font=('arial', 12, 'bold'), height=2, width=13, bd = 4, command=UpdatPublicationData)
        self.btnUpdateData.grid(row=2, column=0)

        self.btnClearData = Button(ButtonFrameRight, text='Clear Data', font=('arial', 12, 'bold'), height=2, width=13, bd = 4, command=ClearData)
        self.btnClearData.grid(row=3, column=0)'''

        self.btnExit = Button(ButtonFrameRight, text='Exit', font=('arial', 12, 'bold'), height=2, width=13, bd = 4, command=iExit)
        self.btnExit.grid(row=4, column=0)

        


#application = student(root)
#root.mainloop()     

root =Tk()
application = student(root)
root.mainloop()     