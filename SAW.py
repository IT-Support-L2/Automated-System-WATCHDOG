import tkinter as tk
import tkinter.ttk as ttk
from tkinter import *
import psutil, shutil
import email.message
import smtplib
import speedtest
from pythonping import ping
import threading
import sys
import time
from win10toast import ToastNotifier
import webbrowser





class App():
    def __init__(self, root):
        root.title("System Watchdog")
        root.geometry("500x620")
        root.minsize(120, 1)
        root.maxsize(1370, 749)
        root.resizable(0,  0)
        root.configure(background="#d9d9d9")
        root.configure(highlightbackground="#d9d9d9")
        root.configure(highlightcolor="black")

        

        self.cpu = IntVar()
        self.ram = IntVar()
        self.storage = IntVar()
        self.Ping = StringVar()
        self.upload_sp = IntVar()
        self.download_sp = IntVar()
        self.latency = IntVar()
        self.seconds = IntVar()
        self.smtp = StringVar()
        self.sender_email = StringVar()
        self.sender_pwd = StringVar()
        self.receiver_email = StringVar()

        self.TSeparator1 = ttk.Separator(root)
        self.TSeparator1.place(x=30, y=40, width=442)

        self.TNotebook1 = ttk.Notebook(root)
        self.TNotebook1.place(x=25, y=53, height=526, width=450)
        self.TNotebook1_t1_1 = tk.Frame(self.TNotebook1)
        self.TNotebook1.add(self.TNotebook1_t1_1, padding=3)
        self.TNotebook1.tab(0, text="System Preferences", compound="left"
                ,underline="-1", )
        self.TNotebook1_t1_1.configure(borderwidth="1")
        self.TNotebook1_t1_1.configure(relief="sunken")
        self.TNotebook1_t1_1.configure(background="#353535")
        self.TNotebook1_t1_1.configure(highlightbackground="#d9d9d9")
        self.TNotebook1_t1_1.configure(highlightcolor="black")
        self.TNotebook1_t2_1 = tk.Frame(self.TNotebook1)
        self.TNotebook1.add(self.TNotebook1_t2_1, padding=3)
        self.TNotebook1.tab(1, text="Email Preferences", compound="left"
                ,underline="-1", )
        self.TNotebook1_t2_1.configure(borderwidth="1")
        self.TNotebook1_t2_1.configure(background="#000000")
        self.TNotebook1_t2_1.configure(highlightbackground="#d9d9d9")
        self.TNotebook1_t2_1.configure(highlightcolor="black")
        self.TNotebook1_t3_1 = tk.Frame(self.TNotebook1)
        self.TNotebook1.add(self.TNotebook1_t3_1, padding=3)
        self.TNotebook1.tab(2, text="Help",compound="left",underline="-1",)
        self.TNotebook1_t3_1.configure(background="#d9d9d9")
        self.TNotebook1_t3_1.configure(highlightbackground="#d9d9d9")
        self.TNotebook1_t3_1.configure(highlightcolor="black")
        self.TNotebook1_t4_1 = tk.Frame(self.TNotebook1)
        self.TNotebook1.add(self.TNotebook1_t4_1, padding=3)
        self.TNotebook1.tab(3, text="Follow me", compound="left", underline="-1")
        self.TNotebook1_t4_1.configure(background="#d9d9d9")
        self.TNotebook1_t4_1.configure(highlightbackground="#d9d9d9")
        self.TNotebook1_t4_1.configure(highlightcolor="black")

        self.Labelframe1 = tk.LabelFrame(self.TNotebook1_t1_1)
        self.Labelframe1.place(x=10, y=10, height=48, width=421)
        self.Labelframe1.configure(relief='ridge')
        self.Labelframe1.configure(font="-family {Segoe UI} -size 9 -weight bold")
        self.Labelframe1.configure(foreground="black")
        self.Labelframe1.configure(relief="ridge")
        self.Labelframe1.configure(text='''CPU Check''')
        self.Labelframe1.configure(background="#d9d9d9")
        self.Labelframe1.configure(highlightbackground="#d9d9d9")
        self.Labelframe1.configure(highlightcolor="black")

        self.CPU_Entry = tk.Entry(self.Labelframe1)
        self.CPU_Entry.place(x=290, y=15, height=27, width=104
                , bordermode='ignore')
        self.CPU_Entry.configure(background="#c1ffc1")
        self.CPU_Entry.configure(cursor="")
        self.CPU_Entry.configure(disabledforeground="#a3a3a3")
        self.CPU_Entry.configure(font="TkFixedFont")
        self.CPU_Entry.configure(foreground="#000000")
        self.CPU_Entry.configure(highlightbackground="#d9d9d9")
        self.CPU_Entry.configure(highlightcolor="black")
        self.CPU_Entry.configure(insertbackground="black")
        self.CPU_Entry.configure(justify='center')
        self.CPU_Entry.configure(selectbackground="blue")
        self.CPU_Entry.configure(selectforeground="white")
        self.CPU_Entry.configure(textvariable=self.cpu)

        self.Label4 = tk.Label(self.Labelframe1)
        self.Label4.place(x=60, y=20, height=14, width=93, bordermode='ignore')
        self.Label4.configure(activebackground="#f9f9f9")
        self.Label4.configure(activeforeground="black")
        self.Label4.configure(background="#d9d9d9")
        self.Label4.configure(disabledforeground="#a3a3a3")
        self.Label4.configure(foreground="#000000")
        self.Label4.configure(highlightbackground="#d9d9d9")
        self.Label4.configure(highlightcolor="black")
        self.Label4.configure(text='''Enter CPU''')

        self.Labelframe2 = tk.LabelFrame(self.TNotebook1_t1_1)
        self.Labelframe2.place(x=10, y=70, height=48, width=421)
        self.Labelframe2.configure(relief='ridge')
        self.Labelframe2.configure(font="-family {Segoe UI} -size 9 -weight bold")
        self.Labelframe2.configure(foreground="black")
        self.Labelframe2.configure(relief="ridge")
        self.Labelframe2.configure(text='''RAM Check''')
        self.Labelframe2.configure(background="#d9d9d9")
        self.Labelframe2.configure(highlightbackground="#d9d9d9")
        self.Labelframe2.configure(highlightcolor="black")

        self.Label5 = tk.Label(self.Labelframe2)
        self.Label5.place(x=60, y=20, height=14, width=93, bordermode='ignore')
        self.Label5.configure(activebackground="#f9f9f9")
        self.Label5.configure(activeforeground="black")
        self.Label5.configure(background="#d9d9d9")
        self.Label5.configure(disabledforeground="#a3a3a3")
        self.Label5.configure(foreground="#000000")
        self.Label5.configure(highlightbackground="#d9d9d9")
        self.Label5.configure(highlightcolor="black")
        self.Label5.configure(text='''Enter RAM''')

        self.RAM_Entry = tk.Entry(self.Labelframe2)
        self.RAM_Entry.place(x=287, y=16, height=27, width=104, bordermode='ignore')
        self.RAM_Entry.configure(background="#c1ffc1")
        self.RAM_Entry.configure(disabledforeground="#a3a3a3")
        self.RAM_Entry.configure(font="TkFixedFont")
        self.RAM_Entry.configure(foreground="#000000")
        self.RAM_Entry.configure(highlightbackground="#d9d9d9")
        self.RAM_Entry.configure(highlightcolor="black")
        self.RAM_Entry.configure(insertbackground="black")
        self.RAM_Entry.configure(justify='center')
        self.RAM_Entry.configure(selectbackground="blue")
        self.RAM_Entry.configure(selectforeground="white")
        self.RAM_Entry.configure(textvariable=self.ram)

        self.Labelframe3 = tk.LabelFrame(self.TNotebook1_t1_1)
        self.Labelframe3.place(x=10, y=130, height=48, width=420)
        self.Labelframe3.configure(relief='ridge')
        self.Labelframe3.configure(font="-family {Segoe UI} -size 9 -weight bold")
        self.Labelframe3.configure(foreground="black")
        self.Labelframe3.configure(relief="ridge")
        self.Labelframe3.configure(text='''Storage Check''')
        self.Labelframe3.configure(background="#d9d9d9")
        self.Labelframe3.configure(highlightbackground="#d9d9d9")
        self.Labelframe3.configure(highlightcolor="black")

        self.Label6 = tk.Label(self.Labelframe3)
        self.Label6.place(x=60, y=20, height=14, width=103, bordermode='ignore')
        self.Label6.configure(activebackground="#f9f9f9")
        self.Label6.configure(activeforeground="black")
        self.Label6.configure(background="#d9d9d9")
        self.Label6.configure(disabledforeground="#a3a3a3")
        self.Label6.configure(foreground="#000000")
        self.Label6.configure(highlightbackground="#d9d9d9")
        self.Label6.configure(highlightcolor="black")
        self.Label6.configure(text='''Enter Storage''')

        self.STORAGE_Entry = tk.Entry(self.Labelframe3)
        self.STORAGE_Entry.place(x=287, y=16, height=27, width=104
                , bordermode='ignore')
        self.STORAGE_Entry.configure(background="#c1ffc1")
        self.STORAGE_Entry.configure(disabledforeground="#a3a3a3")
        self.STORAGE_Entry.configure(font="TkFixedFont")
        self.STORAGE_Entry.configure(foreground="#000000")
        self.STORAGE_Entry.configure(highlightbackground="#d9d9d9")
        self.STORAGE_Entry.configure(highlightcolor="black")
        self.STORAGE_Entry.configure(insertbackground="black")
        self.STORAGE_Entry.configure(justify='center')
        self.STORAGE_Entry.configure(selectbackground="blue")
        self.STORAGE_Entry.configure(selectforeground="white")
        self.STORAGE_Entry.configure(textvariable=self.storage)

        self.Labelframe4 = tk.LabelFrame(self.TNotebook1_t1_1)
        self.Labelframe4.place(x=10, y=190, height=48, width=420)
        self.Labelframe4.configure(relief='ridge')
        self.Labelframe4.configure(font="-family {Segoe UI} -size 9 -weight bold")
        self.Labelframe4.configure(foreground="black")
        self.Labelframe4.configure(relief="ridge")
        self.Labelframe4.configure(text='''Ping / Reachability Check''')
        self.Labelframe4.configure(background="#d9d9d9")
        self.Labelframe4.configure(highlightbackground="#d9d9d9")
        self.Labelframe4.configure(highlightcolor="black")

        self.PING_Entry = tk.Entry(self.Labelframe4)
        self.PING_Entry.place(x=160, y=16, height=27, width=234
                , bordermode='ignore')
        self.PING_Entry.configure(background="#c1ffc1")
        self.PING_Entry.configure(disabledforeground="#a3a3a3")
        self.PING_Entry.configure(font="TkFixedFont")
        self.PING_Entry.configure(foreground="#000000")
        self.PING_Entry.configure(highlightbackground="#d9d9d9")
        self.PING_Entry.configure(highlightcolor="black")
        self.PING_Entry.configure(insertbackground="black")
        self.PING_Entry.configure(justify='center')
        self.PING_Entry.configure(selectbackground="blue")
        self.PING_Entry.configure(selectforeground="white")
        self.PING_Entry.configure(textvariable=self.Ping)

        self.Label12 = tk.Label(self.Labelframe4)
        self.Label12.place(x=40, y=20, height=16, width=94, bordermode='ignore')
        self.Label12.configure(activebackground="#f9f9f9")
        self.Label12.configure(activeforeground="black")
        self.Label12.configure(background="#d9d9d9")
        self.Label12.configure(disabledforeground="#a3a3a3")
        self.Label12.configure(foreground="#000000")
        self.Label12.configure(highlightbackground="#d9d9d9")
        self.Label12.configure(highlightcolor="black")
        self.Label12.configure(text='''Enter IP Address''')

        self.Labelframe5 = tk.LabelFrame(self.TNotebook1_t1_1)
        self.Labelframe5.place(x=10, y=250, height=48, width=420)
        self.Labelframe5.configure(relief='ridge')
        self.Labelframe5.configure(font="-family {Segoe UI} -size 9 -weight bold")
        self.Labelframe5.configure(foreground="black")
        self.Labelframe5.configure(relief="ridge")
        self.Labelframe5.configure(text='''Upload Speed Check''')
        self.Labelframe5.configure(background="#d9d9d9")
        self.Labelframe5.configure(highlightbackground="#d9d9d9")
        self.Labelframe5.configure(highlightcolor="black")

        self.UPLOAD_Entry = tk.Entry(self.Labelframe5)
        self.UPLOAD_Entry.place(x=287, y=16, height=27, width=104
                , bordermode='ignore')
        self.UPLOAD_Entry.configure(background="#c1ffc1")
        self.UPLOAD_Entry.configure(disabledforeground="#a3a3a3")
        self.UPLOAD_Entry.configure(font="TkFixedFont")
        self.UPLOAD_Entry.configure(foreground="#000000")
        self.UPLOAD_Entry.configure(highlightbackground="#d9d9d9")
        self.UPLOAD_Entry.configure(highlightcolor="black")
        self.UPLOAD_Entry.configure(insertbackground="black")
        self.UPLOAD_Entry.configure(justify='center')
        self.UPLOAD_Entry.configure(selectbackground="blue")
        self.UPLOAD_Entry.configure(selectforeground="white")
        self.UPLOAD_Entry.configure(textvariable=self.upload_sp)

        self.Label7 = tk.Label(self.Labelframe5)
        self.Label7.place(x=30, y=20, height=14, width=133, bordermode='ignore')
        self.Label7.configure(activebackground="#f9f9f9")
        self.Label7.configure(activeforeground="black")
        self.Label7.configure(background="#d9d9d9")
        self.Label7.configure(disabledforeground="#a3a3a3")
        self.Label7.configure(foreground="#000000")
        self.Label7.configure(highlightbackground="#d9d9d9")
        self.Label7.configure(highlightcolor="black")
        self.Label7.configure(text='''Enter Upload Speed''')

        self.Labelframe6 = tk.LabelFrame(self.TNotebook1_t1_1)
        self.Labelframe6.place(x=10, y=370, height=48, width=420)
        self.Labelframe6.configure(relief='ridge')
        self.Labelframe6.configure(font="-family {Segoe UI} -size 9 -weight bold")
        self.Labelframe6.configure(foreground="black")
        self.Labelframe6.configure(relief="ridge")
        self.Labelframe6.configure(text='''Latency Check''')
        self.Labelframe6.configure(background="#d9d9d9")
        self.Labelframe6.configure(highlightbackground="#d9d9d9")
        self.Labelframe6.configure(highlightcolor="black")

        self.Label8 = tk.Label(self.Labelframe6)
        self.Label8.place(x=40, y=20, height=14, width=83, bordermode='ignore')
        self.Label8.configure(activebackground="#f9f9f9")
        self.Label8.configure(activeforeground="black")
        self.Label8.configure(background="#d9d9d9")
        self.Label8.configure(disabledforeground="#a3a3a3")
        self.Label8.configure(foreground="#000000")
        self.Label8.configure(highlightbackground="#d9d9d9")
        self.Label8.configure(highlightcolor="black")
        self.Label8.configure(text='''Enter Latency''')

        self.LATENCY_Entry = tk.Entry(self.Labelframe6)
        self.LATENCY_Entry.place(x=287, y=16, height=27, width=104
                , bordermode='ignore')
        self.LATENCY_Entry.configure(background="#c1ffc1")
        self.LATENCY_Entry.configure(disabledforeground="#a3a3a3")
        self.LATENCY_Entry.configure(font="TkFixedFont")
        self.LATENCY_Entry.configure(foreground="#000000")
        self.LATENCY_Entry.configure(highlightbackground="#d9d9d9")
        self.LATENCY_Entry.configure(highlightcolor="black")
        self.LATENCY_Entry.configure(insertbackground="black")
        self.LATENCY_Entry.configure(justify='center')
        self.LATENCY_Entry.configure(selectbackground="blue")
        self.LATENCY_Entry.configure(selectforeground="white")
        self.LATENCY_Entry.configure(textvariable=self.latency)

        self.Labelframe11 = tk.LabelFrame(self.TNotebook1_t1_1)
        self.Labelframe11.place(x=10, y=430, height=48, width=420)
        self.Labelframe11.configure(relief='ridge')
        self.Labelframe11.configure(font="-family {Segoe UI} -size 9 -weight bold")
        self.Labelframe11.configure(foreground="black")
        self.Labelframe11.configure(relief="ridge")
        self.Labelframe11.configure(text='''Timer''')
        self.Labelframe11.configure(background="#d9d9d9")
        self.Labelframe11.configure(highlightbackground="#d9d9d9")
        self.Labelframe11.configure(highlightcolor="black")

        self.Label3 = tk.Label(self.Labelframe11)
        self.Label3.place(x=40, y=20, height=17, width=203, bordermode='ignore')
        self.Label3.configure(activebackground="#f9f9f9")
        self.Label3.configure(activeforeground="black")
        self.Label3.configure(background="#d9d9d9")
        self.Label3.configure(disabledforeground="#a3a3a3")
        self.Label3.configure(foreground="#000000")
        self.Label3.configure(highlightbackground="#d9d9d9")
        self.Label3.configure(highlightcolor="black")
        self.Label3.configure(text='''Enter Check Time Interval in seconds''')

        self.SCHEDULER_Entry = tk.Entry(self.Labelframe11)
        self.SCHEDULER_Entry.place(x=287, y=15, height=27, width=104
                , bordermode='ignore')
        self.SCHEDULER_Entry.configure(background="#c1ffc1")
        self.SCHEDULER_Entry.configure(disabledforeground="#a3a3a3")
        self.SCHEDULER_Entry.configure(font="TkFixedFont")
        self.SCHEDULER_Entry.configure(foreground="#000000")
        self.SCHEDULER_Entry.configure(highlightbackground="#d9d9d9")
        self.SCHEDULER_Entry.configure(highlightcolor="black")
        self.SCHEDULER_Entry.configure(insertbackground="black")
        self.SCHEDULER_Entry.configure(justify='center')
        self.SCHEDULER_Entry.configure(selectbackground="blue")
        self.SCHEDULER_Entry.configure(selectforeground="white")
        self.SCHEDULER_Entry.configure(textvariable=self.seconds)

        self.Labelframe12 = tk.LabelFrame(self.TNotebook1_t1_1)
        self.Labelframe12.place(x=10, y=310, height=48, width=420)
        self.Labelframe12.configure(relief='groove')
        self.Labelframe12.configure(font="-family {Segoe UI} -size 9 -weight bold")
        self.Labelframe12.configure(foreground="black")
        self.Labelframe12.configure(text='''Download Speed Check''')
        self.Labelframe12.configure(background="#d9d9d9")
        self.Labelframe12.configure(highlightbackground="#d9d9d9")
        self.Labelframe12.configure(highlightcolor="black")

        self.Label13 = tk.Label(self.Labelframe12)
        self.Label13.place(x=40, y=20, height=14, width=133, bordermode='ignore')

        self.Label13.configure(activebackground="#f9f9f9")
        self.Label13.configure(activeforeground="black")
        self.Label13.configure(background="#d9d9d9")
        self.Label13.configure(disabledforeground="#a3a3a3")
        self.Label13.configure(foreground="#000000")
        self.Label13.configure(highlightbackground="#d9d9d9")
        self.Label13.configure(highlightcolor="black")
        self.Label13.configure(text='''Enter Download Speed''')

        self.DWONLOAD_Entry = tk.Entry(self.Labelframe12)
        self.DWONLOAD_Entry.place(x=287, y=16, height=27, width=104
                , bordermode='ignore')
        self.DWONLOAD_Entry.configure(background="#c1ffc1")
        self.DWONLOAD_Entry.configure(disabledforeground="#a3a3a3")
        self.DWONLOAD_Entry.configure(font="TkFixedFont")
        self.DWONLOAD_Entry.configure(foreground="#000000")
        self.DWONLOAD_Entry.configure(highlightbackground="#d9d9d9")
        self.DWONLOAD_Entry.configure(highlightcolor="black")
        self.DWONLOAD_Entry.configure(insertbackground="black")
        self.DWONLOAD_Entry.configure(justify='center')
        self.DWONLOAD_Entry.configure(selectbackground="blue")
        self.DWONLOAD_Entry.configure(selectforeground="white")
        self.DWONLOAD_Entry.configure(textvariable=self.download_sp)

        self.Labelframe7 = tk.LabelFrame(self.TNotebook1_t2_1)
        self.Labelframe7.place(x=10, y=30, height=64, width=426)
        self.Labelframe7.configure(relief='ridge')
        self.Labelframe7.configure(font="-family {Segoe UI} -size 9 -weight bold")
        self.Labelframe7.configure(foreground="black")
        self.Labelframe7.configure(relief="ridge")
        self.Labelframe7.configure(text='''SMTP''')
        self.Labelframe7.configure(background="#d9d9d9")
        self.Labelframe7.configure(highlightbackground="#d9d9d9")
        self.Labelframe7.configure(highlightcolor="black")

        self.SMTP_Entry = tk.Entry(self.Labelframe7)
        self.SMTP_Entry.place(x=79, y=19, height=30, width=294
                , bordermode='ignore')
        self.SMTP_Entry.configure(background="#c1ffc1")
        self.SMTP_Entry.configure(disabledforeground="#a3a3a3")
        self.SMTP_Entry.configure(font="TkFixedFont")
        self.SMTP_Entry.configure(foreground="#000000")
        self.SMTP_Entry.configure(highlightbackground="#d9d9d9")
        self.SMTP_Entry.configure(highlightcolor="black")
        self.SMTP_Entry.configure(insertbackground="black")
        self.SMTP_Entry.configure(justify='center')
        self.SMTP_Entry.configure(selectbackground="blue")
        self.SMTP_Entry.configure(selectforeground="white")
        self.SMTP_Entry.configure(textvariable=self.smtp)

        self.Labelframe8 = tk.LabelFrame(self.TNotebook1_t2_1)
        self.Labelframe8.place(x=10, y=120, height=64, width=426)
        self.Labelframe8.configure(relief='ridge')
        self.Labelframe8.configure(font="-family {Segoe UI} -size 9 -weight bold")
        self.Labelframe8.configure(foreground="black")
        self.Labelframe8.configure(relief="ridge")
        self.Labelframe8.configure(text='''Sender email address''')
        self.Labelframe8.configure(background="#d9d9d9")
        self.Labelframe8.configure(highlightbackground="#d9d9d9")
        self.Labelframe8.configure(highlightcolor="black")

        self.SenderEmailAdres_Entry = tk.Entry(self.Labelframe8)
        self.SenderEmailAdres_Entry.place(x=79, y=19, height=30, width=294
                , bordermode='ignore')
        self.SenderEmailAdres_Entry.configure(background="#c1ffc1")
        self.SenderEmailAdres_Entry.configure(cursor="")
        self.SenderEmailAdres_Entry.configure(disabledforeground="#a3a3a3")
        self.SenderEmailAdres_Entry.configure(exportselection="0")
        self.SenderEmailAdres_Entry.configure(font="TkFixedFont")
        self.SenderEmailAdres_Entry.configure(foreground="#000000")
        self.SenderEmailAdres_Entry.configure(highlightbackground="#a4ffa4")
        self.SenderEmailAdres_Entry.configure(highlightcolor="#bfffbf")
        self.SenderEmailAdres_Entry.configure(insertbackground="#000000")
        self.SenderEmailAdres_Entry.configure(justify='center')
        self.SenderEmailAdres_Entry.configure(selectbackground="blue")
        self.SenderEmailAdres_Entry.configure(selectforeground="white")
        self.SenderEmailAdres_Entry.configure(textvariable=self.sender_email)

        self.Labelframe9 = tk.LabelFrame(self.TNotebook1_t2_1)
        self.Labelframe9.place(x=10, y=210, height=64, width=426)
        self.Labelframe9.configure(relief='ridge')
        self.Labelframe9.configure(font="-family {Segoe UI} -size 9 -weight bold")
        self.Labelframe9.configure(foreground="black")
        self.Labelframe9.configure(relief="ridge")
        self.Labelframe9.configure(text='''Sender's Password''')
        self.Labelframe9.configure(background="#d9d9d9")
        self.Labelframe9.configure(highlightbackground="#d9d9d9")
        self.Labelframe9.configure(highlightcolor="black")

        self.SenderPWD_Entry = tk.Entry(self.Labelframe9)
        self.SenderPWD_Entry.place(x=79, y=19, height=30, width=294
                , bordermode='ignore')
        self.SenderPWD_Entry.configure(background="#c1ffc1")
        self.SenderPWD_Entry.configure(cursor="")
        self.SenderPWD_Entry.configure(disabledforeground="#a3a3a3")
        self.SenderPWD_Entry.configure(exportselection="0")
        self.SenderPWD_Entry.configure(font="TkFixedFont")
        self.SenderPWD_Entry.configure(foreground="#000000")
        self.SenderPWD_Entry.configure(highlightbackground="#a4ffa4")
        self.SenderPWD_Entry.configure(highlightcolor="#bfffbf")
        self.SenderPWD_Entry.configure(insertbackground="#000000")
        self.SenderPWD_Entry.configure(justify='center')
        self.SenderPWD_Entry.configure(selectbackground="blue")
        self.SenderPWD_Entry.configure(selectforeground="white")
        self.SenderPWD_Entry.configure(show="*")
        self.SenderPWD_Entry.configure(textvariable=self.sender_pwd)

        self.Labelframe10 = tk.LabelFrame(self.TNotebook1_t2_1)
        self.Labelframe10.place(x=10, y=300, height=64, width=426)
        self.Labelframe10.configure(relief='ridge')
        self.Labelframe10.configure(font="-family {Segoe UI} -size 9 -weight bold")
        self.Labelframe10.configure(foreground="black")
        self.Labelframe10.configure(relief="ridge")
        self.Labelframe10.configure(text='''Receiver email address''')
        self.Labelframe10.configure(background="#d9d9d9")
        self.Labelframe10.configure(highlightbackground="#d9d9d9")
        self.Labelframe10.configure(highlightcolor="black")

        self.ReceiverEmailAdres_Entry = tk.Entry(self.Labelframe10)
        self.ReceiverEmailAdres_Entry.place(x=79, y=19, height=30, width=294
                , bordermode='ignore')
        self.ReceiverEmailAdres_Entry.configure(background="#c1ffc1")
        self.ReceiverEmailAdres_Entry.configure(cursor="")
        self.ReceiverEmailAdres_Entry.configure(disabledforeground="#a3a3a3")
        self.ReceiverEmailAdres_Entry.configure(exportselection="0")
        self.ReceiverEmailAdres_Entry.configure(font="TkFixedFont")
        self.ReceiverEmailAdres_Entry.configure(foreground="#000000")
        self.ReceiverEmailAdres_Entry.configure(highlightbackground="#a4ffa4")
        self.ReceiverEmailAdres_Entry.configure(highlightcolor="#bfffbf")
        self.ReceiverEmailAdres_Entry.configure(insertbackground="#000000")
        self.ReceiverEmailAdres_Entry.configure(justify='center')
        self.ReceiverEmailAdres_Entry.configure(selectbackground="blue")
        self.ReceiverEmailAdres_Entry.configure(selectforeground="white")
        self.ReceiverEmailAdres_Entry.configure(textvariable=self.receiver_email)

        
        self.StartTask_Button = tk.Button(self.TNotebook1_t2_1)
        self.StartTask_Button.place(x=40, y=390, height=34, width=356)
        self.StartTask_Button.configure(activebackground="#bfffbf")
        self.StartTask_Button.configure(activeforeground="#000000")
        self.StartTask_Button.configure(background="#d9d9d9")
        self.StartTask_Button.configure(disabledforeground="#a3a3a3")
        self.StartTask_Button.configure(font="-family {Segoe UI} -size 9 -weight bold")
        self.StartTask_Button.configure(foreground="#000000")
        self.StartTask_Button.configure(highlightbackground="#d9d9d9")
        self.StartTask_Button.configure(highlightcolor="black")
        self.StartTask_Button.configure(pady="0")
        self.StartTask_Button.configure(command=self._resetbutton())


        self.TNotebook2 = ttk.Notebook(self.TNotebook1_t3_1)
        self.TNotebook2.place(x=0, y=10, height=475, width=420)
        self.TNotebook2.configure(takefocus="")
        self.TNotebook2_t1_1 = tk.Frame(self.TNotebook2)
        self.TNotebook2.add(self.TNotebook2_t1_1, padding=3)
        self.TNotebook2.tab(0, text="System Preferences", compound="left", underline="-1")
        self.TNotebook2_t1_1.configure(background="#d9d9d9")
        self.TNotebook2_t1_1.configure(highlightbackground="#d9d9d9")
        self.TNotebook2_t1_1.configure(highlightcolor="black")
        self.TNotebook2_t2_1 = tk.Frame(self.TNotebook2)
        self.TNotebook2.add(self.TNotebook2_t2_1, padding=3)
        self.TNotebook2.tab(1, text="Email Preferences", compound="left", underline="-1")
        self.TNotebook2_t2_1.configure(background="#d9d9d9")
        self.TNotebook2_t2_1.configure(highlightbackground="#d9d9d9")
        self.TNotebook2_t2_1.configure(highlightcolor="black")
        self.TNotebook2_t3_1 = tk.Frame(self.TNotebook2)
        self.TNotebook2.add(self.TNotebook2_t3_1, padding=3)
        self.TNotebook2.tab(2, text="License",compound="left",underline="-1",)
        self.TNotebook2_t3_1.configure(background="#d9d9d9")
        self.TNotebook2_t3_1.configure(highlightbackground="#d9d9d9")
        self.TNotebook2_t3_1.configure(highlightcolor="black")
    
        self.SysPref_Scrolledtext = ScrolledText(self.TNotebook2_t1_1)
        self.SysPref_Scrolledtext.place(x=0, y=19, height=423, width=405)
        self.SysPref_Scrolledtext.configure(background="white")
        self.SysPref_Scrolledtext.configure(font="TkTextFont")
        self.SysPref_Scrolledtext.configure(foreground="black")
        self.SysPref_Scrolledtext.configure(highlightbackground="#d9d9d9")
        self.SysPref_Scrolledtext.configure(highlightcolor="black")
        self.SysPref_Scrolledtext.configure(insertbackground="black")
        self.SysPref_Scrolledtext.configure(insertborderwidth="3")
        self.SysPref_Scrolledtext.configure(selectbackground="blue")
        self.SysPref_Scrolledtext.configure(selectforeground="white")
        self.SysPref_Scrolledtext.configure(wrap='none')
        self.SysPref_Scrolledtext.insert(tk.END,'''
        
        System Preferences Inputs


        •  CPU

        What is CPU? 

        Central Processing Unit or CPU is a small but mighty computer chip found on top of the motherboard in your PC. It’s placed into the CPU socket with its pins facing down. A small lever keeps it secure. 
        CPUs generate a lot of heat, even when running for a short amount of time. Due to this thermal activity, the CPU is usually attached to a heat sink with a fan located right on top of it. In most cases, these two components will arrive bundled if you buy a CPU. 
        In Windows, CPU is monitored using percentage unit measurement. 

        What should I input in CPU tab? 

        Simply input the CPU usage percentage allowed so if the software detects higher percentage than input, you will be notified by a screen pop-up and an email alert will be automatically sent. As an example, let’s say you do not allow more than 50% CPU usage, simply in CPU tab input 50. 

        •  RAM 

        What is RAM? 

        Random-access memory or RAM is a form of computer memory that can be read and changed in any order, typically used to store working data and machine code. A random-access memory device allows data items to be read or written in almost the same amount of time irrespective of the physical location of data inside the memory. 

        What should I input in RAM tab? 

        Let’s say your computer or server has 32GB RAM and in normal state, it does not consume more than 20GB as an example so if it’s consuming more, it means something wrong. To receive an alert of RAM exceeding 20GB, simply input 20.

        •  Storage 

        What is storage? 

        Computer data storage is a technology consisting of computer components and recording media that are used to retain digital data. It is a core function and fundamental component of computers. The central processing unit (CPU) of a computer is what manipulates data by performing computations.
        In Windows, storage is monitored using percentage unit measurement.

        What should I input in Storage tab?

        Sure, you don’t want your server or computer exceed 80% of its storage without getting notified, so simply input 80, as an example.

        •  Ping / Reachability Check 

        What is Ping or IP Reachability?\	

        Ping is a computer network utility used to test the reachability of a host (which could be server, computer, smartphone, surveillance cam, basically any online device) on an Internet Protocol network.

        What should I input in Ping / Reachability Check?

        Enter the IP address of the host you need to check its reachability in loop.

        As an example: 8.8.8.8 which is Google Public DNS.

        •  Upload Speed Check

        What is Upload Speed?

        Upload speed is the number of bytes per second you can send. For a normal ADSL subscription, usually the upload speed is around 1.5 Mbps.

        What should I input in Upload Speed Check tab?

        For example, let’s say you want to get notified as Upload Speed drops under 1 Mbps, simply input 1.

        •  Download Speed Check

        What is Download Speed?

        Download speed is the rate your connection receives data.

        What should I input in Download Speed Check tab?

        If you have for example 20 Mbps Download Speed and you need to be notified as it drops under 15 Mbps, then input 15.

        •  Latency Check

        What is Latency?

        Network latency is the term used to indicate any kind of delay that happens in data communication over a network. In other words, it is the time that for example an email needs to travel to its final destination. The best latency rate is around 35 MS and the worst is 100 MS or more. (MS means milliseconds)

        What should I input in Latency Check?

        As explained, if latency goes over 100 MS, your internet will be very slow and most of your requests will be answered by Request Timed Out which will have crucial impact on your servers performance.

        As an example, to receive instant alert for latency over 35 MS, input 35.

        •  Timer

        What is Timer?

        It is the time interval in seconds in which all checks will be executed in loop.

        What should I input?

        Let’s say, you need to execute all checks every 10 seconds. Simply input 10.
        
        
        
        •  Start

        What does Start button do?

        Once you click on Start, System WATCHDOG will start monitoring your computer resources and watch over your computer or server. After each time interval (seconds), If one or more condition(s) are not met, you will get screen pop-up notification and an automated email will be sent to the receiver using sender’s smtp server address, email address and password.

        •  What does Stop button do?

        If you need to update your inputs or you don’t want to keep System WATCHDOG running, simply click on Stop.

        •  Why after clicking on Stop, I still getting po-up notifications and alerting emails?

        When you click on Stop, System WTACHDOG will be stopped after finishing the running threads or the running tasks, so it’s a very normal behavior. ''')

        self.SysPref_Scrolledtext.configure(state='disabled')

        self.EmailPref_Scrolledtext = ScrolledText(self.TNotebook2_t2_1)
        self.EmailPref_Scrolledtext.place(x=0, y=19, height=423, width=405)
        self.EmailPref_Scrolledtext.configure(background="white")
        self.EmailPref_Scrolledtext.configure(font="TkTextFont")
        self.EmailPref_Scrolledtext.configure(foreground="black")
        self.EmailPref_Scrolledtext.configure(highlightbackground="#d9d9d9")
        self.EmailPref_Scrolledtext.configure(highlightcolor="black")
        self.EmailPref_Scrolledtext.configure(insertbackground="black")
        self.EmailPref_Scrolledtext.configure(insertborderwidth="3")
        self.EmailPref_Scrolledtext.configure(selectbackground="blue")
        self.EmailPref_Scrolledtext.configure(selectforeground="white")
        self.EmailPref_Scrolledtext.configure(wrap="none")
        self.EmailPref_Scrolledtext.insert(tk.END, '''

        •  SMTP

        What is SMTP?

        SMTP or The Simple Mail Transfer Protocol is a communication protocol for electronic mail transmission.

        What should I input in SMTP tab?

        If you are using Outlook than your SMTP is smtp-mail.outlook.com, for Gmail it’s smtp.gmail.com, else ask your email service provider to acquire its SMTP server address.

        •  Sender Email Address

        Input your email address

        •  Sender’s Password

        Input your password.

        Important Note: You will not receive automated emails alerts if you are using 2-factor authentication.

        Best Suggestion: I suggest to register new email address for this purpose only so if someone breaks through, he/she will only fInd System Automated Emails Alerts only.

        •  Receiver Email Address

        Input the receiver’s email address. 
        Hint: It could be the sender’s email address as well.''')

        self.EmailPref_Scrolledtext.configure(state='disabled')

        self.License_Scrolledtext = ScrolledText(self.TNotebook2_t3_1)
        self.License_Scrolledtext.place(x=0, y=19, height=423, width=405)
        self.License_Scrolledtext.configure(background="white")
        self.License_Scrolledtext.configure(font="TkTextFont")
        self.License_Scrolledtext.configure(foreground="black")
        self.License_Scrolledtext.configure(highlightbackground="#d9d9d9")
        self.License_Scrolledtext.configure(highlightcolor="black")
        self.License_Scrolledtext.configure(insertbackground="black")
        self.License_Scrolledtext.configure(insertborderwidth="3")
        self.License_Scrolledtext.configure(selectbackground="blue")
        self.License_Scrolledtext.configure(selectforeground="white")
        self.License_Scrolledtext.configure(wrap="none")
        self.License_Scrolledtext.insert(tk.END, ''' 
        GNU AFFERO GENERAL PUBLIC LICENSE
        Version 3, 19 November 2007

        Copyright (C) 2007 Free Software Foundation, Inc. <https://fsf.org/>
        Everyone is permitted to copy and distribute verbatim copies
        of this license document, but changing it is not allowed.

                            Preamble

        The GNU Affero General Public License is a free, copyleft license for
        software and other kinds of works, specifically designed to ensure
        cooperation with the community in the case of network server software.

        The licenses for most software and other practical works are designed
        to take away your freedom to share and change the works.  By contrast,
        our General Public Licenses are intended to guarantee your freedom to
        share and change all versions of a program--to make sure it remains free
        software for all its users.

        When we speak of free software, we are referring to freedom, not
        price.  Our General Public Licenses are designed to make sure that you
        have the freedom to distribute copies of free software (and charge for
        them if you wish), that you receive source code or can get it if you
        want it, that you can change the software or use pieces of it in new
        free programs, and that you know you can do these things.

        Developers that use our General Public Licenses protect your rights
        with two steps: (1) assert copyright on the software, and (2) offer
        you this License which gives you legal permission to copy, distribute
        and/or modify the software.

        A secondary benefit of defending all users' freedom is that
        improvements made in alternate versions of the program, if they
        receive widespread use, become available for other developers to
        incorporate.  Many developers of free software are heartened and
        encouraged by the resulting cooperation.  However, in the case of
        software used on network servers, this result may fail to come about.
        The GNU General Public License permits making a modified version and
        letting the public access it on a server without ever releasing its
        source code to the public.

        The GNU Affero General Public License is designed specifically to
        ensure that, in such cases, the modified source code becomes available
        to the community.  It requires the operator of a network server to
        provide the source code of the modified version running there to the
        users of that server.  Therefore, public use of a modified version, on
        a publicly accessible server, gives the public access to the source
        code of the modified version.

        An older license, called the Affero General Public License and
        published by Affero, was designed to accomplish similar goals.  This is
        a different license, not a version of the Affero GPL, but Affero has
        released a new version of the Affero GPL which permits relicensing under
        this license.

        The precise terms and conditions for copying, distribution and
        modification follow.

                       TERMS AND CONDITIONS

        0. Definitions.

        "This License" refers to version 3 of the GNU Affero General Public License.

        "Copyright" also means copyright-like laws that apply to other kinds of
        works, such as semiconductor masks.

        "The Program" refers to any copyrightable work licensed under this
        License.  Each licensee is addressed as "you".  "Licensees" and
        "recipients" may be individuals or organizations.

        To "modify" a work means to copy from or adapt all or part of the work
        in a fashion requiring copyright permission, other than the making of an
        exact copy.  The resulting work is called a "modified version" of the
        earlier work or a work "based on" the earlier work.

        A "covered work" means either the unmodified Program or a work based
        on the Program.

        To "propagate" a work means to do anything with it that, without
        permission, would make you directly or secondarily liable for
        infringement under applicable copyright law, except executing it on a
        computer or modifying a private copy.  Propagation includes copying,
        distribution (with or without modification), making available to the
        public, and in some countries other activities as well.

        To "convey" a work means any kind of propagation that enables other
        parties to make or receive copies.  Mere interaction with a user through
        a computer network, with no transfer of a copy, is not conveying.

        An interactive user interface displays "Appropriate Legal Notices"
        to the extent that it includes a convenient and prominently visible
        feature that (1) displays an appropriate copyright notice, and (2)
        tells the user that there is no warranty for the work (except to the
        extent that warranties are provided), that licensees may convey the
        work under this License, and how to view a copy of this License.  If
        the interface presents a list of user commands or options, such as a
        menu, a prominent item in the list meets this criterion.

        1. Source Code.

        The "source code" for a work means the preferred form of the work
        for making modifications to it.  "Object code" means any non-source
        form of a work.

        A "Standard Interface" means an interface that either is an official
        standard defined by a recognized standards body, or, in the case of
        interfaces specified for a particular programming language, one that
        is widely used among developers working in that language.

        The "System Libraries" of an executable work include anything, other
        than the work as a whole, that (a) is included in the normal form of
        packaging a Major Component, but which is not part of that Major
        Component, and (b) serves only to enable use of the work with that
        Major Component, or to implement a Standard Interface for which an
        implementation is available to the public in source code form.  A
        "Major Component", in this context, means a major essential component
        (kernel, window system, and so on) of the specific operating system
        (if any) on which the executable work runs, or a compiler used to
        produce the work, or an object code interpreter used to run it.

        The "Corresponding Source" for a work in object code form means all
        the source code needed to generate, install, and (for an executable
        work) run the object code and to modify the work, including scripts to
        control those activities.  However, it does not include the work's
        System Libraries, or general-purpose tools or generally available free
        programs which are used unmodified in performing those activities but
        which are not part of the work.  For example, Corresponding Source
        includes interface definition files associated with source files for
        the work, and the source code for shared libraries and dynamically
        linked subprograms that the work is specifically designed to require,
        such as by intimate data communication or control flow between those
        subprograms and other parts of the work.

        The Corresponding Source need not include anything that users
        can regenerate automatically from other parts of the Corresponding
        Source.

        The Corresponding Source for a work in source code form is that
        same work.

        2. Basic Permissions.

        All rights granted under this License are granted for the term of
        copyright on the Program, and are irrevocable provided the stated
        conditions are met.  This License explicitly affirms your unlimited
        permission to run the unmodified Program.  The output from running a
        covered work is covered by this License only if the output, given its
        content, constitutes a covered work.  This License acknowledges your
        rights of fair use or other equivalent, as provided by copyright law.

        You may make, run and propagate covered works that you do not
        convey, without conditions so long as your license otherwise remains
        in force.  You may convey covered works to others for the sole purpose
        of having them make modifications exclusively for you, or provide you
        with facilities for running those works, provided that you comply with
        the terms of this License in conveying all material for which you do
        not control copyright.  Those thus making or running the covered works
        for you must do so exclusively on your behalf, under your direction
        and control, on terms that prohibit them from making any copies of
        your copyrighted material outside their relationship with you.

        Conveying under any other circumstances is permitted solely under
        the conditions stated below.  Sublicensing is not allowed; section 10
        makes it unnecessary.

        3. Protecting Users' Legal Rights From Anti-Circumvention Law.

        No covered work shall be deemed part of an effective technological
        measure under any applicable law fulfilling obligations under article
        11 of the WIPO copyright treaty adopted on 20 December 1996, or
        similar laws prohibiting or restricting circumvention of such
        measures.

        When you convey a covered work, you waive any legal power to forbid
        circumvention of technological measures to the extent such circumvention
        is effected by exercising rights under this License with respect to
        the covered work, and you disclaim any intention to limit operation or
        modification of the work as a means of enforcing, against the work's
        users, your or third parties' legal rights to forbid circumvention of
        technological measures.

        4. Conveying Verbatim Copies.

        You may convey verbatim copies of the Program's source code as you
        receive it, in any medium, provided that you conspicuously and
        appropriately publish on each copy an appropriate copyright notice;
        keep intact all notices stating that this License and any
        non-permissive terms added in accord with section 7 apply to the code;
        keep intact all notices of the absence of any warranty; and give all
        recipients a copy of this License along with the Program.

        You may charge any price or no price for each copy that you convey,
        and you may offer support or warranty protection for a fee.

        5. Conveying Modified Source Versions.

        You may convey a work based on the Program, or the modifications to
        produce it from the Program, in the form of source code under the
        terms of section 4, provided that you also meet all of these conditions:

            a) The work must carry prominent notices stating that you modified
            it, and giving a relevant date.

            b) The work must carry prominent notices stating that it is
            released under this License and any conditions added under section
            7.  This requirement modifies the requirement in section 4 to
            "keep intact all notices".

            c) You must license the entire work, as a whole, under this
            License to anyone who comes into possession of a copy.  This
            License will therefore apply, along with any applicable section 7
            additional terms, to the whole of the work, and all its parts,
            regardless of how they are packaged.  This License gives no
            permission to license the work in any other way, but it does not
            invalidate such permission if you have separately received it.

            d) If the work has interactive user interfaces, each must display
            Appropriate Legal Notices; however, if the Program has interactive
            interfaces that do not display Appropriate Legal Notices, your
            work need not make them do so.

        A compilation of a covered work with other separate and independent
        works, which are not by their nature extensions of the covered work,
        and which are not combined with it such as to form a larger program,
        in or on a volume of a storage or distribution medium, is called an
        "aggregate" if the compilation and its resulting copyright are not
        used to limit the access or legal rights of the compilation's users
        beyond what the individual works permit.  Inclusion of a covered work
        in an aggregate does not cause this License to apply to the other
        parts of the aggregate.

        6. Conveying Non-Source Forms.

        You may convey a covered work in object code form under the terms
        of sections 4 and 5, provided that you also convey the
        machine-readable Corresponding Source under the terms of this License,
        in one of these ways:

            a) Convey the object code in, or embodied in, a physical product
            (including a physical distribution medium), accompanied by the
            Corresponding Source fixed on a durable physical medium
            customarily used for software interchange.

            b) Convey the object code in, or embodied in, a physical product
            (including a physical distribution medium), accompanied by a
            written offer, valid for at least three years and valid for as
            long as you offer spare parts or customer support for that product
            model, to give anyone who possesses the object code either (1) a
            copy of the Corresponding Source for all the software in the
            product that is covered by this License, on a durable physical
            medium customarily used for software interchange, for a price no
            more than your reasonable cost of physically performing this
            conveying of source, or (2) access to copy the
            Corresponding Source from a network server at no charge.

            c) Convey individual copies of the object code with a copy of the
            written offer to provide the Corresponding Source.  This
            alternative is allowed only occasionally and noncommercially, and
            only if you received the object code with such an offer, in accord
            with subsection 6b.

            d) Convey the object code by offering access from a designated
            place (gratis or for a charge), and offer equivalent access to the
            Corresponding Source in the same way through the same place at no
            further charge.  You need not require recipients to copy the
            Corresponding Source along with the object code.  If the place to
            copy the object code is a network server, the Corresponding Source
            may be on a different server (operated by you or a third party)
            that supports equivalent copying facilities, provided you maintain
            clear directions next to the object code saying where to find the
            Corresponding Source.  Regardless of what server hosts the
            Corresponding Source, you remain obligated to ensure that it is
            available for as long as needed to satisfy these requirements.

            e) Convey the object code using peer-to-peer transmission, provided
            you inform other peers where the object code and Corresponding
            Source of the work are being offered to the general public at no
            charge under subsection 6d.

        A separable portion of the object code, whose source code is excluded
        from the Corresponding Source as a System Library, need not be
        included in conveying the object code work.

        A "User Product" is either (1) a "consumer product", which means any
        tangible personal property which is normally used for personal, family,
        or household purposes, or (2) anything designed or sold for incorporation
        into a dwelling.  In determining whether a product is a consumer product,
        doubtful cases shall be resolved in favor of coverage.  For a particular
        product received by a particular user, "normally used" refers to a
        typical or common use of that class of product, regardless of the status
        of the particular user or of the way in which the particular user
        actually uses, or expects or is expected to use, the product.  A product
        is a consumer product regardless of whether the product has substantial
        commercial, industrial or non-consumer uses, unless such uses represent
        the only significant mode of use of the product.

        "Installation Information" for a User Product means any methods,
        procedures, authorization keys, or other information required to install
        and execute modified versions of a covered work in that User Product from
        a modified version of its Corresponding Source.  The information must
        suffice to ensure that the continued functioning of the modified object
        code is in no case prevented or interfered with solely because
        modification has been made.

        If you convey an object code work under this section in, or with, or
        specifically for use in, a User Product, and the conveying occurs as
        part of a transaction in which the right of possession and use of the
        User Product is transferred to the recipient in perpetuity or for a
        fixed term (regardless of how the transaction is characterized), the
        Corresponding Source conveyed under this section must be accompanied
        by the Installation Information.  But this requirement does not apply
        if neither you nor any third party retains the ability to install
        modified object code on the User Product (for example, the work has
        been installed in ROM).

        The requirement to provide Installation Information does not include a
        requirement to continue to provide support service, warranty, or updates
        for a work that has been modified or installed by the recipient, or for
        the User Product in which it has been modified or installed.  Access to a
        network may be denied when the modification itself materially and
        adversely affects the operation of the network or violates the rules and
        protocols for communication across the network.

        Corresponding Source conveyed, and Installation Information provided,
        in accord with this section must be in a format that is publicly
        documented (and with an implementation available to the public in
        source code form), and must require no special password or key for
        unpacking, reading or copying.

        7. Additional Terms.

        "Additional permissions" are terms that supplement the terms of this
        License by making exceptions from one or more of its conditions.
        Additional permissions that are applicable to the entire Program shall
        be treated as though they were included in this License, to the extent
        that they are valid under applicable law.  If additional permissions
        apply only to part of the Program, that part may be used separately
        under those permissions, but the entire Program remains governed by
        this License without regard to the additional permissions.

        When you convey a copy of a covered work, you may at your option
        remove any additional permissions from that copy, or from any part of
        it.  (Additional permissions may be written to require their own
        removal in certain cases when you modify the work.)  You may place
        additional permissions on material, added by you to a covered work,
        for which you have or can give appropriate copyright permission.

        Notwithstanding any other provision of this License, for material you
        add to a covered work, you may (if authorized by the copyright holders of
        that material) supplement the terms of this License with terms:

            a) Disclaiming warranty or limiting liability differently from the
            terms of sections 15 and 16 of this License; or

            b) Requiring preservation of specified reasonable legal notices or
            author attributions in that material or in the Appropriate Legal
            Notices displayed by works containing it; or

            c) Prohibiting misrepresentation of the origin of that material, or
            requiring that modified versions of such material be marked in
            reasonable ways as different from the original version; or

            d) Limiting the use for publicity purposes of names of licensors or
            authors of the material; or

            e) Declining to grant rights under trademark law for use of some
            trade names, trademarks, or service marks; or

            f) Requiring indemnification of licensors and authors of that
            material by anyone who conveys the material (or modified versions of
            it) with contractual assumptions of liability to the recipient, for
            any liability that these contractual assumptions directly impose on
            those licensors and authors.

        All other non-permissive additional terms are considered "further
        restrictions" within the meaning of section 10.  If the Program as you
        received it, or any part of it, contains a notice stating that it is
        governed by this License along with a term that is a further
        restriction, you may remove that term.  If a license document contains
        a further restriction but permits relicensing or conveying under this
        License, you may add to a covered work material governed by the terms
        of that license document, provided that the further restriction does
        not survive such relicensing or conveying.

        If you add terms to a covered work in accord with this section, you
        must place, in the relevant source files, a statement of the
        additional terms that apply to those files, or a notice indicating
        where to find the applicable terms.

        Additional terms, permissive or non-permissive, may be stated in the
        form of a separately written license, or stated as exceptions;
        the above requirements apply either way.

        8. Termination.

        You may not propagate or modify a covered work except as expressly
        provided under this License.  Any attempt otherwise to propagate or
        modify it is void, and will automatically terminate your rights under
        this License (including any patent licenses granted under the third
        paragraph of section 11).

        However, if you cease all violation of this License, then your
        license from a particular copyright holder is reinstated (a)
        provisionally, unless and until the copyright holder explicitly and
        finally terminates your license, and (b) permanently, if the copyright
        holder fails to notify you of the violation by some reasonable means
        prior to 60 days after the cessation.

        Moreover, your license from a particular copyright holder is
        reinstated permanently if the copyright holder notifies you of the
        violation by some reasonable means, this is the first time you have
        received notice of violation of this License (for any work) from that
        copyright holder, and you cure the violation prior to 30 days after
        your receipt of the notice.

        Termination of your rights under this section does not terminate the
        licenses of parties who have received copies or rights from you under
        this License.  If your rights have been terminated and not permanently
        reinstated, you do not qualify to receive new licenses for the same
        material under section 10.

        9. Acceptance Not Required for Having Copies.

        You are not required to accept this License in order to receive or
        run a copy of the Program.  Ancillary propagation of a covered work
        occurring solely as a consequence of using peer-to-peer transmission
        to receive a copy likewise does not require acceptance.  However,
        nothing other than this License grants you permission to propagate or
        modify any covered work.  These actions infringe copyright if you do
        not accept this License.  Therefore, by modifying or propagating a
        covered work, you indicate your acceptance of this License to do so.

        10. Automatic Licensing of Downstream Recipients.

        Each time you convey a covered work, the recipient automatically
        receives a license from the original licensors, to run, modify and
        propagate that work, subject to this License.  You are not responsible
        for enforcing compliance by third parties with this License.

        An "entity transaction" is a transaction transferring control of an
        organization, or substantially all assets of one, or subdividing an
        organization, or merging organizations.  If propagation of a covered
        work results from an entity transaction, each party to that
        transaction who receives a copy of the work also receives whatever
        licenses to the work the party's predecessor in interest had or could
        give under the previous paragraph, plus a right to possession of the
        Corresponding Source of the work from the predecessor in interest, if
        the predecessor has it or can get it with reasonable efforts.

        You may not impose any further restrictions on the exercise of the
        rights granted or affirmed under this License.  For example, you may
        not impose a license fee, royalty, or other charge for exercise of
        rights granted under this License, and you may not initiate litigation
        (including a cross-claim or counterclaim in a lawsuit) alleging that
        any patent claim is infringed by making, using, selling, offering for
        sale, or importing the Program or any portion of it.

        11. Patents.

        A "contributor" is a copyright holder who authorizes use under this
        License of the Program or a work on which the Program is based.  The
        work thus licensed is called the contributor's "contributor version".

        A contributor's "essential patent claims" are all patent claims
        owned or controlled by the contributor, whether already acquired or
        hereafter acquired, that would be infringed by some manner, permitted
        by this License, of making, using, or selling its contributor version,
        but do not include claims that would be infringed only as a
        consequence of further modification of the contributor version.  For
        purposes of this definition, "control" includes the right to grant
        patent sublicenses in a manner consistent with the requirements of
        this License.

        Each contributor grants you a non-exclusive, worldwide, royalty-free
        patent license under the contributor's essential patent claims, to
        make, use, sell, offer for sale, import and otherwise run, modify and
        propagate the contents of its contributor version.

        In the following three paragraphs, a "patent license" is any express
        agreement or commitment, however denominated, not to enforce a patent
        (such as an express permission to practice a patent or covenant not to
        sue for patent infringement).  To "grant" such a patent license to a
        party means to make such an agreement or commitment not to enforce a
        patent against the party.

        If you convey a covered work, knowingly relying on a patent license,
        and the Corresponding Source of the work is not available for anyone
        to copy, free of charge and under the terms of this License, through a
        publicly available network server or other readily accessible means,
        then you must either (1) cause the Corresponding Source to be so
        available, or (2) arrange to deprive yourself of the benefit of the
        patent license for this particular work, or (3) arrange, in a manner
        consistent with the requirements of this License, to extend the patent
        license to downstream recipients.  "Knowingly relying" means you have
        actual knowledge that, but for the patent license, your conveying the
        covered work in a country, or your recipient's use of the covered work
        in a country, would infringe one or more identifiable patents in that
        country that you have reason to believe are valid.

        If, pursuant to or in connection with a single transaction or
        arrangement, you convey, or propagate by procuring conveyance of, a
        covered work, and grant a patent license to some of the parties
        receiving the covered work authorizing them to use, propagate, modify
        or convey a specific copy of the covered work, then the patent license
        you grant is automatically extended to all recipients of the covered
        work and works based on it.

        A patent license is "discriminatory" if it does not include within
        the scope of its coverage, prohibits the exercise of, or is
        conditioned on the non-exercise of one or more of the rights that are
        specifically granted under this License.  You may not convey a covered
        work if you are a party to an arrangement with a third party that is
        in the business of distributing software, under which you make payment
        to the third party based on the extent of your activity of conveying
        the work, and under which the third party grants, to any of the
        parties who would receive the covered work from you, a discriminatory
        patent license (a) in connection with copies of the covered work
        conveyed by you (or copies made from those copies), or (b) primarily
        for and in connection with specific products or compilations that
        contain the covered work, unless you entered into that arrangement,
        or that patent license was granted, prior to 28 March 2007.

        Nothing in this License shall be construed as excluding or limiting
        any implied license or other defenses to infringement that may
        otherwise be available to you under applicable patent law.

        12. No Surrender of Others' Freedom.

        If conditions are imposed on you (whether by court order, agreement or
        otherwise) that contradict the conditions of this License, they do not
        excuse you from the conditions of this License.  If you cannot convey a
        covered work so as to satisfy simultaneously your obligations under this
        License and any other pertinent obligations, then as a consequence you may
        not convey it at all.  For example, if you agree to terms that obligate you
        to collect a royalty for further conveying from those to whom you convey
        the Program, the only way you could satisfy both those terms and this
        License would be to refrain entirely from conveying the Program.

        13. Remote Network Interaction; Use with the GNU General Public License.

        Notwithstanding any other provision of this License, if you modify the
        Program, your modified version must prominently offer all users
        interacting with it remotely through a computer network (if your version
        supports such interaction) an opportunity to receive the Corresponding
        Source of your version by providing access to the Corresponding Source
        from a network server at no charge, through some standard or customary
        means of facilitating copying of software.  This Corresponding Source
        shall include the Corresponding Source for any work covered by version 3
        of the GNU General Public License that is incorporated pursuant to the
        following paragraph.

        Notwithstanding any other provision of this License, you have
        permission to link or combine any covered work with a work licensed
        under version 3 of the GNU General Public License into a single
        combined work, and to convey the resulting work.  The terms of this
        License will continue to apply to the part which is the covered work,
        but the work with which it is combined will remain governed by version
        3 of the GNU General Public License.

        14. Revised Versions of this License.

        The Free Software Foundation may publish revised and/or new versions of
        the GNU Affero General Public License from time to time.  Such new versions
        will be similar in spirit to the present version, but may differ in detail to
        address new problems or concerns.

        Each version is given a distinguishing version number.  If the
        Program specifies that a certain numbered version of the GNU Affero General
        Public License "or any later version" applies to it, you have the
        option of following the terms and conditions either of that numbered
        version or of any later version published by the Free Software
        Foundation.  If the Program does not specify a version number of the
        GNU Affero General Public License, you may choose any version ever published
        by the Free Software Foundation.

        If the Program specifies that a proxy can decide which future
        versions of the GNU Affero General Public License can be used, that proxy's
        public statement of acceptance of a version permanently authorizes you
        to choose that version for the Program.

        Later license versions may give you additional or different
        permissions.  However, no additional obligations are imposed on any
        author or copyright holder as a result of your choosing to follow a
        later version.

        15. Disclaimer of Warranty.

        THERE IS NO WARRANTY FOR THE PROGRAM, TO THE EXTENT PERMITTED BY
        APPLICABLE LAW.  EXCEPT WHEN OTHERWISE STATED IN WRITING THE COPYRIGHT
        HOLDERS AND/OR OTHER PARTIES PROVIDE THE PROGRAM "AS IS" WITHOUT WARRANTY
        OF ANY KIND, EITHER EXPRESSED OR IMPLIED, INCLUDING, BUT NOT LIMITED TO,
        THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR
        PURPOSE.  THE ENTIRE RISK AS TO THE QUALITY AND PERFORMANCE OF THE PROGRAM
        IS WITH YOU.  SHOULD THE PROGRAM PROVE DEFECTIVE, YOU ASSUME THE COST OF
        ALL NECESSARY SERVICING, REPAIR OR CORRECTION.

        16. Limitation of Liability.

        IN NO EVENT UNLESS REQUIRED BY APPLICABLE LAW OR AGREED TO IN WRITING
        WILL ANY COPYRIGHT HOLDER, OR ANY OTHER PARTY WHO MODIFIES AND/OR CONVEYS
        THE PROGRAM AS PERMITTED ABOVE, BE LIABLE TO YOU FOR DAMAGES, INCLUDING ANY
        GENERAL, SPECIAL, INCIDENTAL OR CONSEQUENTIAL DAMAGES ARISING OUT OF THE
        USE OR INABILITY TO USE THE PROGRAM (INCLUDING BUT NOT LIMITED TO LOSS OF
        DATA OR DATA BEING RENDERED INACCURATE OR LOSSES SUSTAINED BY YOU OR THIRD
        PARTIES OR A FAILURE OF THE PROGRAM TO OPERATE WITH ANY OTHER PROGRAMS),
        EVEN IF SUCH HOLDER OR OTHER PARTY HAS BEEN ADVISED OF THE POSSIBILITY OF
        SUCH DAMAGES.

        17. Interpretation of Sections 15 and 16.

        If the disclaimer of warranty and limitation of liability provided
        above cannot be given local legal effect according to their terms,
        reviewing courts shall apply local law that most closely approximates
        an absolute waiver of all civil liability in connection with the
        Program, unless a warranty or assumption of liability accompanies a
        copy of the Program in return for a fee.

                            END OF TERMS AND CONDITIONS

                    How to Apply These Terms to Your New Programs

        If you develop a new program, and you want it to be of the greatest
        possible use to the public, the best way to achieve this is to make it
        free software which everyone can redistribute and change under these terms.

        To do so, attach the following notices to the program.  It is safest
        to attach them to the start of each source file to most effectively
        state the exclusion of warranty; and each file should have at least
        the "copyright" line and a pointer to where the full notice is found.

            <one line to give the program's name and a brief idea of what it does.>
            Copyright (C) <year>  <name of author>

            This program is free software: you can redistribute it and/or modify
            it under the terms of the GNU Affero General Public License as published
            by the Free Software Foundation, either version 3 of the License, or
            (at your option) any later version.

            This program is distributed in the hope that it will be useful,
            but WITHOUT ANY WARRANTY; without even the implied warranty of
            MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
            GNU Affero General Public License for more details.

            You should have received a copy of the GNU Affero General Public License
            along with this program.  If not, see <https://www.gnu.org/licenses/>.

        Also add information on how to contact you by electronic and paper mail.

        If your software can interact with users remotely through a computer
        network, you should also make sure that it provides a way for users to
        get its source.  For example, if your program is a web application, its
        interface could display a "Source" link that leads users to an archive
        of the code.  There are many ways you could offer source, and different
        solutions will be better for different programs; see section 13 for the
        specific requirements.

        You should also get your employer (if you work as a programmer) or school,
        if any, to sign a "copyright disclaimer" for the program, if necessary.
        For more information on this, and how to apply and follow the GNU AGPL, see
        <https://www.gnu.org/licenses/>. ''')

        self.License_Scrolledtext.configure(state='disabled')

        self.Label1 = tk.Label(self.TNotebook1_t4_1)
        self.Label1.place(x=30, y=45, height=23, width=162)
        self.Label1.configure(activebackground="#f9f9f9")
        self.Label1.configure(activeforeground="black")
        self.Label1.configure(background="#d9d9d9")
        self.Label1.configure(disabledforeground="#a3a3a3")
        self.Label1.configure(font="-family {Segoe UI} -size 9 -weight bold")
        self.Label1.configure(foreground="#000000")
        self.Label1.configure(highlightbackground="#d9d9d9")
        self.Label1.configure(highlightcolor="black")
        self.Label1.configure(text='''Follow me in Linkedin''')

        self.LINKEDIN_Button = tk.Button(self.TNotebook1_t4_1)
        self.LINKEDIN_Button.place(x=268, y=45, height=24, width=157)
        self.LINKEDIN_Button.configure(activebackground="#bfffbf")
        self.LINKEDIN_Button.configure(activeforeground="#000000")
        self.LINKEDIN_Button.configure(background="#d9d9d9")
        self.LINKEDIN_Button.configure(disabledforeground="#a3a3a3")
        self.LINKEDIN_Button.configure(foreground="#000000")
        self.LINKEDIN_Button.configure(highlightbackground="#d9d9d9")
        self.LINKEDIN_Button.configure(highlightcolor="black")
        self.LINKEDIN_Button.configure(pady="0")
        self.LINKEDIN_Button.configure(text='''Linkedin''')
        self.LINKEDIN_Button.configure(command=lambda:self.linked_in())

        self.Label2 = tk.Label(self.TNotebook1_t4_1)
        self.Label2.place(x=30, y=157, height=23, width=162)
        self.Label2.configure(activebackground="#f9f9f9")
        self.Label2.configure(activeforeground="black")
        self.Label2.configure(background="#d9d9d9")
        self.Label2.configure(disabledforeground="#a3a3a3")
        self.Label2.configure(font="-family {Segoe UI} -size 9 -weight bold")
        self.Label2.configure(foreground="#000000")
        self.Label2.configure(highlightbackground="#d9d9d9")
        self.Label2.configure(highlightcolor="black")
        self.Label2.configure(text='''Follow me in Github''')

        self.GITHUB_Button = tk.Button(self.TNotebook1_t4_1)
        self.GITHUB_Button.place(x=268, y=157, height=24, width=157)
        self.GITHUB_Button.configure(activebackground="#bfffbf")
        self.GITHUB_Button.configure(activeforeground="#000000")
        self.GITHUB_Button.configure(background="#d9d9d9")
        self.GITHUB_Button.configure(disabledforeground="#a3a3a3")
        self.GITHUB_Button.configure(foreground="#000000")
        self.GITHUB_Button.configure(highlightbackground="#d9d9d9")
        self.GITHUB_Button.configure(highlightcolor="black")
        self.GITHUB_Button.configure(pady="0")
        self.GITHUB_Button.configure(text='''Github''')
        self.GITHUB_Button.configure(command=lambda:self.git_hub())

        self.DONATE_Button = tk.Button(self.TNotebook1_t4_1)
        self.DONATE_Button.place(x=20, y=267, height=24, width=407)
        self.DONATE_Button.configure(activebackground="#bfffbf")
        self.DONATE_Button.configure(activeforeground="#000000")
        self.DONATE_Button.configure(background="#d9d9d9")
        self.DONATE_Button.configure(disabledforeground="#a3a3a3")
        self.DONATE_Button.configure(foreground="#000000")
        self.DONATE_Button.configure(highlightbackground="#d9d9d9")
        self.DONATE_Button.configure(highlightcolor="black")
        self.DONATE_Button.configure(pady="0")
        self.DONATE_Button.configure(text='''Donate PayPal''')
        self.DONATE_Button.configure(command=lambda:self.paypal())

        self.Label10 = tk.Label(root)
        self.Label10.place(x=40, y=10, height=21, width=424)
        self.Label10.configure(activebackground="#f9f9f9")
        self.Label10.configure(activeforeground="black")
        self.Label10.configure(background="#d9d9d9")
        self.Label10.configure(disabledforeground="#a3a3a3")
        self.Label10.configure(font="-family {Segoe UI Black} -size 12 -weight bold")
        self.Label10.configure(foreground="#000000")
        self.Label10.configure(highlightbackground="#d9d9d9")
        self.Label10.configure(highlightcolor="black")
        self.Label10.configure(text='''SYSTEM  WATCHDOG''')

        self.Label9 = tk.Label(root)
        self.Label9.place(x=90, y=590, height=21, width=304)
        self.Label9.configure(activebackground="#f9f9f9")
        self.Label9.configure(activeforeground="black")
        self.Label9.configure(background="#d9d9d9")
        self.Label9.configure(disabledforeground="#a3a3a3")
        self.Label9.configure(font="-family {Segoe UI} -size 10 -weight bold")
        self.Label9.configure(foreground="#000000")
        self.Label9.configure(highlightbackground="#d9d9d9")
        self.Label9.configure(highlightcolor="black")
        self.Label9.configure(text='''By iTech ® 2020''')


    def health_check(self):
        t = ToastNotifier()
        def cpu_check():
            cpu_usage = psutil.cpu_percent() 
            return cpu_usage < self.cpu.get()
        
        def available_memory_check():
            available = psutil.virtual_memory().available
            available_in_GB = available / 1000000000
            return available_in_GB >= self.ram.get()

        def disc_space_check():  
            disk_usage = shutil.disk_usage("/")
            disk_total = disk_usage.total
            disk_free = disk_usage.used
            threshold = disk_free / disk_total * 100
            return threshold > self.storage.get()

        def ping_ip():

            p = self.Ping.get()

            l = list(ping(p))

            return str(l[0]).startswith('Reply')
        
        def upload_speed():
            s = speedtest.Speedtest()
            upload_s = round(s.upload()/1000000, 2)
            return upload_s >= self.upload_sp.get()
        
        def download_speed():
            s = speedtest.Speedtest() 
            download_s = round(s.download()/1000000, 2)
            return download_s >= self.download_sp.get()
        

        def latency_check():
            s = speedtest.Speedtest()
            s.get_best_server()
            return s.results.ping <= self.latency.get()

        def generate_email(sender, receiver, subject, body): 

            message = email.message.EmailMessage()
            message['Subject'] = subject
            message['From'] = sender
            message['To'] = receiver
            message.set_content(body)

            return message
                
        def send_email(package):
            mail_server = smtplib.SMTP(self.smtp.get())
            mail_server.starttls() 
            mail_server.login(self.sender_email.get(), self.sender_pwd.get()) 
            mail_server.send_message(package)
            mail_server.quit()

    
        def email_warning(warning):
            
            sender = self.sender_email.get()
            receiver = self.receiver_email.get()
            subject = warning
            body = "Alert! Check Your System ASAP!"
            message = generate_email(sender, receiver, subject, body)
            send_email(message)

            
        if not cpu_check():
            t.show_toast("Warning!", "CPU Usage is greater than " + ' ' + str(self.cpu.get()) + '!', icon_path='C:/Users/user/folder/alarm.ico', duration=5) 
            subject = 'Alert! - CPU Usage is greater than ' + ' ' + str(self.cpu.get()) + '!'
            email_warning(subject)

        if not disc_space_check():
            t.show_toast("Warning!", "Available disk space is less than " + ' ' + str(self.storage.get()) + '!', icon_path='C:/Users/user/folder/alarm.ico', duration=5)
            subject = "Alert! - Available disk space is less than " + ' ' + str(self.storage.get()) + '!'
            email_warning(subject)

        if not available_memory_check():
            t.show_toast("Warning!", "Available memory is less than " + ' ' + str(self.ram.get()) + ' GB' + '!', icon_path='C:/Users/user/folder/alarm.ico', duration=5)
            subject = "Alert! - Available memory is less than " + ' ' + str(self.ram.get()) + ' GB' + '!'
            email_warning(subject)

        if not upload_speed():
            t.show_toast("Warning!", "Low upload speed! Upload speed is less than " + ' ' + str(self.upload_sp.get()) + ' MB' + '!', icon_path='C:/Users/user/folder/alarm.ico', duration=5)
            subject = "Alert! - Low upload speed! Upload speed is less than "  + ' ' + str(self.upload_sp.get()) + ' MB' + '!'
            email_warning(subject)

        if not download_speed():
            t.show_toast("Warning!", "Low download speed! Download speed is less than " + ' ' + str(self.download_sp.get()) + ' MB' + '!', icon_path='C:/Users/user/folder/alarm.ico', duration=5)
            subject = "Alert! - Low download speed! Download speed is less than " + ' ' + str(self.download_sp.get()) + ' MB' + '!'
            email_warning(subject)


        if not latency_check():
            t.show_toast("Warning!", "High Latency! Latency is higher than " + ' ' + str(self.latency.get()) + ' MS' + '!', icon_path='C:/Users/user/folder/alarm.ico', duration=5)
            subject = "Alert! - High Latency! Latency is higher than " + ' ' + str(self.latency.get()) + ' MS' + '!'
            email_warning(subject)

        if not ping_ip():
            t.show_toast("Warning!", "The" + " " + str(self.Ping.get()) + " " + "IP Address is unreachable, Request timed out!", icon_path='C:/Users/user/folder/alarm.ico', duration=5)
            subject = "Alert! - Unreachable IP, Request timed out!" + ' ' + str(self.Ping.get()) + '!'
            email_warning(subject)

       

    def _resetbutton(self):
        self.running = False
        self.StartTask_Button.config(text="Start", command=self.startthread)

    def startthread(self):
        
        self.running = True
        newthread = threading.Thread(target=self.StartTask)
        newthread.start()
        self.StartTask_Button.configure(text="Stop", command=self._resetbutton)

    def StartTask(self):
        t = ToastNotifier()
        if self.cpu.get() == 0 or self.ram.get() == 0 or self.storage.get() == 0 or self.upload_sp.get() == 0 or self.download_sp.get() == 0 or self.latency.get() == 0:
            t.show_toast("Inputs must be greater than 0!", icon_path='C:/Users/user/folder/alarm.ico', duration=10)
            self._resetbutton()
        if self.Ping.get().startswith('0') or self.Ping.get().startswith('255'):
            t.show_toast("IP address could not start with 0 or 255!", icon_path='C:/Users/user/folder/alarm.ico', duration=10)
            self._resetbutton()
        if self.seconds.get() < 20:
            t.show_toast("Timer must be equal to or greater than 20!", icon_path='C:/Users/user/folder/alarm.ico', duration=10)
            self._resetbutton()
        else:
            while self.running:
                try:
                    self.health_check()
                    time.sleep(self.seconds.get()) 

                except smtplib.SMTPAuthenticationError:
                    t.show_toast("Wrong email or password! check your credentails and try again.", icon_path='C:/Users/user/folder/alarm.ico', duration=10)
                    self._resetbutton()
                    
                except smtplib.SMTPConnectError:
                    t.show_toast("Connection error! Please try again.", icon_path='C:/Users/user/folder/alarm.ico', duration=10)
                    self._resetbutton()
                    
                except smtplib.SMTPException:
                    t.show_toast("Unexpected error occured! Please try again.", icon_path='C:/Users/user/folder/alarm.ico', duration=10)
                    self._resetbutton()
                

    def linked_in(self):
        url='https://linkedin.com/in/cyber-services'
        webbrowser.open_new_tab(url)

    def git_hub(self):
        url='https://github.com/IT-Support-L2'
        webbrowser.open_new_tab(url)

    def paypal(self):
        url='https://www.paypal.com/paypalme/HamdiBouaskar'
        webbrowser.open_new_tab(url)

