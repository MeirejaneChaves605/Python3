
# lê o custo de fábrica
custo_fabrica = float(input("Digite o custo de fábrica do carro: R$ "))
# calcula a porcentagem do distribuidor e dos impostos (sobre o custo de fábrica)
percent_distribuidor = 0.12 * custo_fabrica
impostos = 0.30 * custo_fabrica
# calcula o custo final ao consumidor
custo_final = custo_fabrica + percent_distribuidor + impostos
# exibe o resultado
print(f"Custo ao consumidor: R$ {custo_final:.2f}")