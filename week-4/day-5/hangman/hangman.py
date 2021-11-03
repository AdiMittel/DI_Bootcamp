import random
word_list = ['train','motorbike','truck','ocean','computer']

def get_word():
    word = random.choice(word_list)
    print(word)
    return word.upper()

def play(word):
    word_len = len(word)
    word_completion = '_' * word_len
    guessed = False
    guessed_letters = []
    guessed_words = []
    tries = 6
    print('Let\'s Play!')
    print(display_hangman(tries))
    print(word_completion)   
    while not guessed and tries > 0:
        guess = input('Please guess a letter or word: ').upper()
        if len(guess) == 1 and guess.isalpha():
            if guess in guessed_letters:
                print('You already guess this letter!')
            elif guess not in word:
                print(guess,'is not in the word')
                tries -= 1
            else:
                print(guess, 'is in the word')
                guessed_letters.append(guess)
                word_as_list = list(word_completion)
                indices = [i for i,letter in enumerate(word) if letter == guess]
                for index in indices:
                    word_as_list[index] = guess
                word_completion = ''.join(word_as_list)
                if '_' not in word_completion:
                    guessed = True
        elif len(guess) == len(word):
            if guess in guessed_words:
                print('You already guessed the word',guess)
            elif guess != word:
                print(guess,'is not in the word')
                tries -= 1
                guessed_words.append(guess)
            else:
                guess = True
                word_completion = word
        else:
            print('not a valid guess')
            print(display_hangman(tries))
            if guessed:
                print('Good job! You guessed the word')
            else:
                print('You lost! Maybe next time :D')
        print(display_hangman(tries))
        print(word_completion)

def display_hangman(tries):
    stages = [  # final state: head, torso, both arms, and both legs
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / \\
                   -
                """,
                # head, torso, both arms, and one leg
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / 
                   -
                """,
                # head, torso, and both arms
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |      
                   -
                """,
                # head, torso, and one arm
                """
                   --------
                   |      |
                   |      O
                   |     \\|
                   |      |
                   |     
                   -
                """,
                # head and torso
                """
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |     
                   -
                """,
                # head
                """
                   --------
                   |      |
                   |      O
                   |    
                   |      
                   |     
                   -
                """,
                # initial empty state
                """
                   --------
                   |      |
                   |      
                   |    
                   |      
                   |     
                   -
                """
    ]
    return stages[tries]
def main():
    word = get_word()
    play(word)

main()