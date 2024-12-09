def calculate_sum_and_string_lengths(data):
    total = 0

#Функция isinstance() проверяет принадлежность к определенному классу

    if isinstance(data, (int, float)):  # Если число, прибавляем его
        return data
    elif isinstance(data, str):  # Если строка, прибавляем её длину
        return len(data)
    elif isinstance(data, (list, tuple, set)):  # Для списков, кортежей и множеств рекурсивно обрабатываем элементы
        return sum(calculate_sum_and_string_lengths(item) for item in data)
    elif isinstance(data, dict):  # Для словарей обрабатываем ключи и значения
        return sum(calculate_sum_and_string_lengths(key) + calculate_sum_and_string_lengths(value) for key, value in data.items())

    return 0  # Для неподдерживаемых типов данных возвращаем 0


# Пример использования
data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])
]

result = calculate_sum_and_string_lengths(data_structure)
print("Результат:", result)
