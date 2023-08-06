def get_division_remainder(input_number, divide_by):
    return input_number % divide_by

def get_input_result(input_number):
    is_divisible_by_3 = get_division_remainder(input_number, 3) == 0
    is_divisible_by_5 = get_division_remainder(input_number, 5) == 0
    return (is_divisible_by_3, is_divisible_by_5)

def display_result(input_number, is_divisible_by_3, is_divisible_by_5):
    if is_divisible_by_3 and not is_divisible_by_5:
        return 'Fizz'
    elif not is_divisible_by_3 and is_divisible_by_5:
        return 'Buzz'
    elif is_divisible_by_3 and is_divisible_by_5:
        return 'Fizz Buzz'
    else:
        return str(input_number)

def enter_number():
    input_number = int(input('Enter a number: '))
    print(get_input_result(input_number))

def enter_range():
    first_input_number = int(input('Enter first number: '))
    second_input_number = int(input('Enter second number: '))
    input_range = range(first_input_number, second_input_number)

    results = {}
    for n in input_range:
        input_result = get_input_result(n)
        results[n] = display_result(n, input_result[0], input_result[1])
    print(list(results.values()))

menu_options = {
    1: 'Enter a number',
    2: 'Enter a range',
    3: 'Exit'
}
def get_menu_selection():
    for key in menu_options.keys():
        print(str(key) + '.', menu_options[key])
    return int(input())

def main():
    selected_option = 0
    while selected_option != 3:
        selected_option = get_menu_selection()
        if selected_option == 1:
            enter_number()
        elif selected_option == 2:
            enter_range()

if __name__ == "__main__":
    main()
