c1 = input("Nome do candidato: ")
v_c1 = int(input("Numero de votos do candidato: "))
c2 = input("Nome do candidato: ")
v_c2 = int(input("Numero de votos do candidato: "))
c3 = input("Nome do candidato: ")
v_c3 = int(input("Numero de votos do candidato: "))
total = v_c1 + v_c2 + v_c3
p_c1 = (v_c1 / total)*100
p_c2 = (v_c2 / total)*100
p_c3 = (v_c3 / total)*100
if p_c1 > 50:
    print("O candidato",c1,"ganhou as eleicoes com",p_c1,"% dos votos \
com um numero de votos de", v_c1)
elif p_c2 > 50:
    print("O candidato",c2,"ganhou as eleicoes com",p_c2,"% dos votos \
com um numero de votos de", v_c2)
elif p_c3 > 50:
    print("O candidato",c3,"ganhou as eleicoes com",p_c3,"% dos votos \
com um numero de votos de", v_c3)
else:
    print("As eleicoes terá segundo turno.")
