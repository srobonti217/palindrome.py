def is_palindrome(s):
    s = ''.join(c.lower() for c in s if c.isalnum())  # Ignore case and non-alphanumeric characters
    return s == s[::-1]

# Test the function
test_string = input("Enter a string to check if it's a palindrome: ")
if is_palindrome(test_string):
    print(f'"{test_string}" is a palindrome!')
else:
    print(f'"{test_string}" is not a palindrome.')
