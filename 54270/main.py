import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt


monsters = np.array([1, 2, 3, 4, 5, 6, 7], dtype=float)
crystals = np.array([13, 16, 19, 22, 25, 28, 31], dtype=float)


model = tf.keras.Sequential([
    tf.keras.layers.Dense(units=1, input_shape=[1])
])

model.compile(optimizer='sgd', loss='mse')
model.fit(monsters, crystals, epochs=500, batch_size=1)


ai_predict = model.predict(monsters)


plt.plot(monsters, crystals, label='Датасет')
plt.plot(monsters, ai_predict, label='AI')
plt.legend()
plt.show()