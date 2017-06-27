# my handwritten text generator, using a markov chain.
# attempted to be an improvement over markov.py, by using start and end symbols.
# contains code from markov.py.

from dicts import DefaultDict
import random
import itertools

# i initially thought i might want to use bigram probabilities, but ended up bailing on that approach.
'''
# from hw2
def bigrams(words):
    """Given an array of words, returns a dictionary of dictionaries,
    containing occurrence counts of bigrams."""
    d = DefaultDict(DefaultDict(0))
    for (w1, w2) in zip([None] + words, words + [None]):
        d[w1][w2] += 1
    return d
# end from hw2
def try_bigrams():
    with open(filename,'r') as f:
        # read in the file. this time, let's get newlines as an indicator of "end sentence here"
        corpus = f.read()
    print( bigrams(corpus.split()) )
'''


filename = "../output/my-messages-only/xFF5353.txt"

with open(filename,'r') as f:
    corpus = f.readlines()
    corpus = [ line.split() for line in corpus ]
    # corpus is currently a list of messages
    #   where a message is a list of words

    # add start/end symbols
    for message in corpus:
        message.insert(0, "<s>")
        message.append('</s>')

    corpus =  list(itertools.chain.from_iterable(corpus))


cache = {}
    # in: words
    # out: dict, cache, containing { (w1,w2) : w3_a,w3_b,w3_c }
def build_cache():
    # tuple unpacking
    continue_flag = 0
    for w1, w2, w3 in trigrams():
        # if we're at the end of a sentence, skip adding it
        if continue_flag == 1:
            continue_flag = 0
            continue
        if w1 == '</s>' and w2 == '<s>':
            continue

        key = (w1, w2)
        if key in cache:
            cache[key].append(w3)
        else:
            cache[key] = [w3]

        if w3 == "</s>":
            continue_flag = 1
            
def trigrams():
    """
        Generates trigrams from the given data string. So if our string were
        "What a lovely day", we'd generate (What, a, lovely) and then
        (a, lovely, day).
    """
    
    if len(corpus) < 3:
        return
    
    for i in range(len(corpus) - 2):
        # return a generator
            # yield is like return, but returns a generator, which is faster than storing
            # a massive corpus all in memory: we discard it when we're done
        yield (corpus[i], corpus[i+1], corpus[i+2])
        
def generate_markov_text(size=25):
    # get a random bigram out of words
    seed = random.randint(0, len(corpus)-3)
    seed_word, next_word = corpus[seed], corpus[seed+1]

    # edge case handling, skipping certain start symbols in our cache. inelegant and ugly.
    if seed_word == '<s>' or seed_word == '</s>' or next_word == '</s>' or next_word == '<s>':
        seed = random.randint(0, len(corpus)-3)
        seed_word, next_word = corpus[seed], corpus[seed+1]
    w1, w2 = seed_word, next_word

    building_sentence = []
    for i in range(size):
        building_sentence.append(w1)
        if w2 == '</s>': break
        if w1 == '</s>': continue
        w1, w2 = w2, random.choice(cache[(w1, w2)])
    building_sentence.append(w2)
    return ' '.join(building_sentence)



build_cache()
# try to generate first sentence
output = generate_markov_text( 25 )
# make sure it's not just start symbols (consequence of my poor edge case handling)
while output.count('s>') > 3:
    output = generate_markov_text( 25 )

while len(output.split()) < 3:
    output = generate_markov_text( 25 )

output = output.replace('<s>','').replace('</s>','')
if output[0] == ' ': output = output[1:]
print (output)

