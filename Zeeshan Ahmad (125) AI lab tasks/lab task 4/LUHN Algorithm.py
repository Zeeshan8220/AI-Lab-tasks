def luhn_algorithm(number):
    number = [int(digit) for digit in str(number)]
    checksum = 0
    reverse_digits = number[::-1]
    
    for i, digit in enumerate(reverse_digits):
        if i % 2 == 1:
            digit *= 2
            if digit > 9:
                digit -= 9
        checksum += digit
    
    return checksum % 10 == 0

number = input("Enter credit card number: ")
if luhn_algorithm(number):
    print("Valid")
else:
    print("Invalid")



