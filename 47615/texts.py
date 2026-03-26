import tensorflow as tf
from tensorflow.keras.preprocessing.sequence import pad_sequences
import numpy as np


texts = []
labels = []


tokenizer = tf.keras.preprocessing.text.Tokenizer()
tokenizer.fit_on_texts(texts)
word_index = tokenizer.word_index
sequences = tokenizer.texts_to_sequences(texts)
pad_sequences_ = pad_sequences(sequences, padding='post')

model = tf.keras.Sequential([
    tf.keras.layers.Embedding(1000, 16),
    tf.keras.layers.Flatten(),
    tf.keras.layers.Dense(16, activation='relu'),
    tf.keras.layers.Dense(1, activation='sigmoid')
])

model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

model.fit(pad_sequences_, labels, epochs=100)


test_text = "Фильм показался мне скучным"
test_seq = tokenizer.texts_to_sequences(test_text)
test_pad = pad_sequences(test_seq, maxlen=pad_sequences_.shape[1], padding='post')

prediction = model.predict(test_pad)
print(f"Вероятность положительного отзыва: {prediction[0][0]}")
