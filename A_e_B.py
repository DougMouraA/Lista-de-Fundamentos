a = int(input("Digite o valor de A: "))
b = int(input("Digite o valor de B: "))
soma = 0
if a >= b:
    print("Nao e possivel fazer a soma, pois A e maior que B")
n = a + 1
while n < b:
    soma += n
    n += 1
if soma > 0:
    print("A soma dos numetos entre A e B e", soma)
