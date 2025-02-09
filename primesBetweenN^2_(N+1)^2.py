import matplotlib.pyplot as plt
def isPrime(n):
    if n<2:
        return False
    elif n<=3:
        return True
    elif n%2==0 or n%3==0:
        return False
    else:
        for i in range(6, int(n**0.5), 6):
            if n%(i-1)==0 or n%(i+1)==0:
                return False
        return True
arr = []
for i in range(10, 5000):
    curCount = 0
    for j in range(i**2, (i+1)**2):
        if isPrime(j):
            curCount+=1
    if curCount ==1:
        print(i)
    arr.append(curCount)

plt.plot(range(10, 5000), arr)
plt.xlabel('i')
plt.ylabel('Prime Count')
plt.title('Prime Counts between i^2 and (i+1)^2')
plt.grid(True)
plt.show()