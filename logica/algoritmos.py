def gerarNovoID(lstAlunos:list):

    if not lstAlunos:
        return "1"
    
    idsExistentes = []
    for aluno in lstAlunos:
        idsExistentes.append(int(aluno["Id"]))
    
    novo = max(idsExistentes) + 1
    return str(novo)

def ordenarAlunos(lstAlunos:list, campo:str, crescente=True):
    n=len(lstAlunos)
    lista = lstAlunos[:]

    for i in range(n):
        for j in range(0, n -1):
            val1 = lista[j][campo]
            val2 = lista[j+1][campo]

            if campo == "Nota":
                val1, val2 = float(val1), float(val2)
            
            if crescente:
                if val1 > val2:
                    lista[j], lista[j+1] = lista[j+1], lista[j]
            else:
                if val1 < val2:
                    lista[j], lista[j+1] = lista[j+1], lista[j]

    return lista

def pesquisaNome(lstAlunos:list, nomeProcurado:str):
    encontrados = []
    nomeProcurado = nomeProcurado.lower()

    for aluno in lstAlunos:
        if nomeProcurado in aluno["Nome"].lower():
            encontrados.append(aluno)
    
    return encontrados

def pesquisaId(lstAlunos:list, idProcurado:str):

    try:
        alvo = int(idProcurado)
    except ValueError:
        print("O ID fornecido não é um número válido.")
        return None
    
    listaOrdenada = ordenarAlunos(lstAlunos, "Id", True)
    baixo = 0
    alto = len(listaOrdenada) - 1

    while baixo <= alto:
        meio = (baixo + alto) // 2
        valorMeio = int(listaOrdenada[meio]["Id"])
        alvo = int(idProcurado)

        if valorMeio == alvo:
            return listaOrdenada[meio]
        elif valorMeio < alvo:
            baixo = meio + 1
        else:
            alto = meio - 1
    
    return None