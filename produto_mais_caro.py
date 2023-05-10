n_maior = ""
maior = 0
produto = input("Nome do produto: ")
while produto != "XXX":
    preco = float(input("Preco: "))
    if preco > maior:
        maior = preco
        n_maior = produto
    produto = input("Nome do produto: ")
print(n_maior)
