# simple example i used to understand how markov chains are actually implemented.
# modified from
#     http://agiliq.com/blog/2009/06/generating-pseudo-random-text-with-markov-chains-u/
# not great output, but easy to understand
import random

class Markov(object):
    
    def __init__(self, open_file):
        self.cache = {}
        self.open_file = open_file

        #fuction calls
        self.words = self.file_to_words()
        self.words_length = len(self.words)
        self.database()
        
    
    # in: file
    # out: list of words in file
    def file_to_words(self):
        data = self.open_file.read()
        words = data.split()
        return words

    # in: words
    # out: dict, cache, containing { (w1,w2) : w3_a,w3_b,w3_c } 
    def database(self):
        # tuple unpacking
        for w1, w2, w3 in self.trigrams():
            key = (w1, w2)
            if key in self.cache:
                self.cache[key].append(w3)
            else:
                self.cache[key] = [w3]
                
    
    # == trigrams
    def trigrams(self):
        """
            Generates trigrams from the given data string. So if our string were
            "What a lovely day", we'd generate (What, a, lovely) and then
            (a, lovely, day).
        """
        
        if len(self.words) < 3:
            return
        
        for i in range(len(self.words) - 2):
            # return a generator
                # yield is like return, but returns a generator, which is faster than storing
                # a massive corpus all in memory: we discard it when we're done
            yield (self.words[i], self.words[i+1], self.words[i+2])
            
    def generate_markov_text(self, size=25):
        # get a random bigram out of words
        seed = random.randint(0, self.words_length-3)
        seed_word, next_word = self.words[seed], self.words[seed+1]
        w1, w2 = seed_word, next_word

        building_sentence = []
        for i in range(size):
            building_sentence.append(w1)
            w1, w2 = w2, random.choice(self.cache[(w1, w2)])
        building_sentence.append(w2)
        return ' '.join(building_sentence)
            
            
f = open('../output/my-messages-only/xFF5353.txt')

markov = Markov(f)

print(markov.generate_markov_text( random.randint(2,25) ) )
