from nltk.chunk import RegexpParser
from app.tagger import classifier

chunker = RegexpParser(r"""
    WHAT:
      {<.*>+}
      }<ACT|NC|\$|NC\$>+{
    HOW_MUCH:
      {(<NC><\$>)|(<\$><NC>)}
      }<\$>{
    ACTION_I:
      {<ACTP>}
    ACTION_O:
      {<ACT>}
""")

def chunk(tagged_sent,sent):
    tree = chunker.parse(tagged_sent)
    elements = {'ACTION_I':[],'ACTION_O':[],'WHAT':[],'HOW_MUCH':[],'S': []}
    for subtree in tree.subtrees():
        elements[subtree.label()] = get_text(subtree)

    elements['REFERENCE'] = get_words_from_tag('MON',tagged_sent)
    elements['INVOLVED'] = get_words_from_tag('PER',tagged_sent)
    elements['LOC'] = get_words_from_tag('LOC',tagged_sent)
    elements['CLASSIFICATION'] = classify(sent)
    return elements

def classify(sent):
    return classifier.classify(sent)

def get_words_from_tag(tag,tagged_sent):
    words = []
    for (w,t) in tagged_sent:
        if t == tag:
            words += [w]

    return words

def get_text(tree):
    i = -1
    text = []
    last_item = len(tree.leaves()) - 1
    for (w,t) in tree.leaves():
        i += 1
        if i in (0, last_item) and t == 'PRP':
            continue
        else:
            text += [w]
    return text
