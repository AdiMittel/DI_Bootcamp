class AnagramChecker:
    def __init__(self,file_name='words.txt'):
        with open(file_name) as f:
            self.words = [word.strip().upper() for word in f.readlines()]
                
    def is_valid_word(self,word):
        return word.upper() in self.words

    def get_anagrams(self,word):
        word_sorted = sorted(list(word.upper()))
        anagrams = []
        for other_word in self.words:
            if sorted(list(other_word)) == word_sorted:
                anagrams.append(other_word)
        anagrams.remove(word.upper())
        return anagrams



a = AnagramChecker()
print(a.get_anagrams('meat'))

