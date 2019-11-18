from tkinter import * 
from tkinter import ttk
import random
from subprocess import call
from datetime import datetime 
import tkinter.messagebox
from random import randint
import sqlite3
import LibBksDatabase
import re
import requests


#=======================================STUDENT================================================

def check_department(dept):
	conn = sqlite3.connect('libbooks.db')
	cursor = conn.execute("SELECT * from department where name=?", [str(dept)])
	rows = cursor.fetchall()
	return rows[0][1], rows[0][0] 

def get_dept_for_update_books(dept_id):
	conn = sqlite3.connect('libbooks.db')
	cursor = conn.execute("SELECT name from department where dept_id=?", [dept_id])
	rows = cursor.fetchall()
	return rows[0][0]


def check_gender(gender):
	if (gender=="1"):
		gender = "Male"
	else:
		gender = "Female"
	return gender

def email_check(email):
	addressToVerify = email
	match = re.match('^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,4})$', addressToVerify)
	if match == None:
		emailmsg = tkinter.messagebox.showerror("Library Management System", "Invalid Email!")
		return 1
	else:
		return 0

def phoneisValid(s): 
     
    Pattern = re.compile("(0/91/87)?[0-9][0-9]{9}")  
    # 2) and contains 9 digits 
    return Pattern.match(s)


def check_enrollment_no(dept_id, department):
	conn = sqlite3.connect('libbooks.db')
	cursor = conn.execute("SELECT count(*) from student where dept_id=?", [str(dept_id)])
	rows = cursor.fetchall()
	print(rows)
	if(str(rows[0][0]))=="0":
		enrolment_no = "19"+department+"22001"
	else:
		did = (rows[0][0])+1
		print("did : ", did)
		print("len : ", len(str(did)))
		if (len(str(did)) == 1):
			enrolment_no = "19"+department+"2200"+str(did)
		elif (len(str(did))== 2):
			enrolment_no = "19"+department+"220"+str(did)
		elif (len(str(did))== 3):
			enrolment_no = "19"+department+"22"+str(did)
		else:
			print("something went wrong while creating enrolment_no (LMS_VERIFICATION LINE NO.49)")
		print("enrolment_no  : ", enrolment_no)
		conn.commit()
		conn.close()
	return enrolment_no

def email_exist_for_student(email):
	conn = sqlite3.connect('libbooks.db')
	cursor = conn.execute("SELECT email from student")
	for i in cursor:
		if (email.lower()==str(i[0].lower()) ):
			emailmsg = tkinter.messagebox.showerror("Library Management System", "Email Already Exists!")
			return 1

	return 0


def phone_exist_for_student(phone):
	conn = sqlite3.connect('libbooks.db')
	cursor = conn.execute("SELECT phone from student")
	for i in cursor:
		if (phone==str(i[0])):
			phonemsg = tkinter.messagebox.showerror("Library Management System", "Phone No. Already Exists!")
			return 1
	return 0  

def email_exist_for_update_student(email, enrolment_no):
	conn = sqlite3.connect('libbooks.db')
	cursor = conn.execute("SELECT email from student")
	for i in cursor:
		if (email.lower()==str(i[0].lower()) ):
			cursor = conn.execute("SELECT enrollment_no from student where email=?", [str(i[0])] )
			for j in cursor:
				if enrolment_no==j[0]:
					return 0
				else:
					emailmsg = tkinter.messagebox.showerror("Library Management System", "Email Already Exists!")
					return 1

	return 0

def phone_exist_for_update_student(phone, enrolment_no):
	conn = sqlite3.connect('libbooks.db')
	cursor = conn.execute("SELECT phone from student")
	for i in cursor:
		if (phone==str(i[0])):
			cursor = conn.execute("SELECT enrollment_no from student where phone=?", [str(i[0])] )
			for j in cursor:
				if enrolment_no==j[0]:
					return 0
				else:
					phonemsg = tkinter.messagebox.showerror("Library Management System", "Phone No. Already Exists!")
					return 1
	return 0 


#===============================================FACULTY======================================

