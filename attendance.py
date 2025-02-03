from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import csv
from tkinter import filedialog

mydata=[]
class Attendance:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")

        # Define variables
        self.var_atten_id = StringVar()
        self.var_atten_roll = StringVar()
        self.var_atten_name = StringVar()
        self.var_atten_dep = StringVar()
        self.var_atten_time = StringVar()
        self.var_atten_date = StringVar()
        self.var_atten_attendance = StringVar()

        # First image
        img = Image.open(r"C:\Users\nayan\Desktop\Python Projects\Face Recognition System\images\Untitled-design-10-1.jpg")
        img = img.resize((800, 200), Image.Resampling.LANCZOS)
        self.photoimg = ImageTk.PhotoImage(img)

        f_lbl = Label(self.root, image=self.photoimg)
        f_lbl.place(x=0, y=0, width=800, height=200)

        # Second image
        img1 = Image.open(r"C:\Users\nayan\Desktop\Python Projects\Face Recognition System\images\AdobeStock_52125430.jpeg")
        img1 = img1.resize((800, 200), Image.Resampling.LANCZOS)
        self.photoimg1 = ImageTk.PhotoImage(img1)

        f_lbl = Label(self.root, image=self.photoimg1)
        f_lbl.place(x=800, y=0, width=800, height=200)

        # Background image
        img2 = Image.open(r"C:\Users\nayan\Desktop\Python Projects\Face Recognition System\images\1023386.jpg")
        img2 = img2.resize((1530, 710), Image.Resampling.LANCZOS)
        self.photoimg2 = ImageTk.PhotoImage(img2)

        bg_img = Label(self.root, image=self.photoimg2)
        bg_img.place(x=0, y=200, width=1530, height=710)

        # Title
        title_lbl = Label(bg_img, text="ATTENDANCE MANAGEMENT SYSTEM", font=("times new roman", 35, "bold"), bg="white", fg="blue")
        title_lbl.place(x=0, y=0, width=1530, height=45)

        # Main frame
        main_frame = Frame(bg_img, bd=2, bg="white")
        main_frame.place(x=20, y=55, width=1480, height=600)

        # Left label frame
        Left_frame = LabelFrame(main_frame, bd=2, bg="white", relief=RIDGE, text="Student Attendance Details", font=("times new roman", 12, "bold"))
        Left_frame.place(x=10, y=10, width=730, height=580)

        img_left = Image.open(r"C:\Users\nayan\Desktop\Python Projects\Face Recognition System\images\attendance-management.jpg")
        img_left = img_left.resize((720, 130), Image.Resampling.LANCZOS)
        self.photoimg_left = ImageTk.PhotoImage(img_left)

        f_lbl = Label(Left_frame, image=self.photoimg_left)
        f_lbl.place(x=5, y=0, width=720, height=130)

        # Left inside frame
        left_inside_frame = Frame(Left_frame, bd=2, relief=RIDGE, bg="white")
        left_inside_frame.place(x=0, y=135, width=720, height=370)

        # Attendance ID
        attendanceId_label = Label(left_inside_frame, text="AttendanceId:", font=("times new roman", 13, "bold"), bg="white")
        attendanceId_label.grid(row=0, column=0, padx=10, pady=5, sticky=W)

        attendanceID_entry = ttk.Entry(left_inside_frame, textvariable=self.var_atten_id, width=20, font=("times new roman", 13, "bold"))
        attendanceID_entry.grid(row=0, column=1, padx=18, pady=5, sticky=W)

        # Roll
        rollLabel = Label(left_inside_frame, text="Roll:", bg="white", font=("comicsansns", 11, "bold"))
        rollLabel.grid(row=0, column=2, padx=4, pady=8)

        atten_roll = ttk.Entry(left_inside_frame,textvariable=self.var_atten_roll, width=22, font=("comicsansns", 11, "bold"))
        atten_roll.grid(row=0, column=3, padx=18, pady=5, sticky=W)

        # Name
        nameLabel = Label(left_inside_frame, text="Name:", bg="white", font=("comicsansns", 11, "bold"))
        nameLabel.grid(row=1, column=0, padx=10, pady=5, sticky=W)

        atten_name = ttk.Entry(left_inside_frame,textvariable=self.var_atten_name, width=22, font=("comicsansns", 11, "bold"))
        atten_name.grid(row=1, column=1, padx=18, pady=5, sticky=W)

         # Department
        depLabel = Label(left_inside_frame, text="Department:", bg="white", font=("comicsansns", 11, "bold"))
        depLabel.grid(row=1, column=2, padx=10, pady=5, sticky=W)

        atten_dep = ttk.Entry(left_inside_frame,  textvariable=self.var_atten_dep, width=22, font=("comicsansns", 11, "bold"))
        atten_dep.grid(row=1, column=3, padx=18, pady=5, sticky=W)

        # Time
        timeLabel = Label(left_inside_frame, text="Time:", bg="white", font=("comicsansns", 11, "bold"))
        timeLabel.grid(row=2, column=0, padx=10, pady=5, sticky=W)

        atten_time = ttk.Entry(left_inside_frame,textvariable=self.var_atten_time,  width=22, font=("comicsansns", 11, "bold"))
        atten_time.grid(row=2, column=1, padx=18, pady=5, sticky=W)

        # Date
        dateLabel = Label(left_inside_frame, text="Date:", bg="white", font=("comicsansns", 11, "bold"))
        dateLabel.grid(row=2, column=2, padx=10, pady=5, sticky=W)

        atten_date = ttk.Entry(left_inside_frame,textvariable=self.var_atten_date, width=22, font=("comicsansns", 11, "bold"))
        atten_date.grid(row=2, column=3, padx=18, pady=5, sticky=W)

        # Attendance Status
        attendanceLabel = Label(left_inside_frame, text="Attendance Status", bg="white", font=("comicsansns", 11, "bold"))
        attendanceLabel.grid(row=3, column=0, padx=10, pady=5, sticky=W)

        self.atten_status = ttk.Combobox(left_inside_frame, textvariable=self.var_atten_attendance, width=20, font=("comicsansns", 11, "bold"), state="readonly")
        self.atten_status["values"] = ("Status", "Present", "Absent")
        self.atten_status.grid(row=3, column=1, padx=18, pady=5, sticky=W)
        self.atten_status.current(0)

         # Button frame
        btn_frame = Frame(left_inside_frame, bd=2, relief=RIDGE, bg="white")
        btn_frame.place(x=0, y=300, width=715, height=35)

        # Import CSV button
        save_btn = Button(btn_frame, text="Import CSV", command=self.importCsv, width=17, font=("times new roman", 13, "bold"), bg="blue", fg="white")
        save_btn.grid(row=0, column=0)

        # Export CSV button
        update_btn = Button(btn_frame, text="Export CSV",command=self.exportCsv, width=17, font=("times new roman", 13, "bold"), bg="blue", fg="white")
        update_btn.grid(row=0, column=1)

        # Update button
        delete_btn = Button(btn_frame, text="Update", width=17, font=("times new roman", 13, "bold"), bg="blue", fg="white")
        delete_btn.grid(row=0, column=2)

        # Reset button
        reset_btn = Button(btn_frame, text="Reset",command=self.reset_data, width=17, font=("times new roman", 13, "bold"), bg="blue", fg="white")
        reset_btn.grid(row=0, column=3)
            
        # Right label frame
        Right_frame = LabelFrame(main_frame, bd=2, bg="white", relief=RIDGE, text="Attendance Details", font=("times new roman", 12, "bold"))
        Right_frame.place(x=750, y=10, width=720, height=580)

        # Table frame
        table_frame = Frame(Right_frame, bd=2, relief=RIDGE, bg="white")
        table_frame.place(x=5, y=5, width=700, height=455)

