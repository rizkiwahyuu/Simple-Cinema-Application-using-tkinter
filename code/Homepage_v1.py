from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk
import Keterangan
from customtkinter import *

class Homepage:
    pic_list = []
    judul = []
    marvel_list = []
    horor_list = []
    def __init__(self, window, main):
        self.window = window
        self.main = main
        self.fr1 = Frame(self.window, bg='#f5f0e1')
        self.scb = CTkScrollableFrame(self.fr1, orientation='vertical', width=1080, height=600)
        self.scb.place(y=0, x=0)
        self.fr1.place(x=0, y=0, width=1100, height=580)
        self.fr1a = Frame(self.scb, bg='#f5f0e1')
        self.fr1a.pack(ipadx=550, ipady=(700))

        self.lbl_ket1 = Label(self.fr1a, text='Film MARVEL yang rilis baru-baru ini!', font=('Times New Roman', 30, 'bold'), bg='#f5f0e1', fg='#1e3d59')
        self.lbl_ket1.place(x=15, y=0)
        self.fr2 = Frame(self.fr1a, bg='#f5f0e1')
        self.fr2.place(x=15, y=50, width= 1050, height=560)
        self.fr2a = Frame(self.fr2, bg='#f5f0e1')
        self.fr2a.place(x=0, y=10)
        self.btt_n = Button(self.fr2, text='>>', command=lambda: self.nextf(0, self.btt_p, self.btt_n, self.fr2a, 7), font=('Times New Roman', 30, 'bold'), relief='flat', border=0, bg='#f5f0e1')
        self.btt_n.place(x=800, y=480)
        self.btt_p = Button(self.fr2, text='<<', command=lambda: self.prevf(0, self.btt_p, self.btt_n, self.fr2a, 7), font=('Times New Roman', 30, 'bold'), relief='flat', border=0, state=DISABLED, bg='#f5f0e1')
        self.btt_p.place(x=180, y=480)
        self.lbl_line1 = Label(self.fr1a, bg='black')
        self.lbl_line1.place(x=10, y=610, height=10, width=1100)

        self.lbl_ket2 = Label(self.fr1a, text='Film yang cocok ditonton sendirian!', font=('Times New Roman', 30, 'bold'), bg='#f5f0e1', fg='#1e3d59')
        self.lbl_ket2.place(x=15, y=620)
        self.fr3 = Frame(self.fr1a, bg='#f5f0e1')
        self.fr3.place(x=15, y=680, width= 1050, height=560)
        self.fr3a = Frame(self.fr3, bg='#f5f0e1')
        self.fr3a.place(x=0, y=10)
        self.btt_n1 = Button(self.fr3, text='>>', command=lambda: self.nextf(0, self.btt_p1, self.btt_n1, self.fr3a, 8), font=('Times New Roman', 30, 'bold'), relief='flat', border=0, bg='#f5f0e1')
        self.btt_n1.place(x=800, y=480)
        self.btt_p1 = Button(self.fr3, text='<<', command=lambda: self.prevf(0, self.btt_p1, self.btt_n1, self.fr3a, 8), font=('Times New Roman', 30, 'bold'), relief='flat', border=0, state=DISABLED, bg='#f5f0e1')
        self.btt_p1.place(x=180, y=480)

        self.i = 0
        self.a = 0
        self.b = 0 
        self.a1 = 0
        self.b1 = 0

        self.data_new = open('Data/Ket_Film.txt', 'r').read().split('\n\n')

        for film in self.data_new:
            film_n = film.split('\n')
            if int(film_n[4][-4:]) >= 2020:
                Homepage.marvel_list.append(film_n[0])
            if 'Horor' in film_n[-1]:
                Homepage.horor_list.append(film_n[0])

        self.btt_loop(self.fr2a, Homepage.marvel_list)
        self.btt_loop(self.fr3a, Homepage.horor_list)

    def btt_loop(self, fr, homdat):
        Homepage.judul.clear()
        data = open('Data/film.txt', 'r')
        d_film = data.read().split('\n')

        def img_pro(file):
            img_open = Image.open(file).resize((300, 450))
            global gambar
            gambar = ImageTk.PhotoImage(img_open)
            gambar = gambar
            return gambar

        for f in d_film:
            d = f.split(',')
            if d[1] in homdat:
                g = img_pro(d[0])
                Homepage.pic_list.append(g)
                Homepage.judul.append(d[1])
        i = 0
        for jdl in Homepage.judul:
            self.btt_film(fr, x_pos=i, Judul=jdl, gambar=Homepage.pic_list[self.i])
            i+=1
            self.i += 1

    def btt_film(self,frame,  gambar, x_pos, Judul):

        def fb():
            Film = Judul
            ukw = self.window.winfo_screenwidth()
            ukh = self.window.winfo_screenheight()
            self.frm = Frame(self.main, bg='black')
            self.frm.place(x=0, y=0, width=ukw, height=ukh)
            Keterangan.Keterangan(self.frm,Film, self.main)

        btt = Button(frame, image=gambar, border=0, command= fb)
        btt.grid(column=x_pos, row=0, padx=25)


    def nextf(self,b, btp, btn, fr, i):
        inf = fr.place_info()
        if b <= -350:
            if int(inf['x']) <= (-350*i):
                btn.configure(state=DISABLED)
            else:
                btn.configure(state=NORMAL)
            if int(inf['x']) <  0:
                btp.configure(state=NORMAL)
            return b
        else: 
            fr.place_configure(x=(int(inf['x']) - 10))
            self.window.after(10, lambda: self.nextf(b=b-10, btp=btp, btn=btn, fr=fr, i=i))

    def prevf(self,b, btp, btn, fr, i):
        inf = fr.place_info()
        if b >= 350:
            if int(inf['x']) >= (0):
                btp.configure(state=DISABLED)
            else:
                btp.configure(state=NORMAL)
            if int(inf['x']) > (-350*i):
                btn.configure(state=NORMAL)
            return b
        else: 
            fr.place_configure(x=(int(inf['x']) + 10))
            self.window.after(10, lambda: self.prevf(b=b+10, btp=btp, btn=btn, fr=fr, i=i))