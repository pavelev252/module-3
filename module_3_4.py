def single_root_words(root_word, *other_words):
    same_words = []  # пустой список для запипи провериненных элементов
    for word in other_words:  # цикл прохода по всем элементам  *other_words
        if root_word.lower() in word.lower() or word.lower() in root_word.lower():
            same_words.append(word)

    return same_words


'''условие проверки, находится ли слово root_word в 
следующем элементе или наоборот с преобразованием в нижний регистр'''

print(single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies'))
print(single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel'))