# Scroll bars
        scroll_x = ttk.Scrollbar(table_frame, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame, orient=VERTICAL)

        self.AttendanceReportTable = ttk.Treeview(table_frame, columns=("id", "roll", "name", "department", "time", "date", "attendance"), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)

        scroll_x.config(command=self.AttendanceReportTable.xview)
        scroll_y.config(command=self.AttendanceReportTable.yview)

        self.AttendanceReportTable.heading("id", text="Attendance ID")
        self.AttendanceReportTable.heading("roll", text="Roll")
        self.AttendanceReportTable.heading("name", text="Name")
        self.AttendanceReportTable.heading("department", text="Department")
        self.AttendanceReportTable.heading("time", text="Time")
        self.AttendanceReportTable.heading("date", text="Date")
        self.AttendanceReportTable.heading("attendance", text="Attendance")

        self.AttendanceReportTable["show"] = "headings"

        self.AttendanceReportTable.column("id", width=100)
        self.AttendanceReportTable.column("roll", width=100)
        self.AttendanceReportTable.column("name", width=100)
        self.AttendanceReportTable.column("department", width=100)
        self.AttendanceReportTable.column("time", width=100)
        self.AttendanceReportTable.column("date", width=100)
        self.AttendanceReportTable.column("attendance", width=100)

        self.AttendanceReportTable.pack(fill=BOTH, expand=1)

        self.AttendanceReportTable.bind("<ButtonRelease-1>", self.get_cursor)

#=======fetch Data=======

    def fetchData(self, rows):
        self.AttendanceReportTable.delete(*self.AttendanceReportTable.get_children())
        for i in rows:
            self.AttendanceReportTable.insert("", END, values=i)

    def importCsv(self):
        global mydata
        mydata.clear()
        fln = filedialog.askopenfilename(initialdir=os.getcwd(), title="Open CSV", filetypes=(("CSV File", "*.csv"), ("ALL File", "*.*")),parent=self.root)
        with open(fln) as myfile:
            csvread = csv.reader(myfile, delimiter=",")
            for i in csvread:
                mydata.append(i)
        self.fetchData(mydata)

    def exportCsv(self):
        try:
            if len(mydata) < 1:
                messagebox.showerror("No Data", "No Data found to export", parent=self.root)
                return False

            fln = filedialog.asksaveasfilename(initialdir=os.getcwd(), title="Save CSV", filetypes=(("CSV File", "*.csv"), ("ALL File", "*.*")))
            with open(fln, mode="w", newline="") as myfile:
                exp_write = csv.writer(myfile, delimiter=",")
                for i in mydata:
                    exp_write.writerow(i)
                messagebox.showinfo("Data Export", "Your data exported to " + os.path.basename(fln) + " successfully")

        except Exception as es:
            messagebox.showerror("Error", f"Due To : {str(es)}", parent=self.root)


    def get_cursor(self, event=""):
        cursor_row = self.AttendanceReportTable.focus()
        content = self.AttendanceReportTable.item(cursor_row)
        rows = content['values']

        self.var_atten_id.set(rows[0])
        self.var_atten_roll.set(rows[1])
        self.var_atten_name.set(rows[2])
        self.var_atten_dep.set(rows[3])
        self.var_atten_time.set(rows[4])
        self.var_atten_date.set(rows[5])
        self.var_atten_attendance.set(rows[6])

    def reset_data(self):
        self.var_atten_id.set("")
        self.var_atten_roll.set("")
        self.var_atten_name.set("")
        self.var_atten_dep.set("")
        self.var_atten_time.set("")
        self.var_atten_date.set("")
        self.var_atten_attendance.set("")
        
if __name__ == "__main__":
    root = Tk()
    obj = Attendance(root)
    root.mainloop()