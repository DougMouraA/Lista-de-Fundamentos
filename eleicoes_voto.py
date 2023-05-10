c1 = 0
c2 = 0
c3 = 0
c4 = 0
c5 = 0
for i in range(10):
    i = int(input("Digite o Numero do seu candidato. 1 - Joao, \
2 - Jose, 3 - Maria, 4 - Voto em Branco e 5 - Voto nulo: "))
    if i == 1:
        c1 += 1
    elif i == 2:
        c2 += 1
    elif i == 3:
        c3 += 1
    elif i == 4:
        c4 += 1
    elif i == 5:
        c5 += 1
    else:
        print("Voto invalido")
        
print("Candidato 1 recebeu", c1,"votos")
print("Candidato 2 recebeu", c2,"votos")
print("Candidato 3 recebeu", c3,"votos")
print("Votos em Branco", c4)
print("Votos nulos", c5)
if c1 > c2 and c1 > c3:
    print("O candidato mais votado é o Joao da Silva!")
elif c2 > c3:
    print("O candidato mais votado é o Jose Ramalho!")
else:
    print("O candidato mais votado é a Maria Mattos")
