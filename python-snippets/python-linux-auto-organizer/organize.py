# organize.py

import os
import shutil
import sys

def organize_folder(folder_path):
    if not os.path.isdir(folder_path):
        print("Provided path is not a directory.")
        return

    for filename in os.listdir(folder_path):
        full_path = os.path.join(folder_path, filename)

        if os.path.isfile(full_path):
            ext = filename.split('.')[-1].lower()
            dest_dir = os.path.join(folder_path, ext + "_files")

            os.makedirs(dest_dir, exist_ok=True)
            shutil.move(full_path, os.path.join(dest_dir, filename))

    print(f"Organized files in: {folder_path}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python organize.py <folder_path>")
    else:
        organize_folder(sys.argv[1])

