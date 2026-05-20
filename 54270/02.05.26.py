import numpy as np
import matplotlib.pyplot as plt

import tensorflow as tf

# y = x*x
X = np.linspace(0, 1, 200)
Y = np.multiply(X, 2)


model = tf.keras.Sequential([
    tf.keras.layers.Dense(units=128, activation='relu', input_shape=[1]),
    
    tf.keras.layers.Dense(units=64, activation='relu'),
    tf.keras.layers.Dense(units=64, activation='relu'),
    
    tf.keras.layers.Dense(1)
])

my_optimizer = tf.keras.optimizers.Adam(learning_rate=0.001)
model.compile(optimizer=my_optimizer, loss='mse')
model.fit(X, Y, epochs=100, batch_size=10)

model.save('sin_model.keras')

ai_predict = model.predict(X)

plt.plot(X, Y, label='Датасет')
plt.plot(X, ai_predict, label='AI')
plt.legend()
plt.show()


