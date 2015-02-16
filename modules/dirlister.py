# dirlister.py

__version__ = "0.1"

import os

def run(**args):

    print "[*] Dirlister module."
    files = os.listdir(".")
    
    return str(files)


