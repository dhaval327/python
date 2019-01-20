import os
import re

# Specify the directory in which the names are to be switched
os.chdir("/Users/dhaval/PycharmProjects/LearnPython")

# Changes file names within the directory from an underscore name to camel case
# Example: changes test_file.py to testFile.py
# NOTE: ensure all files in the directory are named using underscore
for f in os.listdir():
    f_name, f_ext = os.path.splitext(f)
    if len(f_ext) > 0:
        newName = ""
        list = re.split("_", f_name)
        while "" in list:
            list.remove("")
        # print(list)
        for word in list:
            if list.index(word) > 0:
                word = word.capitalize()
            newName += word
        newName += f_ext
        # print(newName)
        os.rename(f, newName)
