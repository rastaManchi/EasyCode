import tensorflow as tf
import numpy as np
from tensorflow.keras.preprocessing.text import Tokenizer
import pandas as pd

def convert_rating_to_index(rating):
    number = rating.split()[0]
    return int(number) - 1

data = pd.read_csv("mc.csv", encoding="latin-1")
data = data[['review', 'rating']]
X = data['review'].values
Y = data['rating'].map(convert_rating_to_index).values

tokenizer = Tokenizer()
tokenizer.fit_on_texts(X)
sequences = tokenizer.text_to_sequences(X)