def criptografia(frase):
    valorAscii = 0
    novaFrase = ""
    for i in range(0, len(frase)):
        if ord(frase[i])%2 == 0:
            valorAscii = ord(frase[i]) - 1
        else:
            valorAscii = ord(frase[i]) + 1
        novaFrase += chr(valorAscii)
    return novaFrase

frase = input("frase: ")
novaFrase = criptografia(frase)
print(novaFrase)
