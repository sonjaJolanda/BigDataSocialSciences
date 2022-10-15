import pandas as pd
import nltk
nltk.download('averaged_perceptron_tagger')
sentence = "How can we automatically tag each word of a text with its word class?"
tokenized = nltk.word_tokenize(sentence)
pos_tag = nltk.pos_tag(tokenized)
pd.DataFrame(pos_tag).T  # the t is to transpose it !
# --------------------------------------------------------------
nltk.download('tagsets')
nltk.help.upenn_tagset('NN')  # this is just for getting the info what the shortcuts stand for
text = "They refuse to permit us to obtain the refuse permit"
test1 = nltk.pos_tag(text.split())  # instead of the other thing (this is only one line though)
pd.DataFrame(test1).T
# --------------------------------------------------------------
text = nltk.Text(word.lower() for word in nltk.corpus.gutenberg.words('melville-moby_dick.txt'))
text.similar('woman')  # not similar to the meaning but similar like also a noun
# --------------------------------------------------------------
sentence = "I saw a yellow bird flying into my room through my clear window."
tokens = nltk.word_tokenize(sentence)
tags = nltk.pos_tag(tokens)
chunk_grammar = r"NP: {<DT>?<JJ>*<NN>}"
parser = nltk.RegexpParser(chunk_grammar)
tree = parser.parse(tags)
print(tree)
tree.draw()
# --------------------------------------------------------------
sentence2 = "The little yellow dog barked at the angry cat that belongs to Heidi Choi."
tokens = nltk.word_tokenize(sentence2)
tags = nltk.pos_tag(tokens)

pattern = r"""
NP: {<DT>?<JJ>*<NN>}
VBD: {<VBD>}
IN: {<IN>}
NP: {<NNP>+}
"""

NPchunker = nltk.RegexpParser(pattern)
result = NPchunker.parse(tags)
result.draw()
# --------------------------------------------------------------
from nltk.corpus import gutenberg

hamlet = gutenberg.raw('shakespeare-hamlet.txt')
default_st = nltk.sent_tokenize
hamlet_sentences = default_st(text=hamlet)
hamlet_sentences = [x.replace('\n', '') for x in hamlet_sentences]
hamlet_word = nltk.word_tokenize(hamlet)
hamlet_pos = nltk.pos_tag(hamlet_word)
nouns = []
for word, pos in hamlet_pos:
    if pos in ['NN']:
        nouns.append(word)
# ---------- Porter-Stemmer ------------------------------------------
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize

ps = PorterStemmer()
example_words = ['pythoned', 'pythoning', 'pythons']

for w in example_words:
    print(ps.stem(w))

new_text = "it is very important to be pythonly while you are pythoning with python. All pythoners have pythoned at least once"
words = word_tokenize(new_text)
# for w in words:
# print(ps.stem(w)) this does not work!
# ---------- Snowball-Stemmer ----------------------------------------
from nltk.stem.snowball import SnowballStemmer

words = ['plays', 'playing', 'played', 'player', 'pharmacies', 'badly']
ss = SnowballStemmer(language='english')
print([ss.stem(w) for w in words])
# ---------- Lancaster-Stemmer ----------------------------------------
from nltk.stem import LancasterStemmer

ls = LancasterStemmer()
print([ls.stem(w) for w in words])
# ---------- Lemmatization --------------------------------------------
nltk.download('wordnet')
nltk.download('omw-1.4')
from nltk.stem import WordNetLemmatizer

wnl = WordNetLemmatizer()
print([wnl.lemmatize(w) for w in words])  # Remember! Without the POS tag, wnl assume every word as a noun!
print(wnl.lemmatize('dogs', 'n'))
print(wnl.lemmatize('went', 'v'))
print(wnl.lemmatize('happiest', 'a'))
# ---------- Lemmatization --------------------------------------------
sentence = """
There were doors all round the hall, but they were all locked; 
and when Alice had been all the way down one side and up the other, trying every door, 
she walked sadly down the middle, wondering how she was ever to get out again.. 
"""
sentence_words = nltk.word_tokenize(sentence)
punt = "?!:;,."
for word in sentence_words:
    if (word in punt):
        sentence_words.remove(word)

# maybe try it in the other way for for loops
# sentence_words = (sentence_words.remove(word) for word in sentence_words if word in punt)

for word in sentence_words:
    print("{0:10}{1:10}".format(word, wnl.lemmatize(word,
                                                    pos='v')))  # this will not be on the exam (we just did it to view the stuff in there!

for word in sentence_words:
    print("{0:10}{1:10}".format(word, wnl.lemmatize(word,
                                                    pos='n')))  # this will not be on the exam (we just did it to view the stuff in there!
