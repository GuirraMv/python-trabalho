print("Bem-vindo a loja do Matheus Guirra Vieira")
valor_pedido = float(input("Digite o valor do pedido: "))
quantidade_parcelas = int(input("Digite a quantidade de parcelas: "))
juros: float = 0

# faz a verificação de quantas parcelas o usuário escolheu e aplica a fórmula do juros
if quantidade_parcelas < 4:
    juros = 0 / 100
elif quantidade_parcelas >= 4 and quantidade_parcelas < 6:
    juros = 4 / 100
elif quantidade_parcelas >= 6 and quantidade_parcelas < 9:
    juros = 9 / 100
elif quantidade_parcelas >= 9 and quantidade_parcelas < 13:
    juros = 16 / 100
else:
    juros = 32 / 100

# faz o cálculo da valor da parcela utilizando o valor do juros que foi obtido anteriormente no if
valor_parcela = valor_pedido * (1 + juros) / quantidade_parcelas

# obtém o valor total do pedido
valor_total = valor_parcela * quantidade_parcelas

print(f"O valor das parcelas é de: R${valor_parcela:.2f}")
print(f"O valor total da compra é: R${valor_total:.2f}")