import os

def mostrarMenu():
    print("+----------MENU---------+")
    print("| 1 - Inserir Registo   |")
    print("| 2 - Listar Registos   |")
    print("| 3 - Atualizar Registo |")
    print("| 4 - Eliminar Registo  |")
    print("| 5 - Sair              |")
    print("+-----------------------+")
    opcao = input("Escolha uma opção: ")
    return opcao

alunos = []

def adicionarAluno(lstAlunos:list):
    novoId = str(len(alunos) + 1)
    print("+------------+")
    print("|NOVO REGISTO|")
    print("+------------+\n")
    nome = input("Nome: ")
    email = input("Email: ")
    telefone = input("Telefone: ")
    dataNascimento = input("Data de Nascimento: ")
    nota = input("Nota: ")
    aluno = {"Id" : novoId, "Nome" : nome, "Email" : email, "Telefone" : telefone, "DataDeNascimento" : dataNascimento, "Nota" : nota}
    lstAlunos.append(aluno)
    print(f"\nO Aluno {aluno["Nome"]} foi registado com sucesso com o ID: {aluno["Id"]}!")

def ordenarAlunos(lstAlunos:list, campo, crescente=True):
    n=len(lstAlunos)
    lista = lstAlunos

    for i in range(n):
        for j in range(0, n -1):
            val1 = lista[j][campo]
            val2 = lista[j+1][campo]

            if campo == "Nota":
                val1, val2 = float(val1), float(val2)
            
            if crescente:
                if val1 > val2:
                    lista[j][campo], lista[j+1][campo] = lista[j+1][campo], lista[j][campo]
            else:
                if val1 < val2:
                    lista[j][campo], lista[j+1][campo] = lista[j+1][campo], lista[j][campo]

    return lista

def listarAlunos(lstAlunos:list):

    if len(lstAlunos) > 0:

        print("+-----------MENU LISTAR----------+")
        print("| 1 - Listar os Alunos por ID    |")
        print("| 2 - Listar os Alunos por nome  |")
        print("| 3 - Pesquisar Aluno por ID     |")
        print("| 4 - Pesquisar Aluno por nome   |")
        print("| 5 - Listar todos os Alunos     |")
        print("+--------------------------------+")

        opcaoListarAlunos = input("Escolha uma opção: ")
        while opcaoListarAlunos != "1" and opcaoListarAlunos != "2" and opcaoListarAlunos != "3" and opcaoListarAlunos != "4" and opcaoListarAlunos != "5":
            opcaoListarAlunos = input("Escolha uma opção: ")
            
        match opcaoListarAlunos:
            case "1":
                for aluno in lstAlunos:
                    print(f"\nID: {aluno["Id"]} | Nome: {aluno["Nome"]} | Email: {aluno["Email"]} | Telefone: {aluno["Telefone"]} | Data Nascimento: {aluno["DataDeNascimento"]} | Nota: {aluno["Nota"]}")
            case "2":
                listaOrdenada = ordenarAlunos(alunos,"Nome", True)
                for aluno in listaOrdenada:
                     print(f"\nID: {aluno["Id"]} | Nome: {aluno["Nome"]} | Email: {aluno["Email"]} | Telefone: {aluno["Telefone"]} | Data Nascimento: {aluno["DataDeNascimento"]} | Nota: {aluno["Nota"]}")

    else:
        print("A lista de Alunos está vazia!")
        resposta = input("Pretende adicionar um aluno (s/n)?")
        while resposta.lower() != "s" and resposta.lower() != "n":
            print("A sua resposta não é válida!")
            resposta = input("Pretende adicionar um aluno (s/n)?")
        
        if resposta == "s":
            os.system("cls")
            adicionarAluno(lstAlunos)

def atualizarRegisto(lstAlunos:list):
    idResposta = input("Indique o id do Aluno que pretende atualizar: ")
    atualizar = ""
    while atualizar != "s":
        i=0
        if lstAlunos[i]["Id"] == idResposta:
            print(f"ID: {lstAlunos[i]["Id"]} | Nome: {lstAlunos[i]["Nome"]} | Email: {lstAlunos[i]["Email"]} | Telefone: {lstAlunos[i]["Telefone"]} | Data Nascimento: {lstAlunos[i]["DataDeNascimento"]} | Nota: {lstAlunos[i]["Nota"]}")
            atualizar = input("Pretnde editar este aluno?")
        i+=1
    for atributo in lstAlunos[int(idResposta)]:
        resposta = input(f"Pretende atulizar {atributo} do Aluno?")
        


while True:
    os.system("cls")
    opcaoMenu = mostrarMenu()

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
        case "5":
            break
        case _:
            os.system("cls")
            print("Opção inválida!")
            input()