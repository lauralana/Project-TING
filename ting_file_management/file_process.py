import sys
from ting_file_management.file_management import txt_importer


def process(path_file, instance):
    for i in range(0, len(instance)):
        if path_file == instance.search(i)["nome_do_arquivo"]:
            return None

    dict = {
        "nome_do_arquivo": path_file,
        "qtd_linhas": len(txt_importer(path_file)),
        "linhas_do_arquivo": txt_importer(path_file)
    }

    instance.enqueue(dict)
    sys.stdout.write(str(dict))

def remove(instance):
    """Aqui irá sua implementação"""


def file_metadata(instance, position):
    """Aqui irá sua implementação"""
