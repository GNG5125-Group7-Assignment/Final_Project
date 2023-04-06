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

# Take some sample of the data. 
# Since data is too large, TF-IDF take too long to calculate
np.random.seed(100)
data = data.sample(1000)

#--------------------Text Feature Enginnering------------------------------#

# input prepreocess text
nlp = spacy.load("en_core_web_sm")

def preprocess(text):
    doc = nlp(text)
    return " ".join(token.lemma_ for token in doc if not token.is_stop and token.is_alpha)

data["description_preprocessed"] = data["description"].apply(preprocess)

# Create feature vectors for TF_IDF
vectorizer = TfidfVectorizer()
description_matrix = vectorizer.fit_transform(data["description_preprocessed"])

# Recommendation function
def recommend_book(input_text, top_n=1):
    input_text_preprocessed = preprocess(input_text)
    input_vector = vectorizer.transform([input_text_preprocessed])
    
    similarity_scores = cosine_similarity(input_vector, description_matrix)
    best_match_index = np.argmax(similarity_scores)
    
    return data.iloc[best_match_index]

# Test the recommendation system
# input_text = "A thrilling mystery novel with unexpected twists."
# recommended_book = recommend_book(input_text)
# print(recommended_book)