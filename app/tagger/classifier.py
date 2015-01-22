import nltk
from nltk.corpus.reader import TaggedCorpusReader
import collections

def define_features(cat_words):
    features = {}
    for word in words:
        features['contem(%s)' % word] = (word in cat_words)

    return features

def list_of_words_for(category,limit=20):
    category_reader = TaggedCorpusReader('corpus',category)

    most_freq_words = []

    for w,t in category_reader.tagged_words():
        if t not in ["PRP","NC","$","$NC"]:
            most_freq_words.append(w.lower())
    pos_counts = collections.Counter(w for w in most_freq_words)
    result = [word for word, count in pos_counts.most_common(limit)]
    return result

def classify(tweet):
    tweet_features = define_features(tweet.split())
    return classif.classify(tweet_features)

essentials  = list_of_words_for('essentials')
lifestyle   = list_of_words_for('lifestyle')
investments = list_of_words_for('investments')
incoming    = list_of_words_for('incoming')
words       = essentials + lifestyle + investments + incoming

feat_out_essentials  = define_features(essentials)
feat_out_lifestyle   = define_features(lifestyle)
feat_out_investments = define_features(investments)
feat_in_incoming     = define_features(incoming)

classif = nltk.NaiveBayesClassifier.train([(feat_out_essentials,'ES'),(feat_out_lifestyle,'LS'),(feat_out_investments,'IV'),(feat_in_incoming,'IN')])
