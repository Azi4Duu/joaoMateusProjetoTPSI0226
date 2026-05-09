import os
import re

def mostrarMenu(opc:str):
    if opc == "1":
        print("+----------MENU---------+")
        print("| 1 - Inserir Registo   |")
        print("| 2 - Listar Registos   |")
        print("| 3 - Atualizar Registo |")
        print("| 4 - Eliminar Registo  |")
        print("| 5 - Estatísticas      |")
        print("| 6 - Guardar Dados     |")
        print("| 7 - Sair              |")
        print("+-----------------------+")
    elif opc == "2":
        print("+-----------MENU LISTAR----------+")
        print("| 1 - Listar os Alunos por ID    |")
        print("| 2 - Listar os Alunos por nome  |")
        print("| 3 - Listar os Alunos por nota  |")
        print("| 4 - Pesquisar Aluno por nome   |")
        print("| 5 - Pesquisar Aluno por ID     |")
        print("| 6 - Voltar                     |")
        print("+--------------------------------+")

    opcao = input("Escolha uma opção: ")
    return opcao

alunos = []

def validarEmail(email:str):
    reg = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
    return re.match(reg, email) is not None

def validarTelefone(telefone:str):
    reg = r"^9[1236]\d{7}$"
    return re.match(reg, telefone) is not None

def validarData(data:str):
    reg = r"\d{1,2}\/\d{1,2}\/\d{4}"
    return re.match(reg, data) is not None

def adicionarAluno(lstAlunos:list):
    novoId = str(len(alunos) + 1)
    print("+------------+")
    print("|NOVO REGISTO|")
    print("+------------+\n")
    nome = input("Nome: ")
    
    while True:
        email = input("Email: ")
        if validarEmail(email):
            break
        print("Email inválido!")

    while True:
        telefone = input("Telefone: ")
        if validarTelefone(telefone):
            break
        print("Telefone inválido!")
    
    while True:
        dataNascimento = input("Data de Nascimento (DD/MM/AAAA): ")
        if validarData(dataNascimento):
            break
        print("Data inválida!")
    
    while True:
        try:
            nota = float(input("Nota (0-20): "))
            if nota >= 0 and nota <= 20:
                break
            print("A nota deve estar entre 0 e 20.")
        except ValueError:
            print("Nota inválida. Insira um valor númerico!")
    
    aluno = {"Id" : novoId, "Nome" : nome, "Email" : email, "Telefone" : telefone, "DataDeNascimento" : dataNascimento, "Nota" : nota}
    lstAlunos.append(aluno)
    print(f"\nO Aluno {aluno["Nome"]} foi registado com sucesso com o ID: {aluno["Id"]}!")

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

