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


# Scan the files and move them to the associated directory


# GUI built with tkinter for user
def tk_gui():
    root = tk.Tk()
    root.title("File Organizer")
    root.geometry("400x300")
    root.mainloop()

# tk_gui()