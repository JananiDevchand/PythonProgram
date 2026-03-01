def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

# Example Usage
if __name__ == '__main__':
    num = int(input('Enter the number of terms: '))
    print(list(fibonacci(num)))