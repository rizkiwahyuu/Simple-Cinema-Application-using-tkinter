from tkinter import *
from PIL import Image, ImageTk
import textwrap
import string
from random import choices
import qrcode as qr
import Pencetakan
from customtkinter import *


class Pembayaran:
    icon_list = []
    def __init__(self, window, data, makanan='-', main='', home=''):
        self.main = main
        self.window = window
        self.home = home
        self.data = data
        self.tambahan = makanan
        self.d_kursi = self.data[3].split(',')
        self.harga = len(self.d_kursi)*self.data[4]
        self.total = self.harga
        self.dn_icon = ImageTk.PhotoImage(Image.open('Stok_Image/dana_icon.jpg').resize(size=(45,45)))
        self.qr_icon = ImageTk.PhotoImage(Image.open('Stok_Image/qris.png').resize(size=(60,45)))
        self.bri_icon = ImageTk.PhotoImage(Image.open('Stok_Image/BRI.png').resize(size=(50,45)))
        Pembayaran.icon_list.append(self.dn_icon)
        Pembayaran.icon_list.append(self.qr_icon)
        Pembayaran.icon_list.append(self.bri_icon)

        self.FRAME = Frame(self.window, bg='#f5f0e1')
        self.FRAME.pack(ipadx=550, ipady=355)
        self.label = Label(self.FRAME, bg='#1e3d59', text='PAYMENT', font=('Times New Roman', 50, 'bold'),fg='#f5f0e1')
        self.label.place(x=0, y=0, width=1100, height=100)
        self.line = Label(self.FRAME, bg='#ff6e40')
        self.line.place(x=0, y=95, width=1100)
        self.fr1 = Frame(self.FRAME, bg='#f5f0e1')
        self.fr1.place(x=35, y=150, width=1030, height=600)

        if len(self.data[3]) < 35:
            self.lbl_bg1 = Label(self.fr1, bg='#1e3d59')
            self.lbl_bg1.place(x=275, y=20, width=360, height=310)
            self.fr1a = Frame(self.fr1, bg='#f5f0e1')
            self.fr1a.place(x=280, y=25, width=350, height=300)
        else:
            self.frctk = CTkScrollableFrame(self.fr1, bg_color='#f5f0e1', width=350, height=300,fg_color='#1e3d59')
            self.frctk.place(x=270, y=20)
            self.fr1a = Frame(self.frctk, bg='#f5f0e1')
            self.fr1a.pack()

        self.lbl1 = Label(self.fr1a, text= 'Detail Pembelian Tiket', font=('Times New Roman', 20, 'bold'), bg='#f5f0e1', fg='#1e3d59')
        self.lbl1.grid(row=0, column=0, padx=10, sticky='w', columnspan=5)
        self.lbl2 = Label(self.fr1a, text= 'Jumlah Tiket', font=('Times New Roman', 15, 'bold'), bg='#f5f0e1', fg='#1e3d59')
        self.lbl2.grid(row=1, column=0, padx=10, sticky='w', pady=10)
        self.td(self.fr1a,1)
        self.lbl2 = Label(self.fr1a, text= 'Bioskop', font=('Times New Roman', 15, 'bold'), bg='#f5f0e1', fg='#1e3d59')
        self.lbl2.grid(row=2, column=0, padx=10, sticky='w', pady=10)
        self.td(self.fr1a,2)
        self.lbl3 = Label(self.fr1a, text= 'Kursi', font=('Times New Roman', 15, 'bold'), bg='#f5f0e1', fg='#1e3d59')
        self.lbl3.grid(row=3, column=0, padx=10, sticky='w', pady=10)
        self.td(self.fr1a,3)
        self.lbl4 = Label(self.fr1a, text= 'Jam Tayang', font=('Times New Roman', 15, 'bold'), bg='#f5f0e1', fg='#1e3d59')
        self.lbl4.grid(row=4, column=0, padx=10, sticky='w', pady=10)
        self.td(self.fr1a,4)
        self.lbl5 = Label(self.fr1a, text= 'Harga', font=('Times New Roman', 15, 'bold'), bg='#f5f0e1', fg='#1e3d59')
        self.lbl5.grid(row=5, column=0, padx=10, sticky='w', pady=10)
        self.td(self.fr1a,5)
        if len(self.data[3])<15:
            self.Detail(tiket=str(len(self.d_kursi))+' Tiket',tempat=self.data[1], kursi=self.data[3], harga='Rp. '+format(self.harga, ',d').replace(',','.'), tayang=self.data[2])
        else:
            draft_teks = self.data[3].replace(',',' ')
            tex = textwrap.wrap(draft_teks, width=12)
            teks = '\n'.join(tex)
            self.Detail(tiket=str(len(self.d_kursi))+' Tiket',tempat=self.data[1], kursi=teks, harga='Rp. '+format(self.harga, ',d').replace(',','.'), tayang=self.data[2])

        if len(self.tambahan) < 6:
            self.lbl_bg2 = Label(self.fr1, bg='#1e3d59')
            self.lbl_bg2.place(x=650, y=20, width=360, height=(48*(len(makanan)+1))+10)
            self.fr1b = Frame(self.fr1, bg='#f5f0e1')
            self.fr1b.place(x=655, y=25, width=350, height=48*(len(makanan)+1))
        else:
            self.frctk2 = CTkScrollableFrame(self.fr1, bg_color='#f5f0e1', width=350, height=300,fg_color='#1e3d59')
            self.frctk2.place(x=650, y=20)
            self.fr1b = Frame(self.frctk2, bg='#f5f0e1')
            self.fr1b.pack()
        self.lblm1 = Label(self.fr1b, text= 'Detail Pembelian Tambahan', font=('Times New Roman', 20, 'bold'), bg='#f5f0e1', fg='#1e3d59')
        self.lblm1.grid(row=0, column=0, sticky='w', columnspan=5)
        self.btt_bayar = Button(self.fr1, text='BAYAR SEKARANG',bg='#ffc13b' ,font=('Times New Roman', 20, 'bold'), border=0, relief=FLAT, command=self.bayar)
        self.btt_bayar.place(x=685-175, y=400, width=350)
        self.x = (685-175)
        if self.tambahan == '-':
            self.lbl_bg2.destroy()
            self.fr1b.destroy()
            self.x = 280
            self.btt_bayar.place_configure(x=self.x)
        else:
            i = 1
            for t in self.tambahan:
                i += 1
                jh = t.split(':')
                teks = textwrap.wrap(jh[0], width=18)
                tex = '\n'.join(teks)
                self.lbl_tmbhan(jenis=tex, hg=jh[1], i=i)
                self.total += int(jh[1])
        self.lbl_tot = Label(self.fr1, text='Rp. '+format(self.total, ',d').replace(',','.'),bg='#ff6e40', font=('Times New Roman', 15))
        self.lbl_tot.place(x=self.x, y=370, width=350)
        self.film = self.data[0]
        gambar = self.gambar_film()
        self.lbl_img = Label(self.fr1, image=gambar)
        self.lbl_img.place(x=15, y= 20)
        teks = textwrap.wrap(self.data[0], width=20)
        teks = '\n'.join(teks)
        self.lbl_judul = Label(self.fr1, text=teks,bg='#f5f0e1', font=('Times New Roman', 20, 'bold'), justify='left')
        self.lbl_judul.place(x=15, y=420)

        global img_bck
        img_bck = ImageTk.PhotoImage(Image.open('Stok_Image/back_icon.png').resize(size=(60, 60)))
        self.btt_back = Button(self.FRAME, image=img_bck, font=('Verdana', 12, 'bold'), bg='#f5f0e1', border=0, relief=FLAT, command=self.back)
        self.btt_back.place(x=20, y=632)

    def back(self):
        self.window.destroy()

    def gambar_film(self):
        film_file = open('Data/film.txt', 'r').read().split('\n')
        for fg in film_file:
            g = fg.split(',')
            if g[1] == self.film:
                self.lg = g[0]
                break

        img_open = Image.open(self.lg).resize((250, 380))
        global gambar
        gambar = ImageTk.PhotoImage(img_open)
        gambar = gambar
        return gambar


    def td(self,frame,i):
        Label(frame, text=':', font=('Times New Roman', 15), bg='#f5f0e1').grid(row=i, column=1, padx=30)


    def Detail(self, tiket, tempat, kursi, tayang, harga):
        self.lbld1 = Label(self.fr1a, text=tiket,font=('Times New Roman', 15), bg='#f5f0e1', fg='#1e3d59')
        self.lbld1.grid(row=1, column=2, sticky='e')
        self.lbld2 = Label(self.fr1a, text=tempat,font=('Times New Roman', 15), bg='#f5f0e1', fg='#1e3d59')
        self.lbld2.grid(row=2, column=2, sticky='e')
        self.lbld3 = Label(self.fr1a, text=kursi,font=('Times New Roman', 15), bg='#f5f0e1', fg='#1e3d59')
        self.lbld3.grid(row=3, column=2, sticky='e')
        self.lbld3 = Label(self.fr1a, text=tayang,font=('Times New Roman', 15), bg='#f5f0e1', fg='#1e3d59')
        self.lbld3.grid(row=4, column=2, sticky='e')
        self.lbld4 = Label(self.fr1a, text=harga,font=('Times New Roman', 15), bg='#f5f0e1', fg='#1e3d59')
        self.lbld4.grid(row=5, column=2, sticky='e')
    
    def lbl_tmbhan(self, jenis, hg, i):
        self.lbld4 = Label(self.fr1b, text=jenis,font=('Times New Roman', 15), bg='#f5f0e1', fg='#1e3d59')
        if len(jenis) < 15:
            self.lbld4.grid(row=i, column=0, sticky='w', pady=10)
        else:
            self.lbld4.grid(row=i, column=0, sticky='w', pady=0)
        self.td(self.fr1b, i)
        self.lbld4 = Label(self.fr1b, text='Rp. '+format(int(hg), ',d').replace(',', '.'),font=('Times New Roman', 15), bg='#f5f0e1', fg='#1e3d59')
        self.lbld4.grid(row=i, column=3, sticky='e')

    def bayar(self):
        try:
            self.win2.destroy()
        except:
            pass
        self.win2 = Toplevel()
        self.win2.geometry('400x300+600+100')
        self.win2.resizable(0,0)
        self.win2.configure(bg='#f5f0e1')
        self.w_lbl1 = Label(self.win2, text='Payment Method', bg='#1e3d59', font=('Times New Roman', 20, 'bold'),fg='#f5f0e1').place(x=0, y=0, width=400, height=50)
        self.line = Label(self.win2, bg='#ff6e40')
        self.line.place(x=0, y=50, width=400, height=10)
        self.btw_1 = Button(self.win2, bg='white', relief=FLAT, border=0, text='DANI', font='Times 15 bold', command=self.dana)
        self.btw_1.place(x=25, y=90, width=350, height=50)
        self.lbl_dn = Label(self.win2, image=Pembayaran.icon_list[0], bg='white')
        self.lbl_dn.place(x=10+25, y=91)
        self.btw_2 = Button(self.win2, bg='white', relief=FLAT, border=0, text='KERIS', font='Times 15 bold', command=self.qris)
        self.btw_2.place(x=25, y=170, width=350, height=50)
        self.lbl_qr = Label(self.win2, image=Pembayaran.icon_list[1], bg='white')
        self.lbl_qr.place(x=10+25, y=171)

    def dana(self):
        self.win2.destroy()
        self.fr_pay = Frame(self.FRAME, bg='#f5f0e1')
        self.fr_pay.place(x=0, y=120, width=1100, height=600)
        self.fr_dana = Frame(self.fr_pay)
        self.fr_dana.place(x=550-175, y=20, width=350, height=400)
        self.dn1 = Label(self.fr_dana, bg='#008CEB', image=Pembayaran.icon_list[0])
        self.dn1.place(x=0, y=0, width=70, height=70)
        self.dn2 = Label(self.fr_dana, bg='#008CEB', text="Pembayaran Tiket Bioskop", fg='white', font='verdana 12 bold')
        self.dn2.place(x=70, y=0, width=280, height=70)
        self.dn3 = Label(self.fr_dana, bg='white')
        self.dn3.place(x=0, y=70, width=350, height=80)
        self.dn4 = Label(self.dn3, bg='white', text="Total Harga", font='verdana 10')
        self.dn4.place(x=10, y=15)
        self.dn5 = Label(self.dn3, bg='white', text='Rp'+format(self.total, ',d').replace(',','.'), font='verdana 12 bold', fg='orange')
        self.dn5.place(x=230, y=15)
        self.dn6 = Label(self.fr_dana, bg='white')
        self.dn6.place(x=0, y=320, width=350, height=80)
        self.dn7 = Button(self.dn6, bg='#008CEB', text="Bayar Rp"+format(self.total, ',d').replace(',','.'), fg='white', font='verdana 12 bold', border=0, relief=FLAT, command=self.af_dana)
        self.dn7.place(x=15, y=30, width=320, height=35)
        self.bttext = CTkButton(self.FRAME, bg_color='#1e3d59', fg_color='red', text='Batalkan pembayaran', font=('Times', 15, 'bold'), command=self.cancel)
        self.bttext.place(x=30, y=40)

    def qris(self):
        self.win2.destroy()
        self.fr_pay = Frame(self.FRAME, bg='#f5f0e1')
        self.fr_pay.place(x=0, y=120, width=1100, height=600)
        self.fr_qris = Frame(self.fr_pay, bg='white')
        self.fr_qris.place(x=550-175, y=20, width=350, height=550)
        self.qris_ic = ImageTk.PhotoImage(Image.open('Stok_Image/qris.png').resize(size=(130,50)))
        self.qr1 = Label(self.fr_qris, image=self.qris_ic, bg='white').place(x=175-65,y=10)
        ch = (string.ascii_letters + string.digits)
        self.cdpy = "".join(choices(ch, k=6))
        self.qr_gen = qr.make(self.cdpy)
        self.qr_gen.save("Stok_Image/payment_code.png")
        self.qr_code = ImageTk.PhotoImage(Image.open('Stok_Image/payment_code.png').resize(size=(300,300)))
        self.qr2 = Label(self.fr_qris, image=self.qr_code, bg='white').place(x=25, y=60)
        self.qr3 = Entry(self.fr_qris, border=0, highlightbackground='black', highlightcolor='black', highlightthickness=2, justify='center', font='verdana 17 bold')
        self.qr3.place(x=75, y=420, width=200, height=40)
        self.qr4 = Label(self.fr_qris, text="Masukkan Kode yang telah anda Scan", font='verdana 12', bg='white')
        self.qr4.place(x=25, y=390)
        self.qr5 = Button(self.fr_qris, text='Konfirmasi', font='verdana 12 bold', bg='blue', relief=FLAT, border=0, fg='White', command=self.af_qris)
        self.qr5.place(x=30, y=475, width=290, height=50)
        self.bttext = CTkButton(self.FRAME, bg_color='#1e3d59', fg_color='red', text='Batalkan pembayaran', font=('Times', 15, 'bold'), command=self.cancel)
        self.bttext.place(x=30, y=40)

    def af_dana(self):
        self.FRAME.destroy()
        self.fr_pay.destroy()
        self.save()
        Pencetakan.Cetak(self.window, self.data, self.tambahan, 'DANI', self.main, self.home)

    def af_qris(self):
        print(self.cdpy)
        if self.qr3.get() != self.cdpy:
            Label(self.fr_qris, text='Kode yang anda masukkan SALAH!', fg='red', bg='white', font='verdana 8 bold').place(x=15, y=360)
        else:
            self.fr_qris.destroy()
            self.fr_qris2 = Frame(self.fr_pay, bg='white')
            self.fr_qris2.place(x=550-175, y=20, width=350, height=550)
            self.inp = Entry(self.fr_qris2, border=0, highlightbackground='black', highlightcolor='black', highlightthickness=2, justify='center', font='verdana 17 bold')
            self.inp.place(x=85, y=200, width=200, height=40)
            self.rp = Label(self.fr_qris2, text='Rp.', font='verdana 17 bold', bg='white').place(x=30, y=205)
            self.qr1 = Label(self.fr_qris2, image=self.qris_ic, bg='white').place(x=175-65,y=10)
            self.ket1 = Label(self.fr_qris2, text='Pembayaran Tiket Bioskop', font='verdana 15 bold', bg='white').place(x=25, y=70, width=300)
            self.ket1 = Label(self.fr_qris2, text='Total Pembelian', font='verdana 13 bold', bg='white').place(x=25, y=130, width=300)
            self.ket1 = Label(self.fr_qris2, text='Rp'+format(self.total, ',d').replace(',','.'), font='verdana 11 bold', bg='white').place(x=25, y=160, width=300)
            self.qr5 = Button(self.fr_qris2, text='Konfirmasi Pembayaran', font='verdana 12 bold', bg='blue', relief=FLAT, border=0, fg='White', command=self.af_qris1)
            self.qr5.place(x=30, y=300, width=290, height=50)
    
    def af_qris1(self):
        uang = self.inp.get()
        if uang != str(self.total):
            Label(self.fr_qris, text='Nominal yang anda masukkan harus sesuai!', fg='red', bg='white', font='verdana 8 bold').place(x=30, y=260, width=300)
        else:
            self.FRAME.destroy()
            self.fr_pay.destroy()
            self.save()
            Pencetakan.Cetak(self.window, self.data, self.tambahan, 'KERIS', self.main, self.home)

    def save(self):
        l = self.data[3]
        h = open(f'Data/chair_history_{self.data[1]}.txt', 'r')
        c = h.read().split('\n')
        x = open(f'Data/chair_history_{self.data[1]}.txt', 'w')
        p = 0
        for a in c:
            if a == '':
                continue
            if f'{self.film};{self.data[2]}' in a:
                p += 1
                if a == c[-1]:
                    a += ','+l
                    b = a
                else:
                    a += ','+l
                    b = a+'\n'
            else:
                if a == c[-1]:
                    b = a
                else:
                    b = a+'\n'
            x.write(b)
        if p == 0:
            b = f'\n{self.film};{self.data[2]};{l}'
            x.write(b)
        x.close()

    def cancel(self):
        self.bttext.destroy()
        self.fr_pay.destroy()