def palindromo(plvr):
    sim  = 0
    for i in range(0, len(plvr) // 2):
        if plvr[i] != plvr[len(plvr) -i -1]:
            sim = 1
    if sim == 0:
        return 0
    sim = 0
    tamanho = len(plvr)
    if tamanho % 2 != 0:
        tamanho = tamanho - 1
        sim += 1
    for i in range (0, tamanho, 2):
        p = i - 2
        check = 0
        while (p >= 0):
            if (plvr[i] == plvr[p] and plvr[i + 1] == plvr[p + 1]):
                check = 1
            p = p - 2
        if check == 0:
            sim += 1
    return sim

palavra = input("Digite uma palavra: ")
resultado = palindromo(palavra)
print("Número de pares diferentes consecutivos:", resultado)
