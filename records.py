import os
from subprocess import call
import sys
try:
    from Tkinter import *
except ImportError:
    from tkinter import *

try:
    import ttk
    py3 = False
except ImportError:
    import tkinter.ttk as ttk
    py3 = True
def click_search_student_records():
    call(["python3", "search_student_records.py"])
def click_book():
    call(["python3", "monthlyRecords.py"])
def click_search_faculty_records():
    call(["python3", "search_faculty_records.py"])
def click_category():
    call(["python3", "category.py"])
def click_faculty():
    call(["python3", "faculty.py"])
def click_author():
    call(["python3", "author.py"])
def click_publication():
    call(["python3", "publication.py"])
def click_issue_return():
    call(["python3", "issue_return.py"])
def click_list_of_books():
    call(["python3", "list_of_books.py"])


class LIBRARY_MANAGEMENT:
    def __init__(self):
        root = Tk()
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#000000'
        #_bgcolor = '#96cb7f'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#ffffff' # X11 color: 'white'
        _ana1color = '#ffffff' # X11 color: 'white'
        _ana2color = '#ffffff' # X11 color: 'white'
        font14 = "-family {Segoe UI} -size 16 -weight bold -slant "  \
            "roman -underline 0 -overstrike 0"
        font16 = "-family {Swis721 BlkCn BT} -size 40 -weight bold "  \
            "-slant roman -underline 0 -overstrike 0"
        font9 = "-family {Segoe UI} -size 9 -weight normal -slant "  \
            "roman -underline 0 -overstrike 0"

        root.geometry("1350x850+540+110")
        root.title("LIBRARY_MANAGEMENT_SYSTEM")
        root.configure(background="#FFB6C1")
        root.configure(highlightbackground="#87cefa")
        root.configure(highlightcolor="black")

        '''root.geometry("1000x749+540+110")
        root.title("LIBRARY_MANAGEMENT_SYSTEM")
        root.configure(background="#87cefa")
        root.configure(highlightbackground="#FFB6C1")
        root.configure(highlightcolor="black")'''

        self.menubar = Menu(root,font=font9,bg=_bgcolor,fg=_fgcolor)
        root.configure(menu = self.menubar)
        
#96cb7f parrot   #FFB6C1 lightpink
#000000 darkred  #000000 black
#96cb7f         #8B0000 dark red
#87cefa light yello #87cefa sky
#87cefa light sky 
#FF0000 red

        self.Frame1 = Frame(root)
        self.Frame1.place(relx=0.00, rely=0.00, relheight=1.01, relwidth=1.01)
        self.Frame1.configure(relief=GROOVE)
        self.Frame1.configure(borderwidth="2")
        self.Frame1.configure(relief=GROOVE)
        self.Frame1.configure(background="#FFB6C1")
        self.Frame1.configure(highlightbackground="#FFB6C1")
        self.Frame1.configure(highlightcolor="black")
        self.Frame1.configure(width=925)


        self.Button1 = Button(self.Frame1)
        self.Button1.place(relx=0.05, rely=0.06, height=90, width=500)
        self.Button1.configure(activebackground="#87cefa")
        self.Button1.configure(activeforeground="#FF0000")
        self.Button1.configure(background="#87cefa")
        self.Button1.configure(disabledforeground="#bfbfbf")
        self.Button1.configure(font=font14)
        self.Button1.configure(foreground="#8B0000")
        self.Button1.configure(highlightbackground="#FF0000")
        self.Button1.configure(highlightcolor="#FF0000")
        self.Button1.configure(pady="0")
        self.Button1.configure(text='''1. Search Student Records''')
        self.Button1.configure(width=500)
        self.Button1.configure(command=click_search_student_records)

        self.Button2 = Button(self.Frame1)
        self.Button2.place(relx=0.53, rely=0.06, height=93, width=500)
        self.Button2.configure(activebackground="#87cefa")
        self.Button2.configure(activeforeground="#FF0000")
        self.Button2.configure(background="#87cefa")
        self.Button2.configure(disabledforeground="#bfbfbf")
        self.Button2.configure(font=font14)
        self.Button2.configure(foreground="#8B0000")
        self.Button2.configure(highlightbackground="#FF0000")
        self.Button2.configure(highlightcolor="#FF0000")
        self.Button2.configure(pady="0")
        self.Button2.configure(text='''2. Search Faculty Records ''')
        self.Button2.configure(width=500)
        self.Button2.configure(command=click_search_faculty_records)

        self.Button3 = Button(self.Frame1)
        self.Button3.place(relx=0.05, rely=0.28, height=93, width=500)
        self.Button3.configure(activebackground="#87cefa")
        self.Button3.configure(activeforeground="#FF0000")
        self.Button3.configure(background="#87cefa")
        self.Button3.configure(disabledforeground="#bfbfbf")
        self.Button3.configure(font=font14)
        self.Button3.configure(foreground="#8B0000")
        self.Button3.configure(highlightbackground="#FF0000")
        self.Button3.configure(highlightcolor="#FF0000")
        self.Button3.configure(pady="0")
        self.Button3.configure(text='''3. Monthly Records''')
        self.Button3.configure(width=500)
        self.Button3.configure(command=click_book)

        self.Button4 = Button(self.Frame1)
        self.Button4.place(relx=0.53, rely=0.28, height=93, width=500)
        self.Button4.configure(activebackground="#87cefa")
        self.Button4.configure(activeforeground="#FF0000")
        self.Button4.configure(background="#87cefa")
        self.Button4.configure(disabledforeground="#bfbfbf")
        self.Button4.configure(font=font14)
        self.Button4.configure(foreground="#8B0000")
        self.Button4.configure(highlightbackground="#FF0000")
        self.Button4.configure(highlightcolor="#FF0000")
        self.Button4.configure(pady="0")
        self.Button4.configure(text='''4. List of Books ''')
        self.Button4.configure(width=500)
        self.Button4.configure(command=click_list_of_books)

        self.Button8 = Button(self.Frame1)
        self.Button8.place(relx=0.37, rely=0.80, height=50, width=300)
        self.Button8.configure(activebackground="#87cefa")
        self.Button8.configure(activeforeground="#FF0000")
        self.Button8.configure(background="#87cefa")
        self.Button8.configure(disabledforeground="#bfbfbf")
        self.Button8.configure(font=font14)
        self.Button8.configure(foreground="#8B0000")
        self.Button8.configure(highlightbackground="#FF0000")
        self.Button8.configure(highlightcolor="#FF0000")
        self.Button8.configure(pady="0")
        self.Button8.configure(text='''EXIT''')
        self.Button8.configure(width=500)
        self.Button8.configure(command=quit)

        root.mainloop()




if __name__ == '__main__':
    GUUEST=LIBRARY_MANAGEMENT()