def email_exist_for_faculty(email):
	conn = sqlite3.connect('libbooks.db')
	cursor = conn.execute("SELECT email from faculty")
	for i in cursor:
		if (email.lower()==str(i[0].lower()) ):
			emailmsg = tkinter.messagebox.showerror("Library Management System", "Email Already Exists!")
			return 1

	return 0

def phone_exist_for_faculty(phone):
	conn = sqlite3.connect('libbooks.db')
	cursor = conn.execute("SELECT phone from faculty")
	for i in cursor:
		if (phone==str(i[0])):
			phonemsg = tkinter.messagebox.showerror("Library Management System", "Phone No. Already Exists!")
			return 1
	return 0 

def email_exist_for_update_faculty(email, faculty_id):
	conn = sqlite3.connect('libbooks.db')
	cursor = conn.execute("SELECT email from faculty")
	for i in cursor:
		if (email.lower()==str(i[0].lower()) ):
			cursor = conn.execute("SELECT faculty_id from faculty where email=?", [str(i[0])] )
			for j in cursor:
				if faculty_id==j[0]:
					return 0
				else:
					emailmsg = tkinter.messagebox.showerror("Library Management System", "Email Already Exists!")
					return 1

	return 0

def phone_exist_for_update_faculty(phone, faculty_id):
	conn = sqlite3.connect('libbooks.db')
	cursor = conn.execute("SELECT phone from faculty")
	for i in cursor:
		if (phone==str(i[0])):
			cursor = conn.execute("SELECT faculty_id from faculty where phone=?", [str(i[0])] )
			for j in cursor:
				if faculty_id==j[0]:
					return 0
				else:
					phonemsg = tkinter.messagebox.showerror("Library Management System", "Phone No. Already Exists!")
					return 1
	return 0

#==============================Category============================

def check_category_exist(category):
	conn = sqlite3.connect('libbooks.db')
	cursor = conn.execute("SELECT category FROM category")
	for i in cursor:
		if (str(i[0].lower())==category.lower()):
			Categorymsg = tkinter.messagebox.showerror("Library Management System", "Category Already Exists!")
			return 1
		
def check_category_exist_for_update(category_id, category):
	conn = sqlite3.connect('libbooks.db')
	cursor = conn.execute("SELECT category FROM category")
	for i in cursor:
		print(str(i[0]))
		if (category.lower()==str(i[0]).lower() ):
			cursor = conn.execute("SELECT category_id from category where category=?", [str(i[0])] )
			for j in cursor:
				if category_id==j[0]:
					return 0
				else:
					categoryMsg = tkinter.messagebox.showerror("Library Management System", "Category Already Exists!")
					return 1
	return 0 


#=========================================Department========================

def get_departments(): # for category.py drop down list
	conn = sqlite3.connect('libbooks.db')
	cursor = conn.execute("SELECT name from department")
	depts = []
	for i in cursor:
		depts.append(str(i[0]))
	return depts

def check_department_exist(dept):  	 #for department.py
	conn = sqlite3.connect('libbooks.db')
	cursor = conn.execute("SELECT name FROM department")
	for i in cursor:
		if (str(i[0].lower())==dept.lower()):
			deptmsg = tkinter.messagebox.showerror("Library Management System", "Department Already Exists!")
			return 1

def check_department_exist_for_update(dept_id, dept):
	conn = sqlite3.connect('libbooks.db')
	cursor = conn.execute("SELECT name FROM department")
	for i in cursor:
		print(str(i[0]))
		if (dept.lower()==str(i[0]).lower() ):
			cursor = conn.execute("SELECT dept_id from department where name=?", [str(i[0])] )
			for j in cursor:
				if dept_id==j[0]:
					return 0
				else:
					deptMsg = tkinter.messagebox.showerror("Library Management System", "Department Already Exists!")
					return 1
	return 0 


#===============================Author=======================

def check_author_exist(author):
	conn = sqlite3.connect('libbooks.db')
	cursor = conn.execute("SELECT name FROM author")
	for i in cursor:
		if (str(i[0].lower())==author.lower()):
			authormsg = tkinter.messagebox.showerror("Library Management System", "Author Already Exists!")
			return 1

