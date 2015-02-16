# environment.py

__version__ = "0.1"

import os

def run(**args):

    version = "0.1"
    print "[*] Environment module."
    return str(os.version)

