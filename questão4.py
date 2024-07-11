print("Bem vindos a empresa de Matheus Guirra Vieira")

lista_funcionarios = []
id_global = 4907350

def cadastrar_funcionario(id):
    global lista_funcionarios

    print("---- CADASTRAR FUNCIONÁRIO ----")
    nome_funcionario = input("Digite o nome do funcionário: ")
    setor_funcionario = input("Digite o setor do funcionário: ")
    salario = int(input("Digite o salário do funcionário: "))

    novo_funcionario = {"nome": nome_funcionario, "setor": setor_funcionario, "salario": salario, "id": id}

    lista_funcionarios.append(novo_funcionario.copy())

    return lista_funcionarios

def consultar_funcionarios():
    global lista_funcionarios
    while True:
        print("---- CONSULTAR FUNCIONÁRIO ----")
        opcao = int(input(
            "Qual opção deseja?\n 1- Consultar todos\n 2- Consultar por Id\n 3- Consultar por setor\n 4- Retornar ao menu\n "))
        try:
            if opcao == 1:
                print(lista_funcionarios)
            elif opcao == 2:
                id_funcionario = int(input("Digite o id do funcionario: "))
                for id_funcionario in lista_funcionarios:
                    if id_funcionario["id" == id_funcionario]:
                        print(id_funcionario)
            elif opcao == 3:
                setor = input("Digite o setor do funcionario: ")
                for funcionarios_setor in lista_funcionarios:
                    if funcionarios_setor["setor" == setor]:
                        print(funcionarios_setor)
            elif opcao == 4:
                #retornar ao menu principal
                break
            else: print("Opção inválida")
        except ValueError: print("Opção inválida")

def remover_funcionario():
    while True:
        try:
            print("---- REMOVER FUNCIONÁRIO ----")
            id_funcionario = int(input("Digite o id do funcionario: "))
            for id_funcionario in lista_funcionarios:
                if id_funcionario["id"] == id_funcionario:
                    lista_funcionarios.remove(id_funcionario)
            else:
                print("Id inválido")
        except ValueError: print("Id inválido")
def main():
    global id_global

    while True:
        try:
            opcao = int(input("Menu principal\n Escolha uma opção\n 1- Cadastrar funcionários\n 2- Consultar funcionário(s)\n 3- Remover funcionário\n 4- Sair\n "))
            if opcao == 1:
                cadastrar_funcionario(id_global)
            elif opcao == 2:
                consultar_funcionarios()
            elif opcao == 3:
                remover_funcionario()
            else:
                break
        except ValueError:
            print("Opção inválida")


if __name__ == "__main__":
    main()
