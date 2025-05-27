from tkinter import *
from customtkinter import *
from PIL import Image, ImageTk
import textwrap
import Tempat

class Keterangan:
    def __init__(self,window, film, main):
        self.main = main
        self.window = window
        self.film = film
        self.FRAME = Frame(self.window,bg='#f5f0e1')
        self.FRAME.pack(ipadx=550, ipady=355)
        self.line = Label(self.FRAME, bg='#ff6e40')
        self.line.place(x=0, y=95, width=1100)
        self.label = Label(self.FRAME, bg='#1e3d59', text='DESCRIPTION FILM', font=('Perpetua Titling MT', 50, 'bold'), fg='#f5f0e1')
        self.label.place(x=0, y=0, width=1100, height=100)
        self.fr1 = CTkFrame(self.FRAME, fg_color='#1e3d59', corner_radius=30, width=900, height=520)
        self.fr1.place(x=100, y=150)

        img = self.gambar_film()
        self.lbl = Label(self.fr1, bg='#f2f0e4', image=img)
        self.lbl.place(x=30, y=30, width=270, height=380)
        self.btt = CTkButton(self.fr1, text='BUY TICKET', bg_color='transparent', fg_color='#ffc13b', font=('Verdana', 25, 'bold'), command= self.buy, width=270, height=50, text_color='black')
        self.btt.place(x=30, y=415)

        global img_bck
        img_bck = ImageTk.PhotoImage(Image.open('Stok_Image/back_icon.png').resize(size=(60, 60)))
        self.btt_back = Button(self.FRAME, image=img_bck, font=('Verdana', 12, 'bold'), bg='#f5f0e1', border=0, relief=FLAT, command=self.back)
        self.btt_back.place(x=20, y=632)
        
        self.fr2 = Frame(self.fr1, bg='#1e3d59')
        self.fr2.place(x=320, y=30, width=900-(320+30), height=450)
        self.lbl_judul = Label(self.fr2, text=self.film, font=('Century', 18), bg='#1e3d59', fg='#f5f0e1')
        self.lbl_judul.grid(row=0, column=0, columnspan=25, padx=10, pady=10, sticky='w')
        self.lbl_dir = Label(self.fr2, text='Direktur', font=('Century', 15), bg='#1e3d59', fg='#f5f0e1')
        self.lbl_dir.grid(row=1, column=0, padx=10, pady=5, sticky='w', ipadx=0)
        self.td(1)
        self.lbl_cast = Label(self.fr2, text='Pemeran', font=('Century', 15), bg='#1e3d59', fg='#f5f0e1')
        self.lbl_cast.grid(row=2, column=0, padx=10, pady=5, sticky='w', ipadx=0)
        self.td(2)
        self.lbl_dur = Label(self.fr2, text='Durasi', font=('Century', 15), bg='#1e3d59', fg='#f5f0e1')
        self.lbl_dur.grid(row=3, column=0, padx=10, pady=5, sticky='w', ipadx=0)
        self.td(3)
        self.lbl_rilis = Label(self.fr2, text='Tanggal Rilis', font=('Century', 15), bg='#1e3d59', fg='#f5f0e1')
        self.lbl_rilis.grid(row=4, column=0, padx=10, pady=5, sticky='w', ipadx=0)
        self.td(4)
        self.lbl_sinop = Label(self.fr2, text='Sinopsis', font=('Century', 15), bg='#1e3d59', fg='#f5f0e1')
        self.lbl_sinop.grid(row=5, column=0, padx=10, pady=5, sticky='w', ipadx=0)
        self.Keterangan_Film()
        self.photo = Image.open('Stok_Image/tembok.jpg').resize(size=(1100, 600))
        self.img = ImageTk.PhotoImage(self.photo)

    def back(self):
        self.window.destroy()

    def td(self, i):
        Label(self.fr2, text=':', font=('Century', 15), bg='#1e3d59', fg='#f5f0e1').grid(row= i, column= 1, sticky='w')

    def Keterangan_Film(self):
        k_film = open('Data/Ket_Film.txt', 'r')
        film = k_film.read().split('\n\n')
        for kf in film:
            asd = kf.split('\n')
            if asd[0] == self.film:
                self.director = Label(self.fr2, text=asd[1], font=('Century', 13), bg='#1e3d59', fg='#f5f0e1').grid(row= 1, column= 2, sticky='w')

                self.teks1 = asd[2]
                self.wrape1 = textwrap.wrap(self.teks1, width=50)
                self.tx1 = '\n'.join(self.wrape1)
                self.cast = Label(self.fr2, text=self.tx1, font=('Century', 13), justify=LEFT, bg='#1e3d59', fg='#f5f0e1').grid(row= 2, column= 2, sticky='w')
                
                self.duration = Label(self.fr2, text=asd[3], font=('Century', 13), bg='#1e3d59', fg='#f5f0e1').grid(row= 3, column= 2, sticky='w')

                self.duration = Label(self.fr2, text=asd[4], font=('Century', 13), bg='#1e3d59', fg='#f5f0e1').grid(row= 4, column= 2, sticky='w')

                self.teks = asd[5]
                self.wrape = textwrap.wrap(self.teks, width=70)
                self.tx = '\n'.join(self.wrape)
                self.lbl_rilis = Label(self.fr2, text=self.tx, font=('Century', 12), justify=LEFT, bg='#1e3d59', fg='#f5f0e1')
                self.lbl_rilis.grid(row=6, column=0, padx=10, sticky='w', columnspan=25)
                break
            else: continue

    def gambar_film(self):
        film_file = open('Data/film.txt', 'r').read().split('\n')
        for fg in film_file:
            g = fg.split(',')
            if g[1] == self.film:
                self.lg = g[0]
                break

        img_open = Image.open(self.lg).resize((270, 380))
        global gambar
        gambar = ImageTk.PhotoImage(img_open)
        gambar = gambar
        return gambar

    def buy(self):
        Film = self.film
        ukw = self.window.winfo_screenwidth()
        ukh = self.window.winfo_screenheight()
        self.fr_TEMPAT = Frame(self.window, bg='black')
        self.fr_TEMPAT.place(x=0, y=0, width=ukw, height=ukh)
        Tempat.Tempat(self.fr_TEMPAT, Film, self.main, self.window)