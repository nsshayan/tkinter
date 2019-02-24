#!/Users/snaganan/anaconda3/bin/python
import tkinter as tk

root = tk.Tk("CMSP")
label = tk.Label(root,text='This is a label widget')
button = tk.Button(root,text='Submit')
label.pack()
button.pack()
root.mainloop()
