import os
import shutil
import tkinter as tk
from tkinter import messagebox, filedialog

# Dictionary mapping file extensions to associated directory
directories = {
    "Images": [".jpg", ".jpeg", ".png"],
    "Text Files": [".txt"],
    "JSON Files": [".json"],
    "CSV Files": [".csv"],
    "SQL Files": [".sql"],
    "XML Files": [".xml"],
    "Excel Files": [".xlsx"]
}

home = os.environ['HOME']
# Create the directories using keys from the directories dictionary

def handle_choice(choice):
    match choice:
        case ".jpg":
            print("Create Images directory AND move file into the directory") # I'll need to handle the directory already existing
        case _:
            print("Error")

handle_choice(".jpg")

# Scan the files and move them to the associated directory


# GUI built with tkinter for user
def tk_gui():
    root = tk.Tk()
    root.title("File Organizer")
    root.geometry("400x300")
    root.mainloop()

# tk_gui()

def change_directory(path):
    return os.chdir(path)

change_directory(home)


"""
First step is to scan the files in a directory
Keep track of the extensions (maybe save them in a set to scan set for creating directories)
Create directories
Scan files again to move them into their proper directory
"""
 