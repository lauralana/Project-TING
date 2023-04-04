from pathlib import Path
import sys


def txt_importer(path_file):
    path = Path(path_file)
    if path.suffix != '.txt':
        sys.stderr.write("Formato inválido")

    try:
        with open(path_file) as file:
            return file.read().split("\n")
    except FileNotFoundError:
        sys.stderr.write(f"Arquivo {path_file} não encontrado\n")
