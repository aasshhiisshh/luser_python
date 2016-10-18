from Tkinter import *
import Tkinter as tk
import ttk
root = Tk()

label = tk.Label(root, text='Label something for GUI').grid()
ttk.Button(root, text="Press it").grid()
entry = tk.Entry(root)
root.mainloop()
label.pack(side=tk.TOP)
entry.pack()
