Problem 4: Multiples Counter
Language: Python
Count multiples of numbers 1-9 in a list

def count_multiples(input_list):
    divisors = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    result = {divisor: 0 for divisor in divisors}
    
    for num in input_list:
        for divisor in divisors:
            if num % divisor == 0:
                result[divisor] += 1
                
    return result

input_numbers = [1, 2, 8, 9, 12, 46, 76, 82, 15, 20, 30]
print(count_multiples(input_numbers))
