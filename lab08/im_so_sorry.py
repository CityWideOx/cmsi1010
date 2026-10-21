def blocks(n):
    if n <= 0:
        return 0
    else:
        return blocks(n - 1) + n

    return 0 if n <= 0 else blocks(n - 1) + n


def sum_of_digits(n):
    if n < 10:
        return n
    return (n % 10) + sum_of_digits(n // 10)


def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n - 1)


def is_palindrome(s):
    if len(s) <= 1:
        return True
    if s[0] != s[-1]:
        return False
    return is_palindrome(s[1:-1])


def print_count_down(n):
    if n == 0:
        print("BOOM")
    else:
        print(n)
        print_count_down(n - 1)



print(blocks(8))
print(blocks(0))
print(blocks(-1))
print(blocks(1))
print(blocks(100))