def check_author_exist_for_update(author_id, author):
	conn = sqlite3.connect('libbooks.db')
	cursor = conn.execute("SELECT name FROM author")
	for i in cursor:
		print(str(i[0]))
		if (author.lower()==str(i[0]).lower() ):
			cursor = conn.execute("SELECT author_id from author where name=?", [str(i[0])] )
			for j in cursor:
				if author_id==j[0]:
					return 0
				else:
					authorMsg = tkinter.messagebox.showerror("Library Management System", "Author Already Exists!")
					return 1
	return 0 


#=====================================Publication==================
def websiteIsValid(website):
	from requests.exceptions import ConnectionError
	try:
		request = requests.get('http://www.example.com')
	except ConnectionError:
		websiteMsg = tkinter.messagebox.showerror("Library Management System", "Invalid Website!")
	else:
		print('Web site exists')
    

def phone_exist_for_publication(phone):

	conn = sqlite3.connect('libbooks.db')
	cursor = conn.execute("SELECT phone from publication")
	for i in cursor:
		if (phone==str(i[0])):
			return 1
	return 0  



def check_publication_exist(publication):
	conn = sqlite3.connect('libbooks.db')
	cursor = conn.execute("SELECT name FROM publication")
	for i in cursor:
		if (str(i[0].lower())==publication.lower()):
			publicationmsg = tkinter.messagebox.showerror("Library Management System", "Publication Already Exists!")
			return 1
	return 0

def check_publication_exist_for_update(publication_id, publication):
	conn = sqlite3.connect('libbooks.db')
	cursor = conn.execute("SELECT name FROM publication")
	for i in cursor:
		print(str(i[0]))
		if (publication.lower()==str(i[0]).lower() ):
			cursor = conn.execute("SELECT publication_id from publication where name=?", [str(i[0])] )
			for j in cursor:
				if publication_id==j[0]:
					return 0
				else:
					publicationMsg = tkinter.messagebox.showerror("Library Management System", "Publication Already Exists!")
					return 1
	return 0 
#=====================================Books.py==================
def get_book_id_for_unique_id(isbn):
	conn = sqlite3.connect("libbooks.db")
	cur = conn.cursor()
	cur.execute("SELECT book_id FROM books WHERE isbn=?", [isbn])
	rows = cur.fetchall()
	conn.close()
	return rows[0][0]

def get_authors():
	conn = sqlite3.connect('libbooks.db')
	cursor = conn.execute("SELECT name from author")
	author = []
	for i in cursor:
		author.append(str(i[0]))
	return author

def get_categories():
	conn = sqlite3.connect('libbooks.db')
	cursor = conn.execute("SELECT category from category")
	category = []
	for i in cursor:
		category.append(str(i[0]))
	return category

def get_publications():
	conn = sqlite3.connect('libbooks.db')
	cursor = conn.execute("SELECT name from publication")
	publication = []
	for i in cursor:
		publication.append(str(i[0]))
	return publication

def get_isbn(n):
	range_start = 10**(n-1)
	range_end = (10**n)-1
	return "19022"+ str(randint(range_start, range_end))

def get_unique_book_id(book_id, isbn):
	last_four = isbn[-4:]
	conn = sqlite3.connect('libbooks.db')
	cursor = conn.execute("SELECT count(*) from unique_book_id books where book_id=?", [str(book_id)])
	a = cursor.fetchall()
	add = a[0][0]
	add = add+1
	if (len(str(add))==1):
		add = "00"+str(add)
	elif (len(str(add))==2):
		add = "0"+ str(add)
	elif (len(str(add))==3):
		add = add

	unique_book_id = str(last_four)+str(add)  
	return unique_book_id


	'''if (len(str(did)) == 1):
			enrolment_no = "19"+department+"2200"+str(did)
		elif (len(str(did))== 2):
			enrolment_no = "19"+department+"220"+str(did)
		elif (len(str(did))== 3):
			enrolment_no = "19"+department+"22"+str(did)'''
def get_author_id(author):
	conn = sqlite3.connect('libbooks.db')
	cursor = conn.execute("SELECT author_id from author where name=?", [str(author)])
	ids = cursor.fetchall()
	if (len(ids)==0 or len(ids)=="0"):
		authorMsg = tkinter.messagebox.showerror("Library Management System", "No Author Found!!!")
	else:
		author_id = ids[0][0]
	return author_id

