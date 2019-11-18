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
        tree = ttk.Treeview(root, column=("Category_ID", "Category"), show='headings')
    
        tree.column("Category_ID", width=150)
        tree.column("Category", width=170)
        

        tree.heading("#1", text="Category_ID")
        tree.heading("#2", text="Category")
        
        tree.pack(side = BOTTOM, pady=30)



        '''def OnDoubleClick(self):
            print(self.tree.selection())
            print(self.tree.set(selected, '#1'))'''
        def OnDoubleClick(self):
            curItem = tree.focus()
            category_id = tree.item(curItem)['values'][0]
            UpdateData(category_id)

        #self.tree.bind("<Double-1>", OnDoubleClick)
        tree.bind('<ButtonRelease-1>', OnDoubleClick)

        category= StringVar()
        

        def iExit():
            iExit = tkinter.messagebox.askyesno("Library Management System", "Are You Sure You Want to Exit?")
            if iExit>0:
                root.destroy()
                return
        
        def ClearData():
            self.txtCategory.delete(0, END)
            

        def DisplayData():
            conn = sqlite3.connect("libbooks.db")
            cur = conn.cursor()
            cur.execute("SELECT * FROM category")
            for i in tree.get_children():
                tree.delete(i)
            rows = cur.fetchall()
            print(rows)
            for row in rows:
                tree.insert("", tk.END, values=row)
            conn.close()
            
        def addData():
            
            check_category_exist = LMS_verification.check_category_exist(category.get())
            print (check_category_exist)

            if(len(category.get())<=1):
                categorymsg = tkinter.messagebox.showinfo("Library Management System", "Please Enter The Category!")
            
            if (check_category_exist!=1):
                LibBksDatabase.addCategory(category.get())
                tkinter.messagebox.showinfo("Library Management System", "Inserted Data Successfully!")
                self.txtCategory.delete(0, END)
                DisplayData()
            

        def UpdateData(category_id):
            conn = sqlite3.connect("libbooks.db")
            cur = conn.cursor()
            cur.execute("SELECT category FROM category WHERE category_id=?", [category_id])
            rows = cur.fetchall()
            conn.close()
            category.set(rows[0][0])

    
        def UpdatCategoryData():
            curItem = tree.focus()
            category_id = tree.item(curItem)['values'][0]

            check_category_exist_for_update = LMS_verification.check_category_exist_for_update(category_id, category.get())
            print(check_category_exist_for_update)
            if(len(category.get())<=1 ):
                categorymsg = tkinter.messagebox.showinfo("Library Management System", "Please Enter The Category!")
           
            if (check_category_exist_for_update!=1):
                conn = sqlite3.connect("libbooks.db")
                cur = conn.cursor()
                cur.execute("UPDATE category SET category=? where category_id=?", (category.get(), category_id) )
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

        self.categoryTitle = Label(DataFrameLEFT, font=('arial',18,'bold'), text="Add Category", bg = "Cadet blue")
        self.categoryTitle.grid(row =0, column=0, columnspan=2)

        self.extraspacelbl = Label(DataFrameLEFT, font=('arial',12,'bold'), text="", padx=10, pady=5,bg = "Cadet blue")
        self.extraspacelbl.grid(row=1,column=0,sticky=W)
        
        self.lblCategory = Label(DataFrameLEFT, font=('arial',12,'bold'), text="Category", padx=10, pady=5,bg = "Cadet blue")
        self.lblCategory.grid(row=2,column=0,sticky=W)
        self.txtCategory = Entry(DataFrameLEFT, font=('arial',12,'bold'),textvariable=category, width=23)
        self.txtCategory.grid(row=2,column=1)

        
        #======================buttons=============================

        self.btnAddDate = Button(ButtonFrame, text='Add Data', font=('arial', 12, 'bold'), height=2, width=13, bd = 4, command=addData)
        self.btnAddDate.grid(row=0, column=0)

        self.btnDisplayData = Button(ButtonFrame, text=' Display Data', font=('arial', 12, 'bold'), height=2, width=13, bd = 4, command=DisplayData)
        self.btnDisplayData.grid(row=1, column=0)

        self.btnUpdateData = Button(ButtonFrame, text='Update Data', font=('arial', 12, 'bold'), height=2, width=13, bd = 4, command=UpdatCategoryData)
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