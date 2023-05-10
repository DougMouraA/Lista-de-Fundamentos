sexo = input("Qual o sexo? ")
sexo = sexo.lower()
peso_ideal = 0
if sexo == "h" or sexo == "homem":
    peso = float(input("e o seu peso? "))
    altura = float(input("e sua altura? "))
    peso_ideal = (72.7*altura)-58.0
    print("O peso ideal para um homem é:", peso_ideal)
elif sexo == "m" or sexo == "mulher":
    peso = float(input("e o seu peso? "))
    altura = float(input("e sua altura? "))
    peso_ideal = (62.1*altura)-44.7
    print("O peso ideal para um mulher é:", peso_ideal)
else:
    print("Informacao invalida!")
