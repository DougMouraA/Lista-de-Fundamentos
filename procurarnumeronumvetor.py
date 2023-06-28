n = []
i = 0
cont = 0
n.append(int(input("Digite um numer: ")))
while n[i] >= 0:
    n.append(int(input("Digite um numer: ")))
    i += 1
proc = int(input("valor a encontrar: "))
achou = False
for j in range(0, len(n)):
    if n[j] == proc:
        cont = j
        achou = True
if achou == True:
    print(cont)
else:
    print("valor nao encontrado")
