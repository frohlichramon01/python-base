"""Bloco de Notas

$ notes.py new "Minha nota"
tag: tech
text: 
Anotação geral sobre...

$ notes.py read --tag=tech
...

"""
__version__ = "0.1.0"

import os
import sys

cmds = ("read", "new")

path = os.curdir
filepath = os.path.join(path, "notes.txt")

arguments = sys.argv[1:]
if not arguments:
    print(f"Invalid argument. Please specify some of this commands: {cmds}")
    sys.exit(1)

if arguments[0] not in cmds:
    print(f"Invalid command {arguments[0]}")

if arguments[0] == "read":
    for line in open(filepath):
        titulo, tag, text = line.split("\t")
        if tag.lower() == arguments[1].lower():
            print(f"titulo: {titulo}")
            print(f"texto: {text}")
            print("#" * 30)
            print()

if arguments[0] == "new":
    titulo = arguments[1]
    text = [
        f"{titulo}",
        input("tag: ").strip(),
        input("text: ").strip(),
    ]
    
    with open(filepath, "a") as file_:
        file_.write("\t".join(text) + "\n")