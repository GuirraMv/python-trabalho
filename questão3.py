print("Bem vindo à fábrica de camisetas do Matheus Guirra Vieira")

modelo_camisa: str = ""
desconto: float = 0
taxa_frete: int = 0
valor_camisa: int = 0
numero_camisetas: int = 0
total_compra: float = 0

MCS: float = 1.80
MLS: float = 2.10
MCE: float = 2.90
MLE: float = 3.20


def escolha_modelo():
    valor: int = 0
    global valor_camisa
    global modelo_camisa

    while True:
        modelo_selecionado = input(
            "Informe o modelo desejado da camisa\n Utilize MCS para Camisa Manga Curta Simples\n MLS para Camisa Manga Longa Simples\n MCE para Camisa manga curta com estampa \n MLE para Camisa  manga longa com estampa: ")
        try:
            if modelo_selecionado == "MCS":
                modelo = "Camiseta Manga Curta Simples"
                valor += MCS
                break
            elif modelo_selecionado == "MLS":
                modelo = "Camiseta Manga Longa Simples"
                valor += MLS
                break
            elif modelo_selecionado == "MCE":
                modelo = "Camiseta Manga Curta Com Estampa"
                valor += MCE
                break
            elif modelo_selecionado == "MLE":
                modelo = "Camiseta Manga Longa Com Estampa"
                valor += MLE
                break
            else:
                print("Erro ao inserir o modelo.\n Escolha uma opção válida!")
        except ValueError:
            print("Escolha um valor válido")
    modelo_camisa = modelo
    valor_camisa += valor
    return valor_camisa, modelo_camisa


def num_camisetas(valor_camisa):
    global numero_camisetas
    while True:
        try:
            camisetas = int(input("Quantas camisetas deseja? "))
            total = valor_camisa * camisetas
            if camisetas < 20:
                desconto = 0
                break
            elif camisetas >= 20 and camisetas < 200:
                desconto = 5 / 100
                break
            elif camisetas >= 200 and camisetas < 2000:
                desconto = 7 / 100
                break
            elif camisetas >= 2000 and camisetas <= 20000:
                desconto = 12 / 100
                break
            else:
                print("Não aceitamos tantas camisetas!")
        except ValueError:
            print("Digite apenas números")
    numero_camisetas += camisetas
    valor_desconto = total * desconto
    camisa_desconto = total - valor_desconto
    return camisa_desconto, numero_camisetas


def frete():
    frete = 0
    global taxa_frete
    while True:
        try:
            transportadora = int(input(
                "Informe o tipo de frete.\n Utilize 1 para transportadora, 2 para Sedex e 0 para retirar na fábrica: "))
            if transportadora == 1:
                frete += 100
                break
            elif transportadora == 2:
                frete += 200
                break
            elif transportadora == 0:
                frete += 0
                break
            else:
                print("Erro ao escolher o transporta. Utilize um valor válido")
        except ValueError:
            print("Insira somente números")
    taxa_frete += frete
    return taxa_frete


def main():
    global total_compra
    escolha_modelo()
    num_camisetas(valor_camisa)
    frete()
    total_compra += (valor_camisa * numero_camisetas) + taxa_frete
    print(
        f"Resumo da compra: Camiseta: {modelo_camisa}, Quantidade: {numero_camisetas}, frete: R${taxa_frete}.\n O total com desconto e frete ficou em: R${total_compra}")


if __name__ == '__main__':
    main()
