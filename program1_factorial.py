def factorial(n):
    if n < 0:
        return "Factorial not defined for negative numbers"
    elif n == 0:
        return 1
    else:
        return n * factorial(n - 1)

# Example Usage
if __name__ == '__main__':
    num = int(input('Enter a number: '))
    print(f'The factorial of {num} is {factorial(num)}')