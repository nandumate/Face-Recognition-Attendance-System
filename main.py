from tkinter import *
from tkinter import ttk
import tkinter
from PIL import Image, ImageTk
from student import Student
import os
from time import strftime
from datetime import datetime
from train import Train
from face_recognition import FaceRecognition
from attendance import Attendance
from developer import Developer
#from help import Help
from chatbot import ChatBot

class FaceRecognitionSystem:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")

        # First image
        img = Image.open(r"C:\Users\nayan\Desktop\Python Projects\Face Recognition System\images\Best-Facial-Recognition-Software.webp")
        img = img.resize((500, 130), Image.ANTIALIAS)
        self.photoimg = ImageTk.PhotoImage(img)
        f_lbl = Label(self.root, image=self.photoimg)
        f_lbl.place(x=0, y=0, width=500, height=130)

        # Second image
        img1 = Image.open(r"C:\Users\nayan\Desktop\Python Projects\Face Recognition System\images\1_LJa3uwoVHFQ-ojw5JgF3nw.png")
        img1 = img1.resize((500, 130), Image.ANTIALIAS)
        self.photoimg1 = ImageTk.PhotoImage(img1)
        f_lbl1 = Label(self.root, image=self.photoimg1)
        f_lbl1.place(x=500, y=0, width=500, height=130)

        # Third image
        img2 = Image.open(r"C:\Users\nayan\Desktop\Python Projects\Face Recognition System\images\iStock-925574662-scaled.jpg")
        img2 = img2.resize((560, 130), Image.ANTIALIAS)
        self.photoimg2 = ImageTk.PhotoImage(img2)
        f_lbl2 = Label(self.root, image=self.photoimg2)
        f_lbl2.place(x=1000, y=0, width=560, height=130)

        # Background image
        img3 = Image.open(r"C:\Users\nayan\Desktop\Python Projects\Face Recognition System\images\1023386.jpg")
        img3 = img3.resize((1530, 710), Image.ANTIALIAS)
        self.photoimg3 = ImageTk.PhotoImage(img3)
        bg_img = Label(self.root, image=self.photoimg3)
        bg_img.place(x=0, y=130, width=1530, height=710)

        # Title
        title_lbl = Label(bg_img, text="FACE RECOGNITION ATTENDANCE SYSTEM SOFTWARE", font=("times new roman", 35, "bold"), bg="white", fg="red")
        title_lbl.place(x=0, y=0, width=1530, height=45)

        # Time
        def time():
            string = strftime('%H:%M:%S %p')
            lbl.config(text=string)
            lbl.after(1000, time)

        lbl = Label(title_lbl, font=('times new roman', 12, 'bold'), background='white', foreground='blue')
        lbl.place(x=5, y=0, width=110, height=50)
        time()

        # Student button
        img4 = Image.open(r"C:\Users\nayan\Desktop\Python Projects\Face Recognition System\images\happy-young-university-students-studying-600nw-522554425.webp")
        img4 = img4.resize((220, 220), Image.ANTIALIAS)
        self.photoimg4 = ImageTk.PhotoImage(img4)
        b1 = Button(bg_img, image=self.photoimg4, command=self.student_details, cursor="hand2")
        b1.place(x=200, y=100, width=220, height=220)
        b1_1 = Button(bg_img, text="Student Details", command=self.student_details, cursor="hand2", font=("times new roman", 15, "bold"), bg="darkblue", fg="white")
        b1_1.place(x=200, y=300, width=220, height=40)

        # Face Detector button
        img5 = Image.open(r"C:\Users\nayan\Desktop\Python Projects\Face Recognition System\images\istockphoto-1445021758-612x612.jpg")
        img5 = img5.resize((220, 220), Image.ANTIALIAS)
        self.photoimg5 = ImageTk.PhotoImage(img5)
        b2 = Button(bg_img, image=self.photoimg5, cursor="hand2", command=self.face_data)
        b2.place(x=500, y=100, width=220, height=220)
        b2_1 = Button(bg_img, text="Face Detector", cursor="hand2", command=self.face_data, font=("times new roman", 15, "bold"), bg="darkblue", fg="white")
        b2_1.place(x=500, y=300, width=220, height=40)

        # Attendance button
        img6 = Image.open(r"C:\Users\nayan\Desktop\Python Projects\Face Recognition System\images\blog-–-462-1.webp")
        img6 = img6.resize((220, 220), Image.Resampling.LANCZOS)
        self.photoimg6 = ImageTk.PhotoImage(img6)
        b3 = Button(bg_img, image=self.photoimg6, cursor="hand2", command=self.attendance_data)
        b3.place(x=800, y=100, width=220, height=220)
        b3_1 = Button(bg_img, text="Attendance", cursor="hand2", command=self.attendance_data, font=("times new roman", 15, "bold"), bg="darkblue", fg="white")
        b3_1.place(x=800, y=300, width=220, height=40)

        # Help Desk button
        #img7 = Image.open(r"C:\Users\nayan\Desktop\Python Projects\Face Recognition System\images\Help-Desk-Image.png")
        #img7 = img7.resize((220, 220), Image.ANTIALIAS)
        #self.photoimg7 = ImageTk.PhotoImage(img7)
        #b4 = Button(bg_img, image=self.photoimg7, cursor="hand2", command=self.help_data)
        #b4.place(x=1100, y=100, width=220, height=220)
        #b4_1 = Button(bg_img, text="Help Desk", cursor="hand2", command=self.help_data, font=("times new roman", 15, "bold"), bg="darkblue", fg="white")
        #b4_1.place(x=1100, y=300, width=220, height=40)

        # Chat button
        img_chat = Image.open(r"C:\Users\nayan\Desktop\Python Projects\Face Recognition System\images\Robot-working-on-computer-600x400.jpg")
        img_chat = img_chat.resize((220, 220), Image.Resampling.LANCZOS)
        self.photoimg_chat = ImageTk.PhotoImage(img_chat)

        bChat = Button(bg_img, image=self.photoimg_chat, cursor="hand2", command=self.chatbot)
        bChat.place(x=1100, y=100, width=220, height=220)

        b1_Chat = Button(bg_img, text="ChatBot", cursor="hand2", command=self.chatbot, font=("times new roman", 15, "bold"), bg="darkblue", fg="white")
        b1_Chat.place(x=1100, y=300, width=220, height=40)

        # Train Data button
        img8 = Image.open(r"C:\Users\nayan\Desktop\Python Projects\Face Recognition System\images\Blog_Handwriting-Datasets-to-Train-ML-models.jpg")
        img8 = img8.resize((220, 220), Image.ANTIALIAS)
        self.photoimg8 = ImageTk.PhotoImage(img8)
        b5 = Button(bg_img, image=self.photoimg8, cursor="hand2", command=self.train_data)
        b5.place(x=200, y=380, width=220, height=220)
        b5_1 = Button(bg_img, text="Train Data", cursor="hand2", command=self.train_data, font=("times new roman", 15, "bold"), bg="darkblue", fg="white")
        b5_1.place(x=200, y=580, width=220, height=40)

        # Photos button
        img9 = Image.open(r"C:\Users\nayan\Desktop\Python Projects\Face Recognition System\images\istockphoto-1493434989-612x612.jpg")
        img9 = img9.resize((220, 220), Image.ANTIALIAS)
        self.photoimg9 = ImageTk.PhotoImage(img9)
        b6 = Button(bg_img, image=self.photoimg9, cursor="hand2", command=self.open_img)
        b6.place(x=500, y=380, width=220, height=220)
        b6_1 = Button(bg_img, text="Photos", cursor="hand2", command=self.open_img, font=("times new roman", 15, "bold"), bg="darkblue", fg="white")
        b6_1.place(x=500, y=580, width=220, height=40)

        # Developer button
        img10 = Image.open(r"C:\Users\nayan\Desktop\Python Projects\Face Recognition System\images\good-software-developer-1128x635.jpg")
        img10 = img10.resize((220, 220), Image.ANTIALIAS)
        self.photoimg10 = ImageTk.PhotoImage(img10)
        b7 = Button(bg_img, image=self.photoimg10, cursor="hand2", command=self.developer_data)
        b7.place(x=800, y=380, width=220, height=220)
        b7_1 = Button(bg_img, text="Developer", cursor="hand2", command=self.developer_data, font=("times new roman", 15, "bold"), bg="darkblue", fg="white")
        b7_1.place(x=800, y=580, width=220, height=40)

        # Exit button
        img11 = Image.open(r"C:\Users\nayan\Desktop\Python Projects\Face Recognition System\images\istockphoto-460250007-612x612.jpg")
        img11 = img11.resize((220, 220), Image.ANTIALIAS)
        self.photoimg11 = ImageTk.PhotoImage(img11)
        b8 = Button(bg_img, image=self.photoimg11, cursor="hand2", command=self.iExit)
        b8.place(x=1100, y=380, width=220, height=220)
        b8_1 = Button(bg_img, text="Exit", cursor="hand2", command=self.iExit, font=("times new roman", 15, "bold"), bg="darkblue", fg="white")
        b8_1.place(x=1100, y=580, width=220, height=40)

    def open_img(self):
        os.startfile("data")

    def iExit(self):
        self.iExit = tkinter.messagebox.askyesno("Face Recognition", "Are you sure you want to exit this project?", parent=self.root)
        if self.iExit > 0:
            self.root.destroy()
        else:
            return

    # Function button
    def student_details(self):
        self.new_window = Toplevel(self.root)
        self.app = Student(self.new_window)

    def train_data(self):
        self.new_window = Toplevel(self.root)
        self.app = Train(self.new_window)
    
    def face_data(self):
        self.new_window = Toplevel(self.root)
        self.app = FaceRecognition(self.new_window)

    def attendance_data(self):
        self.new_window = Toplevel(self.root)
        self.app = Attendance(self.new_window)

    def developer_data(self):
        self.new_window = Toplevel(self.root)
        self.app = Developer(self.new_window)

    #def help_data(self):
        #self.new_window = Toplevel(self.root)
        #self.app = Help(self.new_window)

    def chatbot(self):
        self.new_window = Toplevel(self.root)
        self.app = ChatBot(self.new_window)
        
if __name__ == "__main__":
    root = Tk()
    obj = FaceRecognitionSystem(root)
    root.mainloop()