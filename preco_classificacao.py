valor = float(input("Valor do produto: "))
preco = 0
if valor <= 50:
    preco = valor + (0.05*valor)
elif valor <= 100:
    preco = valor + (0.10*valor)
else:
    preco = valor + (0.15*valor)

if preco <= 80:
    print("Classificacao: Barato -> ", preco)
elif preco <= 120:
    print("Classificacao: Normal -> ", preco)
elif preco <= 200:
    print("Classificacao: Caro -> ", preco)
else:
    print("Classificacao: Muito Caro ->", preco)
