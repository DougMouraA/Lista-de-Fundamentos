s = input("Digite uma cadeia: ")
ns = ""
size = len(s)
for i in range(0,len(s),  2):
    if i < size - 1:
        ns += s[i+1]
        ns += s[i]
    elif size % 2 != 0 and i+1 == size:
        ns += s[i]
print(ns)
