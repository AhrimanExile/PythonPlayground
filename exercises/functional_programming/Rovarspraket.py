'''
Rövarspråket (со шведского переводится как «язык разбойника») - шведская языковая игра. 
Она стала популярной после книг Астрид Линдгрен о Билле Бергсоне, где дети используют ее в качестве кода, как в игре, 
так и при раскрытии настоящих преступлений.
Формула кодирования проста: каждая согласная удваивается, а между ними вставляется буква o. Гласные остаются нетронутыми.
Тогда согласно этим правилам слово
stubborn
превратится в
sostotubobboborornon
Ваша задача написать функцию translate_to_robber_lang(), которая будет переводить текст на «язык разбойника» (по-шведски ).
Все символы, которые не являются буквами, должны оставаться без изменения.
Гласными будем считать буквы ['a','e', 'i', 'o', 'u']
'''
vowels = ['a','e', 'i', 'o', 'u']
def translate_to_robber_lang(sentence):
    amended_sentence = ''
    for letter in sentence:
        if letter.lower() not in vowels and letter.isalpha():
            amended_sentence += letter + 'o' + letter
        else:
            amended_sentence += letter
    return amended_sentence

#Test
print(translate_to_robber_lang("This is kinda fun"))