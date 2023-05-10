idade = int(input("Qual a idade? "))
maior_s = 0
soma_m = 0
soma_f = 0
count_m = 0
count_f = 0
while idade >= 0:
    sexo = input("Qual o sexo (M ou F)? ")
    salario = float(input("Salario R$ "))
    if idade < 30 and salario > maior_s:
            maior_s = salario
    if sexo == "M":
        soma_m = soma_m + salario
        count_m += 1
    else:
        soma_f = soma_f + salario
        count_f += 1
    idade = int(input("Qual a idade? "))
if count_m > 0:
    media_m = soma_m / count_m
    print("A media salario entre os homens e de R$", media_m)
if count_f > 0:
    media_f = soma_f / count_f
    print("A media salario entre as muheres e de R$", media_f)
if maior_s > 0:
    print("O maior salario entre pessoas abaixo dos 30 anos e de R$", maior_s)
