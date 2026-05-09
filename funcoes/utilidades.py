import re
import json

def carregarFicheiro():
    try:
        with open("alunos.json", "r", encoding="utf-8") as ficheiro:
            return json.load(ficheiro)
    except FileNotFoundError:
        return []
    except Exception as erro:
        print(f"Erro ao carregar ficheiro: {erro}")
        return []

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

def validarEmail(email:str):
    reg = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
    return re.match(reg, email) is not None

def validarTelefone(telefone:str):
    reg = r"^9[1236]\d{7}$"
    return re.match(reg, telefone) is not None

def validarData(data:str):
    reg = r"\d{1,2}\/\d{1,2}\/\d{4}"
    return re.match(reg, data) is not None

def guardarFicheiro(lstAlunos:list):
    try:
        with open("alunos.json", "w", encoding="utf-8") as ficheiro:
            json.dump(lstAlunos, ficheiro, indent="   ", ensure_ascii=True)
        print("Dados guardados com sucesso!")
    except Exception as erro:
        print(f"Erro ao guardar os dados: {erro}")