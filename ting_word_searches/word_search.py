def exists_word(word, instance):
    for w in range(0, len(instance)):
        file = instance.search(w)
        list = {
            "palavra": word,
            "arquivo": file['nome_do_arquivo'],
            "ocorrencias": []
        }
        for i in range(0, len(file['linhas_do_arquivo'])):
            row = file['linhas_do_arquivo'][i]
            if word.lower() in row.lower():
                list['ocorrencias'].append({"linha": i + 1})

        print(len(list['ocorrencias']))
        
        result = []
        if len(list['ocorrencias']) > 0:
            result.append(list)

    return result


def search_by_word(word, instance):
    """Aqui irá sua implementação"""
