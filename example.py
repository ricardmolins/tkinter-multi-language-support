from tkinter import *
from tkinter import ttk
from text_manager.text_and_fonts import *

def ChangeToEnglish(*args):
    text_manager.SetLanguage("eng")
    UpdateTexts()

def ChangeToCatalan(*args):
    text_manager.SetLanguage("cat")
    UpdateTexts()


def UpdateTexts():
    label_1.configure(text=text_manager.GetText("FIRST_BUTTON_TEXT"))
    label_2.configure(text=text_manager.GetText("SECOND_BUTTON_TEXT"))
    label_3.configure(text=text_manager.GetText("THIRD_BUTTON_TEXT"))
    button_1.configure(text=text_manager.GetText("CHANGE_TO_ENG"))
    button_2.configure(text=text_manager.GetText("CHANGE_TO_CAT"))

text_manager = TextAndFontsManager()

root = Tk()
root.geometry('600x200')
root.title("Tkinter Text manager example")

label_1 = ttk.Label(root, text = text_manager.GetText("FIRST_BUTTON_TEXT"))
label_1.config(font = text_manager.GetFontFromText("FIRST_BUTTON_TEXT"))
label_1.grid(column=0, row=0)

label_2 = ttk.Label(root, text = text_manager.GetText("SECOND_BUTTON_TEXT"))
label_2.config(font = text_manager.GetFontFromText("SECOND_BUTTON_TEXT"))
label_2.grid(column=1, row=0)

label_3 = ttk.Label(root, text = text_manager.GetText("THIRD_BUTTON_TEXT"))
label_3.config(font = text_manager.GetFontFromText("THIRD_BUTTON_TEXT"))
label_3.grid(column=2, row=0)

s1 = ttk.Style()
s1.configure('my1.TButton', font=text_manager.GetFontFromText("CHANGE_TO_CAT"))
s2 = ttk.Style()
s2.configure('my2.TButton', font=text_manager.GetFontFromText("CHANGE_TO_ENG"))

button_1 = ttk.Button(root, text=text_manager.GetText("CHANGE_TO_ENG"),style='my1.TButton',command=ChangeToEnglish)
button_1.grid(column=0, row=1)

button_2 = ttk.Button(root, text = text_manager.GetText("CHANGE_TO_CAT"),style='my2.TButton',command=ChangeToCatalan)
button_2.grid(column=1, row=1)

root.mainloop()