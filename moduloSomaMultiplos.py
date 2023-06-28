def retornaDiferenca(n1, n2):
    soma7 = 0
    soma13 = 0
    diferenca = 0
    if n1 > n2:
        return False
    for i in range(n1+1, n2):
        if i % 7 == 0:
            soma7 += i
        elif i % 13 == 0:
            soma13 += i
    diferenca = soma7 - soma13
    return diferenca

n1 = int(input("Digite o primeiro valor: "))
n2 = int(input("Digite o segundo valor: "))
diferenca = retornaDiferenca(n1, n2)
if not diferenca:
    print("Primeiro valor maior que o segundo!")
else:
    print(diferenca)
