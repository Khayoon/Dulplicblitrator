import os
import re
import tkinter as tk
from tkinter import filedialog, simpledialog
from tkinter import messagebox

def find_and_delete_duplicates(directory, max_duplicate_number):
    # Loop from 1 up to max_duplicate_number
    for num in range(1, int(max_duplicate_number) + 1):
        # Create a regex pattern for the duplicate format, like (1), (2), etc.
        duplicate_pattern = re.compile(rf"\({num}\)")
        
        # Walk through the directory and check for duplicate files
        for root, _, files in os.walk(directory):
            for file in files:
                # Check if file contains the duplicate pattern, e.g. "(1)"
                if duplicate_pattern.search(file):
                    file_path = os.path.join(root, file)
                    try:
                        # Delete the duplicate file
                        os.remove(file_path)
                        print(f"Deleted: {file_path}")
                    except Exception as e:
                        print(f"Error deleting {file_path}: {e}")
    
    messagebox.showinfo("Complete", f"Duplicate files numbered up to ({max_duplicate_number}) have been deleted.")

def select_folder():
    # Ask the user to select a folder
    folder_selected = filedialog.askdirectory()
    if folder_selected:
        # Ask user for the maximum duplicate number
        duplicate_number = simpledialog.askstring(
            "Input",
            "Enter the maximum duplicate number to delete (e.g., entering 3 will delete files ending with (1), (2), and (3)):",
            initialvalue="1"
        )
        if duplicate_number and duplicate_number.isdigit():
            find_and_delete_duplicates(folder_selected, duplicate_number)
        else:
            messagebox.showinfo("Cancelled", "Invalid number entered. Operation cancelled.")
    else:
        messagebox.showinfo("Cancelled", "No folder selected.")

# Set up the GUI
root = tk.Tk()
root.title("Duplicate File Remover")

# Configure a simple button to start the process
select_button = tk.Button(root, text="Select Folder and Remove Duplicates", command=select_folder)
select_button.pack(pady=20)

# Start the GUI event loop
root.mainloop()
