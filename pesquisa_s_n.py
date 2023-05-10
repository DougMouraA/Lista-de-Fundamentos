s = 0
n = 0
somapn = 0
for i in range(4):
    gostou = input("Gostou (s ou n)? ")
    sexo = input("Sexo (masculino ou feminino): ")
    if gostou == "s":
        s +=1
    else:
        n +=1
    if sexo == "masculino" and gostou == "n":
        somapn +=1
print("O numero de pessoas que gostaram foram de", s," e de pessoas que nao gostaram \
foi de", n)
if somapn > 0:
    porcentagem = (somapn / n)*100
    print("A porcentagem de pessoas do sexo masculino que nao gostaram foi de",porcentagem,"\
%")
