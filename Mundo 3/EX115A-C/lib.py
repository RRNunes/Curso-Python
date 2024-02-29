def arquivoExiste(nome):
    try:
        a = open(nome, 'rt')
        a.close()
    except FileExistsError:
        return False
    else:
        return True
