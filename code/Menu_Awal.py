from tkinter import *
import Homepage_v1
import Genre
from customtkinter import *


class Menu:
    pic_list = []   
    judul = []
    def __init__(self, window):
        self.window = window

        self.FRAME = Frame(bg='#f5f0e1')
        self.FRAME.pack(ipadx=550, ipady=355)
        self.fr_menu = Frame(self.FRAME, bg='#1e3d59')
        self.fr_menu.place(x=0, y=0, width=1100, height=100)
        self.label = Label(self.fr_menu, text="ALAMBOCA CINEMA", font=('Perpetua Titling MT', 40, 'bold'), bg='#1e3d59', fg='#f5f0e1').grid(row=0,column=0, padx=20, ipady=18)
        self.home = CTkButton(self.fr_menu, text='Home', font=('Verdana', 28, 'bold'), bg_color='transparent', fg_color='#ff6e40', hover=False, text_color='#f5f0e1',command=lambda: self.change(0, 'Home'))
        self.home.grid(row=0, column=1, padx=15)
        self.genre = CTkButton(self.fr_menu, text='Genre', font=('Verdana', 28, 'bold'), bg_color='#1e3d59',fg_color='#ff6e40', hover=False,text_color='black', command=lambda: self.change(-1101, 'Genre'))
        self.genre.grid(row=0, column=2, padx=15)
        self.line = Label(self.FRAME, bg='#ff6e40')
        self.line.place(x=0, y=95, width=1100)

        self.big_fr = Frame(self.FRAME, bg='#f5f0e1')
        self.big_fr.place(x=0, y=100)
        self.fr_home = Frame(self.big_fr, bg='#f5f0e1')
        self.fr_home.grid(row=0, column=0, ipadx=550, ipady=355)
        Homepage_v1.Homepage(window=self.fr_home, main=self.window)
        self.fr_genre = Frame(self.big_fr, bg='#f5f0e1')
        self.fr_genre.grid(row=0, column=1, ipadx=550, ipady=355)
        Genre.Genre(window=self.fr_genre, main=self.window)


    def change(self, pos, k):
        self.big_fr.place_configure(x=pos)
        if k == 'Home':
            self.f_home()
        elif k == 'Genre':
            self.f_genre()


    def f_home(self):
        self.home.configure(text_color='white', command=DISABLED)
        self.genre.configure(text_color='black', command= lambda: self.change(-1101, 'Genre'))


    def f_genre(self):
        self.home.configure(text_color='black', command= lambda: self.change(0, 'Home'))
        self.genre.configure(text_color='white', command= DISABLED)