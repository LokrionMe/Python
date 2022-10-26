import tkinter as tk

# window1 = tk.Tk()
# greeting = tk.Label(
#     text= 'Hello world',
#     width= 20,
#     height= 5
# )
# greeting.pack()
# name_user = tk.Label(text='Please, enter your name: ')
# name_user.pack()
# entry_name = tk.Entry(
#     width=25
# )
# entry_name.pack()
# name_input = entry_name.get()
# print(name_input)
# button_exit = tk.Button(
#     text='Exit',
#     width=20,
#     height=5

# )
# button_exit.pack()
# window1.mainloop() 
# --------------------------
 
# border_effects = {
#     "flat": tk.FLAT,
#     "sunken": tk.SUNKEN,
#     "raised": tk.RAISED,
#     "groove": tk.GROOVE,
#     "ridge": tk.RIDGE,
# }
 
# window = tk.Tk()
 
# for relief_name, relief in border_effects.items():
#     frame = tk.Frame(master=window, relief=relief, borderwidth=5)
#     frame.pack(side=tk.LEFT)
#     label = tk.Label(master=frame, text=relief_name)
#     label.pack()
 
# window.mainloop()
# --------------------
# window1 = tk.Tk()

# ent_name = tk.Entry(width= 40)
# ent_name.pack()
# ent_name.insert(0,'What is your name?')
# window1.mainloop()
# ----------------------
# window = tk.Tk()
 
# frame1 = tk.Frame(master=window, width=200, height=100, bg="red")
# frame1.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)
 
# frame2 = tk.Frame(master=window, width=100, bg="yellow")
# frame2.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)
 
# frame3 = tk.Frame(master=window, width=50, bg="blue")
# frame3.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)
# window.mainloop()
# ----------------
window = tk.Tk()
 
frame = tk.Frame(master=window, width=150, height=150)
frame.pack()
 
label1 = tk.Label(master=frame, text="I'm at (0, 0)", bg="red")
label1.place(x=0, y=0)
 
label2 = tk.Label(master=frame, text="I'm at (75, 75)", bg="yellow")
label2.place(x=75, y=75)
 
window.mainloop()