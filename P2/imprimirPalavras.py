def qtdPalavras(frase):
    cont = 1
    for i in range(0, len(frase)):
        if frase[i] == " ":
            cont += 1
    return cont

def imprimiPalavra(frase, vetPalavra):
    palavra = ""
    j = 0
    for i in range(0, len(frase)):
        if frase[i] != " ":
            palavra += frase[i]
        if frase[i] == " " or i == len(frase) - 1:
            if palavra != "":
                vetPalavra[j] = palavra
                j+=1
                palavra = ""
    return vetPalavra


frase = input("Digite uma frase: ")
vetPalavra = [0]*qtdPalavras(frase)
vetPalavra = imprimiPalavra(frase, vetPalavra)
print(vetPalavra)
