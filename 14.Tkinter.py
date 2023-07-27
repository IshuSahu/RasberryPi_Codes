
# # Window
# from tkinter  import *
# class Window(Frame):
#     def __init__ (self,master =None):
#         Frame.__init__(self, master)
#         self.master = master

# root = Tk()
# app = Window(root)
# root.wm_title("MCA")
# root.mainloop()


# # Exit button
# from tkinter import *

# class Window(Frame):
#     def __init__(self, master=None):
#         Frame.__init__(self, master)
#         self.master = master
#         self.pack(fill=BOTH, expand=1)
#         exitButton = Button(self, text="Exit", command=self.ClickExitButton)  
#         exitButton.place(x=280, y=0)

#     def ClickExitButton(self):
#         exit()

# root = Tk()
# app = Window(root)
# root.wm_title("MCA")
# root.geometry('320x320')  
# root.mainloop()


import tkinter as tk
master = tk.Tk()
tk.Label(master, text="First Name").grid(row=0)
e1 = tk.Entry(master)
e1.grid(row=0,column=1)

tk.Label(master, text="Last Name").grid(row=1)
e2 = tk.Entry(master)
e2.grid(row=1,column=1)

master.mainloop()