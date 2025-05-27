from tkinter import *
from PIL import Image, ImageTk
import time
from customtkinter import *


class Cetak:
    tiket = []
    def __init__(self,window, data, makanan, method, main, home):
        self.main = main
        self.window = window
        self.HOME = home
        self.now = time.localtime(time.time())
        self.date = f'{self.now[0]}/{self.now[1]}/{self.now[2]}'
        self.film = data
        self.kursi = self.film[3].split(',')
        self.h_tiket = len(self.kursi)*self.film[-1]
        self.tambahan = makanan
        self.p_method = method
        self.FRAME = Frame(self.window,bg='#f5f0e1')
        self.FRAME.pack(ipadx=550, ipady=355)
        self.line = Label(self.FRAME, bg='#ff6e40')
        self.line.place(x=0, y=95, width=1100)
        self.label = Label(self.FRAME, bg='#1e3d59', text='Get TICKETS', font=('Perpetua Titling MT', 50, 'bold'), fg='#f5f0e1')
        self.label.place(x=0, y=0, width=1100, height=100)

        
        # Pencetakan Tiket
        self.fr_sc = CTkScrollableFrame(self.FRAME, fg_color='#f5f0e1', orientation='vertical', width=540, height=580)
        self.fr_sc.place(x=0, y=120)
        self.fr_tiket = Frame(self.fr_sc)
        self.fr_tiket.pack(ipadx=270, ipady=(90*len(self.kursi)))
        global img
        img = ImageTk.PhotoImage(Image.open('Stok_Image/Tiket.png').resize(size=(500, 160)))
        Cetak.tiket.append(img)
        a = 20
        for i in self.kursi:
            self.dtiket(a, self.film[0], self.film[1], i, self.film[2])
            a += 175


        # Pencetakan Struk
        self.fr_struk = Frame(self.FRAME, bg='black')
        self.fr_struk.place(x=550+((550/2)-175), y=140, width=350, height=550)
        self.fr_struk_bg = Frame(self.fr_struk, bg='white')
        self.fr_struk_bg.pack(expand=True, ipadx=170, ipady=270)
        self.jdl_str = Label(self.fr_struk_bg, text="ALAMBOCA CINEMA", font=('Verdana', 18, 'bold'), bg='white').place(x=0, y=10, width=340)
        self.line1_str = Label(self.fr_struk_bg, bg='black').place(x=5, y=50, width=330, height=5)
        self.lbl1_str = Label(self.fr_struk_bg, text='Struk Pembelian', font=('Verdana', 13), bg='white').place(x=0, y=60, width=340)
        self.line2_str = Label(self.fr_struk_bg, bg='black').place(x=5, y=88, width=330, height=3)
        self.lbl2_str = Label(self.fr_struk_bg, text=f'{len(self.kursi)} Tiket Bioskop {self.film[1]}', font=('Verdana', 10), justify=LEFT, bg='white').place(x=0, y=105)
        self.lbl3_str = Label(self.fr_struk_bg, text='Rp. '+(format(self.h_tiket, ',d').replace(',','.')),bg='white' , font=('Verdana', 10), justify=RIGHT)
        self.lbl3_str.place(x=338-(len(self.lbl3_str['text'])*8), y=105, width=len(self.lbl3_str['text'])*8)
        self.h_tamb = 0
        self.y = 130
        if self.tambahan == '-' or self.tambahan == []:
            pass
        else :
            for d_tamb in self.tambahan:
                d = d_tamb.split(':')
                self.dstruk(y=self.y, nama=d[0], harga=d[1])
                self.y += 25
                self.h_tamb += int(d[1])
        self.line3_str = Label(self.fr_struk_bg, bg='black').place(x=5, y=self.y, width=330, height=3)
        self.lbl4_str = Label(self.fr_struk_bg, text=f'Total', font=('Verdana', 12, 'bold'), justify=LEFT, bg='white').place(x=0, y=self.y+10)
        self.lbl5_str = Label(self.fr_struk_bg, text='Rp. '+(format(self.h_tiket+self.h_tamb, ',d').replace(',','.')), font=('Verdana', 12, 'bold'), justify=RIGHT, bg='white')
        self.lbl5_str.place(x=338-(len(self.lbl5_str['text'])*10), y=self.y+10, width=len(self.lbl5_str['text'])*10)
        self.lbl6_str = Label(self.fr_struk_bg, text='Metode Pembayaran', font=('Verdana', 11), justify=LEFT, bg='white').place(x=0, y=self.y+30)
        self.lbl7_str = Label(self.fr_struk_bg, text=self.p_method, font=('Verdana', 11, 'bold'), justify=RIGHT, bg='white')
        self.lbl7_str.place(x=338-(len(self.lbl7_str['text'])*20), y=self.y+30, width=len(self.lbl5_str['text'])*10)
        self.lbl6_str = Label(self.fr_struk_bg, text='Terima Kasih!', font=('Verdana', 20), bg='white').place(x=0, y=self.y+60, width=340)
        
        self.bttext = CTkButton(self.FRAME, bg_color='#1e3d59', fg_color='red', text='EXIT', font=('Times', 25, 'bold'), command=self.kelaur)
        self.bttext.place(x=940, y=10)
        self.bttext = CTkButton(self.FRAME, bg_color='#1e3d59', fg_color='red', text='HOMEPAGE', font=('Times', 25, 'bold'), command=self.home)
        self.bttext.place(x=920, y=50)

    def dtiket(self, y_pos, judul, ruang, kursi, jam):
        lbl = Label(self.fr_tiket, image=Cetak.tiket[0])
        lbl.place(x=20, y=y_pos)
        lbl_jdl = Label(lbl, text=judul, fg='#f5f0e1', bg='#1e3d59', font='Times 13 bold')
        lbl_jdl.place(x=166, y=17)
        lbl_ruang = Label(lbl, text=ruang, bg='#f5f0e1', fg='#1e3d59', font=('Arial Narrow', 33, 'bold'))
        lbl_ruang.place(x=175, y=44, height=60)
        lbl_kursi = Label(lbl, text='SEAT: '+kursi, bg='#f5f0e1', fg='#1e3d59', font=('Arial Narrow', 11))
        lbl_kursi.place(x=175, y=100)
        lbl_date = Label(lbl, text='DATE: '+self.date, bg='#f5f0e1', fg='#1e3d59', font=('Arial Narrow', 11))
        lbl_date.place(x=175, y=125)
        lbl_Jam = Label(lbl, text=jam, bg='#f5f0e1', fg='#1e3d59', font=('Arial Narrow', 25, 'bold'))
        lbl_Jam.place(x=290, y=115)

        lbl_ruang1 = Label(lbl, text=ruang, bg='#f5f0e1', fg='#1e3d59', font=('Arial Narrow', 12))
        lbl_ruang1.place(x=65, y=90)
        lbl_kursi = Label(lbl, text='SEAT: '+kursi, bg='#f5f0e1', fg='#1e3d59', font=('Arial Narrow', 11))
        lbl_kursi.place(x=50, y=112)
        lbl_date = Label(lbl, text='DATE: '+self.date, bg='#f5f0e1', fg='#1e3d59', font=('Arial Narrow', 9))
        lbl_date.place(x=40, y=135)

    def dstruk(self, y, nama, harga):
        lbl2_str = Label(self.fr_struk_bg, text=f'{nama}', font=('Verdana', 10), justify=LEFT, bg='white')
        lbl2_str.place(x=0, y=y)
        lbl3_str = Label(self.fr_struk_bg, text='Rp. '+(format(int(harga), ',d').replace(',','.')), font=('Verdana', 10), justify=RIGHT, bg='white')
        lbl3_str.place(x=338-(len(self.lbl3_str['text'])*8), y=y, width=len(self.lbl3_str['text'])*8)


    def kelaur(self):
        self.main.destroy()

    def home(self):
        self.HOME.destroy()