class AutoScroll(object):
    def __init__(self, master):
        try:
            vsb = ttk.Scrollbar(master, orient='vertical', command=self.yview)
        except:
            pass
        hsb = ttk.Scrollbar(master, orient='horizontal', command=self.xview)
        try:
            self.configure(yscrollcommand=self._autoscroll(vsb))
        except:
            pass
        self.configure(xscrollcommand=self._autoscroll(hsb))
        self.grid(column=0, row=0, sticky='nsew')
        try:
            vsb.grid(column=1, row=0, sticky='ns')
        except:
            pass
        hsb.grid(column=0, row=1, sticky='ew')
        master.grid_columnconfigure(0, weight=1)
        master.grid_rowconfigure(0, weight=1)
        methods = tk.Pack.__dict__.keys() | tk.Grid.__dict__.keys() \
                  | tk.Place.__dict__.keys()
        for meth in methods:
            if meth[0] != '_' and meth not in ('config', 'configure'):
                setattr(self, meth, getattr(master, meth))

    @staticmethod
    def _autoscroll(sbar):
        def wrapped(first, last):
            first, last = float(first), float(last)
            if first <= 0 and last >= 1:
                sbar.grid_remove()
            else:
                sbar.grid()
            sbar.set(first, last)
        return wrapped

    def __str__(self):
        return str(self.master)

