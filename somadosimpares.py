n = int(input("Digite a quantidade de numeros inteiros: "))
soma_i = 0
for i in range(n):
    if i % 2 != 0 and i > 0:
        soma_i += i
print(soma_i)
