from tkinter import *
import Pembayaran
import makanan
from customtkinter import *
from PIL import Image, ImageTk

class Kursi:
    chair_list = []
    dahis = []
    def __init__(self,window, film, data, main, home):
        self.window = window
        self.main = main
        self.home = home

        self.data = data
        self.FRAME = Frame(self.window, bg='#f5f0e1')
        self.FRAME.pack(ipadx=550, ipady=355)
        self.label = Label(self.FRAME, bg='#1e3d59', text='TICKETS', font=("Verdana", 50, 'bold'), fg='#f5f0e1')
        self.label.place(x=0, y=0, width=1100, height=100)
        self.line = Label(self.FRAME, bg='#ff6e40')
        self.line.place(x=0, y=95, width=1100)
        self.l_bg = Label(self.FRAME, bg='#1e3d59')
        self.l_bg.place(x=140, y=170, width=820, height=420)
        self.fr1 = Frame(self.FRAME, bg='#f5f0e1')
        self.fr1.place(x=150, y=180, width=400*2, height=200*2)
        self.lbl1 = Label(self.fr1, text='Jumlah Tiket yang Anda pesan', font=("Century", 25, 'bold'), bg='#f5f0e1', fg='#1e3d59').place(x= 400-300, y= 50, width=600)
        self.inp1 = Entry(self.fr1,font=('Century',25), justify='center')
        self.inp1.place(x=400-50, y=100+8, width=100, height=60)

        self.min = CTkButton(self.fr1, text="+", font=("Century", 20, 'bold'), command=self.increment, fg_color='#f0810f',width=50, height=50, corner_radius=5).place(x=400-100, y=100+13)
        self.plus = CTkButton(self.fr1, text="-", font=("Century", 20, 'bold'), command=self.decrement, fg_color='#f0810f',width=50, height=50, corner_radius=5).place(x=400+50, y=100+13)

        self.btt1 = CTkButton(self.fr1, text="NEXT", font=("Century", 20, 'bold'), command=self.OK, fg_color='#f0810f',width=100, height=50, corner_radius=15).place(x=400-50, y=300)
        self.film = film

        global img_bck
        img_bck = ImageTk.PhotoImage(Image.open('Stok_Image/back_icon.png').resize(size=(60, 60)))
        self.btt_back = Button(self.FRAME, image=img_bck, font=('Verdana', 12, 'bold'), bg='#f5f0e1', border=0, relief=FLAT, command=self.back)
        self.btt_back.place(x=20, y=632)

    def increment(self):
        value = int(self.inp1.get())
        self.inp1.delete(0, 'end')
        self.inp1.insert(0, str(value + 1))

    def decrement(self):
        value = int(self.inp1.get())
        if value > 0:
            self.inp1.delete(0, 'end')
            self.inp1.insert(0, str(value - 1))

    # def next(self):
    #     # Implement your logic here
    #     pass

    # def next(self):
    #     self.window.destroy()
    # def back(self):
    #     # Implement your logic here
    #     pass

    # def back(self):
    #     self.window.destroy()

    def back1(self):
        Kursi.chair_list.clear()
        Kursi.dahis.clear()
        self.fr_krs.destroy()

    def OK(self):
        try:
            tiket = int(self.inp1.get())
        except:
            return self.inp1.get()
        if tiket < 1:
            return tiket
        self.fr_krs = Frame(self.FRAME, bg='#f5f0e1')
        self.fr_krs.place(x=0, y=0, width=1100, height=710)
        self.l_bg1 = Label(self.fr_krs, bg='#1e3d59')
        self.l_bg1.place(x=140, y=190, width=820, height=470)
        self.fr2 = Frame(self.fr_krs, bg='#f5f0e1')
        self.fr2.place(x=150, y=200, width=800,height=450)
        self.label = Label(self.fr_krs, bg='#1e3d59', text='TEMPAT DUDUK', font=("Verdana", 50, 'bold'), fg='#f5f0e1')
        self.label.place(x=0, y=0, width=1100, height=100)
        self.lbl_layar = Label(self.fr2, bg='#ff6e40', text='LAYAR').place(x=50, y=10, width=700)
        if self.data[0] == 'K1':
            self.fr2a = Frame(self.fr2, bg='#F3EEEA')
            self.fr2a.place(x=60, y=50, width=160,height=320)
            self.fr2b = Frame(self.fr2, bg='#F3EEEA')
            self.fr2b.place(x=(800-220), y=50, width=160,height=320)
            self.fr2c = Frame(self.fr2, bg='#F3EEEA')
            self.fr2c.place(x=260, y=50, width=280,height=360)
            self.chair_K1(tiket)
            self.t_btt1 = Button(self.fr2, text='Menu Tambahan', font=("Century", 10, 'bold'), command=self.makanan, bg='#ffc13b', border=0, relief=FLAT, activebackground='#ffc13b',activeforeground='white')
            self.t_btt1.place(x=800-170, y=390, width=150, height=40)
            self.t_btt2 = Button(self.fr2, text='Menu Pembayaran', font=("Century", 10, 'bold'), command=self.bayar, bg='#ffc13b', border=0, relief=FLAT, activebackground='#ffc13b',activeforeground='white')
            self.t_btt2.place(x=20, y=390, width=150, height=40)
        elif self.data[0] == 'K2':
            self.fr2a = Frame(self.fr2, bg='#F3EEEA')
            self.fr2a.place(x=100, y=50, width=280, height=280)
            self.fr2b = Frame(self.fr2, bg='#F3EEEA')
            self.fr2b.place(x=(800-380), y=50, width=280,height=280)
            self.fr2c = Frame(self.fr2, bg='#F3EEEA')
            self.fr2c.place(x=100, y=350, width=440,height=40)
            self.chair_K2(tiket)
            self.t_btt1 = Button(self.fr2, text='Menu Tambahan', font=("Century", 10, 'bold'), command=self.makanan, bg='#ffc13b', border=0, relief=FLAT, activebackground='#ffc13b',activeforeground='white')
            self.t_btt1.place(x=800-170, y=400, width=150, height=40)
            self.t_btt2 = Button(self.fr2, text='Menu Pembayaran', font=("Century", 10, 'bold'), command=self.bayar, bg='#ffc13b', border=0, relief=FLAT, activebackground='#ffc13b',activeforeground='white')
            self.t_btt2.place(x=20, y=400, width=150, height=40)
        else:
            pass
        global img_bck2
        img_bck2 = ImageTk.PhotoImage(Image.open('Stok_Image/back_icon.png').resize(size=(60, 60)))
        self.btt_back1 = Button(self.fr_krs, image=img_bck2, font=('Verdana', 12, 'bold'), bg='#f5f0e1', border=0, relief=FLAT, command=self.back1)
        self.btt_back1.place(x=20, y=632)

    def chair_K1(self, tiket):
        history = open('Data/chair_history_K1.txt', 'r')
        h_chair = history.read().split('\n')
        for a in h_chair:
            chair = a.split(';')
            if chair[0] == self.film and chair[1] == self.data[1]:
                Kursi.dahis = chair[2].split(',')
                break
        xa = 0
        ya = 0
        xc = 0
        yc = 0
        xb = 0
        yb = 0
        for i in range(1,128):
            if str(i) in Kursi.dahis:
                st = 1
            else: 
                st = 0

            if 32<i<96:
                if xc > 270:
                    yc += 40
                    xc = 0
                    self.btt_chair(frame=self.fr2c ,no_kursi=str(i), x_pos= xc, y_pos= yc, t = tiket, used=st)
                    xc += 40
                else:
                    self.btt_chair(frame=self.fr2c ,no_kursi=str(i), x_pos= xc, y_pos= yc, t = tiket, used=st)
                    xc += 40

            elif i > 95:
                if xb > 150:
                    yb += 40
                    xb = 0
                    self.btt_chair(frame=self.fr2b ,no_kursi=str(i), x_pos= xb, y_pos= yb, t = tiket, used=st)
                    xb += 40
                else:
                    self.btt_chair(frame=self.fr2b ,no_kursi=str(i), x_pos= xb, y_pos= yb, t = tiket, used=st)
                    xb += 40

            else:
                if xa > 150:
                    ya += 40
                    xa = 0
                    self.btt_chair(frame=self.fr2a ,no_kursi=str(i), x_pos= xa, y_pos= ya, t = tiket, used=st)
                    xa += 40
                else:
                    self.btt_chair(frame=self.fr2a ,no_kursi=str(i), x_pos= xa, y_pos= ya, t = tiket, used=st)
                    xa += 40

    def chair_K2(self, tiket):
        history = open('Data/chair_history_K2.txt', 'r')
        h_chair = history.read().split('\n')
        for a in h_chair:
            chair = a.split(';')
            if chair[0] == self.film and chair[1] == self.data[1]:
                try:
                    Kursi.dahis = chair[2].split(',')
                    break
                except:
                    Kursi.dahis = [chair[2]]
        xa = 0
        ya = 0
        xb = 0
        yb = 0
        xc = 0
        yc = 0
        for i in range(1, 110):
            if str(i) in Kursi.dahis:
                st = 1
            else: 
                st = 0
            if 0<i<=49:
                if xa >= 280:
                    ya += 40
                    xa = 0
                    self.btt_chair(frame=self.fr2a ,no_kursi=str(i), x_pos= xa, y_pos= ya, t = tiket, used=st)
                    xa += 40
                else:
                    self.btt_chair(frame=self.fr2a ,no_kursi=str(i), x_pos= xa, y_pos= ya, t = tiket, used=st)
                    xa += 40
            elif 49<i<=98:
                if xb >= 280:
                    yb += 40
                    xb = 0
                    self.btt_chair(frame=self.fr2b ,no_kursi=str(i), x_pos= xb, y_pos= yb, t = tiket, used=st)
                    xb += 40
                else:
                    self.btt_chair(frame=self.fr2b ,no_kursi=str(i), x_pos= xb, y_pos= yb, t = tiket, used=st)
                    xb += 40
            else:
                self.btt_chair(frame=self.fr2c ,no_kursi=str(i), x_pos= xc, y_pos= yc, t = tiket, used=st)
                xc += 40
                


    def btt_chair(self, frame,  no_kursi='-',x_pos=0, y_pos=0, t=0, used=0):
        def f_btt():
            if btt_c['bg']=='red':
                Kursi.chair_list.remove(btt_c['text'])
                btt_c['bg'] = '#7D7C7C'
            elif len(Kursi.chair_list) >= t:
                pass
            else:
                Kursi.chair_list.append(btt_c['text'])
                btt_c['bg']='red'
        if used == 1:
            btt_c = Button(frame, text=no_kursi, bg='#191717',fg='white', command=f_btt, state=DISABLED)
            btt_c.place(x=x_pos, y=y_pos, width=35, height=35)
        else:
            btt_c = Button(frame, text=no_kursi, bg='#7D7C7C', command=f_btt)
            btt_c.place(x=x_pos, y=y_pos, width=35, height=35)

    def makanan(self):
        l = Kursi.chair_list
        asend = ','.join(l)
        self.send_data = [self.film, self.data[0], self.data[1], asend, int(self.data[2])]
        ukw = self.window.winfo_screenwidth()
        ukh = self.window.winfo_screenheight()
        self.fr_tambahan = Frame(self.window, bg='black')
        self.fr_tambahan.place(x=0, y=0, width=ukw, height=ukh)
        Kursi.chair_list.clear()
        Kursi.dahis.clear()
        makanan.Makanan(self.fr_tambahan, data=self.send_data, main=self.main, home=self.home)
        
    def bayar(self):
        l = Kursi.chair_list
        asend = ','.join(l)
        ukw = self.window.winfo_screenwidth()
        ukh = self.window.winfo_screenheight()
        self.send_data = [self.film, self.data[0], self.data[1], asend, int(self.data[2])]
        self.fr_pembayaran = Frame(self.window, bg='black')
        self.fr_pembayaran.place(x=0, y=0, width=ukw, height=ukh)
        Kursi.chair_list.clear()
        Kursi.dahis.clear()
        Pembayaran.Pembayaran(self.fr_pembayaran, self.send_data, main=self.main, home=self.home)