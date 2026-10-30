import os

path = r"C:\Users\HP\OneDrive\Documents\Desktop\pythonlife\dict.py"

if os.path.exists(path):
    print("Folder exists")
    print(os.listdir(path))
else:
    print("Folder not found")