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



def listarAlunos(lstAlunos:list):

    if len(lstAlunos) > 0:

        print("+-----------MENU LISTAR----------+")
        print("| 1 - Listar os Alunos por ID    |")
        print("| 2 - Listar os Alunos por nome  |")
        print("| 3 - Pesquisar Aluno por ID     |")
        print("| 4 - Pesquisar Aluno por nome   |")
        print("| 5 - Listar todos os Alunos     |")
        print("+--------------------------------+")

        for aluno in lstAlunos:
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