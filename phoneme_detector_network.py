import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers

# model
model = keras.models.Sequential()
model.add(keras.Input(shape=(10, 10)))
model.add(layers.SimpleRNN(1000, activation="relu"))
model.add(layers.Dense(10))

print(model.summary())

# loss and optimizer
loss = keras.losses.SparseCategoricalCrossentropy(from_logits=True)
optim = keras.optimizers.Adam(learning_rate=0.001)
metrics = ["accuracy"]

model.compile(loss=loss, optimizer=optim, metrics=metrics)