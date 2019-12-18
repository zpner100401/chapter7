import os

def run(**args):
    
    print("[*] In dirlister module.\n")
    files = os.listdir(".")
    
    return str(files)