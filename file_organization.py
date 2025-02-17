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
# This function will get the key is a cleaner way than using a switch statement, but should I also include moving the file into the directory in this same function?
def handle_choice(choice):
    for k, v in directories.items():
        if choice in v:
            key = k
            break
    return key

print(handle_choice(".csv"))

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
 