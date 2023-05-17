s = input("s: ")
cont = 0
for i in range(0, len(s)):
    if s[i].lower() == "a" or s[i].lower() == "e" or s[i].lower() == "i" or\
       s[i].lower() == "o" or s[i].lower() == "u":
        cont += 1
print(cont)
