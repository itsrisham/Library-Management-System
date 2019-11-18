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



class student:
    """docstring for student"""
    def __init__(self, root):
        self.root = root

        self.root.title = "Library Management System"
        self.root.geometry("1350x750+0+0")
        self.root.configure(background='powder blue')
        tree = ttk.Treeview(root, column=("ID", "Publication", "Address", "Phone No."), show='headings')
    
        tree.column("ID", width=50)
        tree.column("Publication", width=170,anchor='center')
        tree.column("Address", width=280, anchor='center')
        tree.column("Phone No.", width=170, anchor='center')

        tree.heading("#1", text="ID")
        tree.heading("#2", text="Publication")
        tree.heading("#3", text="Address")
        tree.heading("#4", text="Phone No.")
        
        tree.pack(side = BOTTOM, pady=30)


        '''def OnDoubleClick(self):
            print(self.tree.selection())
            print(self.tree.set(selected, '#1'))'''

        def OnDoubleClick(self):
            curItem = tree.focus()
            publication_id = tree.item(curItem)['values'][0]
            UpdateData(publication_id)

        #self.tree.bind("<Double-1>", OnDoubleClick)
        tree.bind('<ButtonRelease-1>', OnDoubleClick)

        publication = StringVar()
        address = StringVar()
        phone  = StringVar()
        

        def iExit():
            iExit = tkinter.messagebox.askyesno("Library Management System", "Are You Sure You Want to Exit?")
            if iExit>0:
                root.destroy()
                return
        
        def ClearData():
            self.txtPublication.delete(0, END)
            

        def DisplayData():
            conn = sqlite3.connect("libbooks.db")
            cur = conn.cursor()
            cur.execute("SELECT * FROM publication")
            for i in tree.get_children():
                tree.delete(i)
            rows = cur.fetchall()
            for row in rows:
                tree.insert("", tk.END, values=row)
            conn.close()
            
        def addData():
            if(len(publication.get())<=1):
                publicationmsg = tkinter.messagebox.showinfo("Library Management System", "Please Enter Publication Name!")
            elif (len(address.get())<=2  ):
                publicationmsg = tkinter.messagebox.showinfo("Library Management System", "Please Enter Publication Address!")
            elif(len(phone.get())!=10):
                publicationmsg = tkinter.messagebox.showinfo("Library Management System", "Please Enter Publication Phone No.!")
            else:

                pub = publication.get()
                add = address.get()
               
                phone_check = LMS_verification.phoneisValid(phone.get())

                if (phone_check==None):
                    phonenomsg = tkinter.messagebox.showinfo("Library Management System", "Invalid Phone No.!")
                else:
                    phn = phone.get()

                phone_exist_for_publication = LMS_verification.phone_exist_for_publication(phone.get())
                if (phone_exist_for_publication==1):
                    phonemsg = tkinter.messagebox.showerror("Library Management System", "Phone No. Already Exists!")

                check_publication_exist = LMS_verification.check_publication_exist(publication.get())
                if (check_publication_exist!=1 and phone_exist_for_publication!=1 and phone_check!=None):
                    LibBksDatabase.addPublication( ((publication.get()).strip()).lower(), (((address.get()).strip()).lower()).rstrip(), phone.get())
                    tkinter.messagebox.showinfo("Library Management System", "Inserted Data Successfully!")
                    self.txtPublication.delete(0, END)
                    self.txtAddress.delete(0, END)
                    self.txtPhone.delete(0, END)
                    DisplayData()

                else:
                    print("something went wrong publication.py 117")
                    print(check_publication_exist)
                    print(phone_exist_for_publication)
                    print(websiteIsValid)
            

        def UpdateData(publication_id):
            conn = sqlite3.connect("libbooks.db")
            cur = conn.cursor()
            cur.execute("SELECT name, address, phone FROM publication WHERE publication_id=?", [publication_id])
            rows = cur.fetchall()
            conn.close()
            publication.set(rows[0][0])
            address.set(rows[0][1])
            phone.set(rows[0][2])

    
        def UpdatPublicationData():
            curItem = tree.focus()
            publication_id = tree.item(curItem)['values'][0]

            check_publication_exist_for_update = LMS_verification.check_publication_exist_for_update(publication_id, publication.get())
           
            if(len(publication.get())<=1 ):
                publicationmsg = tkinter.messagebox.showinfo("Library Management System", "Please Enter Publication Name!")
           
            if (check_publication_exist_for_update!=1):
                conn = sqlite3.connect("libbooks.db")
                cur = conn.cursor()
                cur.execute("UPDATE publication SET name=?, address=? , phone=?  where publication_id=?", ( ((publication.get()).strip()).lower(), (((address.get()).strip()).lower()).rstrip(), phone.get(), publication_id))
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

        self.PublicationTitle = Label(DataFrameLEFT, font=('arial',18,'bold'), text="Add Publication", bg = "Cadet blue")
        self.PublicationTitle.grid(row =0, column=0, columnspan=2)

        self.extraspacelbl = Label(DataFrameLEFT, font=('arial',12,'bold'), text="", padx=10, pady=5,bg = "Cadet blue")
        self.extraspacelbl.grid(row=1,column=0,sticky=W)
        
        self.lblPublication = Label(DataFrameLEFT, font=('arial',12,'bold'), text="Publication", padx=10, pady=5,bg = "Cadet blue")
        self.lblPublication.grid(row=2,column=0,sticky=W)
        self.txtPublication = Entry(DataFrameLEFT, font=('arial',12,'bold'),textvariable=publication, width=23)
        self.txtPublication.grid(row=2,column=1)

        self.lblAddress = Label(DataFrameLEFT, font=('arial',12,'bold'), text="Address", padx=10, pady=5,bg = "Cadet blue")
        self.lblAddress.grid(row=3,column=0,sticky=W)
        self.txtAddress = Entry(DataFrameLEFT, font=('arial',12,'bold'),textvariable=address, width=23)
        self.txtAddress.grid(row=3,column=1)

    
        self.lblPhone = Label(DataFrameLEFT, font=('arial',12,'bold'), text="Phone No.", padx=10, pady=5,bg = "Cadet blue")
        self.lblPhone.grid(row=4,column=0,sticky=W)
        self.txtPhone = Entry(DataFrameLEFT, font=('arial',12,'bold'),textvariable=phone, width=23)
        self.txtPhone.grid(row=4,column=1)


        
        #======================buttons=============================

        self.btnAddDate = Button(ButtonFrame, text='Add Data', font=('arial', 12, 'bold'), height=2, width=13, bd = 4, command=addData)
        self.btnAddDate.grid(row=0, column=0)

        self.btnDisplayData = Button(ButtonFrame, text=' Display Data', font=('arial', 12, 'bold'), height=2, width=13, bd = 4, command=DisplayData)
        self.btnDisplayData.grid(row=1, column=0)

        self.btnUpdateData = Button(ButtonFrame, text='Update Data', font=('arial', 12, 'bold'), height=2, width=13, bd = 4, command=UpdatPublicationData)
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