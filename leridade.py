n = True
soma = 0
total = 0
i = 0
while n == True:
    idade = int(input("Idade: "))
    if idade >= 21 and idade <= 65:
        soma += idade
    total += idade
    i += 1
    if idade == 100:
        n = False
media = total / i
porcentagem = (soma / total)*100
print("A idade media do grupo e de", media)
print("A porcentagem de pessoas com idade de 21 a 65 anos e de", porcentagem,"%")
