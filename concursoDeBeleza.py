altura1 = 0
altura2 = 0
i = 0
j = 0
nome = ""
while nome != "Maria":
    nome = input("Nome: ")
    altura = float(input("Altura: "))
    if altura == altura1:
        i +=1
    if altura == altura2:
        j +=1
    if altura > altura1:
        altura2 = altura1
        altura1 = altura
        j = i
        i = 1
    elif altura > altura2:
        altura2 = altura
        j = 1
print("A maior altura e", altura1,"com", i,"mocas. A segunda maior altura e",altura2,"com \
com", j,"mocas")
