"""
Initial model for phoneme detection. It is expected that this model should be able to map the audio
into a sequence of phonemes correctly. So because of the sequence nature of the audio signal, it is
supposed that a RNN (Recurrent Neural Network) should be used to peform this task.
Along with that, the audio should be transformed into a mel frequency spectogram, a technique which
allows the audio wave to be represented by a set of image frames. These frames could be fed into
a CNN (Convolutional Neural Network), and then resulting in a feature map, this feature map will
then be fed into the RNN, resulting in the probability for each phoneme.
The resulting probabilities will be compared in order to find the right sequence of phonemes,
basing on the CTC algorithm.
"""

import tensorflow as tf
from tensorflow.keras.layers import LSTM, CuDNNLSTM, BatchNormalization, Dropout, Dense, Conv2D
from tensorflow.keras.models import Sequential
import pandas as pd

# Load the phoneme labels format
phoneme_labels = pd.read_csv('phoneme_code.csv').set_index('phoneme_label').T.to_dict('list')
output_length = len(len(phoneme_labels))

model = Sequential()

# Write a Convolutional Layer

model.add(CuDNNLSTM(output_length*8, return_sequences=True)) # Inform the input shape: input_shape=(train_x.shape[1:])
model.add(Dropout(0.2))
model.add(BatchNormalization())  #normalizes activation outputs, same reason you want to normalize your input data.

model.add(CuDNNLSTM(output_length*8, return_sequences=True))
model.add(Dropout(0.1))
model.add(BatchNormalization())

model.add(CuDNNLSTM(output_length*8))
model.add(Dropout(0.2))
model.add(BatchNormalization())

model.add(Dense(output_length*16, activation='relu'))
model.add(Dropout(0.2))

model.add(Dense(output_length, activation='softmax'))

opt = tf.keras.optimizers.Adam(lr=0.001, decay=1e-6)

# Compile model
model.compile(
    loss='sparse_categorical_crossentropy',
    optimizer=opt,
    metrics=['accuracy']
)

# model
# model = keras.models.Sequential()
# model.add(keras.Input(shape=(10, 10)))
# model.add(layers.SimpleRNN(1000, activation="relu"))
# model.add(layers.Dense(10))

# print(model.summary())

# loss and optimizer
# loss = keras.losses.SparseCategoricalCrossentropy(from_logits=True)
# optim = keras.optimizers.Adam(learning_rate=0.001)
# metrics = ["accuracy"]

# model.compile(loss=loss, optimizer=optim, metrics=metrics)