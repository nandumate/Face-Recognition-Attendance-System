from tkinter import *
from tkinter import ttk
import random
from PIL import Image, ImageTk
import os
from main import FaceRecognitionSystem
from time import strftime
from datetime import datetime
from tkinter import messagebox
import mysql.connector


def main():
    win = Tk()
    app = LoginWindow(win)
    win.mainloop()

class LoginWindow:
    def __init__(self, root):
        self.root = root
        self.root.title("Login")
        self.root.geometry("1550x800+0+0")


  # Background image
        img_bg = Image.open(r"C:\Users\nayan\Desktop\Python Projects\Face Recognition System\images\360_F_119115529_mEnw3lGpLdlDkfLgRcVSbFRuVl6sMDty.jpg")
        img_bg = img_bg.resize((1550, 800), Image.Resampling.LANCZOS)
        self.bg = ImageTk.PhotoImage(img_bg)
        lbl_bg = Label(self.root, image=self.bg)
        lbl_bg.place(x=0, y=0, relwidth=1, relheight=1)

        # First image
        img = Image.open(r"C:\Users\nayan\Desktop\Python Projects\Face Recognition System\images\Untitled-design-10-1.jpg")
        img = img.resize((500, 130), Image.Resampling.LANCZOS)
        self.photoimg = ImageTk.PhotoImage(img)
        f_lbl = Label(self.root, image=self.photoimg)
        f_lbl.place(x=0, y=0, width=500, height=130)

        # Second image
        img1 = Image.open(r"C:\Users\nayan\Desktop\Python Projects\Face Recognition System\images\1_LJa3uwoVHFQ-ojw5JgF3nw.png")
        img1 = img1.resize((500, 130), Image.Resampling.LANCZOS)
        self.photoimg1 = ImageTk.PhotoImage(img1)
        f_lbl1 = Label(self.root, image=self.photoimg1)
        f_lbl1.place(x=500, y=0, width=500, height=130)

        # Third image
        img2 = Image.open(r"C:\Users\nayan\Desktop\Python Projects\Face Recognition System\images\AdobeStock_183480624.jpeg")
        img2 = img2.resize((560, 130), Image.Resampling.LANCZOS)
        self.photoimg2 = ImageTk.PhotoImage(img2)
        f_lbl2 = Label(self.root, image=self.photoimg2)
        f_lbl2.place(x=1000, y=0, width=560, height=130)

        # Title
        title_lbl = Label(self.root, text="FACE  RECOGNITION  ATTENDANCE  SYSTEM", font=("times new roman", 35, "bold"), bg="white", fg="red")
        title_lbl.place(x=0, y=130, width=1530, height=45)


        # Frame
        frame = Frame(self.root, bg="black")
        frame.place(x=610, y=170, width=340, height=450)

        # Login icon
        img = Image.open(r"C:\Users\nayan\Desktop\Python Projects\Face Recognition System\images\—Pngtree—3d user icon with transparent_20141366 (1).png")
        img = img.resize((100, 100), Image.Resampling.LANCZOS)
        self.photoimage1 = ImageTk.PhotoImage(img)
        lbl_img = Label(image=self.photoimage1, bg="black", borderwidth=0)
        lbl_img.place(x=730, y=175, width=100, height=100)

        # Get Started label
        get_str = Label(frame, text="Get Started", font=("times new roman", 20, "bold"), fg="white", bg="black")
        get_str.place(x=95, y=100)

        # Username label and entry
        username_lbl = Label(frame, text="Username", font=("times new roman", 15, "bold"), fg="white", bg="black")
        username_lbl.place(x=70, y=155)
        self.txtuser = ttk.Entry(frame, font=("times new roman", 15, "bold"))
        self.txtuser.place(x=40, y=180, width=270)

        # Password label and entry
        password_lbl = Label(frame, text="Password", font=("times new roman", 15, "bold"), fg="white", bg="black")
        password_lbl.place(x=70, y=225)
        self.txtpass = ttk.Entry(frame, font=("times new roman", 15, "bold"))
        self.txtpass.place(x=40, y=250, width=270)

        # Username icon
        img2 = Image.open(r"C:\Users\nayan\Desktop\Python Projects\Face Recognition System\images\—Pngtree—3d user icon with transparent_20141366 (1).png")
        img2 = img2.resize((25, 25), Image.Resampling.LANCZOS)
        self.photoimage2 = ImageTk.PhotoImage(img2)
        lbl_img2 = Label(image=self.photoimage2, bg="black", borderwidth=0)
        lbl_img2.place(x=650, y=323, width=25, height=25)

        # Password icon
        img3 = Image.open(r"C:\Users\nayan\Desktop\Python Projects\Face Recognition System\images\PikPng.com_lock-icon-png_887400.png")
        img3 = img3.resize((25, 25), Image.Resampling.LANCZOS)
        self.photoimage3 = ImageTk.PhotoImage(img3)
        lbl_img3 = Label(image=self.photoimage3, bg="black", borderwidth=0)
        lbl_img3.place(x=650, y=395, width=25, height=25)

        # Login button
        loginbtn = Button(frame, command=self.login, text="Login", font=("times new roman", 15, "bold"), bd=3, relief=RIDGE, fg="white", bg="red", activeforeground="white", activebackground="red")
        loginbtn.place(x=110, y=300, width=120, height=35)

        # Register button
        registerbtn = Button(frame, text="New User Register",command=self.register_window, font=("times new roman", 12, "bold"), bd=3, relief=RIDGE, fg="white", bg="black", activeforeground="white", activebackground="black")
        registerbtn.place(x=20, y=350, width=160, height=35)

        # Forget password button
        forgetpassbtn = Button(frame, text="Forget Password",command=self.forgot_password_window, font=("times new roman", 12, "bold"), bd=3, relief=RIDGE, fg="white", bg="black", activeforeground="white", activebackground="black")
        forgetpassbtn.place(x=20, y=400, width=160, height=35)

    def register_window(self):
        self.new_window = Toplevel(self.root)
        self.app = Register(self.new_window)

    def login(self):
        if self.txtuser.get() == "" or self.txtpass.get() == "":
            messagebox.showerror("Error", "All fields are required")
        elif self.txtuser.get() == "kapu" and self.txtpass.get() == "ashu":
            messagebox.showinfo("Success", "Welcome to codewithkiran channel. Please subscribe to my channel")
        else:
            try:
                conn = mysql.connector.connect(host="localhost", user="root", password="Nandini06@", database="face_recognizer")
                my_cursor = conn.cursor()
                my_cursor.execute("select * from register where email=%s and pass=%s", (
                    self.txtuser.get(),
                    self.txtpass.get()
                ))
                row = my_cursor.fetchone()
                if row == None:
                    messagebox.showerror("Error", "Invalid Username & Password")
                else:
                    open_main = messagebox.askyesno("YesNo", "Access only admin")
                    if open_main > 0:
                        self.new_window = Toplevel(self.root)
                        self.app = FaceRecognitionSystem(self.new_window)
                conn.close()
            except Exception as es:
                messagebox.showerror("Error", f"Due to: {str(es)}")
    
    
    def reset_password(self):
        if self.combo_security_Q.get() == "Select":
            messagebox.showerror("Error", "Select Security Question",parent=self.root2)
        elif self.txt_security.get() == "":
            messagebox.showerror("Error", "Please enter the answer",parent=self.root2)
        elif self.txt_newpass.get() == "":
            messagebox.showerror("Error", "Please enter the new password",parent=self.root2)
        else:
            try:
                conn = mysql.connector.connect(host="localhost", user="root", password="Nandini06@", database="face_recognizer")
                my_cursor = conn.cursor()
                query = "select * from register where email=%s and securityQ=%s and securityA=%s"
                value = (self.txtuser.get(), self.combo_security_Q.get(), self.txt_security.get())
                my_cursor.execute(query, value)
                row = my_cursor.fetchone()
                if row is None:
                    messagebox.showerror("Error", "Please enter the correct answer",parent=self.root2)
                else:
                    query = "update register set pass=%s where email=%s"
                    value = (self.txt_newpass.get(), self.txtuser.get())
                    my_cursor.execute(query, value)

                    conn.commit()
                    conn.close()
                    messagebox.showinfo("Success", "Your password has been reset, please login with new password",parent=self.root2)
                    self.root2.destroy()
            except Exception as es:
                messagebox.showerror("Error", f"Due to: {str(es)}")
    
    
    def forgot_password_window(self):
        if self.txtuser.get() == "":
            messagebox.showerror("Error", "Please enter the email address to reset password")
        else:
            try:
                conn = mysql.connector.connect(host="localhost", user="root", password="Nandini06@", database="face_recognizer")
                my_cursor = conn.cursor()
                query = "select * from register where email=%s"
                value = (self.txtuser.get(),)
                my_cursor.execute(query, value)
                row = my_cursor.fetchone()
                if row is None:
                    messagebox.showerror("Error", "Please enter a valid username")
                else:
                    conn.close()
                    self.root2 = Toplevel()
                    self.root2.title("Forget Password")
                    self.root2.geometry("340x450+610+170")

                    l = Label(self.root2, text="Forget Password", font=("times new roman", 20, "bold"), fg="red", bg="white")
                    l.place(x=0, y=10, relwidth=1)

                    security_Q = Label(self.root2, text="Select Security Question", font=("times new roman", 15, "bold"), bg="white")
                    security_Q.place(x=50, y=80)

                    self.combo_security_Q = ttk.Combobox(self.root2, font=("times new roman", 15, "bold"), state="readonly")
                    self.combo_security_Q["values"] = ("Select", "Your Birth Place", "Your Girlfriend's name", "Your Pet Name") 
                    self.combo_security_Q.place(x=50, y=110, width=250)
                    self.combo_security_Q.current(0)

                    security_A = Label(self.root2, text="Security Answer", font=("times new roman", 15, "bold"), bg="white")
                    security_A.place(x=50, y=150)

                    self.txt_security = ttk.Entry(self.root2, font=("times new roman", 15, "bold"))
                    self.txt_security.place(x=50, y=180, width=250)

                    new_password = Label(self.root2, text="New Password", font=("times new roman", 15, "bold"), bg="white")
                    new_password.place(x=50, y=220)

                    self.txt_newpass = ttk.Entry(self.root2, font=("times new roman", 15, "bold"))
                    self.txt_newpass.place(x=50, y=250, width=250)

                    btn = Button(self.root2, text="Reset", command=self.reset_password, font=("times new roman", 15, "bold"), fg="white", bg="green")
                    btn.place(x=100, y=298)
            except Exception as es:
                messagebox.showerror("Error", f"Due to: {str(es)}")


