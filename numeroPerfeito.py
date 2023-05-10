n = int(input("Digite um numero: "))
soma = 0
for i in range(1, (n//2)+ 1):
    if n % i == 0:
        soma +=i
if soma == n:
    print("E um numero perfeito")
else:
    print("Nao e um numero perfeito")
