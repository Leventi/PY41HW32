import hashlib
import os

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
FILENAME = 'wikilinks.txt'
PATH = os.path.join(ROOT_DIR, FILENAME)

def md_gen(PATH):
    while True:
        line = file.readline()
        if not line:
            break
        yield line

with open(PATH, 'r') as file:
    for piece in md_gen(file):
        md5 = hashlib.md5(piece.strip().encode('utf-8')).hexdigest()
        print(md5)