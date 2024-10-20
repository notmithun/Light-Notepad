"""
This is Light Notepad. A simple light-weight text editor written in Python.

This might sound like only for Windows but it's also for Linux and MacOS.

Written by - Mithun \n
Written in - Python (3.11.5)
"""
# Imports
import customtkinter as ctk
from json import load as ld
from tkinter import messagebox as mbox
from os import system
from sys import platform
import sys
from tkinter import Menu
from customtkinter import filedialog as fd
import webbrowser
# Imports finish

# Delcaring variables

# The version of the app.
VERSION: float = 1.1

# In Unix-based systems, the cls command will be clear.
# In NT based systems, the clear command will be cls
CLS: str = ""

# This is text will be show in the about the app window.
ABOUT_TXT: str = """
Light Notepad is a simple light-weight text editor written in Python.

Written / Created by - Mithun (GitHub: notmithun; Discord: notmithun_)
Written in - Python (3.11.5)
"""

# This text will be shown in start of the app. Can be disabled in "config.json". Set the "start_up_txt" to false
START_UP_TXT: str = f"""
Version : {VERSION} \n
Python and system version : {sys.version} \n
Made by Mithun
"""
CENTER: str = ctk.CENTER


IS_FILE_SAVED: bool = True

global filename

filename: str = ""

txt_file: str = ''

# End of delcaring variables

if platform == "linux" or platform == "linux2" or  platform == "darwin":
    # For Unix-based
    CLS = "clear"
elif platform == "win32":
    # For NT based
    CLS = "cls"

# Functions to be used in buttons or other things

def new():
    global IS_FILE_SAVED, filename
    if IS_FILE_SAVED:
        temp = mbox.askyesnocancel("Waring: File not saved", "Do you want to save the file?")
        if temp:
            save(txt_box.get(0.0, "end"), save_file_dialog())
            txt_box.delete(0.0, "end")
            filename = ""
            IS_FILE_SAVED = False
        elif temp == None:
            pass
        else:
            txt_box.delete(0.0, "end")
            IS_FILE_SAVED = False
            filename = ""
    else:
        txt_box.delete(0.0, "end")

def open_file():
    global filename
    global IS_FILE_SAVED
    if not IS_FILE_SAVED:
        temp = mbox.askyesnocancel("Warning: File not saved", "Do you want to save your file?")
        if temp:
            save(txt_box.get(0.0, "end"), save_file_dialog())
            txt_box.delete(0.0, "end")
            filename = ""
            IS_FILE_SAVED = False
        elif temp == None:
            return ''
        elif not temp:
            pass
    IS_FILE_SAVED = False
    fn = fd.askopenfilename(defaultextension="*.txt, *.log")
    if fn.endswith(".iso") or fn.endswith(".img"):
        mbox.showerror("Error", "Error code: 5\n\n Light Notepad cannot read '.iso' / '.img' files")
        fn = ''
    filename = fn 
    return fn

def save_file_dialog():
    svd = fd.asksaveasfilename(confirmoverwrite=True, defaultextension="*.txt, *.log")
    return svd

def set_txt(filename: str="test.txt"):
    if filename == '':
        mbox.showerror("Cannot save.", "Error code: 3\n\nFilename is empty. Either use save as or make a new document.")
        return 1
    txt_box.delete(0.0, "end")
    with open (filename, 'r') as read_file:
        try:
            txt_box.insert(index=0.0, text=read_file.read())
        except UnicodeDecodeError as e:
            mbox.showerror("Error: UnicodeDecodeError", f"Error message: {e}. \n\nError code: 4\n\nThat file you tried to open is not a valid text file.")
        except FileNotFoundError as fe:
            print(f"FileNotFoundError: {fe}")
        read_file.close()

def save(information: str="Text....", fn: str="test.txt"):
    global IS_FILE_SAVED
    if fn == '':
        mbox.showerror("Cannot save.", "Error code: 3\n\nFilename is empty. Either use save as or make a new document.")
        return 1
    try:
        txt_saved = open(fn, 'w')
    except FileNotFoundError as fnfe:
        mbox.showerror("Error: FileNotFoundError", f"Error message: {fnfe}.\n\n Please recheck that the file is there")
    txt_saved.writelines(information)
    txt_saved.close()
    IS_FILE_SAVED = True
    mbox.showinfo("Successfully saved", "Successfully saved to " + fn)

print(f"Version: {VERSION}")

# Reading the "config.json file (atleast trying to)"
try:
    # Reading "config.json"
    with open("config.json", 'r') as config_file:
        data = ld(config_file)

        # 1 for System's appearance mode
        # 2 for light mode
        # 3 for dark mode

        if data["appearance_mode"] == 1:
            # Default
            ctk.set_appearance_mode("system")
        elif data["appearance_mode"] == 2:
            # Light mode
            ctk.set_appearance_mode("light")
        elif data["appearance_mode"] == 3:
            # Dark mode
            ctk.set_appearance_mode("dark")
        else:
            ctk.set_appearance_mode("system")

        if data["start_up_txt"]:
            mbox.showinfo(f"Light Notepad. Version: {VERSION}", START_UP_TXT)
        elif not data["start_up_txt"]:
            print("Start up text disabled.")
# If it fails to find "config.json" then you would have to download from the GitHub page or make your own one.
except FileNotFoundError as e:
    print(f"Error: {e}")
    mbox.showerror("Error: FileNotFoundError", f"Error message: {e} \nError Code: 1\n\nHow to fix this error:\n\n1.Make a file named 'config.json' in the directory where the source is located\n\n2.Put this code in there: " + '{ "appearance_mode": 1, "start_up_txt": true }')
    exit(1)
# If it falis to find any of configs.
except KeyError as ke:
    print(f"Key Error: {ke}")
    mbox.showerror("Error: KeyError", f"Error message: {ke} \nError Code: 2\n\nHow to fix this error:\n\n1.In the file 'config.json', erase everything and type this " + '{ "appearance_mode": 1, "start_up_txt": true }')
    exit(2)

app = ctk.CTk()

app.title(f"Light Notepad - Version {VERSION}")
app.geometry("400x400")


menu = Menu(app)
app.config(menu=menu)

# File menu
file_menu = Menu(menu)
menu.add_cascade(label="File", menu=file_menu)


file_menu.add_cascade(label="New", command=lambda: new())
file_menu.add_cascade(label="Open", command=lambda: set_txt(open_file()))
file_menu.add_cascade(label="Save", command=lambda: save(txt_box.get(0.0, "end"), filename))
file_menu.add_cascade(label="Save as", command=lambda: save(txt_box.get(0.0, "end"), save_file_dialog()))

# Help menu
help_menu = Menu(menu)
menu.add_cascade(label="Help", menu=help_menu)

help_menu.add_cascade(label="Open GitHub Wiki", command=lambda: webbrowser.open("https://github.com/notmithun/Light-Notepad/wiki"))
help_menu.add_cascade(label="Solve errors!", command=lambda: webbrowser.open("https://github.com/notmithun/Light-Notepad/wiki/Error-codes"))
help_menu.add_separator()
help_menu.add_cascade(label="About Light Notepad", command=lambda: mbox.showinfo("Light Notepad - Created by Mithun", ABOUT_TXT))

txt_box = ctk.CTkTextbox(app, width=600, height=600)
txt_box.pack(expand=True, fill='both')
txt_box.place(relx=0.5, rely=0.5, anchor=CENTER)

app.mainloop()