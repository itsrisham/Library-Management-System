import sqlite3
from tkinter import * 
from tkinter import ttk
import random
from subprocess import call
from datetime import datetime 
from datetime import timedelta  
import mail
import tkinter.messagebox
import sqlite3
import LibBksDatabase
import LMS_verification
import tkinter as tk
import os
import rec
from subprocess import call
import sys
from datetime import date
import socket

class student:
    """docstring for student"""
    def __init__(self, root):
        self.root = root

        self.root.title = "Library Management System"
        self.root.geometry("1350x750+0+0")
        self.root.configure(background='powder blue')
        tree = ttk.Treeview(root, column=("ID", "ENROLLMENT_NO", "F_ID", "UNIQUE_BOOK_ID", "ISSUE_DATE", "RETURN_DATE", "ACTUAL_DATE", "STATUS"), show='headings')

        tree.column("ID", width=60, anchor=W)
        tree.column("ENROLLMENT_NO", width=160, anchor='center')
        tree.column("F_ID", width=60, anchor='center')
        tree.column("UNIQUE_BOOK_ID", width=140, anchor='center')
        tree.column("ISSUE_DATE", width=175, anchor='center')
        tree.column("RETURN_DATE", width=175, anchor='center')
        tree.column("ACTUAL_DATE", width=175, anchor='center')
        tree.column("STATUS", width=100, anchor='center')

        tree.heading("#1", text="ID")
        tree.heading("#2", text="ENROLLMENT_NO")
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

            conn = sqlite3.connect("libbooks.db")
            cur = conn.cursor()
            cur.execute("SELECT * FROM student")
            student_data = cur.fetchall()
            conn.close()

            data = [list(elem) for elem in rows]
            print("data", data)
            print("student_data", student_data)

            for i in range(0, len(data)):
                if (data[i][1]!=None):
                    indx = data[i][1]
                    indx-=1
                    print("indx: ",indx)
                    print("i: ", i)
                    try:

                        data[i][1] = student_data[indx][1]
                    except TypeError as e:
                        pass
                    else:
                        pass
                    finally:
                        pass                
            for row in data:
                tree.insert("", tk.END, values=row)
            conn.close()
                
        

        def issueBook():
            if (len(enrollment_no.get())<=0 and len(faculty_id.get())<=0):
                enrlmnandfacultytstudent_msg = tkinter.messagebox.showinfo("Library Management System", "Please Enter ENROLLMENT_NO or FACULTY ID!")
            if(len(book_id.get())==0):
                unqbkidstudent_msg = tkinter.messagebox.showinfo("Library Management System", "Please Enter Book ID!")
            elif (len(enrollment_no.get())>=1 and len(faculty_id.get())>=1):
                student_msg = tkinter.messagebox.showinfo("Library Management System", "Please Enter ENROLLMENT_NO or FACULTY ID! Not Both!")
            else:
                studentIsValid = 0
                faculty_idIsValid=0

                uniqueBookIdIsValid = LMS_verification.uniqueBookIdIsValid(book_id.get())
                if (uniqueBookIdIsValid!=1):
                    student_msg = tkinter.messagebox.showinfo("Library Management System", "Book ID Not Exist!")
                

                if(len(enrollment_no.get())>=1):
                    studentIsValid = LMS_verification.studentIsValid(enrollment_no.get())

                if (len(enrollment_no.get())>=2):
                    if (studentIsValid==1):
                        student_id = LMS_verification.get_student_id(enrollment_no.get())

                        print("student is valid")
                        student_email = LMS_verification.getStudentEmailForSendingEmail(enrollment_no.get())
                        student_fullname  = LMS_verification.getStudentFullnameForSendingEmaill(enrollment_no.get())
                        print(student_fullname)
                    else:
                        student_msg = tkinter.messagebox.showinfo("Library Management System", "Invalid ENROLLMENT_NO!")



                if(len(faculty_id.get())>=1):
                    faculty_idIsValid = LMS_verification.faculty_idIsValid(faculty_id.get())


                if(len(faculty_id.get())>=1):
                    if (faculty_idIsValid==1):
                        print("faculty_id is valid")
                        faculty_email = LMS_verification.getFacultyEmailForSendingEmail(faculty_id.get())
                        faculty_fullname  = LMS_verification.getFacultyFullnameForSendingEmail(faculty_id.get())
                        print(faculty_fullname)

                    else:
                        student_msg = tkinter.messagebox.showinfo("Library Management System", "Invalid FACULTY ID.!")
                


                if(uniqueBookIdIsValid==1 and (studentIsValid==1 or faculty_idIsValid==1 )):
                    if (uniqueBookIdIsValid==1 and studentIsValid==1):
                        enrollment = enrollment_no.get()
                        unique_book_id = book_id.get()

                        bk_id = LMS_verification.get_book_id_for_issue(book_id.get())
                        print("bk_id", bk_id)
                        book_quantity = LMS_verification.get_quantity_for_update_books(bk_id)
                        (book_quantity)

                        issued_current_book = LMS_verification.issued_current_book(unique_book_id)
                        print(issued_current_book)
                        print("ss", int(book_quantity))
                        print("ss", int(issued_current_book))
                        if (int(book_quantity)-int(issued_current_book)>0):
                            student_issued_books = LMS_verification.student_issued_books(student_id)
                            book_already_issued = LMS_verification.book_already_issued(unique_book_id)
                            if (student_issued_books>=2):
                                tkinter.messagebox.showinfo("Library Management System", "Student Has Issued Two Books Already")
                            elif(book_already_issued==1):
                                tkinter.messagebox.showinfo("Library Management System", "Book Issued By Other Student/Faculty")
                            else:
                                issue_date = date.today()
                                actual_return_date = date.today() + timedelta(days=15)
                                print(actual_return_date)
                                status = "issued"
                                LibBksDatabase.addIssueReturn(student_id, unique_book_id, issue_date, actual_return_date, status)
                                tkinter.messagebox.showinfo("Library Management System", "Book Issued Successfully!")
                                student_msg  = "Hello "+ student_fullname + "("+enrollment+")" +".\nYou Have Issued a book.\nKindly Return it Before "+str(actual_return_date)+".\nThank you.!!"
                                try:
                                    mail.sendmail(student_email, student_msg)
                                except socket.gaierror as a:
                                    tkinter.messagebox.showinfo("Library Management System", "Email Coudnt Sent! You Are Not Connected with the Internet.")
                                else:
                                    pass
                                DisplayData()
                        
                        elif (int(book_quantity)-int(issued_current_book)==0):
                            print( int(book_quantity)-int(issued_current_book) )
                            qntynstudent_msg = tkinter.messagebox.showinfo("Library Management System", "Sorry! Book Out Of Stock")
                        else:
                            qntynstudent_msg = tkinter.messagebox.showinfo("Library Management System", "Something Went Wrong")

                    
                    elif(uniqueBookIdIsValid==1 and faculty_idIsValid==1):
                        unique_book_id = book_id.get()
                        f_id = faculty_id.get()

                        bk_id = LMS_verification.get_book_id_for_issue(book_id.get())

                        book_quantity = LMS_verification.get_quantity_for_update_books(bk_id)

                        issued_current_book = LMS_verification.issued_current_book(unique_book_id)
                        print(issued_current_book)

                        if (int(book_quantity)-int(issued_current_book)>0):
                            faculty_issued_books = LMS_verification.faculty_issued_books(f_id)
                            print(faculty_issued_books)
                            book_already_issued = LMS_verification.book_already_issued(unique_book_id)
                            print("knjn ", book_already_issued)
                            if (faculty_issued_books>=2):
                                tkinter.messagebox.showinfo("Library Management System", "Faculty Already Has Issued Two Books")
                            elif(book_already_issued==1):
                                tkinter.messagebox.showinfo("Library Management System", "Book Issued By Other Student/Faculty")
                            else:
                                issue_date = date.today()
                                actual_return_date = date.today() + timedelta(days=15)
                                print(actual_return_date)
                                status = "issued"
                                LibBksDatabase.bookIssueFaculty(f_id, unique_book_id, issue_date, actual_return_date, status)
                                tkinter.messagebox.showinfo("Library Management System", "Book Issued Successfully!")
                                DisplayData()
                                faculty_msg  = "Hello "+ faculty_fullname + "("+f_id+")" +".\nYou Have Issued a book.\nKindly Return it Before "+str(actual_return_date)+".\nThank you.!!"
                                try:
                                    mail.sendmail(faculty_email, faculty_msg)
                                except socket.gaierror as a:
                                    tkinter.messagebox.showinfo("Library Management System", "Email Coudnt Sent! You Are Not Connected with the Internet.")
                                else:
                                    pass
                                
                        
                        elif (int(book_quantity)-int(issued_current_book)==0):
                            print( int(book_quantity)-int(issued_current_book) )
                            qntynstudent_msg = tkinter.messagebox.showinfo("Library Management System", "Sorry! Book Out Of Stock")
                        else:
                            qntynstudent_msg = tkinter.messagebox.showinfo("Library Management System", "Something Went Wrong")


        def returnBook():
            
            if(len(book_id.get())==0):
                unqbkidstudent_msg = tkinter.messagebox.showinfo("Library Management System", "Please Enter Book ID!")
                book_id_is_valid = 0
            elif(len(book_id.get())!=7):
                unqbkidstudent_msg = tkinter.messagebox.showinfo("Library Management System", "Please Enter 7 Digit Book ID!")
                book_id_is_valid = 0
            elif(len(enrollment_no.get())==0):
                unqbkidstudent_msg = tkinter.messagebox.showinfo("Library Management System", "Please Enter Enrollment No.!")

            else:
                book_id_is_valid = 1
                studentIsValid = 0

                Bookissued = LMS_verification.Bookissued(book_id.get())
                if (not(Bookissued==1)):
                    tkinter.messagebox.showinfo("Library Management System", "Invalid Book ID!")
                else:
                    if (len(enrollment_no.get())>=2):
                        studentIsValid = LMS_verification.studentIsValid(enrollment_no.get())
                        if (studentIsValid==1):
                            student_id = LMS_verification.get_student_id(enrollment_no.get())
                            print("student is valid")
                            student_email = LMS_verification.getStudentEmailForSendingEmail(enrollment_no.get())
                            student_fullname  = LMS_verification.getStudentFullnameForSendingEmaill(enrollment_no.get())
                            print(student_fullname)
                        else:
                            student_msg = tkinter.messagebox.showinfo("Library Management System", "Invalid ENROLLMENT_NO!")
                    '''if (not(Bookissued!=1) and (not(studentIsValid==1))):
                        print("guuuuuuuuuuud")
                    else:
                        tkinter.messagebox.showinfo("Library Management System", "Something Went Wrong")'''
                    get_student_id = LMS_verification.get_student_id(enrollment_no.get())
                    checkForValidStudentHasIssuedBook = LMS_verification.checkForValidStudentHasIssuedBook(book_id.get(), get_student_id)
                    print(checkForValidStudentHasIssuedBook)
                    if(checkForValidStudentHasIssuedBook!=1):
                        tkinter.messagebox.showinfo("Library Management System", "Check ENROLLMENT NO. and Book Id.")
                    else:
                        unique_book_id = book_id.get()
                        book_detail = LMS_verification.get_book_detail_for_return(unique_book_id) 
                        print(book_detail)
                        return_date =  date.today()    
                        if (not(book_detail[0][1] == None)):
                            status = "returned"
                            get_stu_id =LMS_verification.get_student_id(enrollment_no.get())
                            get_return_date = LMS_verification.get_return_date(book_id.get(), get_stu_id)
                            #issued_date = datetime.strptime(book_detail[0][4], '%Y-%m-%d').date()
                            issued_date = datetime.strptime(get_return_date, '%Y-%m-%d').date()
                            print("get_return_date", get_return_date)
                            print("issued_date", issued_date)
                            diff =  return_date-issued_date 
                            print("r ",return_date)
                            print("i ",issued_date)
                            print(diff)
                            if (diff.days>=16):
                                email = LMS_verification.getStudentEmailForSendingEmail(enrollment_no.get())
                                u_book_id = LMS_verification.getBookIdForInvoice(unique_book_id)
                                print("book_id: ", u_book_id)
                                book_name =  LMS_verification.getBookNameForInvoice(u_book_id)
                                print("book_name ",book_name)
                                fee = LMS_verification.fee_calc(diff.days)

                        
                                fee_msg = tkinter.messagebox.askyesno("Library Management System", "Sorry! You Are "+str(diff.days) +" Days Late To Return The Book. Have Student/Faculty Paid Fine ₹"+str(fee)+"?")
                                print(fee_msg)
                                if (fee_msg==1):
                                    paid = 1
                                    rec.fee_invoice(fee, unique_book_id, email, book_name, paid)
                                    LibBksDatabase.returnBook(unique_book_id, return_date,status)
                                    tkinter.messagebox.showinfo("Library Management System", "Returned Book Successfully!")
                                    DisplayData()
                                    student_msg  = "Hello "+ student_fullname + "("+enrollment_no.get()+")" +".\nYou Have Succesfully Returned The Book."
                                    try:
                                        mail.sendmail(student_email, student_msg)
                                    except socket.gaierror as a:
                                        tkinter.messagebox.showinfo("Library Management System", "Email Coudnt Sent! You Are Not Connected with the Internet.")
                                    else:
                                        pass


                                elif(fee_msg==0):
                                    paid = 0
                                    rec.fee_invoice(fee, unique_book_id, email, book_name, paid)

                                    fee_msg = tkinter.messagebox.showinfo("Library Management System", "Please Pay The Fine ₹"+str(fee))
                                else:
                                    pass
                            else:
                                LibBksDatabase.returnBook(unique_book_id, return_date,status)
                                tkinter.messagebox.showinfo("Library Management System", "Returned Book Successfully!")
                                student_msg  = "Hello "+ student_fullname + "("+enrollment_no.get()+")" +".\nYou Have Succesfully Returned The Book."
                                try:
                                    mail.sendmail(student_email, student_msg)
                                except socket.gaierror as a:
                                    tkinter.messagebox.showinfo("Library Management System", "Email Coudnt Sent! You Are Not Connected with the Internet.")
                                else:
                                    pass
                                DisplayData()
                        elif(not(book_detail[0][2]==None)):
                            status = "returned"
                            LibBksDatabase.returnBook(unique_book_id, return_date,status)
                            tkinter.messagebox.showinfo("Library Management System", "Returned Book Successfully!")
                            DisplayData()
                        else:
                            print("Something Went Wrong")


        ''' eData(publication_id):
            conn = sqlite3.connect("libbooks.db")
            cur = conn.cursor()
            cur.execute("SELECT name FROM publication WHERE publication_id=?", [publication_id])
            rows = cur.fetchall()
            conn.close()
            publication.set(rows[0][0])

    
        def UpdatPublicationData():
            curItem = tree.focus()
            publication_id = tree.item(curItem)['values'][0]

            check_publication_exist_for_update = LMS_verification.check_publication_exist_for_update(publication_id, publication.get())
           
           
            if(len(publication.get())<=1 ):
                publicationstudent_msg = tkinter.messagebox.showinfo("Library Management System", "Please Enter Publication Name!")
           
            if (check_publication_exist_for_update!=1):
                conn = sqlite3.connect("libbooks.db")
                cur = conn.cursor()
                cur.execute("UPDATE publication SET name=? where publication_id=?", (publication.get(), publication_id) )
                conn.commit()
                conn.close()
                tkinter.messagebox.showinfo("Library Management System", "Updated Data Successfully!")'''
            

        MainFrame = Frame(self.root, padx=10, pady=0)
        MainFrame.pack(side=TOP)

        FrameDetail = Frame(MainFrame, bd=0, width=0,height=0, padx=0, relief=RIDGE)
        FrameDetail.pack(side=BOTTOM)

        ButtonFrameLeft = Frame(MainFrame, width=200, height=335, padx=0, pady=0, relief=RIDGE, bg="Cadet blue")
        ButtonFrameLeft.pack(side=LEFT)

        DataFrame = Frame(MainFrame, bd=1, width=900,height=100, padx=50,pady=20)
        DataFrame.pack(side=LEFT)
        
        DataFrameLEFT = LabelFrame(DataFrame,  width=100,height=100, padx=100, pady=40 ,relief=RIDGE,font=('arial',12,'bold'), bg="Cadet blue")
        DataFrameLEFT.pack(side=TOP)

        ButtonFrameRight = Frame(MainFrame, width=500, height=100, padx=30, pady=25, relief=RIDGE, bg="Cadet blue")
        ButtonFrameRight.pack(side=RIGHT)

        
        #========================widgets ==================

        self.issuereturnTitle = Label(DataFrameLEFT, font=('arial',18,'bold'), text="Issue/Return Book", bg = "Cadet blue")
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
        self.txtunqbkid.grid(row=2 ,column=1)

        #========================================buttons===============================

        self.btnReturnBook = Button(ButtonFrameLeft, text='Return Book', font=('arial', 12, 'bold'), height=2, width=10, bd = 4, command=returnBook)
        self.btnReturnBook.grid(row=0, column=0)

        self.btnAddDate = Button(ButtonFrameRight, text='Issue Book', font=('arial', 12, 'bold'), height=2, width=13, bd = 4, command=issueBook)
        self.btnAddDate.grid(row=0, column=0)

        self.btnDisplayData = Button(ButtonFrameRight, text =' Display Data', font=('arial', 12, 'bold'), height=2, width=13, bd = 4, command=DisplayData)
        self.btnDisplayData.grid(row=1, column=0)

        '''self.btnUpdateData = Button(ButtonFrameRight, text='Update Data', font=('arial', 12, 'bold'), height=2, width=13, bd = 4, command=UpdatPublicationData)
        self.btnUpdateData.grid(row=2, column=0)'''

        self.btnClearData = Button(ButtonFrameRight, text='Clear Data', font=('arial', 12, 'bold'), height=2, width=13, bd = 4, command=ClearData)
        self.btnClearData.grid(row=3, column=0)

        self.btnExit = Button(ButtonFrameRight, text='Exit', font=('arial', 12, 'bold'), height=2, width=13, bd = 4, command=iExit)
        self.btnExit.grid(row=4, column=0)

        


#application = student(root)
#root.mainloop()     

root =Tk()
application = student(root)
root.mainloop()     