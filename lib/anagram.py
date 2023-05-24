# your code goes here!

class Anagram:
    def __init__(self, word):
        self.word = word


    def match(self, list):
        word_to_list = sorted([char for char in self.word])
        match_list = []
        for word in list:
            word_chars_list = sorted([letter for letter in word])
            if word_chars_list == word_to_list:
                match_list.append(word)
        return match_list






  