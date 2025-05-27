from tkinter import *
from customtkinter import *
from PIL import Image, ImageTk
import Menu_Awal

class Welcome:

    def __init__(self,window):
        self.window = window
        self.window.configure(bg='black')
        self.window.state('zoomed')
        self.FRAME = Frame(self.window,bg='#f5f0e1')
        self.FRAME.pack(ipadx=550, ipady=355)
        global bg
        bg = ImageTk.PhotoImage(Image.open('Stok_Image/Welcome to ALAMBOCA CINEMA.png'))
        self.bg_label = Label(self.FRAME, image=bg).place(x=-2, y=-1)
        self.fr_login = CTkFrame(self.FRAME, fg_color='#1e3d59', width=500, height=400, corner_radius=50)
        self.fr_login.place(x=550, y=175)

        self.lbl_login = Label(self.fr_login, text='LOGIN', font=("yu gothic ui", 25, 'bold'), bg='#1e3d59', fg='#f5f0e1').place(x=200, y=30, width=100, height=35)
        self.btn_signin = Button(self.fr_login, text='Buat Akun Baru', font=("yu gothic ui", 12, 'bold'), border=0, relief=FLAT, command=self.sign_in, bg='#1e3d59', fg='#ffc13b', activebackground='#1e3d59', cursor='hand2')
        self.btn_signin.place(x=175, y=70, width=150, height=20)
        self.btn_signin.bind('<Enter>', self.enter)
        self.btn_signin.bind('<Leave>', self.leave)
        self.email_label = Label(self.fr_login, text='• Username', fg='#f5f0e1', bg='#1e3d59', font=("yu gothic ui", 11, 'bold'))
        self.email_label.place(x=110, y=110)
        self.a = StringVar()
        self.email_entry = CTkEntry(self.fr_login, text_color="black", font=("yu gothic ui semibold", 15), textvariable=self.a, width=256, height=34, corner_radius=30, border_color='#ff6e40')
        self.email_entry.place(x=110, y=140)

        self.password_label = Label(self.fr_login, text='• Password', fg='#f5f0e1', bg='#1e3d59', font=("yu gothic ui", 11, 'bold'))
        self.password_label.place(x=110, y=180)
        self.password_entry = CTkEntry(self.fr_login, text_color="black", font=("yu gothic ui semibold", 15), show='•', width=256, height=34, corner_radius=30, border_color='#ff6e40')
        self.password_entry.place(x=110, y=210)

        self.checkButton = Checkbutton(self.fr_login, bg='#1e3d59', command=self.password_command, text='Show password', fg='#ffc13b', activebackground='#1e3d59', activeforeground='#ffc13b')
        self.checkButton.place(x=110, y=245)

        self.loginBtn1 = CTkButton(self.fr_login, text_color='#1e3d59', text='Login', fg_color='#ffc13b', font=("yu gothic ui bold", 25, 'bold'), cursor='hand2', width=200, height=40, corner_radius=30, command=self.login)
        self.loginBtn1.place(x=140, y=280)


    def enter(self, e):
        self.btn_signin.configure(fg='#40e7f2')

    def leave(self, e):
        self.btn_signin.configure(fg='#ffc13b')

    def sign_in(self):
        self.fr_signin = CTkFrame(self.FRAME, fg_color='#1e3d59', width=500, height=400, corner_radius=50)
        self.fr_signin.place(x=550, y=175)

        self.name_label = Label(self.fr_signin, text='• Name', fg='#f5f0e1', bg='#1e3d59', font=("yu gothic ui", 11, 'bold'))
        self.name_label.place(x=100, y=70)
        self.nn = StringVar()
        self.name_entry = CTkEntry(self.fr_signin, font=("yu gothic ui semibold", 15), textvariable=self.nn, width=290, height=35, corner_radius=30, border_color='#ff6e40')
        self.name_entry.place(x=100, y=100)

        self.n_email_label = Label(self.fr_signin, text='• Email', fg='#f5f0e1', bg='#1e3d59', font=("yu gothic ui", 11, 'bold'))
        self.n_email_label.place(x=100, y=140)
        self.nu = StringVar()
        self.n_email_entry = CTkEntry(self.fr_signin, font=("yu gothic ui semibold", 15), textvariable=self.nu, width=290, height=35, corner_radius=30, border_color='#ff6e40')
        self.n_email_entry.place(x=100, y=170)

        self.n_password_label = Label(self.fr_signin, text='• Password', fg='#f5f0e1', bg='#1e3d59', font=("yu gothic ui", 11, 'bold'))
        self.n_password_label.place(x=100, y=215)
        self.n_password_entry = CTkEntry(self.fr_signin, font=("yu gothic ui semibold", 15), show='•', width=290, height=35, corner_radius=30, border_color='#ff6e40')
        self.n_password_entry.place(x=100, y=245)
        self.n_checkButton = Checkbutton(self.fr_signin, bg='#1e3d59', command=self.password_command1, text='Show password', fg='#ffc13b', activebackground='#1e3d59', activeforeground='#ffc13b')
        self.n_checkButton.place(x=100, y=280)
        self.loginBtn1 = CTkButton(self.fr_signin, text_color='#1e3d59', text='Sign Up', fg_color='#ffc13b', font=("yu gothic ui bold", 25, 'bold'), cursor='hand2', width=200, height=40, corner_radius=30, command=self.sign_up)
        self.loginBtn1.place(x=150, y=320)

        global img_bck
        img_bck = ImageTk.PhotoImage(Image.open('Stok_Image/back_icon.png').resize(size=(40, 40)))
        self.btt_back = Button(self.fr_signin, image=img_bck, font=('Verdana', 12, 'bold'), bg='#1e3d59', border=0, relief=FLAT, activebackground='#1e3d59', command=self.back)
        self.btt_back.place(x=20, y=20)


    def password_command(self):
        if self.password_entry.cget('show') == '•':
            self.password_entry.configure(show='')
        else:
            self.password_entry.configure(show='•')

    def password_command1(self):
        if self.n_password_entry.cget('show') == '•':
            self.n_password_entry.configure(show='')
        else:
            self.n_password_entry.configure(show='•')


    def back(self):
        self.fr_signin.destroy()


    def login(self):
        dt_akun = open('Data/logindatabase.txt', 'r').read().split('\n\n')
        un = self.a.get()
        pw = self.password_entry.get()
        loc = 0
        for akun in dt_akun:
            acc = akun.split('\n')
            if un == acc[1] and pw == acc[2]:
                self.FRAME.destroy()
                Menu_Awal.Menu(self.window)
                loc += 1
                break
        if loc == 0:
            Label(self.fr_login, text='Username and Password are not registered!', fg='red', bg='#1e3d59').place(x=20, y=350, height=20)

    def sign_up(self):
        dt_akunr = open('Data/logindatabase.txt', 'r')
        dt_akun = open('Data/logindatabase.txt', 'a')
        akun = dt_akunr.read().split('\n\n')
        new_name = self.nn.get()
        new_un = self.nu.get()
        new_pw = self.n_password_entry.get()
        p = 0

        for un in akun:
            if new_un in un:
                p += 1
            else:
                continue
        
        if p == 0:
            akun = f'\n{new_name}\n{new_un}\n{new_pw}\n'
            dt_akun.write(akun)

        else:
            Label(self.fr_signin, text='Username sudah digunakan', fg='red', bg='#1e3d59').place(x=20, y=360, height=20)
        dt_akun.close()
        self.fr_signin.destroy()

Tampilan = Tk()
Welcome(Tampilan)
Tampilan.mainloop()