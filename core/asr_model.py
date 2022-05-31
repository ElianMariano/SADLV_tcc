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

# X shape: (N, 16, 8, 1)
# Y shape: (N)
# Where N is the batch size

import tensorflow as tf
from tensorflow.keras.layers import LSTM, BatchNormalization, Dropout, Dense, MaxPooling1D, Flatten, Conv1D
from tensorflow.keras.models import Sequential
import pandas as pd

def phoneme_detector(length):
    model = Sequential()
    model.add(Conv1D(16, 3, activation='relu', input_shape=(16, 8)))
    model.add(MaxPooling1D(3, 3))
    model.add(Dropout(0.2))
    model.add(LSTM(length*2, activation='relu', return_sequences=True))
    model.add(Dropout(0.2))
    model.add(BatchNormalization())
    model.add(Flatten())
    model.add(Dense(length*2, activation='softmax'))
    model.add(Dropout(0.2))
    # model.add(Dense(128, activation='softmax'))
    # model.add(Dropout(0.2))
    # model.add(Dense(64, activation='softmax'))
    # model.add(Dropout(0.2))
    # model.add(TimeDistributed(Dropout(0.2)))
    model.add(Dense(length, activation='softmax'))

    return model

if __name__ == '__main__':
    # Load the phoneme labels format
    phoneme_labels = pd.read_csv('phoneme_code.csv').set_index('phoneme_label').T.to_dict('list')
    output_length = len(phoneme_labels)

    model = phoneme_detector(output_length)

    opt = tf.keras.optimizers.Adam(learning_rate=0.001, decay=1e-6)

    model.compile(
        loss='sparse_categorical_crossentropy',
        optimizer=opt,
        metrics=['accuracy']
    )

    print(model.summary())