

def get_division_remainder(input_number, divide_by):
    return input_number % divide_by

def main():
    input_number = int(input('Enter a number: '))
    is_divisible_by_3 = get_division_remainder(input_number, 3) == 0
    is_divisible_by_5 = get_division_remainder(input_number, 5) == 0

    if is_divisible_by_3 and not is_divisible_by_5:
        print('Fizz')
    elif not is_divisible_by_3 and is_divisible_by_5:
        print('Buzz')
    elif is_divisible_by_3 and is_divisible_by_5:
        print('Fizz Buzz')
    else:
        print(str(input_number) + ' not divisible by 3 or 5')

if __name__ == "__main__":
    while True:
        main()