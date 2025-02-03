from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2

class Developer:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")

        title_lbl = Label(self.root, text="DEVELOPER", font=("times new roman", 35, "bold"), bg="white", fg="blue")
        title_lbl.place(x=0, y=0, width=1530, height=45)

        img_top = Image.open(r"C:\Users\nayan\Desktop\Python Projects\Face Recognition System\images\680412f79b2f46f105ff7c71a72ade43.png")
        img_top = img_top.resize((1530, 720), Image.Resampling.LANCZOS)
        self.photoimg_top = ImageTk.PhotoImage(img_top)

        f_lbl = Label(self.root, image=self.photoimg_top)
        f_lbl.place(x=0, y=55, width=1530, height=720)
        
        # Main frame
        main_frame = Frame(f_lbl, bd=2, bg="white")
        main_frame.place(x=1000, y=0, width=500, height=600)

        img_top1 = Image.open(r"C:\Users\nayan\Desktop\Python Projects\Face Recognition System\images\WhatsApp Image 2024-04-28 at 11.49.25 AM.jpeg")
        img_top1 = img_top1.resize((200, 200), Image.Resampling.LANCZOS)
        self.photoimg_top1 = ImageTk.PhotoImage(img_top1)

        f_lbl1 = Label(main_frame, image=self.photoimg_top1)
        f_lbl1.place(x=300, y=0, width=200, height=200)

        # Developer info
        dev_label1 = Label(main_frame, text="Hello, my name is Nandini", font=("times new roman", 18, "bold"), fg="blue", bg="white")
        dev_label1.place(x=0, y=5)

        dev_label2 = Label(main_frame, text="I am a full stack developer", font=("times new roman", 18, "bold"), fg="blue", bg="white")
        dev_label2.place(x=0, y=40)

        img2 = Image.open(r"C:\Users\nayan\Desktop\Python Projects\Face Recognition System\images\which-desk-setup-is-best-for-a-developer.jpg")
        img2 = img2.resize((500, 390), Image.Resampling.LANCZOS)
        self.photoimg2 = ImageTk.PhotoImage(img2)

        f_lbl2 = Label(main_frame, image=self.photoimg2)
        f_lbl2.place(x=0, y=210, width=500, height=390)

if __name__ == "__main__":
    root = Tk()
    obj = Developer(root)
    root.mainloop()