def get_category_id(category):
	conn = sqlite3.connect('libbooks.db')
	cursor = conn.execute("SELECT category_id from category where category=?", [str(category)])
	ids = cursor.fetchall()
	if (len(ids)==0 or len(ids)=="0"):
		categoryMsg = tkinter.messagebox.showerror("Library Management System", "No Category Found!!!")
	else:
		category_id = ids[0][0]
	return category_id

def get_publication_id(publication):
	conn = sqlite3.connect('libbooks.db')
	cursor = conn.execute("SELECT publication_id from publication where name=?", [str(publication)])
	ids = cursor.fetchall()
	if (len(ids)==0 or len(ids)=="0"):
		publicationMsg = tkinter.messagebox.showerror("Library Management System", "No Publication Found!!!")
	else:
		publication_id = ids[0][0]
	return publication_id

def check_book_exist(tit, author_id, category_id, publication_id, pagecnt):
	conn = sqlite3.connect('libbooks.db')
	cursor = conn.execute("SELECT * from books")
	for i in cursor:
		print("3: ", str(i[3]))
		print("4: ", str(author_id))
		if (str(i[2])==str(tit) and str(i[3])==str(author_id) and str(i[4])==str(category_id) and str(i[5])==str(publication_id)  ):
			print("Book Already Available")
			return 1	
	return 0
	conn.close()

def get_exist_isbn(tit, author_id, category_id, publication_id):
	conn = sqlite3.connect('libbooks.db')
	cursor = conn.execute("SELECT * from books")
	for i in cursor:
		if (str(i[2])==str(tit) and str(i[3])==str(author_id) and str(i[4])==str(category_id) and str(i[5])==str(publication_id) ):
			return str(i[1])
	return 0
	conn.close()
	
def get_exist_unique_id(isbn):
	conn = sqlite3.connect('libbooks.db')
	cursor = conn.execute("SELECT count(*) from books where isbn=?", [isbn])
	unique_id = cursor.fetchall()
	return unique_id[0] 

def get_author_for_update_books(author_id):
	conn = sqlite3.connect("libbooks.db")
	cur = conn.cursor()
	cur.execute("SELECT name FROM author WHERE author_id =?", [author_id])
	rows = cur.fetchall()
	conn.close()
	return rows[0][0]

def	get_category_for_update_books(category_id):
	conn = sqlite3.connect("libbooks.db")
	cur = conn.cursor()
	cur.execute("SELECT category FROM category WHERE category_id =?", [category_id])
	rows = cur.fetchall()
	conn.close()
	return rows[0][0]

def get_publicatiob_for_update_books(publication_id):
	conn = sqlite3.connect("libbooks.db")
	cur = conn.cursor()
	cur.execute("SELECT name FROM publication WHERE publication_id =?", [publication_id])
	rows = cur.fetchall()
	conn.close()
	return rows[0][0]

def get_quantity_for_update_books(book_id):
	conn = sqlite3.connect("libbooks.db")
	cur = conn.cursor()
	cur.execute("SELECT count(*) FROM unique_book_id WHERE book_id = ?", [book_id])
	rows = cur.fetchall()
	for i in rows:
		print(i)
	conn.close()
	return rows[0][0]
#===================================issue/return.py==================================


def studentIsValid(enrollment_no):
	conn = sqlite3.connect("libbooks.db")
	cur = conn.cursor()
	cursor = conn.execute("SELECT enrollment_no FROM student")
	enrollment_no = str(enrollment_no)
	for i in cursor:
		if ((str(i[0]))==str(enrollment_no)):
			return 1
	return 0
	conn.close()

def isbnIsValid(isbn):
	conn = sqlite3.connect("libbooks.db")
	cur = conn.cursor()
	cursor = conn.execute("SELECT isbn FROM books")
	for i in cursor:
		if (str(i[0])==str(isbn)):

			return 1
	return 0
	conn.close()

def faculty_idIsValid(faculty_id):
	conn = sqlite3.connect("libbooks.db")
	cur = conn.cursor()
	cursor = conn.execute("SELECT faculty_id FROM faculty")
	for i in cursor:
		if ((str(i[0]))==str(faculty_id)):
			return 1
	return 0
	conn.close()

