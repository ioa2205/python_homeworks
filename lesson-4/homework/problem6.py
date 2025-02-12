# Problem 6
def prime_numbers(n):
    prime_numbers = []
    for i in range(2, n):
        is_prime = True
        for j in range(2, i):
            if i%j == 0:
                is_prime = False
                break
        if is_prime:
            prime_numbers.append(i)
    return prime_numbers
# print(prime_numbers(100))
print(prime_numbers(20))