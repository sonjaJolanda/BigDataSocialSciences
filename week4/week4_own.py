[x for x in range(1, 10)]
[x for x in range(1, 10) if x % 2 == 0]
["Even" if i%2==0 else "Odd" for i in range(10)]
#--------------------------------------------------------------
import requests
data = requests.get("https://www.gutenberg.org/cache/epub/8001/pg8001.html")
#--------------------------------------------------------------
from bs4 import BeautifulSoup as bs
import re
def strip_html_tag(text): # get rid of unnecessary spaces
    soup = bs(text, 'html.parser')
    stripped_text = soup.get_text()
    stripped_text = re.sub(r'[\r|\n]+', '\n', stripped_text)
    return stripped_text
clean_content = strip_html_tag(data.content)
#------- word tokenization ------------------------------------
import nltk
nltk.download('punkt')
cleaned_contents = nltk.word_tokenize(clean_content)
contents = list(filter(None, [re.sub(r'[^a-zA-Z]', '', a) for a in cleaned_contents]))
# filter(None, ...) means filter all the elements that are None or '' -->  so this filtered None, and everything that is not text
contents = [content.lower() for content in contents] # make everything lowercase
#------- Counter ----------------------------------------------
from collections import Counter
c = Counter(contents)
c.most_common(10)

nltk.download('stopwords')
from nltk.corpus import stopwords
stopwords = nltk.corpus.stopwords.words('english') # you can google which stopwords each language has
contents_without_stopwords = [word for word in contents if word not in stopwords]
c = Counter(contents_without_stopwords)
# c.most_common(10)
#------- Sentence Tokenization --------------------------------
from nltk.corpus import gutenberg
nltk.download('gutenberg')
nltk.corpus.gutenberg.fileids()
alice = gutenberg.raw(fileids='carroll-alice.txt')
len(alice)
print(alice[0:500])

default_st = nltk.sent_tokenize
alice_sentences = default_st(text=alice)
alice_sentences = [x.replace('\n', '') for x in alice_sentences]
alice_word = nltk.word_tokenize(alice)
alice_contents = list(filter(None, [re.sub(r'[^a-zA-Z]', '', a) for a in alice_word]))
alice_contents = [word.lower() for word in alice_contents if word.lower() not in stopwords]

ac = Counter(alice_contents)
# ac.most_common(10)
new_stopwords = ['nt', 'said', 'would', 'know', 'like', 'went'] # Let's add more to stop words
for i in new_stopwords:
    stopwords.append(i)
alice_contents = [word for word in alice_contents if word not in stopwords]
ac = Counter(alice_contents)
# ac.most_common(10)