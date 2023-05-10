soma = 0
n = 0
np = 1
k
while n <= 4:
    for i in range(1, (k//2)+1):
        if k % i == 0:
            soma+=i
    if soma == np:
        print(k)
        n +=1
    k +=1
        
        
