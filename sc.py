from app.tagger import tagger,chunker
import nltk

p = "Comprei 1 sapato para ketlyn na loja Shoes. 100 reais."

taggr = tagger.Tagger(p)

t = taggr.tag()

print(t)
chunkr = chunker.Chunker(t)

print(chunkr.chunk())

print("----------------------------")
print(taggr.list_of_words_for('tagged_corpus'))
