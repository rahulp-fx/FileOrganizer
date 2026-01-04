# Automated File Organizer

A Python-based productivity utility that automates the organization of cluttered directories by sorting files into categorized subfolders.

## Overview

This script allows users to select a directory and automatically categorize files (Images, Documents, Archives, etc.) based on their specific file extensions. It also maintains a timestamped log of every operation for easy auditing.

---

## Technical Components

* **GUI Integration**: Uses tkinter to provide a native Windows folder selection dialog.


* **Filesystem Management**: Utilizes pathlib for object-oriented path handling and shutil for high-level file movement.


* **Logging**: Implemented via the datetime library to generate detailed audit trails for every file moved.



---

## Code Logic Breakdown

### A. User Input and Validation

* **tk.Tk() / root.withdraw()**: Initializes the GUI engine while hiding the main window to maintain a clean user interface.


* **filedialog.askdirectory()**: Pauses execution to allow the user to browse and select a target folder.


* **Safety Check**: Validates the selection; if the user cancels or selects the root script directory (.), the program exits safely to prevent accidental reorganization.



### B. Directory Preparation

* The script iterates through the dictionary keys and uses .mkdir(exist_ok=True) to ensure all destination folders exist without crashing the program if they are already present.



### C. File Processing Loop

* **.iterdir()**: Scans the target directory for all items.


* **is_dir()**: Acts as a safety filter to ensure the script only moves files, skipping existing folders.


* **suffix.lower()**: Standardizes file extensions to lowercase to ensure accurate matching regardless of original capitalization.



### D. Logging and Execution

* **Context Manager (with open)**: Opens Organization_log.txt in append mode (a).


* **Persistence**: This ensures the log is not deleted every time the script runs; it just keeps adding to the bottom.


* **strftime("%Y-%m-%d %H:%M:%S")**: Generates a human-readable timestamp for each move.


* **shutil.move()**: Performs the physical transfer of the file from the source to the appropriate category subfolder.



---

## Project Structure

```text
FileOrganizer/
├── organizer.py         # Main Python script
├── README.md            # Project documentation
└── TestEnv/Organization_log.txt # Automatically generated log file

```
