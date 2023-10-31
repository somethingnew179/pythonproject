import os
import sys

def show_python_version():
    print(sys.version)

def create_directory(directory_name):
    os.mkdir(directory_name)

def list_files_and_folders():
    items = os.listdir("./")
    for item in items:
        print(item)
