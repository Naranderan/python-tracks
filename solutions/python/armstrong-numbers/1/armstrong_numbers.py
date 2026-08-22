def is_armstrong_number(number):
    digits_count = count_digits(number)
    sum_of_digits = 0
    original_number = number

    while number>=10:
        digit = number%10
        sum_of_digits += digit**digits_count
        number//=10
    sum_of_digits += (number%10)**digits_count
    return sum_of_digits == original_number

def count_digits(number):
    digits_count = 0
    while number>=10:
        number//=10
        digits_count += 1
    return digits_count+1
    
