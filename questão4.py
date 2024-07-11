print("Bem vindos a empresa de Matheus Guirra Vieira")

lista_funcionarios = []
id_global = 4907350


#funcao para cadastrar funcionarios
def cadastrar_funcionario(id):
    global lista_funcionarios

    print("---- CADASTRAR FUNCIONÁRIO ----")
    print(f"Id do funcionário: {id_global}")
    nome_funcionario = input("Digite o nome do funcionário: ")
    setor_funcionario = input("Digite o setor do funcionário: ")
    salario = int(input("Digite o salário do funcionário: "))

    #armazenando dados fornecidos pelo usuario em um dicionario
    novo_funcionario = {"nome": nome_funcionario, "setor": setor_funcionario, "salario": salario, "id": id}

    #copiando o dicionario em uma lista e adicionando seu valor
    lista_funcionarios.append(novo_funcionario.copy())

    return lista_funcionarios

#funcao para consultar funcionarios
def consultar_funcionarios():
    global lista_funcionarios

    #while para repetir as opções enquanto o usuario nao opatar para sair
    while True:
        print("---- CONSULTAR FUNCIONÁRIO ----")
        opcao = int(input(
            "Qual opção deseja?\n 1- Consultar todos\n 2- Consultar por Id\n 3- Consultar por setor\n 4- Retornar ao menu\n "))
        try:
            if opcao == 1:
                #exibe todos os funcionarios disponiveis na lista
                for funcionario in lista_funcionarios:
                    print(funcionario)
            elif opcao == 2:
                id = int(input("Digite o id do funcionario: "))
                for id_funcionario in lista_funcionarios:
                    #compara o id digitado pelo usuario com os que estao disponiveis na lista
                    if id_funcionario["id"] == id:
                        print(id_funcionario)
            elif opcao == 3:
                setor = input("Digite o setor do funcionario: ")
                for funcionarios_setor in lista_funcionarios:
                    # compara o setor digitado pelo usuario com os que estao disponiveis na lista
                    if funcionarios_setor["setor"] == setor:
                        print(funcionarios_setor)
            elif opcao == 4:
                #retornar ao menu principal
                return main()
            else:
                print("Opção inválida")
        except ValueError:
            print("Opção inválida")

#funcao para remover funcionario mediante o id fornecido
def remover_funcionario():
    while True:
        try:
            print("---- REMOVER FUNCIONÁRIO ----")
            id_funcionario = int(input("Digite o id do funcionario: "))
            for id_funcionarios in lista_funcionarios:
                # compara o id digitado pelo usuario com os que estao disponiveis na lista
                if id_funcionarios["id"] == id_funcionario:
                    lista_funcionarios.remove(id_funcionarios)
                    print("Funcionario removido!")
                    return lista_funcionarios
            else:
                print("Id não encontrado")
        except ValueError:
            print("Id inválido")


def main():
    global id_global

    while True:
        try:
            print("---- MENU PRINCIPAL ----")
            opcao = int(input(
                "Escolha uma opção\n 1- Cadastrar funcionários\n 2- Consultar funcionário(s)\n 3- Remover funcionário\n 4- Sair\n "))
            if opcao == 1:
                id_global += 1
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
