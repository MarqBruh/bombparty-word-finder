from operator import contains
#from vars import wordlist #not sure if i need this, so i'l just leave it for now :)

words = open("words.txt")

dict = {'a': 'b'}
dict.clear()

ulc = ['a', 'b']

top_ulc = 0
top_word = 'rodney'
longest_word = ''
current_word = 'rodney'

for word in words:
    current_word = ''.join(word.splitlines())
    for letter in current_word:
        if letter not in ulc:
            ulc.append(letter)
        dict[current_word] = len(ulc)
    if len(ulc) > top_ulc:
        top_ulc = len(ulc)
        top_word = current_word
    if len(current_word) > len(longest_word):
        longest_word = current_word
    ulc.clear()

print("The best word in your list is " + top_word + " with a ULC of " + str(top_ulc))
print("The longest word in your list is " + longest_word + " with a length of " + str(len(longest_word)))

search = input("Enter word or 2/3 letter bombparty prompt prefixed by an ! to search: ")
if search[0] == "!":
    for word in words:
        if search[1:] in word:
            print(word)
else:
    if search in dict:
        search_ulc = dict.get(search)
    else:
        for letter in search:
            if letter not in ulc:
                ulc.append(letter)
            search_ulc = str(len(ulc))
            search_ulc += " (and isn't in the list btw)"
        ulc.clear()

    print((search.capitalize() + " has a ULC of " + str(search_ulc)))