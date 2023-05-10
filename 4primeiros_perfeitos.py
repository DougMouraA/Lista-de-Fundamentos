n = 0
k = 1
while n <= 4:
    soma = 0
    for i in range(1, k):
        if k % i == 0:
            soma+=i
    if soma == k:
        print(k)
        n +=1
    k +=1
        
