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
# Imports finish

# Delcaring variables

# The version of the app.
VERSION: float = 1.0

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
START_UP_TXT: str = f""""
Version : {VERSION}
Python and system version : {sys.version}
Made by Mithun
"""

if platform == "linux" or platform == "linux2" or  platform == "darwin":
    # For Unix-based
    CLS = "clear"
elif platform == "win32":
    # For NT based
    CLS = "cls"


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
    mbox.showerror("Error: FileNotFoundError", f"Error message: {e} \nError Code: 1\n\nHow to fix this error:\n\n1.Make a file named 'config.json' in the directory where the source is located\n\n2.Put this code in there: " + '{"appearance_mode": 1}')
    exit(1)

app = ctk.CTk()

app.mainloop()