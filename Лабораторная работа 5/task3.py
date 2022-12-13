from random import sample, randint


# Вариант 1 с использованием метода random

def get_unique_list_numbers() -> list[int]:
    return sample(range(-10, 11), 15)


list_unique_numbers = get_unique_list_numbers()
print(list_unique_numbers)
print(len(list_unique_numbers) == len(set(list_unique_numbers)))


# Вариант 2 с использованием цикла

def get_unique_list_numbers2() -> list[int]:
    set_ = set()
    while len(set_) < 15:
        set_.add(randint(-10, 10))
    return list(set_)


list_unique_numbers2 = get_unique_list_numbers2()
print(list_unique_numbers2)
print(len(list_unique_numbers2) == len(set(list_unique_numbers2)))