def _create_container(func):
    
    def wrapped(cls, master, **kw):
        container = ttk.Frame(master)
        container.bind('<Enter>', lambda e: _bound_to_mousewheel(e, container))
        container.bind('<Leave>', lambda e: _unbound_to_mousewheel(e, container))
        return func(cls, container, **kw)
    return wrapped

class ScrolledText(AutoScroll, tk.Text):
    @_create_container
    def __init__(self, master, **kw):
        tk.Text.__init__(self, master, **kw)
        AutoScroll.__init__(self, master)


import platform
def _bound_to_mousewheel(event, widget):
    child = widget.winfo_children()[0]
    if platform.system() == 'Windows' or platform.system() == 'Darwin':
        child.bind_all('<MouseWheel>', lambda e: _on_mousewheel(e, child))
        child.bind_all('<Shift-MouseWheel>', lambda e: _on_shiftmouse(e, child))
    else:
        child.bind_all('<Button-4>', lambda e: _on_mousewheel(e, child))
        child.bind_all('<Button-5>', lambda e: _on_mousewheel(e, child))
        child.bind_all('<Shift-Button-4>', lambda e: _on_shiftmouse(e, child))
        child.bind_all('<Shift-Button-5>', lambda e: _on_shiftmouse(e, child))

def _unbound_to_mousewheel(event, widget):
    if platform.system() == 'Windows' or platform.system() == 'Darwin':
        widget.unbind_all('<MouseWheel>')
        widget.unbind_all('<Shift-MouseWheel>')
    else:
        widget.unbind_all('<Button-4>')
        widget.unbind_all('<Button-5>')
        widget.unbind_all('<Shift-Button-4>')
        widget.unbind_all('<Shift-Button-5>')

def _on_mousewheel(event, widget):
    if platform.system() == 'Windows':
        widget.yview_scroll(-1*int(event.delta/120),'units')
    elif platform.system() == 'Darwin':
        widget.yview_scroll(-1*int(event.delta),'units')
    else:
        if event.num == 4:
            widget.yview_scroll(-1, 'units')
        elif event.num == 5:
            widget.yview_scroll(1, 'units')

def _on_shiftmouse(event, widget):
    if platform.system() == 'Windows':
        widget.xview_scroll(-1*int(event.delta/120), 'units')
    elif platform.system() == 'Darwin':
        widget.xview_scroll(-1*int(event.delta), 'units')
    else:
        if event.num == 4:
            widget.xview_scroll(-1, 'units')
        elif event.num == 5:
            widget.xview_scroll(1, 'units')

if __name__ == "__main__":

    root = tk.Tk()
    app = App(root)
    root.mainloop()
