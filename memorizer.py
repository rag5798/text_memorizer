import random

class Replacer:
    def __init__(self, list: list):
        self.original_list = list
        self.copy_list = list
        self.replace_words = []
        self.blanks = []
    
    def replace(self, times):
        for _ in range(times):
            word = random.choice(self.copy_list)
        
            while '(' in word or ')' in word or '_' in word:
                word = random.choice(self.copy_list)
            
            self.replace_words.append(word)
            
            if '”' in word:
                blank = '_' * (len(word)-1)
                blank += '”'
            elif '“' in word:
                blank = '“'
                blank += '_' * (len(word)-1)
            elif ',' in word:
                blank = '_' * (len(word)-1)
                blank += ','
            elif '.' in word:
                blank = '_' * (len(word)-1)
                blank += '.'
            else:
                blank = '_' * len(word)
            self.blanks.append(blank)

        for index, word in enumerate(self.replace_words):
            self.copy_list[self.copy_list.index(word)] = self.blanks[index]
        
        self.replace_words = []


def main():
    with open('family_proclamation.txt', 'r', encoding='utf-8') as file:
        content = file.read()
        content = content.replace('\n', '')
        words = content.split(' ')

    replacer = Replacer(words)
    counter = 0
    while counter < len(words):
        replacer.replace(1)
        for word in range(len(replacer.copy_list)-2):
            print(replacer.copy_list[word], end=' ', )
        


if __name__ == '__main__':
    main()
    


    