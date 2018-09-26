#Victor Alexandru ETI2IA
#Student Number 459241

n = 600851475143
i = 2
while i * i < n:
    while n % i == 0:
        n = n / i
    i = i + 1
print n
