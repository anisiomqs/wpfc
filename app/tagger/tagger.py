import nltk
from nltk.tag import RegexpTagger
from nltk.corpus.reader import TaggedCorpusReader

reader = TaggedCorpusReader('corpus','tagged_corpus')
train = reader.tagged_sents()

tagger0 = nltk.DefaultTagger('n')
tagger1 = nltk.UnigramTagger(train,backoff=tagger0)
tagger2 = nltk.BigramTagger(train,backoff=tagger1)
patterns = [
    (r'^\d+((.|,)\d+)?\.?$', 'NC'),
    (r'^.*\$$','$'),
    (r'R\$\d+((.|,)\d+)?\.?$','NC$'),
    (r'^(R|r)eais$','$'),
    (r'^(D|d)(o|ó)lares','$')
]
tagger3 = RegexpTagger(patterns,backoff=tagger2)

def tag(sent):
    result = tagger3.tag(sent.split())

    return result
