s = input("Digite uma palavra: ")
tam = len(s)
ns = ""
j = tam // 2
k = 0
for i in range (tam - 1):
    if j != tam:
        ns += s[j]
        j += 1
    if j == tam:
        ns += s[k]
        k += 1

print(ns)
