for i in range(3):
    n = int(input("Numero de identificacao: "))
    peso = float(input("Peso Kg: "))
    if i == 0:
        maior = peso
        menor = peso
        identMaior = n
        identMenor = n
    if peso > maior:
        maior = peso
        identMaior = n
    if peso < menor:
        menor = peso
        identMenor = n
if maior > 0:
    print("O boi mais gordo e", identMaior,"com o peso de",maior,"kg")
if menor > 0:
    print("O boi mais gordo e", identMenor,"com o peso de",menor,"kg")
