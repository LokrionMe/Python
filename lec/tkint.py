import tkinter as tk

# window = tk.Tk()
# window.title('Address Entry Form')

# frm_form = tk.Frame(relief = tk.SUNKEN,borderwidth=3)
# frm_form.pack()

# lst = [
#     'Name:',
#     'Second name:',
#     'Adress1:',
#     'Adress2:',
#     'City:',
#     'Region:',
#     'Index:',
#     'Country:'
# ]

# for i in range(8):
#     lbl_lst = tk.Label(master = frm_form, text=lst[i])
#     entry = tk.Entry(master = frm_form,width=60,bg='white',fg='black')
#     lbl_lst.grid(row=i,column=0,sticky='e')
#     entry.grid(row=i,column=1)

# frm_buttons = tk.Frame()
# frm_buttons.pack(fill = tk.X,ipadx=5,ipady=5)
# btn_submit = tk.Button(master=frm_buttons, text='Submit')
# btn_submit.pack(side=tk.RIGHT,padx=10,ipadx=30)
# btn_clear = tk.Button(master=frm_buttons, text='Clear')
# btn_clear.pack(side=tk.RIGHT,ipadx=30)

# window.mainloop()

# ------------------------
# import random

# def random_points():
#     lbl_points['text'] = str(random.randint(1,6))

# window.title('Dice')
# window.rowconfigure([0,1],minsize=50)
# window.columnconfigure(0,minsize=150)


# lbl_points = tk.Label()
# lbl_points.grid(row=0,column=0,sticky='nsew')

# btn_roll = tk.Button(text='Roll', command=random_points)
# btn_roll.grid(row=1,column=0)
# window.mainloop()

# -------------------------------------------

# def fahrenheit_to_cilsius():
#     fahrenheit = ent_temperature.get()
#     celsius = (5/9)*(float(fahrenheit)-32)
#     lbl_result['text'] = f'{round(celsius, 2)} \N{DEGREE CELSIUS}'

# window = tk.Tk()
# window.title('Converter to fahrenheit')
# window.resizable(width=False, height=False)

# frm_entry = tk.Frame(master=window)
# ent_temperature = tk.Entry(master=frm_entry,width=10)
# lbl_temp = tk.Label(master=frm_entry,text='\N{DEGREE FAHRENHEIT}')

# ent_temperature.grid(row=0,column=0,sticky='e')
# lbl_temp.grid(row=0,column=1,sticky='w')

# btn_convert = tk.Button(master=window,text='\N{RIGHTWARDS BLACK ARROW}',command=fahrenheit_to_cilsius)
# lbl_result = tk.Label(master=window, text = '\N{DEGREE CELSIUS}')

# frm_entry.grid(row=0,column=0,padx=10)
# btn_convert.grid(row=0,column=1,pady=10)
# lbl_result.grid(row=0,column=2,padx=10)

# window.mainloop()

# --------------------------------------
