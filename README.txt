Project Documentation: Automated File Organizer
1. Overview
This Python-based utility automates the organization of files within a user-selected directory. It categorizes files into subfolders (Images, Documents, Archives, etc.) based on their extensions and maintains a timestamped log of all operations.

2. Technical Components
GUI Integration: Uses tkinter to provide a native Windows folder selection dialog.

Filesystem Management: Utilizes pathlib for object-oriented path handling and shutil for high-level file movement.

Logging: Implements the datetime library to generate audit trails for every file moved.

3. Code Logic Breakdown
A. User Input & Validation
tk.Tk() / root.withdraw(): Initializes the GUI engine but hides the unnecessary main window to keep the interface clean.

filedialog.askdirectory(): Pauses execution to allow the user to browse and select a target folder.

Safety Check: The script validates the selection. If the user cancels (empty string) or selects the root script directory (.), the program exits safely to prevent accidental reorganization.

B. Directory Preparation
The script iterates through the FILE_TYPES dictionary keys and uses .mkdir(exist_ok=True) to ensure destination folders exist without crashing if they are already present.

C. File Processing Loop
.iterdir(): Scans the target directory for all items.

is_dir(): A safety filter that ensures the script only attempts to move files, skipping existing folders.

suffix.lower(): Standardizes file extensions to lowercase to ensure accurate matching regardless of original capitalization (e.g., .JPG vs .jpg).

D. Logging & Execution
Context Manager (with open): Opens the Organization_log.txt in "append" mode (a). This ensures the log isn't deleted every time the script runs; it just keeps adding to the bottom.

strftime("%Y-%m-%d %H:%M:%S"): Generates a human-readable timestamp for each move.

shutil.move(): Performs the physical transfer of the file from the source to the categorized subfolder.