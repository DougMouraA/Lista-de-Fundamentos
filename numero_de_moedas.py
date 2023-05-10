valor = float(input("valor em R$: "))
cont = valor
if cont >= 1:
    moeda = cont // 1
    print("Numero de moedas de 1 Real:", moeda)
    cont = cont % 1
if cont >= 0.50:
    moeda = cont // 0.50
    print("Numero de moedas de 50 centavos:", moeda)
    cont = cont % 0.50
if cont >= 0.25:
    moeda = cont // 0.25
    print("Numero de moedas de 25 centavos:", moeda)
    cont = cont % 0.25
if cont >= 0.10:
    moeda = cont // 0.10
    print("Numero de moedas de 10 centavos:", moeda)
    cont = cont % 0.10
if cont >= 0.05:
    moeda = cont // 0.05
    print("Numero de moedas de 5 centavos:", moeda)
    cont = cont % 0.05
if cont >= 0.01:
    moeda = cont // 0.01
    print("Numero de moedas de 1 centavos:", moeda)
print("o valor total calculado foi de:", valor)
