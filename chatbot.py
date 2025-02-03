from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk

class ChatBot:
    def __init__(self, root):
        self.root = root
        self.root.title("ChatBot")
        self.root.geometry("730x620+0+0")
        self.root.bind('<Return>', self.enter_func)

        main_frame = Frame(self.root, bd=4, bg='powder blue', width=610)
        main_frame.pack()

        img_chat = Image.open(r"C:\Users\nayan\Desktop\Python Projects\Face Recognition System\images\9a1133d4af3b637e1c6c8ff251785f27.jpg")
        img_chat = img_chat.resize((120, 70), Image.Resampling.LANCZOS)
        self.photoimg = ImageTk.PhotoImage(img_chat)

        Title_label = Label(main_frame, bd=3, relief=RAISED, anchor='n', width=730, compound=LEFT, image=self.photoimg, text="ChatBot", font=("arial", 20, "bold"), fg="blue")
        Title_label.pack(side=TOP)

        self.scroll_y = ttk.Scrollbar(main_frame, orient=VERTICAL)
        self.text = Text(main_frame, width=65, height=20, bd=3, relief=RAISED, font=("arial", 14), yscrollcommand=self.scroll_y.set)
        self.scroll_y.pack(side=RIGHT, fill=Y)
        self.scroll_y.config(command=self.text.yview)
        self.text.pack()

        btn_frame = Frame(self.root, bd=4, bg='white', width=730)
        btn_frame.pack()

        label_1 = Label(btn_frame, text="Type Something", font=("arial", 14, "bold"), fg="green", bg="white")
        label_1.grid(row=0, column=0, padx=5, sticky=W)
         
        self.entry = StringVar() 
        self.entry1 = ttk.Entry(btn_frame, textvariable=self.entry, width=40, font=("times new roman", 16, "bold"))
        self.entry1.grid(row=0, column=1, padx=5, sticky=W)

        self.send = Button(btn_frame, text="Send>>", command=self.send, font=("arial", 15, "bold"), width=8, bg="green", fg="white")
        self.send.grid(row=0, column=2, padx=5, sticky=W)

        self.clear = Button(btn_frame, text="Clear Data", command=self.clear_data, font=("arial", 15, "bold"), width=8, bg="red", fg="white")
        self.clear.grid(row=1, column=0, padx=5, sticky=W)

        self.label_1 = label_1

    def enter_func(self, event):
        self.send.invoke()
        self.entry.set('')

    def send(self):
        send = '\t\t\t' + 'You: ' + self.entry.get()
        self.text.insert(END, '\n' + send)
        self.text.yview(END)

        if self.entry.get() == '':
            self.msg = "Please enter some input"
            self.label_1.config(text=self.msg, fg="red")
        else:
            self.msg = ""
            self.label_1.config(text=self.msg, fg="red")

            user_input = self.entry.get().lower()

            if user_input == "hello":
                self.text.insert(END, "\n\n" + "Bot: Hi")
            elif user_input == "hi":
                self.text.insert(END, "\n\n" + "Bot: Hello")
            elif user_input == "how are you?":
                self.text.insert(END, "\n\n" + "Bot: Fine and you?")
            elif user_input == "fantastic":
                self.text.insert(END, "\n\n" + "Bot: Nice to hear")
            elif user_input == "who created you?":
                self.text.insert(END, "\n\n" + "Bot: Nandini did using Python")
            elif user_input == "what is your name?":
                self.text.insert(END, "\n\n" + "Bot: My name is Mr. Hacker")
            elif user_input == "bye":
                self.text.insert(END, "\n\n" + "Bot: Thank you for chatting")
            elif user_input == "how does face recognition work?":
                self.text.insert(END, "\n\n" + "Bot: Facial recognition is a way of recognizing a human face through technology.")
            elif user_input == "how does facial recognition work step by step?":
                self.text.insert(END, "\n\n" + "Bot: Step 1: Face detection. The camera detects and locates the image of a face.")
            elif user_input == "how many countries use facial recognition?":
                self.text.insert(END, "\n\n" + "Bot: In Use 98\nApproved, but not implemented 12\nConsidering facial recognition 13")
            elif user_input == "what is python programming?":
                self.text.insert(END, "\n\n" + "Bot: Python is a general-purpose and high-level programming language.")
            elif user_input == "what is chatbot?":
                self.text.insert(END, "\n\n" + "Bot: A chatbot is a computer program that's designed to simulate human conversation.")
            elif user_input == "what is machine learning?":
                self.text.insert(END, "\n\n" + "Bot: Machine learning is a branch of artificial intelligence (AI) focused on building applications that learn from data and improve their accuracy over time without being programmed to do so.")
            else:
                self.text.insert(END, "\n\n" + "Bot: Sorry, I didn't get it")

            self.entry.set('')

    def clear_data(self):
        self.text.delete(1.0, END)

if __name__ == "__main__":
    root = Tk()
    obj = ChatBot(root)
    root.mainloop()