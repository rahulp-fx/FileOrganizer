import os
import shutil
import tkinter as tk
from tkinter import filedialog
from pathlib import Path
from datetime import datetime

#Asking user for path using tkinter, GUI
def get_folder_path():
  root = tk.Tk() #This initializes the main Tkinter engine
  root.withdraw() #This immediately hides that blank main window so only the file dialog appears.

  folder_selected = filedialog.askdirectory()
  root.destroy() #Once user select a file, tkinter engine is stopped
  return Path(folder_selected)

TARGET_DIR = get_folder_path() #function call

#Check if the user actually selected a folder or cancelled
if not TARGET_DIR or str(TARGET_DIR) == ".": 

#if not TARGET_DIR - If the user clicks "Cancel" on the pop-up, folder_selected becomes an empty string
# str(TARGET_DIR) == "." - if you don't provide a path, it defaults to . (the current folder)

  print("No folder selected. Exiting...")
  exit()

FILE_TYPES = {
  "Images":[".jpg", ".jpeg", ".png", ".gif"],
  "Documents": [".pdf", ".docx", ".txt"],
  "Archives": [".zip", ".rar", ".7z", ".tar"],
  "Programs": [".exe", ".msi"],
  "Videos": [".mp4", ".mov", ".avi"],
  "Audio":[".mp3",".wav",".aac",".aiff","opus"]
}

def organize():
  for folder in FILE_TYPES.keys():
    folder_path = TARGET_DIR / folder
    folder_path.mkdir(exist_ok=True)
    
  for file_path in TARGET_DIR.iterdir():
    if file_path.is_dir():
      continue
    
    ext = file_path.suffix.lower()
    with open(TARGET_DIR / "Organization_log.txt","a") as log:
      timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S") #strftime - string format time

      for folder, extensions in FILE_TYPES.items():
        if ext in extensions:
          dest = TARGET_DIR / folder / file_path.name
          shutil.move(str(file_path), str(dest))
          
          #Write log
          log.write(f"[{timestamp}] MOVED: {file_path.name} TO {folder}\n")
          break
        
if __name__ == "__main__":
  organize()
      