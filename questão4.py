#cadastrar, consultar, remover e encerrar programa
print("Bem vindos a empresa de Matheus Guirra Vieira")

lista_funcionarios = []
id_global = 4907350

def cadastrar_funcionario(id):
    novo_funcionario = {"nome": [], "setor": [], "salário": [], "id": []}

    nome_funcionario = input("Digite o nome do funcionário: ")
    setor_funcionario = input("Digite o setor do funcionário: ")
    salario = int(input("Digite o salário do funcionário: "))

    novo_funcionario["nome"].append(nome_funcionario)
    novo_funcionario["setor"].append(setor_funcionario)
    novo_funcionario["salário"].append(salario)
    novo_funcionario["id"].append(id)
    print(novo_funcionario)
    lista_funcionarios = novo_funcionario.copy()
    print(lista_funcionarios)
    return lista_funcionarios




def consultar_funcionarios():
    while True:
        opcao = int(input(
            "Qual opção deseja?\n 1- Consultar todos\n 2- Consultar por Id\n 3- Consultar por setor\n 4- Retornar ao menu\n "))
        try:
            if opcao == 1:
                print(lista_funcionarios)
                break
            elif opcao == 2:
                id_funcionario = int(input("Digite o id do funcionario: "))
                break
            elif opcao == 3:
                setor = input("Digite o setor do funcionario: ")
            elif opcao == 4: continue
            else: print("Opção inválida")
        except ValueError: print("")

def remover_funcionario():
    id_funcionario = int(input("Digite o id do funcionario: "))
    remove = lista_funcionarios.remove(id_funcionario)


def main():
    while True:
        opcao = int(input("Menu principal\n Escolha uma opção\n 1- Cadastrar funcionários\n 2- Consultar funcionário(s)\n 3- Remover funcionário\n 4- Sair"))
        if opcao == 1:
            id_funcionario = input("")
            cadastrar_funcionario(id)

if __name__ == "__main__":
    main()
