import os

def mostrarMenu():
    print("+-----MENU----+")
    print("| 1 - Inserir |")
    print("| 2 - Listar  |")
    print("| 3 - Sair    |")
    print("+-------------+")
    opcao = input("Escolha uma opção: ")
    return opcao

alunos = []

def adicionarAluno(lstAlunos:list):
    novoId = len(alunos) + 1
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


while True:
    os.system("cls")
    opcao = mostrarMenu()

    match opcao:
        case "1":
            os.system("cls")
            adicionarAluno(alunos)
            input()
        case "2":
            os.system("cls")
            listarAlunos(alunos)
            input()
        case "3":
            break
        case _:
            print("Opção inválida")