frase = input("Digite uma frase: ")
contV = 0
contB = 0
contO = 0
for i in range(0, len(frase)):
    if frase[i].lower() == "a" or frase[i].lower() == "e" or frase[i].lower() == "i" \
       or frase[i].lower() == "o" or frase[i].lower() == "u":
        contV += 1
    elif frase[i] == " ":
        contB += 1
    else:
        contO += 1
print(contV, contB, contO)
        
