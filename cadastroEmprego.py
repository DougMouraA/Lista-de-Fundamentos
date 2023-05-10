ins = 1
m = 0
h = 0
hxp = 0
mixp = 0
mais45 = 0
fixp = 0
while ins > 0:
    ins = int(input("Numero de inscricao do candidato: "))
    idade = int(input("Idade: "))
    sexo = input("Sexo (masculino ou feminino): ")
    xp = input("Experiencia (sim ou nao): ")
    if sexo == "masculino":
        h +=1
    else:
        m +=1
    if sexo == "masculino" and xp == "sim":
        mixp += idade
        hxp +=1
    if sexo == "masculino" and idade > 45:
        mais45 += 1
    if sexo == "feminino" and idade < 35 and xp == "sim":
        menorIf = idade
        fixp += 1
        if idade < menorIf:
            menorIf = idade
if h > 0:
    print("O numero de candidatos homens e de:", h)
    media = mixp // hxp
    print("A idade media entre os homens com experiencia e de", media)
    p = (mais45 / h)*100
    print("O percentual de homens com mais de 45 com experiencia e de",p,"%")
if m > 0:
    print("O numero de candidatas mulheres e de:", m)
    print("Mulheres com menos de 35 anos com experiencia e de",fixp)
    print("A menor idade entre as mulheres com experiencia e de", menorIf)
