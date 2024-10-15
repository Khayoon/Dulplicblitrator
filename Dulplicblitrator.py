import os
import re
import tkinter as tk
from tkinter import filedialog, simpledialog
from tkinter import messagebox

def find_and_delete_duplicates(directory, duplicate_number):
    # Create a regex pattern for the duplicate format, like (1), (2), etc.
    duplicate_pattern = re.compile(rf"\({duplicate_number}\)")
    
    # Walk through the directory and check for duplicate files
    for root, _, files in os.walk(directory):
        for file in files:
            # Check if file contains the duplicate pattern, e.g. "(1)"
            if duplicate_pattern.search(file):
                file_path = os.path.join(root, file)
                # Delete the duplicate file
                os.remove(file_path)
                print(f"Deleted: {file_path}")
    
    # Now search for other numbered duplicates like (2), (3), etc.
    for num in range(int(duplicate_number) + 1, 100):  # Limiting to 100 dups, change as needed
        duplicate_pattern = re.compile(rf"\({num}\)")
        for root, _, files in os.walk(directory):
            for file in files:
                if duplicate_pattern.search(file):
                    file_path = os.path.join(root, file)
                    # Delete the duplicate file
                    os.remove(file_path)
                    print(f"Deleted: {file_path}")

def select_folder():
    # Ask the user to select a folder
    folder_selected = filedialog.askdirectory()
    if folder_selected:
        # Ask user for the duplicate number (e.g. "1" will handle (1), (2), (3), etc.)
        duplicate_number = simpledialog.askstring("Input", "Enter the number for duplicate detection (e.g., 1):",
                                                  initialvalue="1")
        if duplicate_number:
            find_and_delete_duplicates(folder_selected, duplicate_number)
            messagebox.showinfo("Complete", "Duplicate files have been deleted.")
        else:
            messagebox.showinfo("Cancelled", "Operation cancelled by the user.")
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
