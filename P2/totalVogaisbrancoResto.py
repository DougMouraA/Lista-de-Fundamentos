def totalResto(frase):
    contR = 0
    for i in range(0, len(frase)):
        if not(frase[i].lower() == "a" or frase[i].lower() == "e" or frase[i].lower() == "i"\
           or frase[i].lower() == "o" or frase[i].lower() == "u") and \
           frase[i] != " ":
            contR += 1
    return contR
           

def totalBranco(frase):
    contB = 0
    for i in range(0, len(frase)):
        if frase[i] == " ":
            contB += 1
    return contB

def totalVogais(frase):
    contV = 0
    for i in range(0, len(frase)):
        if frase[i].lower() == "a" or frase[i].lower() == "e" or frase[i].lower() == "i"\
           or frase[i].lower() == "o" or frase[i].lower() == "u":
            contV += 1
    return contV

frase = input("Digite uma frase: ")
contV = totalVogais(frase)
contB = totalBranco(frase)
contR = totalResto(frase)
print("O total de vogais e", contV)
print("O total de espacos e", contB)
print("O total de outros caracteres e", contR)
