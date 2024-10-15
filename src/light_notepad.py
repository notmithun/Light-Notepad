"""
This is Light Notepad. A simple light-weight text editor written in Python.

This might sound like only for Windows but it's also for Linux and MacOS.

Written by - Mithun
Written in - Python (3.11.5)
"""
import customtkinter as ctk
from json import load as ld
from tkinter import messagebox as mbox
from os import system

try:
    with open("config.json", 'r') as config_file:
        data = ld(config_file)
        if data[1] == 1:
            ctk.set_appearance_mode("system")
        elif data["dark_mode"] == 2:
            ctk.set_appearance_mode("light")
        elif data["dark_mode"] == 3:
            ctk.set_appearance_mode("dark")
        else:
            ctk.set_appearance_mode("system")
except FileNotFoundError as e:
    print(f"Error: {e}")
    mbox.showerror("Error: FileNotFoundError", f"Error message: {e} \nError Code: 1\n\nHow to fix this error:\n\n1.Make a file named 'config.json' in the directory where the source is located\n\n2.Put this code in there: " + '{"appearance_mode": 1}')
    exit(1)
    
    


VERSION = 1.0

app = ctk.CTk()

app.mainloop()