# Python code​​​​​​‌​‌​‌​‌​​‌‌‌‌‌‌​‌​​​‌​‌​‌ below
# Use print("messages...") to debug your solution.
import os
from os import path

show_expected_result = True
show_hints = True

def file_info():
    # Your code goes here.
    # create an array of text files in the directory
    total_size = 0
    txt_files = [file for file in os.listdir("deps") if file.endswith('.txt')]
    print("txt_files" , txt_files)

    for file in txt_files:
        print("File: ", file)
        src = path.realpath(file)
        rootdir, actual_file = path.split(src)
        file_path = path.join("deps", actual_file)
        print("File Path", file_path)
        file_size = path.getsize(file_path)
        total_size += file_size
    return total_size

def file_info2():
    # Your code goes here.
    # create an array of text files in the directory
    total_size = 0
    folder = "deps"
    
    # get a list of all files in the current directory
    dirlist = os.listdir(folder)

    for file in dirlist:
        # make sure its a file
        if path.isfile(folder + "/" + file) and file.endswith(".txt"):
            # add the file size to the total
            filesize = path.getsize(folder + "/" + file)
            total_size += filesize
    return total_size