def listarAlunos(lstAlunos:list):
    if len(lstAlunos) > 0:

        opcaoListarAlunos = mostrarMenu("2")
        os.system("cls")

        while opcaoListarAlunos != "1" and opcaoListarAlunos != "2" and opcaoListarAlunos != "3" and opcaoListarAlunos != "4" and opcaoListarAlunos != "5" and opcaoListarAlunos != "6":
            opcaoListarAlunos = mostrarMenu("2")
            
        match opcaoListarAlunos:
            case "1":
                listaOrdenada = ordenarAlunos(alunos,"Id", True)

                for aluno in listaOrdenada:
                     print(f"\nID: {aluno["Id"]} | Nome: {aluno["Nome"]} | Email: {aluno["Email"]} | Telefone: {aluno["Telefone"]} | Data Nascimento: {aluno["DataDeNascimento"]} | Nota: {aluno["Nota"]}")
            case "2":
                listaOrdenada = ordenarAlunos(alunos,"Nome", True)

                for aluno in listaOrdenada:
                     print(f"\nID: {aluno["Id"]} | Nome: {aluno["Nome"]} | Email: {aluno["Email"]} | Telefone: {aluno["Telefone"]} | Data Nascimento: {aluno["DataDeNascimento"]} | Nota: {aluno["Nota"]}")
            case "3":
                listaOrdenada = ordenarAlunos(alunos,"Nota", True)

                for aluno in listaOrdenada:
                     print(f"\nID: {aluno["Id"]} | Nome: {aluno["Nome"]} | Email: {aluno["Email"]} | Telefone: {aluno["Telefone"]} | Data Nascimento: {aluno["DataDeNascimento"]} | Nota: {aluno["Nota"]}")
            case "4":
                nomeProcura = input("Indique o Nome: ")
                resultados = pesquisaNome(alunos, nomeProcura)

                if len(resultados) > 0:
                    for aluno in resultados:
                        print(f"\nID: {aluno["Id"]} | Nome: {aluno["Nome"]} | Email: {aluno["Email"]} | Telefone: {aluno["Telefone"]} | Data Nascimento: {aluno["DataDeNascimento"]} | Nota: {aluno["Nota"]}")
                else:
                    print("Não foi encontrado nenhum Aluno com esse nome!")
            case "5":
                idBusca = input("Indique o ID do aluno: ")
                resultado = pesquisaId(lstAlunos, idBusca)

                if resultado:
                    print(print(f"\nID: {resultado["Id"]} | Nome: {resultado["Nome"]} | Email: {resultado["Email"]} | Telefone: {resultado["Telefone"]} | Data Nascimento: {resultado["DataDeNascimento"]} | Nota: {resultado["Nota"]}"))
                else:
                    print("Aluno não encontrado!")
            case "6":
                return
    else:
        print("A lista de Alunos está vazia!")

def atualizarRegisto(lstAlunos:list):
    idResposta = input("Indique o ID do Aluno que pretende atualizar: ")
    alunoEncontrado = None

    alunoEncontrado = pesquisaId(lstAlunos, idResposta)

    if alunoEncontrado:
        print(f"\n--- A Editar Aluno (ID: {alunoEncontrado['Id']}) ---")
        print(f"Nome Atual: {alunoEncontrado['Nome']}")
        
        confirmar = input("Pretende mesmo editar este aluno? (s/n): ").lower()
        
        if confirmar == "s":
            novoNome = input(f"Novo Nome [{alunoEncontrado['Nome']}]: ")
            if novoNome: alunoEncontrado["Nome"] = novoNome

            novoEmail = input(f"Novo Email [{alunoEncontrado['Email']}]: ")
            if novoEmail: alunoEncontrado["Email"] = novoEmail

            while True:
                try:
                    novaNota = input(f"Nova Nota [{alunoEncontrado['Nota']}]: ")
                    if novaNota:
                        alunoEncontrado["Nota"] = float(novaNota)
                    break
                except ValueError:
                    print("A nota deve ser um número!")

            print("\nRegisto atualizado com sucesso!")
        else:
            print("Edição cancelada.")
    else:
        print("Aluno não encontrado!")

def eliminarRegisto(lstAlunos:list):
    idBusca = input("Indique o ID do Aluno a eliminar: ")
    aluno = pesquisaId(lstAlunos, idBusca)

    if aluno:
        print(f"\nID: {aluno["Id"]} | Nome: {aluno["Nome"]} | Email: {aluno["Email"]} | Telefone: {aluno["Telefone"]} | Data Nascimento: {aluno["DataDeNascimento"]} | Nota: {aluno["Nota"]}")
        confimar = input("Tem a certeza que deseja eliminar este registo (s/n)? ").lower
        if confimar == "s":
            lstAlunos.remove(aluno)
            print("Registo eliminado com sucesso!")
        else:
            print("Operação cancelada!")
    else:
        print("Aluno não encontrado!")

while True:
    os.system("cls")
    opcaoMenu = mostrarMenu("1")

    match opcaoMenu:
        case "1":
            os.system("cls")
            adicionarAluno(alunos)
            input()
        case "2":
            os.system("cls")
            listarAlunos(alunos)
            input()
        case "3":
            atualizarRegisto(alunos)
        case "7":
            break
        case _:
            os.system("cls")
            print("Opção inválida!")
            input()