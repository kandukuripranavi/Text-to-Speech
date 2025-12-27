import pyttsx3
import tkinter as tk
from tkinter import messagebox

engine = pyttsx3.init()

def convert_text_to_speech():
    text = text_input.get()
    if text.strip() == "":
        messagebox.showwarning("Warning", "Please enter some text!")
        return
    engine.say(text)
    engine.runAndWait()

app = tk.Tk()
app.title("Text-to-Speech")
app.geometry("650x400")
app.configure(bg="pink")

frame = tk.Frame(app, bg="pink")
frame.place(relx=0.5, rely=0.5,anchor="center")

label = tk.Label(app, text="Enter text:", font=("Arial", 13), bg="#f0f0f0")
label.pack(pady=10)

text_input = tk.Entry(app, font=("Arial", 20), width=30)
text_input.pack(pady=5)

speak_button = tk.Button(app, text="Speak", command=convert_text_to_speech,
                         bg="#4CAF50", fg="white", font=("Arial", 12))
speak_button.pack(pady=20)

app.mainloop()
