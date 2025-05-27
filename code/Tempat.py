from tkinter import *
import time
import Kursi
from PIL import Image, ImageTk
from customtkinter import *


class Tempat:
    data = []
    d_time = ['08:00', '11:00', '14:00', '17:00', '20:00', '23:00']
    i_time = ['8', '11', '14', '17', '20', '24']
    def __init__(self,window,  Film, main, home):
        self.window = window
        self.main = main
        self.home = home
        self.film = Film
        self.FRAME = Frame(self.window, bg='#f5f0e1')
        self.FRAME.pack(ipadx=550, ipady=355)
        self.label = Label(self.FRAME, bg='#1e3d59', text='BIOSKOP', font=("Verdana", 50, 'bold'), fg='#f5f0e1')
        self.label.place(x=0, y=0, width=1100, height=100)
        self.line = Label(self.FRAME, bg='#ff6e40')
        self.line.place(x=0, y=95, width=1100)
        self.now = time.localtime(time.time())

        # K1
        self.fr1 = CTkFrame(self.FRAME, fg_color='#EBE3D5', width=510, height=365, corner_radius=30)
        self.fr1.place(x=20, y=150)
        self.lblh2 = Label(self.fr1, text='Rp. '+format(35000,',d').replace(',','.'), font='Times 15', bg='#EBE3D5')
        self.lblh2.place(x=400, y=325)
        self.lbla1 = Label(self.fr1, text='K1', font=("Times 50 bold"), fg='black', bg='#EBE3D5')
        self.lbla1.place(x=20, y=20)
        self.lbla2 = Label(self.fr1, text='PLAZANESA\nKetintang', font=("Times 20 bold"), fg='black', bg='#EBE3D5', justify='left')
        self.lbla2.place(x=110, y=25)
        self.lbla3 = Label(self.fr1, text='Universitas Negeri Surabaya', font=("Times 20"), fg='black', bg='#EBE3D5', justify='left')
        self.lbla3.place(x=20, y=100)
        self.lbla4 = Label(self.fr1, text='Jl. Ketintang, Ketintang, Kec. Gayungan, \nSurabaya, Jawa Timur', font=("Times 18"), fg='black', bg='#EBE3D5', justify='left')
        self.lbla4.place(x=20, y=135)
        self.fr1a = Frame(self.fr1, bg='#EBE3D5')
        self.fr1a.place(x=(510/2)-200, y=220, width=400, height=100)
        self.btt1a = CTkButton(self.fr1a,fg_color=self.wkt_bg(0), text=Tempat.d_time[0], font=('Felix Titling', 20), command=lambda: self.btt_f('K1', '08:00'), state=self.waktu(0), width=90, height=40, corner_radius=15)
        self.btt1a.grid(row=0, column=0, padx=25, pady=5)
        self.btt1b = CTkButton(self.fr1a,fg_color=self.wkt_bg(1), text=Tempat.d_time[1], font=('Felix Titling', 20), command=lambda: self.btt_f('K1', '11:00'), state=self.waktu(1), width=90, height=40, corner_radius=15)
        self.btt1b.grid(row=0, column=1, padx=25, pady=5)
        self.btt1d = CTkButton(self.fr1a,fg_color=self.wkt_bg(2), text=Tempat.d_time[2], font=('Felix Titling', 20), command=lambda: self.btt_f('K1', '14:00'), state=self.waktu(2), width=90, height=40, corner_radius=15)
        self.btt1d.grid(row=0, column=2, padx=25, pady=5)
        self.btt1e = CTkButton(self.fr1a,fg_color=self.wkt_bg(3), text=Tempat.d_time[3], font=('Felix Titling', 20), command=lambda: self.btt_f('K1', '17:00'), state=self.waktu(3), width=90, height=40, corner_radius=15)
        self.btt1e.grid(row=1, column=0, padx=25, pady=5)
        self.btt1f = CTkButton(self.fr1a,fg_color=self.wkt_bg(4), text=Tempat.d_time[4], font=('Felix Titling', 20), command=lambda: self.btt_f('K1', '20:00'), state=self.waktu(4), width=90, height=40, corner_radius=15)
        self.btt1f.grid(row=1, column=1, padx=25, pady=5)
        self.btt1g = CTkButton(self.fr1a,fg_color=self.wkt_bg(5), text=Tempat.d_time[5], font=('Felix Titling', 20), command=lambda: self.btt_f('K1', '23:00'), state=self.waktu(5), width=90, height=40, corner_radius=15)
        self.btt1g.grid(row=1, column=2, padx=25, pady=5)

        # K2
        self.fr2 = CTkFrame(self.FRAME, fg_color='#EBE3D5', width=510, height=365, corner_radius=30)
        self.fr2.place(x=570, y=150)
        self.lblh2 = Label(self.fr2, text='Rp. '+format(20000,',d').replace(',','.'), font='Times 15', bg='#EBE3D5')
        self.lblh2.place(x=400, y=325)
        self.lblb1 = Label(self.fr2, text='K2', font=("Times 50 bold"), fg='black', bg='#EBE3D5')
        self.lblb1.place(x=20, y=20)
        self.lblb2 = Label(self.fr2, text='PLAZANESA\nLidah Wetan', font=("Times 20 bold"), fg='black', bg='#EBE3D5')
        self.lblb2.place(x=110, y=25)
        self.lblb3 = Label(self.fr2, text='Universitas Negeri Surabaya', font=("Times 20"), fg='black', bg='#EBE3D5', justify='left')
        self.lblb3.place(x=20, y=100)
        self.lblb4 = Label(self.fr2, text='Jl. Lidah Wetan, Lidah Wetan, Kec. Lakarsantri,\nSurabaya, Jawa Timur', font=("Times 18"), fg='black', bg='#EBE3D5', justify='left')
        self.lblb4.place(x=20, y=135)
        self.fr2a = Frame(self.fr2, bg='#EBE3D5')
        self.fr2a.place(x=(510/2)-200, y=220, width=400, height=100)
        self.btt2a = CTkButton(self.fr2a,fg_color=self.wkt_bg(0), text=Tempat.d_time[0], font=('Felix Titling', 20), command=lambda: self.btt_f('K2', '08:00'), state=self.waktu(0), width=90, height=40, corner_radius=15)
        self.btt2a.grid(row=0, column=0, padx=25, pady=5)
        self.btt2b = CTkButton(self.fr2a,fg_color=self.wkt_bg(1), text=Tempat.d_time[1], font=('Felix Titling', 20), command=lambda: self.btt_f('K2', '11:00'), state=self.waktu(1), width=90, height=40, corner_radius=15)
        self.btt2b.grid(row=0, column=1, padx=25, pady=5)
        self.btt2d = CTkButton(self.fr2a,fg_color=self.wkt_bg(2), text=Tempat.d_time[2], font=('Felix Titling', 20), command=lambda: self.btt_f('K2', '14:00'), state=self.waktu(2), width=90, height=40, corner_radius=15)
        self.btt2d.grid(row=0, column=2, padx=25, pady=5)
        self.btt2e = CTkButton(self.fr2a,fg_color=self.wkt_bg(3), text=Tempat.d_time[3], font=('Felix Titling', 20), command=lambda: self.btt_f('K2', '17:00'), state=self.waktu(3), width=90, height=40, corner_radius=15)
        self.btt2e.grid(row=1, column=0, padx=25, pady=5)
        self.btt2f = CTkButton(self.fr2a,fg_color=self.wkt_bg(4), text=Tempat.d_time[4], font=('Felix Titling', 20), command=lambda: self.btt_f('K2', '20:00'), state=self.waktu(4), width=90, height=40, corner_radius=15)
        self.btt2f.grid(row=1, column=1, padx=25, pady=5)
        self.btt2g = CTkButton(self.fr2a,fg_color=self.wkt_bg(5), text=Tempat.d_time[5], font=('Felix Titling', 20), command=lambda: self.btt_f('K2', '23:00'), state=self.waktu(5), width=90, height=40, corner_radius=15)
        self.btt2g.grid(row=1, column=2, padx=25, pady=5)

        global img_bck
        img_bck = ImageTk.PhotoImage(Image.open('Stok_Image/back_icon.png').resize(size=(60, 60)))
        self.btt_back = Button(self.FRAME, image=img_bck, font=('Verdana', 12, 'bold'), bg='#f5f0e1', border=0, relief=FLAT, command=self.back)
        self.btt_back.place(x=20, y=632)

    def back(self):
        self.window.destroy()

    def waktu(self, i):
        if self.now[3] >= int(Tempat.i_time[i]):
            return 'disabled'
        elif self.now[3] == int(Tempat.i_time[i]):
            if self.now[4] > 0:
                return 'disabled'
            else:
                return 'normal'
        else:
            return 'normal'

    def wkt_bg(self, i):
        if self.now[3] >= int(Tempat.i_time[i]):
            return '#706233'
        elif self.now[3] == int(Tempat.i_time[i]):
            if self.now[4] > 0:
                return '#706233'
            else:
                return '#f0810f'
        else:
            return '#f0810f'

    def btt_f(self,ruangan, jam):
        Tempat.data.clear()
        Tempat.data.append(ruangan)
        Tempat.data.append(jam)
        if ruangan == 'K1':
            self.harga = 35000
        else:
            self.harga = 20000
        Tempat.data.append(self.harga)
        ukw = self.window.winfo_screenwidth()
        ukh = self.window.winfo_screenheight()
        self.fr_KURSI = Frame(self.window, bg='black')
        self.fr_KURSI.place(x=0, y=0, width=ukw, height=ukh)
        Kursi.Kursi(self.fr_KURSI, film=self.film, data=Tempat.data, main=self.main, home=self.home)