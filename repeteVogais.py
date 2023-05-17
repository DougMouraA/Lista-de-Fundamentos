s = input("Digite uma cadeia: ")
ns = ""
for i in range(len(s)):
    if s[i] == "a" or s[i] == "e" or s[i] == "i" or s[i] == "o" or s[i] == "u":
        ns += s[i] * 2
    else:
        ns += s[i]
print(ns)
