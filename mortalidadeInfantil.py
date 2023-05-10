i = 0
m = 0
tm = 0
n = int(input("Numero de criancas nascidas no periodo: "))
sexo = input("Sexo (masculino ou feminino): ")
while sexo != "vazio":
    meses = int(input("Meses: "))
    i += 1
    if sexo == "masculino":
        m +=1
    if meses <= 24:
      tm +=1  
    sexo = input("Sexo (masculino ou feminino): ")
if i > 0:
    morte = (i / n)*100
    mortesM = (m / i)*100
    morteTempo = (tm / i)*100
    print("Nesse periodo,",n,"criancas nasceram e. Nesse mesmo periodo,",morte,"% criancas\
morreram")
    print("Dentro dessa porcentagem,",mortesM,"% eram do sexo masculino e",morteTempo,"\
% tinham menos até 24 meses de vida")
