def odd_and_even_sum_of_digits(num: str):
    odd_sum = 0
    even_sum = 0

    for ch in num:            # for every symbol from the number
        digit = int(ch)

        if digit % 2 == 0:    # even digit
            even_sum += digit
        else:                # odd digit
            odd_sum += digit

    return f'Odd sum = {odd_sum}, Even sum = {even_sum}'

number = input()

print(odd_and_even_sum_of_digits(number))