import random
# num_of_words  = int(input('how many words should be in the sentence? '))


def get_words_from_file():
    words = []
    # num = input('How many words?')
    with open('words.txt', 'r') as f:
        for line in f:
            words.append(line.rstrip('\n'))
        f.close()
        return words


def get_random_sentence(num):
    sentence = ''
    get_words = get_words_from_file()
    rndm_words = random.choices(get_words, k=num)
    for word in rndm_words:
        sentence += word+' '
    print(sentence.lower())


def get_num():
    num = input('Enter a number of words should create your sentence: ')
    if 2 <= int(num) <= 20:
        get_random_sentence(int(num))
        main()
    else:
        SyntaxError


def main():
    print('The program job is to take random words and make a sentence in a length YOU CHOOSE!')


get_num()
