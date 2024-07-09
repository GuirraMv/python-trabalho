print("Bem vindo(a) a loja de marmitas do Matheus Guirra Vieira")
print("--------Confira o nosso cardápio-------------")
print("Tamanho || Bife acebolado ||  Filé de frango")
print("  P     ||    16,00       ||   15,00         ")
print("  M     ||    18,00       ||   17,00         ")
print("  G     ||    22,00       ||   21,00         ")

# listagem do valor dos pedidos
Bife_acebolado_pequeno: float = 16.00
File_frango_pequeno: float = 15.00
Bife_acebolado_medio: float = 18.00
File_frango_medio: float = 17.00
Bife_acebolado_grande: float = 22.00
File_frango_grande: float = 21.00

# variável para mostrar o valor do pedido atual
valor_pedido: float = 0

# inicializa a variável acumuladora
valor_total: float = 0

# variável para mostrar o nome do pedido atual
nome_pedido: str = ""

while True:
    sabor = input("Selecione o sabor da sua marmita.\n Digite BA para bife acebolado e FF para Filé de frango: ")
    # verifica o sabor da marmita
    if sabor == "BA" or sabor == "ba" or sabor == "FF" or sabor == "ff":
        tamanho = input("Escolha o tamanho da marmita.\n Digite P para pequena, M para média e G para grande : ")
        # verifica o tamanho da marmita
        if tamanho == "P" or tamanho == "p" or tamanho == "M" or tamanho == "m" or tamanho == "G" or tamanho == "g":
            if sabor == "BA" or sabor == "ba" and tamanho == "P" or tamanho == "p":
                valor_pedido = Bife_acebolado_pequeno
                valor_total += Bife_acebolado_pequeno
                nome_pedido = "Bife acebolado pequeno"
            elif sabor == "FF" or sabor == "ff" and tamanho == "P" or tamanho == "p":
                valor_pedido = File_frango_pequeno
                valor_total += File_frango_pequeno
                nome_pedido = "Filé de frango pequeno"
            elif sabor == "BA" or sabor == "ba" and tamanho == "M" or tamanho == "m":
                valor_pedido = Bife_acebolado_medio
                valor_total += Bife_acebolado_medio
                nome_pedido = "Bife acebolado medio"
            elif sabor == "FF" or sabor == "ff" and tamanho == "M" or tamanho == "m":
                valor_pedido = File_frango_medio
                valor_total += File_frango_medio
                nome_pedido = "Filé de frango medio"
            elif sabor == "BA" or sabor == "ba" and tamanho == "G" or tamanho == "g":
                valor_pedido = Bife_acebolado_grande
                valor_total += Bife_acebolado_grande
                nome_pedido = "Bife acebolado grande"
            else:
                valor_pedido = File_frango_grande
                valor_total += File_frango_grande
                nome_pedido = "Filé de frango grande"
            print(f"Você pediu {nome_pedido} no valor de: R${valor_pedido}")
            # decide se finaliza ou não a execução do while
            finalizar = input('Deseja pedir mais alguma coisa?\n Responda usando "sim" ou "não"')
            if finalizar == "sim" or finalizar == "SIM":
                continue
            else:
                print(f"Seu pedido ficou no valor de R${valor_total}.\n Agradecemos a preferênica!")
                break
        else:
            print("Tamanho inválido. Tente novamente.")
    else:
        print("Sabor inválido. Tente novamente.")