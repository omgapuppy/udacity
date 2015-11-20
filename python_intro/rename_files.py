import os

def rename_files():
    # Get file names in directory
    file_list = os.listdir("/Users/ardimehist/github/udacity/python_intro/prank")
    print(file_list)
    saved_path = os.getcwd()
    os.chdir("/Users/ardimehist/github/udacity/python_intro/prank")
    # Rename all files
    for file_name in file_list:
        os.rename(file_name, file_name.translate(None, "0123456789"))
    os.chdir(saved_path)
    
rename_files()
