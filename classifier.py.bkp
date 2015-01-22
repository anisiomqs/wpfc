import nltk

words = 'recebi paguei pago desconto recebimento deposito transferencia previdencia compra gasolina financiamento casa'
words_e = 'gasolina financiamento casa'
words_i = 'deposito transferencia previdencia desconto'
words_l = 'paguei pago compra'

def define_features(cat_words):
    features = {}
    for word in words.split():
        features['contem(%s)' % word] = (word in cat_words)
    return features

features_50 = define_features(words_e.split())
features_15 = define_features(words_i.split())
features_35 = define_features(words_l.split())

classifier = nltk.NaiveBayesClassifier.train([(features_15,'15'),(features_50,'50'),(features_35,'35')])

test = 'jucca'

print(classifier.classify(define_features(test.split())))