def get_unique_book_id_for_issue_return(isbn):
	conn = sqlite3.connect("libbooks.db")
	cur = conn.cursor()
	cursor = conn.execute("SELECT unique_book_id FROM books where isbn=?", [isbn])
	ids = cursor.fetchall()
	return ids[0][0]
	conn.close()

def check_book_quantity(book_id):
	conn = sqlite3.connect("libbooks.db")
	cur = conn.cursor()
	cursor = conn.execute("SELECT count(*) from (select unique_book_id FROM unique_book_id where book_id=?)", [book_id])
	ids = cursor.fetchall()
	print("bhbh", ids[0][0])
	return ids[0][0]
	conn.close()

def issued_current_book(unique_book_id):
	conn = sqlite3.connect("libbooks.db")
	cur = conn.cursor()
	cursor = conn.execute("SELECT count(*) FROM issue_return where unique_book_id=? and status='issued' ", [unique_book_id])
	ids = cursor.fetchall()
	return ids[0][0]
	conn.close()

def student_issued_books(student_id):
	conn = sqlite3.connect("libbooks.db")
	cur = conn.cursor()
	cursor = conn.execute("SELECT count(*) FROM issue_return where student_id=? and status='issued' ", [student_id])
	ids = cursor.fetchall()
	return ids[0][0]
	conn.close()

def uniqueBookIdIsValid(unique_book_id):
	conn = sqlite3.connect("libbooks.db")
	cur = conn.cursor()
	cursor = conn.execute("SELECT unique_book_id FROM unique_book_id")
	for i in cursor:
		if (str(i[0])==str(unique_book_id)):

			return 1
	return 0
	conn.close()

def get_book_id_for_issue(unique_book_id):
	print("unique_book_id : ", unique_book_id)
	conn = sqlite3.connect("libbooks.db")
	cur = conn.cursor()
	cursor = conn.execute("SELECT book_id FROM unique_book_id where unique_book_id=?", [unique_book_id])
	ids = cursor.fetchall()
	print("cd ", ids[0][0])
	id = ids[0][0]
	return id
	conn.close()


	conn = sqlite3.connect("libbooks.db")
	cur = conn.cursor()
	cursor = conn.execute("SELECT isbn FROM books where book_id=?", [id])
	ids = cursor.fetchall()
	print("Csd", ids[0][0])
	conn.close()
	return ids[0][0]


def faculty_issued_books(faculty_id):
	conn = sqlite3.connect("libbooks.db")
	cur = conn.cursor()
	cursor = conn.execute("SELECT count(*) FROM issue_return where faculty_id=? and status='issued' ", [faculty_id])
	ids = cursor.fetchall()
	return ids[0][0]
	conn.close()

def get_book_detail_for_return(unique_book_id):
	conn = sqlite3.connect("libbooks.db")
	cur = conn.cursor()
	cursor = conn.execute("SELECT * FROM issue_return where unique_book_id=?", [unique_book_id])
	book_details = cursor.fetchall()
	return book_details
	conn.close()

def book_already_issued(unique_book_id):
	conn = sqlite3.connect("libbooks.db")
	cur = conn.cursor()
	cursor = conn.execute("SELECT unique_book_id FROM issue_return where status='issued' ")
	for i in cursor:
		if (str(i[0])==str(unique_book_id)):
			return 1
	return 0
	conn.close()


def get_student_id(enrollment_no):
	conn = sqlite3.connect("libbooks.db")
	cur = conn.cursor()
	cursor = conn.execute("SELECT student_id FROM student where enrollment_no=?  ", [enrollment_no])
	ids = cursor.fetchall()
	return ids[0][0]
	conn.close()

def Bookissued(book_id):
	
	conn = sqlite3.connect("libbooks.db")
	cur = conn.cursor()
	cursor = conn.execute("SELECT unique_book_id FROM issue_return where status='issued' " )
	ids = cursor.fetchall()
	for i in ids:
		print(str(i[0]),str(book_id))
		if (str(i[0])==str(book_id)):
			return 1
	return 0
	conn.close()

