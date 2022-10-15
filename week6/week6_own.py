names = ['Heidi', 'John', 'Jenny']
print("-and-".join(names)) # Heidi-and-John-and-Jenny
# --------------------------------------------------------------
name = 'Heidi'
name.isalpha() # False if there were 0-9
age = '22'
age.isdigit() # False if there were a-z
nameAndAge = 'Heidi22'
nameAndAge.isalnum() # can be both
# ----- lambda -------------------------------------------------
m = lambda x: x+10
print(m(3)) # 13
# --------------------------------------------------------------
import nltk
import pandas as pd
sentences = """
Regularly and thoroughly clean your hands with an alcohol-based hand rub or wash them with soap and water. 
This eliminates germs including viruses that may be on your hands.
Avoid touching your eyes, nose and mouth. 
Hands touch many surfaces and can pick up viruses. 
Once contaminated, hands can transfer the virus to your eyes, nose or mouth. 
From there, the virus can enter your body and infect you.
Cover your mouth and nose with your bent elbow or tissue when you cough or sneeze. 
Then dispose of the used tissue immediately into a closed bin and wash your hands.
By following good ‘respiratory hygiene’, you protect the people around you from viruses, which cause colds, flu and COVID-19.
Clean and disinfect surfaces frequently especially those which are regularly touched, 
such as door handles, faucets and phone screens or mouth. 
From there, the virus can enter your body and infect you.
"""
tokenized_sent = nltk.sent_tokenize(sentences)
# --------------------------------------------------------------
from sklearn.feature_extraction.text import CountVectorizer
vectorizer = CountVectorizer()
X = vectorizer.fit(tokenized_sent)
print(X.vocabulary_)   # ToDo what was the underscore at the end for again? -> look up later
# --------------------------------------------------------------
vectorizer = CountVectorizer(lowercase=False)
X = vectorizer.fit(tokenized_sent)
print(X.vocabulary_)
# --------------------------------------------------------------
vectorizer = CountVectorizer(stop_words='english')
x = vectorizer.fit(tokenized_sent)
print(x.vocabulary_)

print(vectorizer.get_stop_words())  # to see the stopwords of the library
x.vocabulary_.get('clean') # ToDo what was this again?
# ------- Fit Transform ----------------------------------------
ft = vectorizer.fit_transform(tokenized_sent)
count_array = ft.toarray()
print(count_array)
print(count_array.shape)  # There are 11 sentences, and there are 60 unique words in these sentences

count_token = vectorizer.get_feature_names_out()
count_token

df_countvect = pd.DataFrame(data=count_array, columns=count_token)
df_countvect
# ------- TF-IDF -----------------------------------------------
from sklearn.feature_extraction.text import TfidfVectorizer
tfidf = TfidfVectorizer(stop_words='english')
tf_results = tfidf.fit_transform(tokenized_sent)
tfidf_token = tfidf.get_feature_names_out()
df_tfidfvect = pd.DataFrame(data=tf_results.toarray(), columns=tfidf_token)
print(df_tfidfvect)

word_count = pd.DataFrame({
    'words': tfidf_token,
    'tf-idf score': tf_results.sum(axis=0).flat # ToDo think about why we need the .flat again!
})
word_count.sort_values(by=['tf-idf score'], ascending=False)