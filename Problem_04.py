def is_palindrome(number):
    number = str(number)
    return number == number[::-1]

def largest_palindrome(min_value, max_value):
    max = 0
    for i in range(min_value, max_value):
        for k in range(min_value, max_value):
            prod = i * k
            if is_palindrome(prod):
                if prod > max:
                    max = prod
    return max

print largest_palindrome(100, 1000)
