from tkinter import*
from PIL import ImageTk, Image
import pymysql
from tkinter import messagebox
from tkinter import ttk


class admin:
    def __init__(self, root):
        self.root = root
        self.root.title("The Emergency Lane")
        self.root.geometry("1650x800+0+0")

        self.bg_icon = ImageTk.PhotoImage(file="image/bg1.jpg")

        self.location_icon = ImageTk.PhotoImage(file="image/Location1.jpg")

        bg_lbl = Label(self.root, image=self.bg_icon).pack()

        title = Label(self.root, text="Map",
                      font=("times new roman", 40, "bold"), bg="silver", fg="white", bd=10, relief=GROOVE)
        title.place(x=0, y=0, relwidth=1)

        Map_Frame = Frame(self.root, bd=4, relief=RIDGE, bg="crimson")
        Map_Frame.place(x=400, y=150, width=550, height=70)

        Detail_Frame = Frame(self.root, bg="crimson")
        Detail_Frame.place(x=180,
                           y=250, width=950, height=450)

        locationlbl = Label(Detail_Frame, image=self.location_icon, bd=0)
        locationlbl.place(x=0,
                          y=0, width=950, height=450)

        lbl_location = Label(Map_Frame, text="Location", bg="crimson",
                             fg="white", font=("times new roman", 30, "bold"))
        lbl_location.grid(row=1, column=0, pady=5, padx=15, sticky="w")

        txt_location = Entry(Map_Frame, font=(
            "times new roman", 15, "bold"), bd=5, relief=GROOVE)
        txt_location.grid(row=1, column=1, pady=0, padx=20, sticky="w")

        Searchbtn = Button(Map_Frame, text="Search", width=10).grid(
            row=1, column=3, padx=10, pady=0)


root = Tk()
obj = admin(root)
root.mainloop()
