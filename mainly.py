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
def click_checkinn():
    call(["python3", "librarian.py"])
def click_list():
    call(["python3", "records.py"])
#carpet lite

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
        font14 = "-family {Segoe UI} -size 18 -weight bold -slant "  \
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
#96cb7f 		#8B0000 dark red
#87cefa light yello #87cefa sky
#87cefa light sky 
#FF0000 red

        self.Frame1 = Frame(root)
        self.Frame1.place(relx=0.00, rely=0.00, relheight=1.00, relwidth=1.01)
        self.Frame1.configure(relief=GROOVE)
        self.Frame1.configure(borderwidth="2")
        self.Frame1.configure(relief=GROOVE)
        self.Frame1.configure(background="#FFB6C1")
        self.Frame1.configure(highlightbackground="#FFB6C1")
        self.Frame1.configure(highlightcolor="black")
        self.Frame1.configure(width=925)

        self.Message1 = Message(self.Frame1)
        self.Message1.place(relx=0.07, rely=0.05, relheight=0.15, relwidth=0.86)
        self.Message1.configure(background="#FFB6C1")
        self.Message1.configure(font=font16)
        self.Message1.configure(foreground="#000000")
        self.Message1.configure(highlightbackground="#96cb7f")
        self.Message1.configure(highlightcolor="#8B0000")
        self.Message1.configure(text='''WELCOME''')
        self.Message1.configure(width=791)

        self.Button1 = Button(self.Frame1)
        self.Button1.place(relx=0.26, rely=0.25, height=103, width=566)
        self.Button1.configure(activebackground="#87cefa")
        self.Button1.configure(activeforeground="#FF0000")
        self.Button1.configure(background="#87cefa")
        self.Button1.configure(disabledforeground="#bfbfbf")
        self.Button1.configure(font=font14)
        self.Button1.configure(foreground="#8B0000")
        self.Button1.configure(highlightbackground="#FF0000")
        self.Button1.configure(highlightcolor="#FF0000")
        self.Button1.configure(pady="0")
        self.Button1.configure(text='''1. Librarian''')
        self.Button1.configure(width=566)
        self.Button1.configure(command=click_checkinn)

        self.Button2 = Button(self.Frame1)
        self.Button2.place(relx=0.26, rely=0.47, height=93, width=566)
        self.Button2.configure(activebackground="#87cefa")
        self.Button2.configure(activeforeground="#FF0000")
        self.Button2.configure(background="#87cefa")
        self.Button2.configure(disabledforeground="#bfbfbf")
        self.Button2.configure(font=font14)
        self.Button2.configure(foreground="#8B0000")
        self.Button2.configure(highlightbackground="#FF0000")
        self.Button2.configure(highlightcolor="#FF0000")
        self.Button2.configure(pady="0")
        self.Button2.configure(text='''2. Records''')
        self.Button2.configure(width=566)
        self.Button2.configure(command=click_list)

        self.Button3 = Button(self.Frame1)
        self.Button3.place(relx=0.26, rely=0.80, height=70, width=566)
        self.Button3.configure(activebackground="#87cefa")
        self.Button3.configure(activeforeground="#FF0000")
        self.Button3.configure(background="#87cefa")
        self.Button3.configure(disabledforeground="#bfbfbf")
        self.Button3.configure(font=font14)
        self.Button3.configure(foreground="#8B0000")
        self.Button3.configure(highlightbackground="#FF0000")
        self.Button3.configure(highlightcolor="#FF0000")
        self.Button3.configure(pady="0")
        self.Button3.configure(text=''' EXIT''')
        self.Button3.configure(width=566)
        self.Button3.configure(command=quit)
        root.mainloop()


if __name__ == '__main__':
    GUUEST=LIBRARY_MANAGEMENT()


