from tkinter import *
from tkinter import ttk
import re
'''
def show_message():
    label["text"] = e1.get()     # получаем введенный текст

def is_valid(newval):
    count=8
    if count!=8
    return re.match("^\d[0-9]$", newval) is not None
    '''
#окно класс Tk
root = Tk() 
root.title("Парсер")
#размер окна
root.geometry("400x450")
e1 = Entry(width=50)
#e1.show()
e1.pack()
btn = ttk.Button(text="начать парсинг" )
label = ttk.Label()
label.pack(anchor=NW, padx=6, pady=6)
btn.pack(expand = 1)
#show_message()
root.mainloop()

