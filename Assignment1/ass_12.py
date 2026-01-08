def is_prime(n):
    if n <= 1:
        raise ValueError("n must be greater than one")
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

output = is_prime(11)
print(output)