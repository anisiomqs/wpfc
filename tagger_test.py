#!flask/bin/python
import unittest
from app.tagger import tagger
from app.tagger import chunker

class TestTaggingAndChunking(unittest.TestCase):
    def setUp(self):
        sent = "Pago conta de luz, referente a janeiro. R$ 10,00."
        self.tag = tagger.Tagger(sent)

    def test_normalizing_sentence(self):
        expected = "Pago conta de luz referente a janeiro R$ 10,00"
        assert self.tag.normalize() == expected

    def test_tagging_and_chunking(self):
        expected = [('Pago','ACT'),('conta','N'),('de','PRP'),('luz','N'),('referente','ADJ'),('a','PRP'),('janeiro','MON'),('R$','$'),('10,00','NC')]
        tagged = self.tag.tag()
        assert(tagged == expected)
        chunk = chunker.Chunker(tagged)
        c = chunk.chunk()
        assert(c['HOW_MUCH'] == ['R$','10,00'])
        assert(c['ACTION'] == ['Pago'])
        assert(c['WHAT'] == ['conta','de','luz','referente','a','janeiro'])
        assert(c['REFERENCE'] == ['janeiro'])

if __name__ == '__main__':
    unittest.main()
