soma = 0
cont = 0
notas = [0.0]*10
for i in range(0, 10):
    notas.append(float(input("nota: ")))
    soma += notas[i]
media = soma / 10
print("A media da turma foi:", media)
for j in range(0, 10):
    if notas[j] > media:
        cont += 1
print("A quantidade de alunos com nota acima da media da turma e de", cont)
