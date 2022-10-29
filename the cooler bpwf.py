from ast import Str
import copy

dict = {}
original_dict = {}
ulc = []
used_letters = []
used_words = []
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'y']
suggested_word_count = 5



with open('words.txt', encoding='utf8') as words:
    for word in words:
        current_word = ''.join(word.splitlines())
        for letter in current_word:
            if letter not in ulc and letter != 'x' and letter != 'z' and letter != '-':
                ulc.append(letter)
            dict[current_word] = len(ulc)          
        ulc.clear()

original_dict = copy.copy(dict)

while True:
    for word in dict:
        for letter in used_letters:
            if letter in word:
                dict[word] -= 0.25
    answer = input('Prompt: ')

    print('Suggested words:')

    counter = 0

    for word in reversed(sorted(dict, key=dict.get)):
        if answer in word and word not in used_words:
            print(word)
            counter += 1
            if counter == suggested_word_count:
                break

    answer = input('What word did you play? ')
    used_words.append(answer)
    for letter in answer:
        if letter not in used_letters and letter != 'x' and letter != 'z' and letter != '-':
            used_letters.append(letter)
    used_letters.sort()
    if used_letters == alphabet:
        used_letters.clear()
        dict = copy.copy(original_dict)
        print('Extra Life!')
    print("Used letters: " + str(used_letters))
    print("Needed letters: " + str([x for x in alphabet if x not in used_letters]))