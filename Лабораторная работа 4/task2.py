def get_count_char(str_):
    # Создаем пустой словарь, куда будем записывать наши ключи и значения
    count_char_dict = {}
    # Заводим счетчик для подсчета количества символов в строке
    COUNT_INITIAL_VALUE = 0
    # Переводим строку в н. регистр с пом. метода lower(), чтобы буквы в. и н. регистра не разбивались на 2 отд. символа
    # Убираем в строке пробелы с помощью метода split()
    # Склеиваем слова с помощью метода join()
    count_char_str = "".join(str_.lower().split())

    for char in list(count_char_str):  # Перебираем каждый символ в списке
        if char.isalpha():  # Проверяем, что символ является буквой
            # Записываем ключ "символ" и значение "количество" в словарь
            count_char_dict[char] = count_char_dict.get(char, COUNT_INITIAL_VALUE) + 1
    return count_char_dict


def get_percentage(dict_):
    sum_values = sum(dict_.values())
    for value in dict_:
        dict_[value] = "{0:.2f}".format(dict_.get(value) * 100 / sum_values)
    return dict_


main_str = """
    Данное предложение будет разбиваться на отдельные слова. 
    В качестве разделителя для встроенного метода split будет выбран символ пробела. На выходе мы получим список отдельных слов. 
    Далее нужно отсортировать слова в алфавитном порядке, а после сортировки склеить их с помощью метода строк join. Приступим!!!!
"""

main_dict = get_count_char(main_str)
percent_dict = get_percentage(get_count_char(main_str))

print(main_dict, "\n", percent_dict)
