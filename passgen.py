import random
from tkinter import *
from tkinter import messagebox 
root = Tk()
root['bg'] = 'black'
root.title('Password generator')
root.geometry('700x600')
root.resizable(False, False)
text1 = Text(width=67, height=20, font='verdana')
text1.place(relx=0.01, rely=0.37)
scroll = Scrollbar(command=text1.yview)
scroll.pack(side=RIGHT, fill=Y)
scroll.place(in_=text1, relx=1.0, relheight=1.0, bordermode="outside")
text1.config(yscrollcommand=scroll.set)
def callback(event):
  messagebox.showinfo(title='License', message='Автор: Пулатов Камран\nГод: 2021\nЯзык: Python\nВсе права защищены\nAll rights reserved')
def on_enter(event):
  text3['fg'] = 'red'
def on_leave(event):
  text3['fg'] = 'yellow'
def gen():
  inp = inputhole.get()
  a = 'abcdefghijklmnopqrstuvwxyz'
  b = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
  C = '1234567890'
  sym = '*()@#!^][{}+=-_$%&;:?></.'
  abc = a + b + C + sym
  try:
    process = "".join(random.sample(abc, int(inp)))
    text1.insert(1.0, process+'\n')
  except:
    messagebox.showerror(title='Ошибка', message='Возможно вы ввели что-то неправильное')
    
text = Label(text='PASSGEN--', bg='black', fg='green', font=('Bahnschrift', 30))
text.place(relx=0.1, rely=0.02)

text3 = Label(text='Pulatov Kamran(c) 2021', bg='black', fg='yellow', font=('Bahnschrift', 13))
text3.place(relx=0.7, rely=0.02)
text3.bind("<Button-1>", callback)
text3.bind("<Enter>", on_enter)
text3.bind("<Leave>", on_leave)

text2 = Label(text='Введите количесвто символов:', bg='black', fg='magenta', font=('Bahnschrift', 13))
text2.place(relx=0.25, rely=0.1)

inputhole = Entry(bg='yellow', fg='black', font=('Bahnschrift', 15))
inputhole.place(relx=0.25, rely=0.15, relwidth=0.5, relheight=0.05)

button = Button(text='START', bg='magenta', font=('Bahnschrift', 15), fg='black', command=gen)
button.place(relx=0.35, rely=0.23, relwidth=0.3, relheight=0.06)

root.mainloop()
