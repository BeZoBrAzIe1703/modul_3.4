def single_root_words (root_word = 'мороз', *other_words):
    same_words = []
    for i in other_words:
        if root_word.lower() in i.lower():
            same_words.append(i)
    return print (same_words)

result1 = single_root_words('мороз', 'морозный', 'мор' 'мирный', 'морок')
result2 = single_root_words('дом', 'домовой', 'бездомный', 'доклад', 'дробь')
print (result1)
print (result2)