p = 0
i = 0
somapar = 0
n = int(input("Digite um numero: "))
while n > 0:
    if n % 2 == 0:
        somapar  += n
        p += 1
    else:
        i += 1
    n = int(input("Digite um numero: "))
print("Há", p,"numeros pares e", i,"impares")
if somapar > 0:
    media = somapar / p
    print("A media entre os numeros pares e de",media)
