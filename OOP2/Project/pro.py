from tkinter import*
from PIL import ImageTk
import pymysql
from tkinter import messagebox


class The_Emargency_Lane:
    def __init__(self, root):
        self.root = root
        self.root.title("The Emergency Lane")
        self.root.geometry("1350x750+0+0")

        # ==========Image============

        self.bg_icon = ImageTk.PhotoImage(file="image/bg1.jpg")
        self.user_icon = PhotoImage(file="image/user.png")
        self.pass_icon = PhotoImage(file="image/padlock.png")
        self.logo_icon = PhotoImage(file="image/ambulance.png")

        self.username = StringVar()
        self.pass_ = StringVar()

        bg_lbl = Label(self.root, image=self.bg_icon).pack()

        title = Label(self.root, text="The Emargency Lane",
                      font=("times new roman", 40, "bold"), bg="silver", fg="white", bd=10, relief=GROOVE)
        title.place(x=0, y=0, relwidth=1)

        Login_Frame = Frame(self.root, bg="white")
        Login_Frame.place(x=400, y=150)
        logolbl = Label(Login_Frame,
                        image=self.logo_icon, bd=0).grid(row=0, columnspan=2, pady=20)
        lbluser = Label(Login_Frame, text="Username",
                        image=self.user_icon, compound=LEFT, font=("times new roman", 20, "bold"), bg="white").grid(row=1, column=0, padx=20, pady=10)
        txtuser = Entry(Login_Frame, bd=5, textvariable=self.username, relief=GROOVE,
                        font=("", 15)).grid(row=1, column=1, padx=20)

        lblpass = Label(Login_Frame, text="Password",
                        image=self.pass_icon, compound=LEFT, font=("times new roman", 20, "bold"), bg="white").grid(row=2, column=0, padx=20, pady=10)
        txtpass = Entry(Login_Frame, bd=5, textvariable=self.pass_, relief=GROOVE,
                        font=("", 15)).grid(row=2, column=1, padx=20)

        btn_log_admin = Button(Login_Frame, text="Admin", command=self.admin_window, width=10,
                               font=("times new roman", 14, "bold"), bg="black", fg="white").grid(row=3, pady=10)
        btn_log_traffic = Button(Login_Frame, text="Traffic", command=self.map_window, width=10,
                                 font=("times new roman", 14, "bold"), bg="black", fg="white").grid(row=3, column=1, pady=10)

    def login(self):
        if self.username.get() == "" or self.pass_.get() == "":
            messagebox.showerror(
                "Error", "All fields are required", parent=self.root)
        else:
            try:
                con = pymysql.connect(
                    host="localhost", user="root", password="", database="traffic")
                cur = con.cursor()
                cur.execute("select * from admin where userName=%s and password=%s",
                            (self.username.get(), self.pass_.get()))
                row = cur.fetchone()
                if row == None:
                    messagebox.showerror(
                        "Error", "Invalid USERNAME OR PASSWORD", parent=self.root)
                else:
                    messagebox.showinfo("Welcome", parent=self.root)
                con.close()
            except Exception as es:
                messagebox.showerror(
                    "Error", f"Error Due to: {str(es)}", parent=self.root)

    def admin_window(self):
        self.root.destroy()
        import admin

    def map_window(self):
        self.root.destroy()
        import map


root = Tk()
obj = The_Emargency_Lane(root)
root.mainloop()
