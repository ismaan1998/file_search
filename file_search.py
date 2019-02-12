#author - indrajeet
#tutor at Tech-Gram Academy

import os
import platform


os_info = platform.platform()
path = '/'
files_total = []

def set_root(s):
    global path
    path = s


#this function is working for function file_search()
def file_search2(name, name_words):
    check = True
    for word in name_words:
        if word not in name:
            check = False
            break
    return check

#search a file and open it.
def searchFile(filename):
    filename = filename.lower()
    if filename == "":
        print("nothing entered")
        return
    file_found = False
    words = filename.split()

    for root, dirs, files in os.walk(path, topdown=False):

        for name in files:
            l_name = name.lower()

            os_info = platform.platform()

            if file_search2(l_name, words):
                file_found = True
                if('Windows' in os_info):
                    files_total.append(root+'\\'+name)
                else:
                    files_total.append(root+'/'+name)
    return files_total
