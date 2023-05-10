total = 0
valor = 0
for i in range(2):
    i = float(input("Preco do produto: "))
    qtd = int(input("Quantidade do produto: "))
    valor = i * qtd
    total += valor
print("O valor total de gasto e de", total)
