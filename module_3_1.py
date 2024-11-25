calls = 0


def count_calls():
    global calls
    calls += 1


def string_info(string):
    count_calls()
    info = (len(string), string.upper(), string.lower())
    return print(info)


def is_contains(string, list_to_search):
    count_calls()
    lower_string = string.lower()
    lower_list = list(map(str.lower, list_to_search))
    if lower_string in lower_list:
        return print(True)
    else:
        return print(False)


string_info('Capybara')
string_info('Armageddon')
string_info('Arbalet')
is_contains('cycle', ['recycling', 'cyclic'])
is_contains('Urban', ['ban', 'BaNaN', 'urBAN'])
is_contains('ARM', ['Arm', 'ARMOR', 'Roman'])
print(calls)
