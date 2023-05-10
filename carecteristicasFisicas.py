idade = int(input("Idade :"))
somaIdade = 0
fovcl = 0
maior = idade
i = 0
while idade > 0:
    sexo = input("Sexo (masculino ou feminino): ")
    olho = input("Cor dos olhos (azuis, verdes ou castanhos): ")
    cabelo = input("Cor do cabelo (loiro, castanho ou preto): ")
    i += 1
    if idade > maior:
        maior = idade
    if sexo == "feminino" and (idade >= 18 and idade <= 35) and olho == "verdes" \
       and cabelo == "loiro":
        fovcl += 1
    idade = int(input("Idade :"))
if maior > 0:
    print("A maior idade e", maior)
if fovcl > 0:
    porcentagem = (fovcl / i)*100
    print("A porcentagem de individuos femininos com idade entre 18 e 35 anos com \
olhos verdes e cabelos loiros de",porcentagem)
