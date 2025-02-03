from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
from time import strftime
from datetime import datetime
import cv2
import os
import numpy as np

class FaceRecognition:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")
        
        title_lbl = Label(self.root, text="FACE RECOGNITION", font=("times new roman", 35, "bold"), bg="white", fg="blue")
        title_lbl.place(x=0, y=0, width=1530, height=45)

        img_top = Image.open(r"C:\Users\nayan\Desktop\Python Projects\Face Recognition System\images\istockphoto-1445021758-612x612.jpg")
        img_top = img_top.resize((650, 700), Image.Resampling.LANCZOS)
        self.photoimg_top = ImageTk.PhotoImage(img_top)

        f_lbl = Label(self.root, image=self.photoimg_top)
        f_lbl.place(x=0, y=55, width=650, height=700)

        img_bottom = Image.open(r"C:\Users\nayan\Desktop\Python Projects\Face Recognition System\images\iStock-925574662-scaled.jpg")
        img_bottom = img_bottom.resize((950, 700), Image.Resampling.LANCZOS)
        self.photoimg_bottom = ImageTk.PhotoImage(img_bottom)

        f_lbl = Label(self.root, image=self.photoimg_bottom)
        f_lbl.place(x=650, y=55, width=950, height=700)

        # Button
        b1_1 = Button(f_lbl, text="Face Recognition", cursor="hand2", font=("times new roman", 20, "bold"), bg="red", fg="white", command=self.face_recog)
        b1_1.place(x=100, y=620, width=250, height=40)

    #====attendence=====
    def mark_attendance(self, i, r, n, d):
        with open("attendance.csv", "r+", newline="\n") as f:
            myDataList = f.readlines()
            name_list = []

            for line in myDataList:
                entry = line.split(",")
                name_list.append(entry[0])

            if ((i not in name_list) and (r not in name_list) and (n not in name_list)):
                now = datetime.now()
                d1 = now.strftime("%d/%m/%Y")
                dtString = now.strftime("%H:%M:%S")
                f.writelines(f"\n{i}, {r}, {n}, {d}, {dtString}, {d1}, Present")
    
    #=====face recognition=====
    def draw_boundary(self, img, classifier, scaleFactor, minNeighbors, color, text, clf):
        gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        features = classifier.detectMultiScale(gray_image, scaleFactor, minNeighbors)

        coord = []

        for (x, y, w, h) in features:
            cv2.rectangle(img, (x, y), (x + w, y + h), color, 3)
            id, predict = clf.predict(gray_image[y:y + h, x:x + w])
            confidence = int((100 * (1 - predict / 300)))

            if confidence > 77:
                conn = mysql.connector.connect(host="localhost", username="root", password="Nandini06@", database="face_recognizer")
                my_cursor = conn.cursor()

                my_cursor.execute("select Name from student where Student_id=" + str(id))
                n = my_cursor.fetchone()
                if n:
                    n = "+".join(n)

                my_cursor.execute("select Roll from student where Student_id=" + str(id))
                r = my_cursor.fetchone()
                if r:
                    r = "+".join(r)

                my_cursor.execute("select Dep from student where Student_id=" + str(id))
                d = my_cursor.fetchone()
                if d:
                    d = "+".join(d)

                my_cursor.execute("select Student_id from student where Student_id=" + str(id))
                i = my_cursor.fetchone()
                if i:
                    d = "+".join(i)    

                if n and r and d:
                    cv2.putText(img, f"Name: {i}", (x, y - 75), cv2.FONT_HERSHEY_SIMPLEX, 0.8, color, 2)
                    cv2.putText(img, f"Name: {n}", (x, y - 55), cv2.FONT_HERSHEY_SIMPLEX, 0.8, color, 2)
                    cv2.putText(img, f"Roll: {r}", (x, y - 30), cv2.FONT_HERSHEY_SIMPLEX, 0.8, color, 2)
                    cv2.putText(img, f"Dep: {d}", (x, y - 5), cv2.FONT_HERSHEY_SIMPLEX, 0.8, color, 2)
                    self.mark_attendance(i,r,n,d)
            else:
                cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 3)
                cv2.putText(img, "Unknown Face", (x, y - 5), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 255, 255), 2)

            coord = [x, y, w, h]

        return coord

    def recognize(self, img, clf, faceCascade):
        coord = self.draw_boundary(img, faceCascade, 1.1, 10, (255, 25, 255), "Face", clf)
        return img

    def face_recog(self):
        faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        clf = cv2.face.LBPHFaceRecognizer_create()
        clf.read("classifier.xml")

        video_cap = cv2.VideoCapture(0)

        while True:
            ret, img = video_cap.read()
            img = self.recognize(img, clf, faceCascade)
            cv2.imshow("Welcome To Face Recognition", img)

            if cv2.waitKey(1) == 13:
                break

        video_cap.release()
        cv2.destroyAllWindows()

if __name__ == "__main__":
    root = Tk()
    obj = FaceRecognition(root)
    root.mainloop()