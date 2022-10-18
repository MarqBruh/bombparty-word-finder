import os

dict = {}
ulc = []

if not os.path.isfile('ulc_cache.txt'):
    with open('words.txt') as words:
        for word in words:
            current_word = ''.join(word.splitlines())
            for letter in current_word:
                if letter not in ulc:
                    ulc.append(letter)
                dict[current_word] = len(ulc)          
            ulc.clear()

    ulc_cache = open('ulc_cache.txt', 'a+')

    for item in reversed(sorted(dict, key=dict.get)):
      ulc_cache.write(item + ' ')


x = int(input('How many top words do you want to show? '))

if x == 1:
    print('The best word in your list is ')
else:
    print('The ' + str(x) + ' best words in your list are: ')

with open('ulc_cache.txt') as file:
    print(file.read().split()[:x])

while True:
    dict.clear()
    search = input('Enter bombparty prompt or string to find all words containing that string (Sorts by ULC, ascending): ')
    with open('words.txt') as words:
        for word in words:
            current_word = ''.join(word.splitlines())
            for letter in current_word:
                if letter not in ulc:
                    ulc.append(letter)
                dict[current_word] = len(ulc)          
            ulc.clear()

    for item in (sorted(dict, key=dict.get)):
        if search in item:
            print(item)