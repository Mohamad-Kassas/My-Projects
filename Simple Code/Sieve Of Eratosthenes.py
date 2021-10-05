def sieve_eratosthenes(n):
    primes = [i for i in range(2, n + 1)]
    popped = 0
    for i in range(len(primes)):
        current_prime = primes[i]
        if current_prime != 0:
            for i in range(current_prime + i, len(primes), current_prime):
                primes[i] = 0

    for k in range(len(primes)):
        if primes[k - popped] == 0:
            primes.pop(k - popped)
            popped += 1

    return primes


print(sieve_eratosthenes(150))
