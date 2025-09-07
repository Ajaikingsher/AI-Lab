def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def generate_primes(start, end):
    primes = []
    for n in range(start, end + 1):
        if is_prime(n):
            primes.append(n)
    return primes

def compute_gcd(a, b):
    while b:
        a,b = b,a % b
    return a

print("Primes:", generate_primes(0, 10))
print("GCD:", compute_gcd(5, 10))

