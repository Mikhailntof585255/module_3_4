def single_root_words(root_word, *other_words):
    same_words = []
    for i in other_words:

        if root_word.lower() in i.lower() or i.lower() in root_word.lower():
            same_words.append(i)
    return same_words


rezult1 = single_root_words('Rich', 'richiest', 'orichalcum', 'cheers', 'richies')
result2 = single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')
print(rezult1)
print(result2)



