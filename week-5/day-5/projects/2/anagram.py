from anagram_checker import AnagramChecker
def is_word_valid(word):
    return len(word.split()) == 1 and word.isalpha()

while True:
    user_choice = input('A. find a word\'s anargams.\n X. Exit\n')
    if user_choice in 'xX':
        print('Goodbye!')
        break
    elif user_choice.upper() == 'A':
        selected_word = input('give us the word to check for anagrams\n')
        if is_word_valid(selected_word):
            clean_word = selected_word.strip()
            a = AnagramChecker()
            anagrams = a.get_anagrams(clean_word)
            msg = f'''You\'re word: {clean_word}
    is a valid English word.
    Anagrams of the words are {anagrams}'''
            print(msg, *anagrams)
        else:
            print('Not a valid word!')
        