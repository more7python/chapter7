# dirlister.py

import os

def run(**args):

    version = "0.1"
    print "[*] Dirlister module."
    files = os.listdir(".")
    
    return str(files)


