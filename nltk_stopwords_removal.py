import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer
import numpy as np

df = pd.read_csv("json_to_csv/csv_files/Irish/All_combined_Irish.csv").dropna()
print(df)
print(df.columns)
import nltk

nltk.download('stopwords')
nltk.download('words')

from nltk.corpus import stopwords

stop = stopwords.words('english')
words = set(nltk.corpus.words.words())

df['content'] = df['content'] \
    .apply(lambda x: ' '.join([word for word in x.split() if (word in words) and (word not in stop)]))
# print("1\n", df)

df['content'].to_csv("json_to_csv/csv_files/Irish/All_combined_Irish_stopwords_removed.csv", index=False)

# ...................................
# Extra..............................
# ...................................
"""TFIDF Vectorizor trial with PCA"""

# Create a Vectorizer Object
vectorizer = TfidfVectorizer()
count_df = vectorizer.fit_transform(df.content)
# print("2\n", count_df)

# # Printing the identified Unique words along with their indices
# print("3\n", vectorizer.vocabulary_)  # print("4\n", df[["content"]])

# Encode the Document
vector = vectorizer.transform(df.content)
print(len(vectorizer.get_feature_names()))

# Summarizing the Encoded Texts
print("Encoded Document is:")

# print(vector.toarray())
vec_df = pd.DataFrame(np.matrix.transpose(vector.toarray()))

# vec_df["columns"] = vectorizer.get_feature_names()
print(np.shape(vector.toarray()))
print(vec_df)

from sklearn.decomposition import PCA

pca = PCA(n_components=2)
pca_df = pd.DataFrame(pca.fit_transform(vec_df))
pca_df["columns"] = vectorizer.get_feature_names()
pca_df.reset_index().to_csv("json_to_csv/pca_data/pca_data.csv")
