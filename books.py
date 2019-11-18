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

#[x[1] for x in a]

class student:
	
    def __init__(self, root):
        self.root = root

        self.root.title = "Library Management System"
        self.root.geometry("1350x750+0+0")
        self.root.configure(background='powder blue')
        tree = ttk.Treeview(root, column=("BOOK_ID", "ISBN","TITLE", "AUTHOR", "CATEGORY", "PUBLICATION", "PAGES"), show='headings')

        tree.column("BOOK_ID", width=70, anchor=W)
        tree.column("ISBN", width=130, anchor='center')
        tree.column("TITLE", width=240, anchor='center')
        tree.column("AUTHOR", width=140, anchor='center')
        tree.column("CATEGORY", width=140, anchor='center')
        tree.column("PUBLICATION", width=180, anchor='center')
        tree.column("PAGES", width=80, anchor='center')


        tree.heading("#1", text="BOOK_ID")
        tree.heading("#2", text="ISBN")
        tree.heading("#3", text="TITLE")
        tree.heading("#4", text="AUTHOR")
        tree.heading("#5", text="CATEGORY")
        tree.heading("#6", text="PUBLICATION")
        tree.heading("#7", text="PAGES")
        tree.pack(side = BOTTOM, pady=30)


        title = StringVar()

        '''def OnDoubleClick(self):
            print(self.tree.selection())
            print(self.tree.set(selected, '#1'))'''

        def OnDoubleClick(self):
            curItem = tree.focus()
            book_id_to_update = tree.item(curItem)['values'][0]
            isbn = tree.item(curItem)['values'][1]

            UpdateData(book_id_to_update, isbn)

        #self.tree.bind("<Double-1>", OnDoubleClick)
        tree.bind('<ButtonRelease-1>', OnDoubleClick)

        author= StringVar()
        author.set("Select")
        category = StringVar()
        category.set("Select")
        publication = StringVar()
        publication.set("Select")
        pagecount = StringVar()
        isbn = StringVar()
        quantity = StringVar()
        quantity10 = StringVar()

        def addAuthor():
            call(["python3", "author.py"])
            root.destroy()
            return

        def addCategory():
            call(["python3", "category.py"])
            root.destroy()
            return

        def addPublication():
            call(["python3", "publication.py"])
            root.destroy()
            return

      
        def iExit():
            iExit = tkinter.messagebox.askyesno("Library Management System", "Are You Sure You Want to Exit?")
            if iExit>0:
                root.destroy()
                return

        def ClearData():
            self.txtTitle.delete(0, END)
            self.txtPagecount.delete(0, END)
            category.set("Select")
            author.set("Select")
            publication.set("Select")
            self.txtQuantity.delete(0, END)

        def AddQuantity():

            a = quantity.get()
            if (a==""):
                quantity.set(10)
            else:
                a = int(a)+10
                quantity.set(a)

        def DisplayData():
            a = []
            conn = sqlite3.connect("libbooks.db")
            cur = conn.cursor()
            cur.execute("SELECT * FROM books")
            for i in tree.get_children():
                tree.delete(i)
            rows = cur.fetchall()
            conn.close()

            data = [list(elem) for elem in rows]

            conn = sqlite3.connect("libbooks.db")
            cur = conn.cursor()
            cur.execute("SELECT * FROM author")
            authors_data = cur.fetchall()
            conn.close()

            conn = sqlite3.connect("libbooks.db")
            cur = conn.cursor()
            cur.execute("SELECT * FROM category")
            category_data = cur.fetchall()
            conn.close()

            conn = sqlite3.connect("libbooks.db")
            cur = conn.cursor()
            cur.execute("SELECT * FROM publication")
            publication_data = cur.fetchall()

            conn.close()
            
            for i in range(0, len(data)):
                author_indx = data[i][3]-1
                category_indx = data[i][4]-1
                publication_indx = data[i][5]-1

                data[i][3] = authors_data[author_indx][1]
                data[i][4] = category_data[category_indx][1]
                data[i][5] = publication_data[publication_indx][1]

            for i in data:
                tree.insert("", tk.END, values=i)


        def addData():
            page = pagecount.get()
            if (len(title.get())<=1):
                titlemsg = tkinter.messagebox.showinfo("Library Management System", "Please Enter Title of The Book!")
            elif(len(author.get())==0 or author.get()=="Select"):
                authormsg = tkinter.messagebox.showinfo("Library Management System", "Please Select The Author Name!")
            elif(len(category.get())==0 or category.get()=="Select"):
                categorymsg = tkinter.messagebox.showinfo("Library Management System", "Please Select the Category!")
            elif(len(publication.get())==0 or publication.get()=="Select"):
                publicationmsg = tkinter.messagebox.showinfo("Library Management System", "Please Select the Publication!")
            elif(len(pagecount.get())==0 ):
                pagecountmsg = tkinter.messagebox.showinfo("Library Management System", "Please Enter pagecount!")
            elif (not(page.isnumeric())):
                pagecountmsg = tkinter.messagebox.showinfo("Library Management System", "Invalid pagecount!")
            elif (len(quantity.get())==0):
                quantitymsg= tkinter.messagebox.showinfo("Library Management System", "Please Enter Quantity of The Book!")
            elif (not(quantity.get().isnumeric())):
                quantitymsg = tkinter.messagebox.showinfo("Library Management System", "Invalid Quantity!")
            else:
                isbn = LMS_verification.get_isbn(4)
                tit = title.get()
                author_id = LMS_verification.get_author_id(author.get()) 
                category_id = LMS_verification.get_category_id(category.get())
                publication_id = LMS_verification.get_publication_id(publication.get())
                pagecnt = pagecount.get()
                qnt = quantity.get()
                book_exist = LMS_verification.check_book_exist(tit.strip(), author_id, category_id, publication_id, pagecnt.strip())

                if (book_exist==0 or book_exist==None) :
                    pass

                elif(book_exist==1):
                    get_isbn = LMS_verification.get_exist_isbn(tit, author_id, category_id, publication_id)
                    get_exist_unique_id = LMS_verification.get_exist_unique_id(get_isbn)
                    book_id = LMS_verification.get_book_id_for_unique_id(get_isbn)

                    for i in range(0, int(qnt)):
                        unique_book_id = LMS_verification.get_unique_book_id(book_id, get_isbn)
                        LibBksDatabase.adduniqueid(book_id, unique_book_id)
                    tkinter.messagebox.showinfo("Library Management System", "Book Exist! Inserted Data Successfully!")
                    DisplayData()

                else:
                    tkinter.messagebox.showinfo("Library Management System", "Something Went Wrong!")
                
                if (not(book_exist==1)):
                    LibBksDatabase.addBook(isbn.strip(), tit, author_id, category_id, publication_id, pagecnt)
                    book_id = LMS_verification.get_book_id_for_unique_id(isbn)

                    for j in range(0, int(qnt)):
                        unique_book_id = LMS_verification.get_unique_book_id(book_id, isbn)
                        print(unique_book_id)
                        LibBksDatabase.adduniqueid(book_id, unique_book_id)
                    
                    tkinter.messagebox.showinfo("Library Management System", "Inserted Data Successfully!")
                    DisplayData()
       

        def UpdateData(book_id, isbn):

            conn = sqlite3.connect("libbooks.db")
            cur = conn.cursor()
            cur.execute("SELECT title, author_id, category_id, publication_id, pagecount FROM books WHERE book_id =?", [book_id])
            rows = cur.fetchall()
            conn.close()


            title.set(rows[0][0])

            author_to_update = LMS_verification.get_author_for_update_books(rows[0][1])
            author.set(author_to_update)

            category_to_update = LMS_verification.get_category_for_update_books(rows[0][2])
            category.set(category_to_update)
            
            publication_to_update = LMS_verification.get_publicatiob_for_update_books(rows[0][3])
            publication.set(publication_to_update)

            pagecount.set(rows[0][4])

            quantity_to_update = LMS_verification.get_quantity_for_update_books(book_id)
            quantity.set(quantity_to_update)
            

        def UpdateBooksData():


            page = pagecount.get()

            if (len(title.get())<=1):
                titlemsg = tkinter.messagebox.showinfo("Library Management System", "Please Enter Title of The Book!")
            elif(len(author.get())==0 or author.get()=="Select"):
                authormsg = tkinter.messagebox.showinfo("Library Management System", "Please Select The Author Name!")
            elif(len(category.get())==0 or category.get()=="Select"):
                categorymsg = tkinter.messagebox.showinfo("Library Management System", "Please Select the Category!")
            elif(len(publication.get())==0 or publication.get()=="Select"):
                publicationmsg = tkinter.messagebox.showinfo("Library Management System", "Please Select the Publication!")
            elif (len(pagecount.get())==0 ):
                pagecountmsg = tkinter.messagebox.showinfo("Library Management System", "Please Enter pagecount!")
            elif (not(page.isnumeric())):
                pagecountmsg = tkinter.messagebox.showinfo("Library Management System", "Invalid pagecount!")
            elif (len(quantity.get())==0):
                quantitymsg= tkinter.messagebox.showinfo("Library Management System", "Please Enter Quantity of The Book!")
            elif (not(quantity.get().isnumeric())):
                quantitymsg = tkinter.messagebox.showinfo("Library Management System", "Invalid Quantity!")

            
            tit = title.get()

            author_id = LMS_verification.get_author_id(author.get()) 
            
            print("author_id : ", author_id)

            category_id = LMS_verification.get_category_id(category.get())
            print("category id: ", category_id)

            publication_id = LMS_verification.get_publication_id(publication.get())
            print("publication id: ", publication_id)

            pagecnt = pagecount.get()

            book_exist = LMS_verification.check_book_exist(tit.strip(), author_id, category_id, publication_id, pagecnt.strip())
            print("book_exist: ", book_exist)

            if (book_exist==0 or book_exist==None) :
                pass
                
            elif(book_exist==1):
                tkinter.messagebox.showinfo("Library Management System", "Book Already Available ")   
            else:
                tkinter.messagebox.showinfo("Library Management System", "Something Went Wrong!")
            if (not(book_exist==1)):
                curItem = tree.focus()
                try:
                    isbn_no = tree.item(curItem)['values'][1]
                except IndexError as e:
                    tkinter.messagebox.showinfo("Library Management System", "Please Select Book!")
                else:
                    pass
                finally:
                    pass


                conn = sqlite3.connect("libbooks.db")
                cur = conn.cursor()
                cur.execute("UPDATE books SET title=?, author_id=?, category_id=?, publication_id=?, pagecount=? where isbn =?", (tit.strip(), author_id, category_id, publication_id, pagecnt.strip(),isbn_no))
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

        self.studenttitle = Label(DataFrameLEFT, font=('arial',18,'bold'), text="Add Book", bg = "Cadet blue")
        self.studenttitle.grid(row =0, column=0, columnspan=2)

        self.lblTitle = Label(DataFrameLEFT, font=('arial',12,'bold'), text="Title", padx=10, pady=5 ,bg = "Cadet blue")
        self.lblTitle.grid(row=1,column=0,sticky=W)
        self.txtTitle = Entry(DataFrameLEFT, font=('arial',12,'bold'),textvariable=title, width=23)
        self.txtTitle.grid(row=1,column=1)
        

        self.lblAuthor = Label(DataFrameLEFT, font=('arial',12,'bold'), text="Author", padx=10, pady=5,bg = "Cadet blue")
        self.lblAuthor.grid(row=2,column=0,sticky=W)

        authors = LMS_verification.get_authors()

        self.txtAuthor = OptionMenu(DataFrameLEFT, author,*authors )
        self.txtAuthor.grid(row=2,column=1)

        '''self.btnAddAuthorSpace = Label(DataFrameLEFT, text='', bg = "Cadet blue", padx=30)
        self.btnAddAuthorSpace.grid(row=2, column=2)'''


        self.btnAddAuthor = Button(DataFrameLEFT, text='Add Author', font=('arial', 10), height=0, width=0, bd = 0, padx=7,  command=addAuthor)
        self.btnAddAuthor.grid(row=2, column=3)

        categories = LMS_verification.get_categories()

        self.lblCategory = Label(DataFrameLEFT, font=('arial',12,'bold'), text="Category", padx=10, pady=5,bg = "Cadet blue")
        self.lblCategory.grid(row=3,column=0,sticky=W)
        if (len(categories)>=1):
            self.txtCategory = OptionMenu(DataFrameLEFT, category, *categories)
            self.txtCategory.grid(row=3,column=1)
        else:
            self.txtCategory = OptionMenu(DataFrameLEFT, category, "Select")
            self.txtCategory.grid(row=3,column=1)


        self.btnAddCategory = Button(DataFrameLEFT, text='Add Category', font=('arial', 10), height=0, width=0, bd = 0, padx=7,  command=addCategory)
        self.btnAddCategory.grid(row=3, column=3)

        publications = LMS_verification.get_publications()

        self.lblPublication = Label(DataFrameLEFT,font=('arial', 12, 'bold'), text="Publication",padx=10,pady=5,bg = "Cadet blue")
        self.lblPublication.grid(row=4, column=0, sticky=W)
        self.txtPublication = OptionMenu(DataFrameLEFT, publication, *publications)
        self.txtPublication.grid(row=4, column=1)

        self.btnAddPublication = Button(DataFrameLEFT, text='Add Publication', font=('arial', 10), height=0, width=0, bd = 0, padx=7,  command=addPublication)
        self.btnAddPublication.grid(row=4, column=3)

        self.lblPagecount = Label(DataFrameLEFT, font=('arial',12,'bold'), text="Pagecount", padx=10, pady=5,bg = "Cadet blue")
        self.lblPagecount.grid(row=5,column=0,sticky=W)
        self.txtPagecount = Entry(DataFrameLEFT, font=('arial',12,'bold'), textvariable=pagecount, width=10)
        self.txtPagecount.grid(row=5,column=1)
        

        '''self.lblIsbn = Label(DataFrameLEFT, font=('arial',12,'bold'), text="ISBN", padx=10, pady=5,bg = "Cadet blue")
        self.lblIsbn.grid(row=6,column=0,sticky=W)
        self.txtIsbn= Entry(DataFrameLEFT, font=('arial',12,'bold'),textvariable=isbn, width=23)
        self.txtIsbn.grid(row=6,column=1)'''

        self.lblQuantity = Label(DataFrameLEFT, font=('arial',12,'bold'), text="Quantity", padx=10, pady=5,bg = "Cadet blue")
        self.lblQuantity.grid(row=7,column=0,sticky=W)
        self.txtQuantity= Entry(DataFrameLEFT, font=('arial',12,'bold'),textvariable=quantity, width=10)
        self.txtQuantity.grid(row=7,column=1)

        self.btnAddQuantity10= Button(DataFrameLEFT, text='+10', font=('arial', 8, 'bold'), height=1, width=1, bd = 0, command = AddQuantity)
        self.btnAddQuantity10.grid(row=7,column=2)


        #======================buttons=============================


        self.btnAddDate = Button(ButtonFrame, text='Add Book', font=('arial', 12, 'bold'), height=2, width=13, bd = 4, command=addData)
        self.btnAddDate.grid(row=0, column=0)

        self.btnDisplayData = Button(ButtonFrame, text=' Display Books', font=('arial', 12, 'bold'), height=2, width=13, bd = 4, command=DisplayData)
        self.btnDisplayData.grid(row=1, column=0)

        self.btnUpdateData = Button(ButtonFrame, text='Update Book', font=('arial', 12, 'bold'), height=2, width=13, bd = 4, command=UpdateBooksData)
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
