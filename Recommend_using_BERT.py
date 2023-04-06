# Library
import pandas as pd
import numpy as np
import spacy
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
from transformers import AutoTokenizer, AutoModel
import torch
from sklearn import feature_extraction
from bs4 import BeautifulSoup
import re
import nltk
import matplotlib.pyplot as plt
from sklearn.metrics import calinski_harabasz_score, davies_bouldin_score
from sklearn.metrics import silhouette_score


# Load the data
data = pd.read_csv('cleaned_data.csv')

# Drop missing values
data = data.dropna()
# Drop duplicates
data = data.drop_duplicates()

# Take some sample of the data, since data is too large, it take too long to calculate
np.random.seed(10)
data = data.sample(10)

#--------------------Text Feature Enginnering------------------------------#

# input prepreocess text
nlp = spacy.load("en_core_web_sm")

def preprocess(text):
    doc = nlp(text)
    return " ".join(token.lemma_ for token in doc if not token.is_stop and token.is_alpha)

data["description_preprocessed"] = data["description"].apply(preprocess)

# BERT feature extraction
tokenizer = AutoTokenizer.from_pretrained("bert-base-uncased")
model = AutoModel.from_pretrained("bert-base-uncased")

def get_bert_embedding(text):
    inputs = tokenizer(text, return_tensors="pt", padding=True, truncation=True, max_length=512)
    outputs = model(**inputs)
    return outputs.last_hidden_state.mean(axis=1).detach().numpy()

data["bert_embedding"] = data["description_preprocessed"].apply(get_bert_embedding)

# Standardize BERT embeddings
scaler = StandardScaler()
bert_embeddings = np.vstack(data["bert_embedding"].values)
scaled_bert_embeddings = scaler.fit_transform(bert_embeddings)

# Cluster books using K-Means
n_clusters = 20
kmeans = KMeans(n_clusters=n_clusters)
data["cluster"] = kmeans.fit_predict(scaled_bert_embeddings)

# Recommendation function
def recommend_book(input_text, top_n=1):
    input_text_preprocessed = preprocess(input_text)
    input_bert_embedding = get_bert_embedding(input_text_preprocessed)
    input_scaled_bert_embedding = scaler.transform(input_bert_embedding)
    
    input_cluster = kmeans.predict(input_scaled_bert_embedding)
    filtered_books = data[data["cluster"] == input_cluster[0]]

    similarity_scores = []
    for book_embedding in filtered_books["bert_embedding"]:
        similarity_scores.append(torch.nn.functional.cosine_similarity(
            torch.tensor(input_bert_embedding), torch.tensor(book_embedding))[0].item())
    
    best_match_index = np.argmax(similarity_scores)
    
    return filtered_books.iloc[best_match_index]

# Test the recommendation system
input_text = "A thrilling mystery novel with unexpected twists."
recommended_book = recommend_book(input_text)
print(recommended_book)