import string
from tkinter import *
import tkinter as tk
from matplotlib import pyplot as plt
from mtp_result.mtp_res import create_plt, plt_inic
from text_conver.load_text import remove_chars_from_text
import sql_db.sql_bd as sdb
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


window = Tk()


def show_word(args: list):
    l = []
    for widget in plot_frame.winfo_children():
        widget.destroy()
    
    ax = plt.figure(figsize=(10,5), facecolor='azure')
    plt.axes().set_facecolor('azure')
    canv = FigureCanvasTkAgg(ax, master = plot_frame)
    for q in args:
        lst = sdb.word_query(q)
        if len(lst) != 0:
            l.append(q)
            create_plt(lst)
    plt_inic(args)
    canv._tkcanvas.pack(fill=tk.BOTH, expand=1)
    
    plot_frame.pack(fill=tk.BOTH, expand=1)


def btn_click(event):
    spec_chars = string.punctuation + '\n\xa0«»\t—…0123456789'
    asd = remove_chars_from_text(TextInput.get(), spec_chars)
    asd = asd.split()
    show_word(asd)


window['bg'] = 'azure'
window.title('text-analysis')
window.wm_attributes('-alpha', 0.95)
window.geometry('800x650')


frame = Frame(window, bg='azure')
frame.place(relwidth=1, relheight=1)

plot_frame = Frame(frame, bg='azure')
plot_frame.place(relwidth=1, relheight=0.7, rely=0.3)

plabel = Label(frame, text='ВВЕДИТЕ СЛОВА ДЛЯ ПОИСКА ', justify='center', font=40, width=100, bg='azure', pady=15)
plabel.pack()


TextInput = Entry(frame, bg='ghostwhite', width=100, justify='center')
TextInput.pack()


def click(*args):
    TextInput.delete(0, 'end')


def foc(event):
    TextInput.focus()


TextInput.bind("<Button-1>", click)
TextInput.bind_all("<Key>", foc)


btn = Button(frame, text='показать график', bg='lightgray', command=btn_click, width=15, height=1, fg='black')
btn.place()
btn.pack(pady=20)

window.bind('<Return>', btn_click)


window.mainloop()