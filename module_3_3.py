'''Функция с параметрами по умолчанию'''


def print_params(a=1, b='строка', c=True):
    print(a, b, c)


print_params()
print_params(1, 3, 4)
print_params(b=25)
print_params(c=[1,2,3])


'''Распаковка параметров'''

values_list = [99, 'список', False]
values_dict = {'a': 100, 'b': 'словарь', 'c': None}

print_params(*values_list)
print_params(**values_dict)


'''Распаковка + отдельные параметры'''

values_list_2 = [54.32, 'Строка']
print_params(*values_list_2, 42)
