def is_prime(n):
    if n == 2:
        return True
    if n < 2:
        print("Try with another larger number, it should be higher than 2! ")
        return 0
        
    for i in range(2,n):
        if n%i == 0:
            return False
    return True
n = int(input("Enter a number: "))
print(is_prime(n))