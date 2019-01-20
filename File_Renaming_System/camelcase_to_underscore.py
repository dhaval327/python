import os
import re

# Specify the directory in which the names are to be switched
os.chdir("/Users/dhaval/PycharmProjects/LearnPython")

# Changes file names within the directory from an camel case name to underscore
# Example: changes testFile.py to test_file.py
# NOTE: ensure all files in the directory are named using camel case
for f in os.listdir():
    f_name, f_ext = os.path.splitext(f)
    if len(f_ext) > 0:
        newName = ""
        list = re.split(r"([A-Z])", f_name)
        while "" in list:
            list.remove("")
        for item in list:
            if list.index(item) > 0 and item.isupper():
                newName += "_" + item
            else:
                newName += item
        newName += f_ext
        newName = newName.lower()
        # print(newName)
        os.rename(f, newName)





