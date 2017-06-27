# based on https://books.google.com/books?id=KGIbfiiP1i4C&pg=PA55&lpg=PA55&dq=random+text+generation+bigrams&source=bl&ots=Y2Hjx6NIJ7&sig=XUsmPYog1rouW81lKz5TYm6PxIw&hl=en&sa=X&ved=0ahUKEwjKraKf-eDTAhVB7YMKHYQRC0sQ6AEIPzAE#v=onepage&q=random%20text%20generation%20bigrams&f=false

# didn't end up working, so I gave up on fiddling with this.

import nltk

def generate_model(cfdist, word, num=15):
    for i in range(num):
        print(word,end=" ")
        word = cfdist[word].max() # get most probable next word
    print()

text = nltk.corpus.PlaintextCorpusReader('../output/my-messages-only/','.*')
text = text.words()
bigrams = nltk.bigrams(text)
cfd = nltk.ConditionalFreqDist(bigrams)
