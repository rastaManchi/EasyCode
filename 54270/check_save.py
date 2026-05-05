import tensorflow as tf
import numpy as np


model = tf.keras.models.load_model('sin_model.keras')

test_data = np.array([200.0])
result = model.predict(test_data)
print(result)
