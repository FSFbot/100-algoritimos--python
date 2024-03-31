def NextPrime(n):
    def is_prime(num):
        if num > 1:
            for i in range(2, num):
                if (num % i) == 0:
                    return False
                    break
                else:
                    return True
        else:
            return False

    if is_prime(n):
        return n
    else:
        while True:
            n += 1
            if is_prime(n):
                return n

print("New test ssh")
print(NextPrime(12))
print(NextPrime(24))
print(NextPrime(11))