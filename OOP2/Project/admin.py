from tkinter import *
from PIL import ImageTk
import pymysql
from tkinter import messagebox
from tkinter import ttk


class admin:
    def __init__(self, root):
        self.root = root
        self.root.title("The Emergency Lane")
        self.root.geometry("1650x800+0+0")

        self.bg_icon = ImageTk.PhotoImage(file="image/bg1.jpg")

        bg_lbl = Label(self.root, image=self.bg_icon).pack()
        title = Label(self.root, text="Admin Panel",
                      font=("times new roman", 40, "bold"), bg="silver", fg="white", bd=10, relief=GROOVE)
        title.place(x=0, y=0, relwidth=1)

# ========variable======

        self.ID = StringVar()
        self.name = StringVar()
        self.mail = StringVar()
        self.pass_ = StringVar()

# ==========admin frame===============

        Admin_Frame = Frame(self.root, bd=4, relief=RIDGE, bg="crimson")
        Admin_Frame.place(x=40, y=180, width=550, height=450)

        # a_title = Label(Admin_Frame, text="ID :", bg="crimson",
        # fg="white", font=("times new roman", 30, "bold"))
        # a_title.grid(row=20, columnspan=2, pady=20)
        lbl_id = Label(Admin_Frame, text="ID :", bg="crimson",
                       fg="white", font=("times new roman", 30, "bold"))
        lbl_id.grid(row=1, column=0, pady=10, padx=20, sticky="w")

        txt_id = Entry(Admin_Frame, textvariable=self.ID, font=(
            "times new roman", 15, "bold"), bd=5, relief=GROOVE)
        txt_id.grid(row=1, column=1, pady=10, padx=20, sticky="w")

        lbl_userName = Label(Admin_Frame, text="Name :", bg="crimson",
                             fg="white", font=("times new roman", 30, "bold"))
        lbl_userName.grid(row=2, column=0, pady=10, padx=20, sticky="w")

        txt_userName = Entry(Admin_Frame, textvariable=self.name, font=(
            "times new roman", 15, "bold"), bd=5, relief=GROOVE)
        txt_userName.grid(row=2, column=1, pady=10, padx=20, sticky="w")

        lbl_mail = Label(Admin_Frame, text="Mail :", bg="crimson",
                         fg="white", font=("times new roman", 30, "bold"))
        lbl_mail.grid(row=3, column=0, pady=10, padx=20, sticky="w")

        txt_mail = Entry(Admin_Frame, textvariable=self.mail, font=(
            "times new roman", 15, "bold"), bd=5, relief=GROOVE)
        txt_mail.grid(row=3, column=1, pady=10, padx=20, sticky="w")

        lbl_password = Label(Admin_Frame, text="Password :", bg="crimson",
                             fg="white", font=("times new roman", 30, "bold"))
        lbl_password.grid(row=4, column=0, pady=10, padx=20, sticky="w")

        txt_password = Entry(Admin_Frame, textvariable=self.pass_, font=(
            "times new roman", 15, "bold"), bd=5, relief=GROOVE)
        txt_password.grid(row=4, column=1, pady=10, padx=20, sticky="w")

        # =========button===========
        btn_Frame = Frame(Admin_Frame, bd=4, relief=RIDGE, bg="crimson")
        btn_Frame.place(x=65, y=320, width=410)

        Addbtn = Button(btn_Frame, text="Add", width=10, command=self.add_info).grid(
            row=0, column=0, padx=10, pady=10)
        Updatebtn = Button(btn_Frame, text="Update", width=10, command=self.update_data).grid(
            row=0, column=1, padx=10, pady=10)
        Deletebtn = Button(btn_Frame, text="Delete", width=10, command=self.delete_data).grid(
            row=0, column=2, padx=10, pady=10)
        Removebtn = Button(btn_Frame, text="Remove", width=10, command=self.remove).grid(
            row=0, column=3, padx=10, pady=10)
# =======Detail frame==============

        Detail_Frame = Frame(self.root, bd=4, relief=RIDGE, bg="crimson")
        Detail_Frame.place(x=650, y=180, width=690, height=450)

        d_title = Label(Detail_Frame, text="INFORMATION", bg="crimson",
                        fg="white", font=("times new roman", 25, "bold"))
        d_title.grid(row=0, columnspan=2, pady=5, padx=220)

        # ==========table frame=======

        Table_Frame = Frame(Detail_Frame, bd=4, relief=RIDGE, bg="crimson")
        Table_Frame.place(x=10, y=50, width=660, height=390)

        scroll_x = Scrollbar(Table_Frame, orient=HORIZONTAL)
        scroll_y = Scrollbar(Table_Frame, orient=VERTICAL)
        self.Admin_table = ttk.Treeview(Table_Frame, columns=(
            "ID", "name", "mail", "password"), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.Admin_table.xview)
        scroll_y.config(command=self.Admin_table.yview)

        self.Admin_table.heading("ID", text="ID")
        self.Admin_table.heading("name", text="Name")
        self.Admin_table.heading("mail", text="Mail")
        self.Admin_table.heading("password", text="Password")

        self.Admin_table['show'] = 'headings'
        self.Admin_table.column("ID", width=130)
        self.Admin_table.column("name", width=180)
        self.Admin_table.column("mail", width=180)
        self.Admin_table.column("password", width=180)

        self.Admin_table.pack(fill=BOTH, expand=1)
        self.Admin_table.bind("<ButtonRelease-1>", self.get_coursor)
        self.fetch_data()

    def add_info(self):
        con = pymysql.connect(host="localhost", user="root",
                              password="", database="traffic")
        cur = con.cursor()
        cur.execute("insert into people values(%s,%s,%s,%s)", (self.ID.get(),
                                                               self.name.get(), self.mail.get(), self.pass_.get()))

        con.commit()
        self.fetch_data()
        self.remove()
        con.close()

    def fetch_data(self):
        con = pymysql.connect(host="localhost", user="root",
                              password="", database="traffic")
        cur = con.cursor()
        cur.execute("select * from people")
        rows = cur.fetchall()
        if len(rows) != 0:
            self.Admin_table.delete(*self.Admin_table.get_children())
            for row in rows:
                self.Admin_table.insert('', END, values=row)
            con.commit()
        con.close()

    def remove(self):
        self.ID.set("")
        self.name.set("")
        self.mail.set("")
        self.pass_.set("")

    def get_coursor(self, ev):
        coursor_row = self.Admin_table.focus()
        contents = self.Admin_table.item(coursor_row)
        row = contents['values']
        self.ID.set(row[0])
        self.name.set(row[1])
        self.mail.set(row[2])
        self.pass_.set(row[3])

    def update_data(self):
        con = pymysql.connect(host="localhost", user="root",
                              password="", database="traffic")
        cur = con.cursor()
        cur.execute("update people set name=%s,mail=%s,pass=%s where ID=%s",
                    (self.name.get(), self.mail.get(), self.pass_.get(), self.ID.get()))

        con.commit()
        self.fetch_data()
        self.remove()
        con.close()

    def delete_data(self):
        con = pymysql.connect(host="localhost", user="root",
                              password="", database="traffic")
        cur = con.cursor()
        cur.execute("delete from people where ID=%s", self.ID.get())
        con.commit()
        con.close()
        self.fetch_data()
        self.remove()


root = Tk()
obj = admin(root)
root.mainloop()
