import math
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
gcd = math.gcd(a, b)

print("The GCD is", gcd)

n = int(input("Enter how many prime numbers you want: "))
primes=[]
i=2

while len(primes) < n:
    if all(i % j for j in range(2, int(i**0.5) + 1)):
        primes.append(i)
    i += 1

print("First", n, "prime numbers:", primes)
