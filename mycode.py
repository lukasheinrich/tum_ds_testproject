
def calculate_the_mean(numbers):
    sum = 0
    for n in numbers:
        sum += n
    return sum/len(numbers)

def get_the_max(numbers):
    max_number = numbers[0]
    for n in numbers:
        if n > max_number:
            max_number = n
    return max_number

def get_the_min(numbers):
    min_number = numbers[0]
    for n in numbers:
        if n < min_number:
            min_number = n
    return min_number
