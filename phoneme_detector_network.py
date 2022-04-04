"""
Initial model for phoneme detection. It is expected that this model should be able to map the audio
into a sequence of phonemes correctly. So because the sequence nature of the audio signal, it is
supposed that a RNN (Recurrent Neural Network) should be use to peform this task.
Along with that, the audio could transformed into a mel frequency spectogram, a technique which
allows the audio wave to be represented by a set of image frames. These frames could be fed into
a CNN (Convolutional Neural Network), and then resulting in a feature map, this feature map will
then be fed into the RNN, resulting in the probability for each phoneme.
The resulting probabilities will be compared in order to find the right sequence of phonemes,
basing on the CTC algorithm.
"""

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