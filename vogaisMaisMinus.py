s = input("s: ")
contL = 0
contN = 0
contO = 0
for i in range(0, len(s)):
    if s[i].isalpha() == True:
        contL += 1
    elif s[i].isdigit() == True:
        contN += 1
    else:
        contO += 1
print("A string",s,"tem",contL,"de letras,",contN,"de numeros,",\
      contO,"de outros caracteres")
