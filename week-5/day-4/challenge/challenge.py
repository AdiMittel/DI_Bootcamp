class Text:
    def __init__(self,content) :
        self.content = content
        self.word_list = self.content.split()
        self.unique = set(self.word_list)

    def word_frequency(self,word):
        if word in self.word_list:
            return f'the word {word} shows up {self.__word_frequency(word)} times'

    def __word_frequency(self,word):    
        if word in self.word_list:
            return self.word_list.count(word)

    def most_common_word(self):
        word_set = set(self.word_list)
        word_dict = {}
        for word in word_set:
            word_dict.update({word:self.__word_frequency(word)})
        list_of_tuples = list(word_dict.items())
        return sorted(list_of_tuples, key=lambda x:x[1], reverse=True)[0][0]
    
    def unique_words(self):
        return list(self.unique)
    
    @classmethod
    def from_file(cls,file_name):
        with open(file_name,'r') as f:
            file_text = f.read()
        return cls(file_text)


text = Text('hello the hello man how hello are you?')
print(text.word_frequency('hello'))
print(text.most_common_word())
strange = Text.from_file('the_stranges.txt')
print(strange.most_common_word())