s  = input("Digite uma palavra: ")
p = ""
for i in range(len(s)-1, -1, -1):
    p += s[i]
    
if s == p:
    print("A palavra e palindromo")
else:
    print("A palavra nao e palindromo")
