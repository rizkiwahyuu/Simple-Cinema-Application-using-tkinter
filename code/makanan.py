from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk
from customtkinter import *
import textwrap
import Pembayaran

class Makanan:
    pic_list = []
    nama_f = []
    user = []

    def __init__(self,window,  data, main, home):
        self.main = main
        self.window = window
        self.home = home
        self.FRAME = Frame(self.window, bg='#f5f0e1')
        self.FRAME.pack(ipadx=550, ipady=355)
        self.Ptk = data

        self.lbl = Label(self.FRAME, bg='#ff6e40')
        self.lbl.place(x= 0, y=100, height=50, width=1100) 
        self.label = Label(self.FRAME, bg='#1e3d59', text='FOODS', font=('Century', 50, 'bold'), fg='#f5f0e1')
        self.label.place(x=0, y=0, width=1100, height=100)
        self.fr_makanan = Frame(self.FRAME, bg='#ff6e40')
        self.fr_makanan.place(x=(1100/2)-450, y=100, width=900, height=50)
        self.fr1 = Frame(self.FRAME,bg='#f5f0e1')
        self.fr1.place(x=0, y=150)
        self.sh = CTkButton(self.fr_makanan, text='COMBO', font=('Times New Roman', 15, 'bold'), fg_color='#ffc13b', command=lambda: self.slide(0), bg_color='#ff6e40', text_color='black', height=35, corner_radius=20)
        self.sh.grid(column=0, row=0, padx=10, pady=7)
        self.fi = CTkButton(self.fr_makanan, text='PROMO COMBO', font=('Times New Roman', 15, 'bold'), fg_color='#ffc13b', command=lambda: self.slide(-1100), bg_color='#ff6e40', text_color='black', height=35, corner_radius=20)
        self.fi.grid(column=1, row=0, padx=10, pady=7)
        self.hr = CTkButton(self.fr_makanan, text='POPCORN', font=('Times New Roman', 15, 'bold'), fg_color='#ffc13b', command=lambda: self.slide(-2200), bg_color='#ff6e40', text_color='black', height=35, corner_radius=20)
        self.hr.grid(column=2, row=0, padx=10, pady=7)
        self.an = CTkButton(self.fr_makanan, text='MINUMAN', font=('Times New Roman', 15, 'bold'), fg_color='#ffc13b',command=lambda: self.slide(-1100*3), bg_color='#ff6e40', text_color='black', height=35, corner_radius=20)
        self.an.grid(column=3, row=0, padx=10, pady=7)
        self.km = CTkButton(self.fr_makanan, text='MAKANAN', font=('Times New Roman', 15, 'bold'), fg_color='#ffc13b',command=lambda: self.slide(-1100*4), bg_color='#ff6e40', text_color='black', height=35, corner_radius=20)
        self.km.grid(column=4, row=0, padx=10, pady=7)
        self.data=open('Data/makanan.txt', "r").read().split('\n')
        self.i = 0

        self.fr1a = Frame(self.fr1, bg= '#f5f0e1')
        self.fr1a.grid(row=0, column=0, ipadx=550, ipady=300)
        self.fr2b = CTkFrame(self.fr1a, fg_color='#f5f0e1', corner_radius=20, width=650, height=250)
        self.fr2b.place(x=(1100/2)-325, y=0)
        self.btt_loop(self.fr2b, 'Combo')

        self.fr1b = Frame(self.fr1, bg= '#f5f0e1')
        self.fr1b.grid(row=0, column=1, ipadx=550, ipady=300)
        self.fr2c = Frame(self.fr1b, bg='#f5f0e1')
        self.fr2c.place(x=(1100/2)-175, y=0, width=350, height=250)
        self.btt_loop(self.fr2c, 'Promo')

        self.fr1c = Frame(self.fr1, bg= '#f5f0e1')
        self.fr1c.grid(row=0, column=2, ipadx=550, ipady=300)
        self.fr2d = Frame(self.fr1c, bg='#f5f0e1')
        self.fr2d.place(x=150, y=0, width=800, height=480)
        self.btt_loop(self.fr2d, 'Popcorn')

        self.fr1d = Frame(self.fr1, bg= '#f5f0e1')
        self.fr1d.grid(row=0, column=3, ipadx=550, ipady=300)
        self.fr_can = Frame(self.fr1d, bg='#f0810f')
        self.c = Canvas(self.fr_can, bg='#f5f0e1')
        self.c.place(x=0, y=0, width=1030, height=580)
        self.sb = ttk.Scrollbar(self.fr_can, orient='vertical', command= self.c.yview)
        self.sb.place(relheight=1, relx=1, rely=0, anchor='ne')
        self.c.configure(yscrollcommand= self.sb.set)
        self.c.bind('<Configure>', lambda e: self.c.configure(scrollregion = self.c.bbox('all')))
        self.frc = Frame(self.c, bg='black')
        self.c.create_window((0,0), window= self.frc, anchor= 'nw')
        self.fr_can.place(x=150, y=0, width=800, height=570)
        self.fr2 = Frame(self.frc, bg='#f5f0e1')
        self.fr2.pack(ipadx=550, ipady=450)
        self.btt_loop(self.frc, 'Drink')

        self.fr1e = Frame(self.fr1, bg= '#f5f0e1')
        self.fr1e.grid(row=0, column=4, ipadx=550, ipady=300)
        self.fr_can1 = Frame(self.fr1e, bg='#f0810f')
        self.c1 = Canvas(self.fr_can1, bg='white')
        self.c1.place(x=0, y=0, width=1030, height=580)
        self.sb1 = ttk.Scrollbar(self.fr_can1, orient='vertical', command= self.c1.yview)
        self.sb1.place(relheight=1, relx=1, rely=0, anchor='ne')
        self.c1.configure(yscrollcommand= self.sb1.set)
        self.c1.bind('<Configure>', lambda e: self.c1.configure(scrollregion = self.c1.bbox('all')))
        self.frc1 = Frame(self.c1, bg='black')
        self.c1.create_window((0,0), window= self.frc1, anchor= 'nw')
        self.fr_can1.place(x=150, y=0, width=800, height=570)
        self.fr2a = Frame(self.frc1, bg='#f5f0e1')
        self.fr2a.pack(ipadx=550, ipady=450)
        self.btt_loop(self.fr2a, 'Food')

        self.lastbtt = CTkButton(self.FRAME, text='Pembayaran =>', width=160, height=40, font=('Verdana', 15, 'bold'),fg_color='#ffc13b', command=self.send, text_color='black', corner_radius=15, bg_color='#1e3d59')
        self.lastbtt.place(x=932, y=60)

        global img_bck
        img_bck = ImageTk.PhotoImage(Image.open('Stok_Image/back_icon.png').resize(size=(60, 60)))
        self.btt_back = Button(self.FRAME, image=img_bck, font=('Verdana', 12, 'bold'), bg='#f5f0e1', border=0, relief=FLAT, command=self.back)
        self.btt_back.place(x=20, y=632)


    def back(self):
        self.window.destroy()

    def slide(self, stop):
        self.fr1.place_configure(x=stop)


    def btt_loop(self,frame,  promo):
        Makanan.nama_f.clear()
        x = 0
        y = 10
        def img_pro(file):
            img_open = Image.open(file).resize((150, 150))
            global gambar
            gambar = ImageTk.PhotoImage(img_open)
            gambar = gambar
            return gambar

        for dafma in self.data:
            df1 = dafma.split(',')
            if promo in df1[1]:
                g = img_pro(df1[0])
                nama = df1[0][11:df1[0].index('.')].title()
                harga = df1[2]
                Makanan.pic_list.append(g)
                Makanan.nama_f.append([nama,harga])


        for jdl in Makanan.nama_f:
            if x > (800-150):
                x = 0
                y += 250
            self.btt_makanan(frame=frame, gambar=Makanan.pic_list[self.i], x_pos=x, y_pos=y, Judul=jdl[0], harga=jdl[1])
            x+=160
            self.i += 1

    def btt_makanan(self,frame, gambar, x_pos, y_pos, Judul, harga):

        def fb():
            try:
                self.wb.destroy()
            except:
                pass
            self.wb = Toplevel()
            self.wb.title(Judul)
            self.wb_fr = Frame(self.wb, bg='#f5f0e1')
            self.wb_fr.pack(ipadx=200, ipady=150)
            self.wb_lbl1 = Label(self.wb_fr, image=gambar, bg='#f5f0e1')
            self.wb_lbl1.place(x=200-75, y=0)
            self.wb_lbl2 = Label(self.wb_fr, text="JUMLAH\t:", bg='#f5f0e1')
            self.wb_lbl2.place(x=200-55, y=170)
            self.wb_lbl3 = Entry(self.wb_fr, highlightthickness=2, highlightbackground='#1e3d59', highlightcolor='#1e3d59', border=0)
            self.wb_lbl3.place(x=275-50, y=170, width=30)
            self.wb_lbl4 = Button(self.wb_fr, text='OK', command= lambda: self.add(harga=harga, nama=Judul), bg='#ffc13b', border=0, highlightbackground='#1e3d59', highlightcolor='#1e3d59')
            self.wb_lbl4.place(x=200, y=200)

        text = textwrap.wrap(Judul, width=15)
        teks = '\n'.join(text)
        l_judul = Label(frame, text= teks, font=('Times New Roman', 15), bg='#f5f0e1')
        l_judul.place(x=x_pos+5, y=y_pos+155)
        l_harga = Label(frame, text='Rp. '+format(int(harga),',d').replace(',','.'), bg='#f5f0e1')
        l_harga.place(x=x_pos+5, y=y_pos+200)
        btt = Button(frame, image=gambar, border=0, command= fb, bg='#f5f0e1')
        btt.place(x=x_pos, y=y_pos)

    def add(self, harga, nama):
        a = self.wb_lbl3.get()
        h = int(harga)*int(a)
        penulisan = f'{a} {nama}:{h}'
        Makanan.user.append(penulisan)
        self.wb.destroy()

    def send(self):
        ukw = self.window.winfo_screenwidth()
        ukh = self.window.winfo_screenheight()
        self.fr_pembayaran = Frame(self.window, bg='black')
        self.fr_pembayaran.place(x=0, y=0, width=ukw, height=ukh)
        Pembayaran.Pembayaran(self.fr_pembayaran, data=self.Ptk, makanan=Makanan.user, main=self.main, home=self.home)