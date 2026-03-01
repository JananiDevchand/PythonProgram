def is_palindrome(s):
    return s == s[::-1]

# Example Usage
if __name__ == '__main__':
    string = input('Enter a string: ')
    print(f'{string} is palindrome: {is_palindrome(string)}')