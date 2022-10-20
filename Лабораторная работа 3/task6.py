list_numbers = [2, -93, -2, 8, -36, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

# TODO Оформить решение

max_value_index = 0  # предположим, что значение, стоящее под 0 индексом, максимальное
max_value = list_numbers[max_value_index]

for i, current_value in enumerate(list_numbers):
    if current_value > max_value:
        max_value = current_value
        max_value_index = i

list_numbers[-1], list_numbers[max_value_index] = list_numbers[max_value_index], list_numbers[-1]

print(list_numbers)
