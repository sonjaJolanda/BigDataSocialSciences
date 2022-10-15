name = 'Heidi'
name.isalpha() # False if there were 0-9
age = '22'
age.isdigit() # False if there were a-z
nameAndAge = 'Heidi22'
nameAndAge.isalnum() # can be both
# ToDo everything above is not part of the midterm, that's why I haven't included it in the summary
# ----- lambda -------------------------------------------------
m = lambda x: x+10
print(m(3)) # 13
# --------------------------------------------------------------
names = ['Heidi', 'John', 'Jenny']
print("-and-".join(names)) # Heidi-and-John-and-Jenny
# --------------------------------------------------------------
import pandas as pd
import re
from nltk.corpus import stopwords
imdb = pd.read_csv('imdb_dataset.csv', nrows=5000, encoding='cp949')  # read only the first 5000 rows
# encoding: just test which one works: utf-8, utf-16, euc-kr, cp949, latin_1
reviews = pd.DataFrame(imdb)
stop_words = stopwords.words('english')

def preprocess_reviews(review):
    preprocessed_review = review
    preprocessed_review = re.sub(r'<.*?>', '', review)
    preprocessed_review = " ".join(word for word in preprocessed_review.split() if word not in stop_words)
    return preprocessed_review

reviews['Processed review'] = reviews['review'].apply(lambda x: preprocess_reviews(x))

from textblob import Word, TextBlob
text = TextBlob("Hello, I hat to admit, but I am working on Saturday night! I am leaving for a business trip in a couple of hours, damn")
text.tags # just to show that you could do that
text.sentences
text.sentiment
# --------------------------------------------------------------
reviews['polarity'] = reviews['Processed review'].apply(lambda x: TextBlob(x).sentiment.polarity)
reviews['subjectivity'] = reviews['Processed review'].apply(lambda x: TextBlob(x).sentiment.subjectivity)
# ------- Visualize --------------------------------------------
import seaborn as sns
import matplotlib.pyplot as plt
#%matplotlib inline
sns.displot(reviews['polarity'])
sns.displot(reviews['subjectivity'])