class Register:
    def __init__(self, root):
        self.root = root
        self.root.title("Register")
        self.root.geometry("1600x900+0+0")

        # Variables
        self.var_fname = StringVar()
        self.var_lname = StringVar()
        self.var_contact = StringVar()
        self.var_email = StringVar()
        self.var_securityQ = StringVar()
        self.var_securityA = StringVar()
        self.var_pass = StringVar()
        self.var_confpass = StringVar()
        self.var_check = IntVar()

        # Background image
        img_bg = Image.open(r"C:\Users\nayan\Desktop\Python Projects\Face Recognition System\images\registration-online-membership-network-internet-business-technology-concept-104512007.webp")
        img_bg = img_bg.resize((1600, 900), Image.Resampling.LANCZOS)
        self.bg = ImageTk.PhotoImage(img_bg)
        bg_lbl = Label(self.root, image=self.bg)
        bg_lbl.place(x=0, y=0, relwidth=1, relheight=1)

        # Left image
        img_left = Image.open(r"C:\Users\nayan\Desktop\Python Projects\Face Recognition System\images\depositphotos_219835454-stock-photo-hand-unrecognizable-man-using-interactive.jpg")
        img_left = img_left.resize((470, 550), Image.Resampling.LANCZOS)
        self.bg1 = ImageTk.PhotoImage(img_left)
        left_lbl = Label(self.root, image=self.bg1)
        left_lbl.place(x=50, y=100, width=470, height=550)

        # Main frame
        frame = Frame(self.root, bg="white")
        frame.place(x=520, y=100, width=800, height=550)

        # Title and subtitle
        register_lbl = Label(frame, text="REGISTER HERE", font=("times new roman", 20, "bold"), fg="green", bg="white")
        register_lbl.place(x=20, y=20)

        # Labels and entry fields
        fname_lbl = Label(frame, text="First Name", font=("times new roman", 15, "bold"), bg="white")
        fname_lbl.place(x=50, y=100)
        self.txt_fname = ttk.Entry(frame, textvariable=self.var_fname, font=("times new roman", 15, "bold"))
        self.txt_fname.place(x=50, y=130, width=250)

        lname_lbl = Label(frame, text="Last Name", font=("times new roman", 15, "bold"), bg="white")
        lname_lbl.place(x=370, y=100)
        self.txt_lname = ttk.Entry(frame, textvariable=self.var_lname, font=("times new roman", 15, "bold"))
        self.txt_lname.place(x=370, y=130, width=250)

        contact_lbl = Label(frame, text="Contact No", font=("times new roman", 15, "bold"), bg="white")
        contact_lbl.place(x=50, y=170)
        self.txt_contact = ttk.Entry(frame, textvariable=self.var_contact, font=("times new roman", 15, "bold"))
        self.txt_contact.place(x=50, y=200, width=250)

        email_lbl = Label(frame, text="Email", font=("times new roman", 15, "bold"), bg="white")
        email_lbl.place(x=370, y=170)
        self.txt_email = ttk.Entry(frame, textvariable=self.var_email, font=("times new roman", 15, "bold"))
        self.txt_email.place(x=370, y=200, width=250)

        security_q_lbl = Label(frame, text="Select Security Question", font=("times new roman", 15, "bold"), bg="white")
        security_q_lbl.place(x=50, y=240)
        self.combo_security_q = ttk.Combobox(frame, textvariable=self.var_securityQ, font=("times new roman", 15, "bold"), state="readonly")
        self.combo_security_q["values"] = ("Select", "Your Birth Place", "Your Girlfriend's name", "Your Pet Name")
        self.combo_security_q.place(x=50, y=270, width=250)
        self.combo_security_q.current(0)

        security_a_lbl = Label(frame, text="Security Answer", font=("times new roman", 15, "bold"), bg="white")
        security_a_lbl.place(x=370, y=240)
        self.txt_security_a = ttk.Entry(frame, textvariable=self.var_securityA, font=("times new roman", 15, "bold"))
        self.txt_security_a.place(x=370, y=270, width=250)

        pswd_lbl = Label(frame, text="Password", font=("times new roman", 15, "bold"), bg="white")
        pswd_lbl.place(x=50, y=310)
        self.txt_pswd = ttk.Entry(frame, textvariable=self.var_pass, font=("times new roman", 15, "bold"))
        self.txt_pswd.place(x=50, y=340, width=250)

        confirm_pswd_lbl = Label(frame, text="Confirm Password", font=("times new roman", 15, "bold"), bg="white")
        confirm_pswd_lbl.place(x=370, y=310)
        self.txt_confirm_pswd = ttk.Entry(frame, textvariable=self.var_confpass, font=("times new roman", 15, "bold"))
        self.txt_confirm_pswd.place(x=370, y=340, width=250)

        checkbtn = Checkbutton(frame, text="I Agree The Terms & Conditions", variable=self.var_check, font=("times new roman", 12, "bold"), onvalue=1, offvalue=0)
        checkbtn.place(x=50, y=380)

        # Register button
        registerbtn = Button(frame, command=self.register_data, text="Register", font=("times new roman", 15, "bold"), bd=3, relief=RIDGE, fg="white", bg="green", activeforeground="white", activebackground="green")
        registerbtn.place(x=50, y=420, width=200, height=45)

        # Login button
        loginbtn = Button(frame, text="Login", font=("times new roman", 15, "bold"), bd=3, relief=RIDGE, fg="white", bg="blue", activeforeground="white", activebackground="blue")
        loginbtn.place(x=330, y=420, width=200, height=45)

    def register_data(self):
        if self.var_fname.get() == "" or self.var_email.get() == "" or self.var_securityQ.get() == "Select":
            messagebox.showerror("Error", "All fields are required")
        elif self.var_pass.get() != self.var_confpass.get():
            messagebox.showerror("Error", "Password & Confirm Password must be same")
        elif self.var_check.get() == 0:
            messagebox.showerror("Error", "Please agree to our terms and conditions")
        else:
            try:
                conn = mysql.connector.connect(host="localhost", user="root", password="Nandini06@", database="face_recognizer")
                my_cursor = conn.cursor()
                query = "select * from register where email=%s"
                value = (self.var_email.get(),)
                my_cursor.execute(query, value)
                row = my_cursor.fetchone()
                if row != None:
                    messagebox.showerror("Error", "User already exists, please try another email")
                else:
                    my_cursor.execute("insert into register values(%s, %s, %s, %s, %s, %s, %s)", (
                        self.var_fname.get(),
                        self.var_lname.get(),
                        self.var_contact.get(),
                        self.var_email.get(),
                        self.var_securityQ.get(),
                        self.var_securityA.get(),
                        self.var_pass.get()
                    ))
                    conn.commit()
                    conn.close()
                    messagebox.showinfo("Success", "Register Successfully")
            except Exception as es:
                messagebox.showerror("Error", f"Due to: {str(es)}")





if __name__ == "__main__":
    main()