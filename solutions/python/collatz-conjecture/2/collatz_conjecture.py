def steps(number):
    if number <= 0:
        raise ValueError("Only positive integers are allowed")
    elif number == 1:
        return 0
    
    steps_count = 0
    while number != 1:
        steps_count += 1
        number = number//2 if number%2==0 else (3*number) + 1
    return steps_count
            