def getStudentEmailForSendingEmail(enrollment_no):
	conn = sqlite3.connect("libbooks.db")
	cur = conn.cursor()
	cursor = conn.execute("SELECT email FROM student where enrollment_no=?  ", [enrollment_no])
	ids = cursor.fetchall()
	return ids[0][0]

def getStudentFullnameForSendingEmaill(enrollment_no):
	conn = sqlite3.connect("libbooks.db")
	cur = conn.cursor()
	cursor = conn.execute("SELECT firstname,lastname FROM student where enrollment_no=?  ", [enrollment_no])
	ids = cursor.fetchall()

	return ids[0][0]+" "+ids[0][1]

def getFacultyEmailForSendingEmail(faculty_id):
	conn = sqlite3.connect("libbooks.db")
	cur = conn.cursor()
	cursor = conn.execute("SELECT email FROM faculty where faculty_id=?  ", [faculty_id])
	ids = cursor.fetchall()
	return ids[0][0]

def getFacultyFullnameForSendingEmail(faculty_id):
	conn = sqlite3.connect("libbooks.db")
	cur = conn.cursor()
	cursor = conn.execute("SELECT firstname,lastname FROM faculty where faculty_id=?  ", [faculty_id])
	ids = cursor.fetchall()
	return ids[0][0]+" "+ids[0][1]


#====================================student search ==================================


def getStudentBookRecords(student_id):
	conn = sqlite3.connect("libbooks.db")
	cur = conn.cursor()
	cursor = conn.execute("SELECT student_id, faculty_id, unique_book_id, issue_date, return_date, actual_return_date, status FROM issue_return where student_id=?  ", [student_id])
	ids = cursor.fetchall()
	print("enr", ids)
	return ids
	conn.close()

def getBookId(unique_book_id):
	conn = sqlite3.connect("libbooks.db")
	cur = conn.cursor()
	cursor = conn.execute("SELECT book_id FROM unique_book_id where unique_book_id=?  ", [unique_book_id])
	ids = cursor.fetchall()
	return ids[0][0]
	conn.close()

def getBookTitle(book_id):
	print(book_id)
	conn = sqlite3.connect("libbooks.db")
	cur = conn.cursor()
	cursor = conn.execute("SELECT title FROM books where book_id=?", [book_id])
	ids = cursor.fetchall()
	return ids[0][0]
	conn.close()

#=====================faculty search=====================

def getFacultyBookRecords(faculty_id):
	conn = sqlite3.connect("libbooks.db")
	cur = conn.cursor()
	cursor = conn.execute("SELECT faculty_id, faculty_id, unique_book_id, issue_date, return_date, actual_return_date, status FROM issue_return where faculty_id=?  ", [faculty_id])
	ids = cursor.fetchall()
	print("enr", ids)
	return ids
	conn.close()

def fee_calc(days):
	return days

def getBookIdForInvoice(unique_book_id):
	conn = sqlite3.connect("libbooks.db")
	cur = conn.cursor()
	cursor = conn.execute("SELECT book_id FROM unique_book_id where unique_book_id=?  ", [unique_book_id])
	ids = cursor.fetchall()
	print("enr", ids)
	return ids[0][0]
	conn.close()


def getBookNameForInvoice(book_id):

	conn = sqlite3.connect("libbooks.db")
	cur = conn.cursor()
	cursor = conn.execute("SELECT title FROM books where book_id=?  ", [book_id])
	ids = cursor.fetchall()
	print("enr", ids)
	return ids[0][0]
	conn.close()

def checkForValidStudentHasIssuedBook(book_id, student_id):
	conn = sqlite3.connect("libbooks.db")
	cur = conn.cursor()
	cursor = conn.execute("SELECT unique_book_id FROM issue_return where status='issued' and student_id=?  ", [student_id])
	ids = cursor.fetchall()
	print("ok")
	for i in ids:
		print(i[0], book_id)
		if str(i[0])==str(book_id):
			return 1
	return 0
	conn.close()

def get_return_date(book_id, student_id):
	conn = sqlite3.connect("libbooks.db")
	cur = conn.cursor()
	cursor = conn.execute("SELECT actual_return_date FROM issue_return where student_id=? and unique_book_id=?  ", [student_id,book_id])
	ids = cursor.fetchall()
	print("enr", ids)
	return ids[0][0]
	conn.close()
