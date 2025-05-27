from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk
import Keterangan

class Genre:
    pic_list = []
    judul_f = []

    def __init__(self, window, main):
        self.window = window
        self.FRAME = main
        self.fr_genre = Frame(self.window, bg='#ff6e40')
        self.fr_genre.place(x=0, y=0, width=1101, height=45)
        self.fr1 = Frame(self.window,bg='#f5f0e1')
        self.fr1.place(x=0, y=55)

        self.sh = Button(self.fr_genre, text='Super Hero', font=('Verdana', 15, 'bold'), bg='#f5f0e1', fg='#1e3d59', activebackground='#f5f0e1', border=0, relief=FLAT,  command=lambda: self.slide(0, self.sh))
        self.sh.grid(column=0, row=0, padx=10, pady=7)
        self.hr = Button(self.fr_genre, text='Horor', font=('Verdana', 15, 'bold'), bg='#ffc13b', border=0, relief=FLAT, activebackground='#ffc13b',activeforeground='white', command=lambda: self.slide(-1100, self.hr))
        self.hr.grid(column=1, row=0, padx=10, pady=7)
        self.an = Button(self.fr_genre, text='Animasi', font=('Verdana', 15, 'bold'), bg='#ffc13b', border=0, relief=FLAT, activebackground='#ffc13b',activeforeground='white',command=lambda: self.slide(-1100*2, self.an))
        self.an.grid(column=3, row=0, padx=10, pady=7)
        self.ind = Button(self.fr_genre, text='Indonesia', font=('Verdana', 15, 'bold'), bg='#ffc13b', border=0, relief=FLAT, activebackground='#ffc13b',activeforeground='white',command=lambda: self.slide(-1100*3, self.ind))
        self.ind.grid(column=4, row=0, padx=10, pady=7)
        self.ac = Button(self.fr_genre, text='Aksi', font=('Verdana', 15, 'bold'), bg='#ffc13b', border=0, relief=FLAT, activebackground='#ffc13b',activeforeground='white',command=lambda: self.slide(-1100*4, self.ac))
        self.ac.grid(column=5, row=0, padx=10, pady=7) 
        self.d_film = open('Data/Ket_Film.txt', 'r').read().split('\n\n')
        self.x = 0
        self.i = 0

        # Super Hero
        self.fr_can = Frame(self.fr1, bg='#f5f0e1')
        self.c = Canvas(self.fr_can, bg='white')
        self.c.place(x=0, y=0, width=1100, height=580)
        self.sb = ttk.Scrollbar(self.fr_can, orient='vertical', command= self.c.yview)
        self.sb.place(relheight=1, relx=1, rely=0, anchor='ne')
        self.c.configure(yscrollcommand= self.sb.set)
        self.c.bind('<Configure>', lambda e: self.c.configure(scrollregion = self.c.bbox('all')))
        self.frc = Frame(self.c, bg='black')
        self.c.create_window((0,0), window= self.frc, anchor= 'nw')
        self.fr_can.grid(row=0, column=0, ipadx=550, ipady=270)
        self.fr1a = Frame(self.frc, bg='#f5f0e1')
        self.fr1a.pack(ipadx=550, ipady=900)
        self.btt_loop('Super Hero', self.fr1a)

        # Horor
        self.fr_can2 = Frame(self.fr1, bg='#f5f0e1')
        self.c3 = Canvas(self.fr_can2, bg='white')
        self.c3.place(x=0, y=0, width=1100, height=580)
        self.sb3 = ttk.Scrollbar(self.fr_can2, orient='vertical', command= self.c3.yview)
        self.sb3.place(relheight=1, relx=1, rely=0, anchor='ne')
        self.c3.configure(yscrollcommand= self.sb3.set)
        self.c3.bind('<Configure>', lambda e: self.c3.configure(scrollregion = self.c3.bbox('all')))
        self.frc3 = Frame(self.c3, bg='black')
        self.c3.create_window((0,0), window= self.frc3, anchor= 'nw')
        self.fr_can2.grid(row=0, column=2, ipadx=550, ipady=270)
        self.fr1c = Frame(self.frc3, bg='#f5f0e1')
        self.fr1c.pack(ipadx=550, ipady=350)
        self.btt_loop('Horor', self.fr1c)

        # Animasi
        self.fr_can4 = Frame(self.fr1, bg='#f5f0e1')
        self.c1 = Canvas(self.fr_can4, bg='white')
        self.c1.place(x=0, y=0, width=1100, height=580)
        self.sb1 = ttk.Scrollbar(self.fr_can4, orient='vertical', command= self.c1.yview)
        self.sb1.place(relheight=1, relx=1, rely=0, anchor='ne')
        self.c1.configure(yscrollcommand= self.sb1.set)
        self.c1.bind('<Configure>', lambda e: self.c1.configure(scrollregion = self.c1.bbox('all')))
        self.frc1 = Frame(self.c1, bg='black')
        self.c1.create_window((0,0), window= self.frc1, anchor= 'nw')
        self.fr_can4.grid(row=0, column=3, ipadx=550, ipady=270)
        self.fr1e = Frame(self.frc1, bg='#f5f0e1')
        self.fr1e.pack(ipadx=550, ipady=750)
        self.btt_loop('Animasi', self.fr1e)

        # Indonesia
        self.fr_can7 = Frame(self.fr1, bg='#f5f0e1')
        self.c7 = Canvas(self.fr_can7, bg='white')
        self.c7.place(x=0, y=0, width=1030, height=580)
        self.sb7 = ttk.Scrollbar(self.fr_can7, orient='vertical', command= self.c7.yview)
        self.sb7.place(relheight=1, relx=1, rely=0, anchor='ne')
        self.c7.configure(yscrollcommand= self.sb7.set)
        self.c7.bind('<Configure>', lambda e: self.c7.configure(scrollregion = self.c7.bbox('all')))
        self.frc7 = Frame(self.c7, bg='black')
        self.c7.create_window((0,0), window= self.frc7, anchor= 'nw')
        self.fr_can7.grid(row=0, column=4, ipadx=550, ipady=270)
        self.fr1k = Frame(self.frc7, bg='#f5f0e1')
        self.fr1k.pack(ipadx=550, ipady=420)
        self.btt_loop('Indonesia', self.fr1k)

        # Aksi
        self.fr_can9 = Frame(self.fr1, bg='#f5f0e1')
        self.c2 = Canvas(self.fr_can9, bg='white')
        self.c2.place(x=0, y=0, width=1030, height=580)
        self.sb2 = ttk.Scrollbar(self.fr_can9, orient='vertical', command= self.c2.yview)
        self.sb2.place(relheight=1, relx=1, rely=0, anchor='ne')
        self.c2.configure(yscrollcommand= self.sb2.set)
        self.c2.bind('<Configure>', lambda e: self.c2.configure(scrollregion = self.c2.bbox('all')))
        self.frc2 = Frame(self.c2, bg='black')
        self.c2.create_window((0,0), window= self.frc2, anchor= 'nw')
        self.fr_can9.grid(row=0, column=8, ipadx=540, ipady=270)
        self.fr1j = Frame(self.frc2, bg='#f5f0e1')
        self.fr1j.pack(ipadx=540, ipady=1300)
        self.btt_loop('Aksi', self.fr1j)

    def slide(self, stop, btt):
        self.fr1.place_configure(x=stop)
        self.ac.configure(bg='#ffc13b', fg='black', activebackground='#ffc13b')
        self.ind.configure(bg='#ffc13b', fg='black', activebackground='#ffc13b')
        self.an.configure(bg='#ffc13b', fg='black', activebackground='#ffc13b')
        self.hr.configure(bg='#ffc13b', fg='black', activebackground='#ffc13b')
        self.sh.configure(bg='#ffc13b', fg='black', activebackground='#ffc13b')
        btt.configure(bg='#f5f0e1', fg='#1e3d59', activebackground='#f5f0e1')

    def btt_loop(self, gnr, frame):
        Genre.judul_f.clear()

        data = open('Data/film.txt', 'r')
        d_film = data.read().split('\n')
        x = 40
        y = 10
        def img_pro(file):
            img_open = Image.open(file).resize((150, 225))
            global gambar
            gambar = ImageTk.PhotoImage(img_open)
            gambar = gambar
            return gambar
        
        for dafi in self.d_film:
            df1 = dafi.split('\n')
            if gnr in df1[-1]:
                for f in d_film:
                    d = f.split(',')
                    if d[1] == df1[0]:
                        g = img_pro(d[0])
                        Genre.pic_list.append(g)
                        Genre.judul_f.append(d[1])
        for jdl in Genre.judul_f:
            if x > (1030-100):
                x = 40
                y += 295
            self.btt_film(frame=frame, gambar=Genre.pic_list[self.i], x_pos=x, y_pos=y, Judul=jdl)
            x+=170
            self.i += 1

    def btt_film(self,frame, gambar, x_pos, y_pos, Judul):
        def enter(e):
            global l_judul
            l_judul = Label(frame, text= Judul, bg='#f5f0e1', font=('Verdana', 10, 'bold'))
            l_judul.place(x=x_pos, y=y_pos+235)

        def leave(e):
            l_judul.destroy()

        def fb():
            Film = Judul
            ukw = self.window.winfo_screenwidth()
            ukh = self.window.winfo_screenheight()
            self.frm = Frame(self.FRAME, bg='black')
            self.frm.place(x=0, y=0, width=ukw, height=ukh)
            Keterangan.Keterangan(self.frm, Film, self.FRAME)

        btt = Button(frame, image=gambar, border=0, command= fb)
        btt.place(x=x_pos, y=y_pos)
        btt.bind('<Enter>', enter)
        btt.bind('<Leave>', leave)