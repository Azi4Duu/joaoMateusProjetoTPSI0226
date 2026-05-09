import os
from funcoes.utilidades import *
from logica.algoritmos import *

alunos = carregarFicheiro()

def adicionarAluno(lstAlunos:list):
    novoId = gerarNovoID(lstAlunos)
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
                    print(f"\nID: {resultado["Id"]} | Nome: {resultado["Nome"]} | Email: {resultado["Email"]} | Telefone: {resultado["Telefone"]} | Data Nascimento: {resultado["DataDeNascimento"]} | Nota: {resultado["Nota"]}")
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
        print(f"A Editar Aluno (ID: {alunoEncontrado['Id']})")
        print(f"Nome Atual: {alunoEncontrado['Nome']}")
        
        confirmar = input("Pretende mesmo editar este aluno? (s/n): ").lower()
        
        if confirmar == "s":
            novoNome = input(f"Novo Nome [{alunoEncontrado["Nome"]}]: ")
            if novoNome: alunoEncontrado["Nome"] = novoNome

            while True:
                novoEmail = input(f"Novo Email [{alunoEncontrado["Email"]}]: ")
                if not novoEmail:
                    break
                if validarEmail(novoEmail):
                    alunoEncontrado["Email"] = novoEmail
                    break
                print("Email inválido!")
            
            while True:
                novoTelefone = input(f"Novo Telefone [{alunoEncontrado["Telefone"]}]: ")
                if not novoTelefone:
                    break
                if validarTelefone(novoTelefone):
                    alunoEncontrado["Telefone"] = novoTelefone
                    break
                print("Telefone inválido!")
            
            while True:
                novaData = input(f"Nova Data de Nascimento DD/MM/AAAA [{alunoEncontrado["DataDeNascimento"]}]: ")
                if not novaData:
                    break
                if validarData(novaData):
                    alunoEncontrado["DataDeNascimento"] = novaData
                    break
                print("Data inválida!")

            while True:
                novaNotaInput = input(f"Nova Nota [{alunoEncontrado["Nota"]}]: ")
                if not novaNotaInput:
                    break
                try:
                    novaNota = float(novaNotaInput)
                    if novaNota >= 0 and novaNota <= 20:
                        alunoEncontrado["Nota"] = novaNota
                        break
                    else:
                        print("A nota deve estar entre 0 e 20!")
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
        confimar = input("Tem a certeza que deseja eliminar este registo (s/n)? ").lower()
        if confimar == "s":
            lstAlunos.remove(aluno)
            print("Registo eliminado com sucesso!")
        else:
            print("Operação cancelada!")
    else:
        print("Aluno não encontrado!")

def mostrarEstatistica(lstAlunos:list):
    if not lstAlunos:
        print("A lista de Alunos está vazia!")
    
    notas = []

    for aluno in lstAlunos:
        notas.append(float(aluno["Nota"]))

    media = sum(notas) / len(notas)
    notaMax = max(notas)
    notaMin = min(notas)

    print("+------------+")
    print("|ESTATÍSTICAS|")
    print("+------------+\n")
    print(f"Media: {round(media, 2)}")
    print(f"Melhor Nota: {notaMax}")
    print(f"Pior Nota: {notaMin}")
    print(f"Total de Alunos: {len(lstAlunos)}")

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
            os.system("cls")
            atualizarRegisto(alunos)
            input()
        case "4":
            os.system("cls")
            eliminarRegisto(alunos)
            input()
        case "5":
            os.system("cls")
            mostrarEstatistica(alunos)
            input()
        case "6":
            os.system("cls")
            guardarFicheiro(alunos)
            input()
        case "7":
            break
        case _:
            os.system("cls")
            print("Opção inválida!")
            input()