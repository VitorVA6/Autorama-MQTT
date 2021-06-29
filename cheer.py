from tkinter import *
from tkinter import ttk
import time
import _thread as thread
from sub import *

def cont():
    thread.start_new_thread(t, ())
    
    

s = Tk()
s.title('Torcedor')
s.geometry('680x570')

screen = Frame(s)

label = Label(screen, text='abc', font = 'verdana 11 bold')
label.pack()
button = Button(screen, text='Contar', width = 12, font = 'verdana 10 bold', command=cont)
button.pack()
screen.pack()

s.mainloop()

