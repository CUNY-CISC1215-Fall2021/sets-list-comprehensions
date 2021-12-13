# Determine if a number is prime
def is_prime(x):
    # Iterate through every number between 2 and x (non-inclusive)
    for i in range(2, x):
        # If any of those numbers divides x, then it cannot be prime
        if x % i == 0:
            return False
    return True

# Use a list comprehension to find all primes between 2 and 100
numbers = [x for x in range(2, 100) if is_prime(x)]
print(numbers)