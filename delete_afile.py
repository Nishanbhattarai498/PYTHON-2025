import os
import shutil

try:
    path='folder'
    # os.remove(path)  # remove the file test.txt:: file is removed
    # os.rmdir(path)  # remove the directory empty_folder:: empty folder is removed
    shutil.rmtree(path)  # remove the directory and all its contents:: non empty folder is removedd with its all contents
    print(path + " has been removed")

except FileNotFoundError as e:
    print(e)
    print("Error: File not found.")

except PermissionError as e:
    print(e)
    print("Error: Permission denied.")
except OSError as e:
    print(e)
    print("Error: Directory not empty or in use.")
