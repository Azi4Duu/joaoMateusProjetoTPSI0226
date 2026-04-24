def mostrarMenu():
    print("+-----MENU----+")
    print("| 1 - Inserir |")
    print("| 2 - Listar  |")
    print("| 3 - Sair    |")
    print("+-------------+")
    opcao = input("Escolha uma opção: ")
    return opcao

alunos = []

def adicionarAluno(nome, email, telefone, dataNascimento, nota):
    novoId = len(alunos) + 1
    aluno = {"Id" : novoId, "Nome" : nome, "Email" : email, "Telefone" : telefone, "DataDeNascimento" : dataNascimento, "Nota" : nota}
    alunos.append(aluno)
    print(f"\nO Aluno {aluno["Nome"]} foi registado com sucesso com o ID: {aluno["Id"]}!")

while True:
    opcao = mostrarMenu()
    
    match opcao:
        case "1":
            nome = input("Nome: ")
            email = input("Email: ")
            telefone = input("Telefone: ")
            dataNascimento = input("Data de Nascimento: ")
            nota = input("Nota: ")

            adicionarAluno(nome, email, telefone, dataNascimento, nota)
        case "2":
            for aluno in alunos:
                print(f"\nID: {aluno["Id"]} | Nome: {aluno["Nome"]} | Email: {aluno["Email"]} | Telefone: {aluno["Telefone"]} | Data Nascimento: {aluno["DataDeNascimento"]} | Nota: {aluno["Nota"]}")
        case "3":
            break
        case _:
            print("Opção inválida")