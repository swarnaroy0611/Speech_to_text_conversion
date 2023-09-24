import tkinter as tk
import speech_recognition as sr
import pywhatkit as pwt


from tkinter import messagebox


def Speech_to_Text():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        try:
            audio = r.listen(source)
            text = r.recognize_google(audio)
            txtSpeech.insert(tk.END, text + "\n")
        except sr.UnknownValueError:
            txtSpeech.insert(tk.END, "Could not understand audio\n")
        except sr.RequestError as e:
            txtSpeech.insert(tk.END, "Error:{0}\n".format(e))


def reset_txtSpeech():
    txtSpeech .delete("1.0", tk.END)


def exit_system():
    result = messagebox.askquestion("Exit System", "Confirm if you want to exit?") 
    if result == 'yes':
        messagebox.showinfo("Goodbye", "Good bye")
        root.destroy() 


root = tk.Tk()
root.title("speech To Text")           

MainFrame = tk.Frame(root, bd=20, width=900, height=300)
MainFrame .pack()
lblTitle = tk.Label(MainFrame, font=('arial', 80, 'bold'), text="Speech To Text", width=18) 
lblTitle.pack()

txtSpeech = tk.Text(MainFrame, font=('arial', 30, 'bold'), width=68, height=12)
txtSpeech.pack() 

btnConvert = tk.Button(MainFrame, font=('arial', 30, 'bold'), text="Convert To Text", width=20, height=2, command=Speech_to_Text)
btnConvert.pack(side=tk.LEFT, padx=5)

btnReset = tk.Button(MainFrame, font=('arial', 30, 'bold'), text="Reset", width=20, height=2, command=reset_txtSpeech)
btnReset.pack(side=tk.LEFT, padx=5)

btnExit = tk.Button(MainFrame, font=('arial', 30, 'bold'), text="Exit", width=20, height=2, command=exit_system)
btnExit.pack(side=tk.LEFT, padx=5)
root.mainloop()
pwt.text_to_handwriting("text","C:\\Users\\sunde\\Desktop\\output.png",[10,10,10])         