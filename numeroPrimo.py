cont = 0
n = int(input("Digite um numero: "))
for i in range(2,n):
    if(n%i == 0):
        cont += 1
if cont == 0 and n!= 1:
    print("E primo")
else:
    print("Nao E primo")
        
