from collections import defaultdict

def isPrime(n):
    if n<=1:
        return False
    elif n<=3:
        return True
    elif n%2==0 or n%3==0:
        return False
    else:
        val = int(n**0.5)
        for i in range(5, val+1, 6):
            if n%i==0 or n%(i+2)==0:
                return False
        return True
    

listPrimes = []
amount = 1000000
current = 0
d = defaultdict(int)
for i in range(amount+1):
    if isPrime(i):
        listPrimes.append(i)
        current+=1
    d[i] = current

expectationSum = 1
for i in range(3, amount+1):
    prod = 1
    index = 0
    while listPrimes[index]<=int(i**0.5):
        prod*=(1-1/listPrimes[index])
        index+=1
    expectationSum+=prod
print(d[amount], expectationSum, expectationSum/d[amount])
    