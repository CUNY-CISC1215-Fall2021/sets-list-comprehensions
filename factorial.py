# Conditional expression variant of the factorial recursive function
def factorial(x):
    return 1 if x < 1 else factorial(x-1) * x

print(factorial(10))