s = input("Digite uma cadeia: ")
c = input("Digite um caracter: ")
ns = ""
for i in range(len(s)):
    if s[i] != c.lower() and s[i] != c.upper():
     ns = ns + s[i]   
print(ns)
