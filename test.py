#!/usr/bin/python3

from tkinter import *

tk=Tk()
tk.title('MegaChat')
tk.geometry('400x300')
log = Text(tk)
nick = Entry(tk)
msg = Entry(tk)
msg.pack(side='bottom', fill='x', expand='true')
nick.pack(side='bottom', fill='x', expand='true')
log.pack(side='top', fill='both',expand='true')
tk.mainloop()
