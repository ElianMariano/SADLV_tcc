"""
    This file will input the data into the NN and will result a file of
    the current learning process of the neural network.
"""

from load_audio import load
from config import read_config
from asr_model import phoneme_detector
import tensorflow as tf

def train(EPOCHS, BATCH_SIZE, DATASET):
    model = phoneme_detector(62)

    opt = tf.keras.optimizers.Adam(learning_rate=0.001, decay=1e-6)

    model.compile(
        loss='sparse_categorical_crossentropy',
        optimizer=opt,
        metrics=['accuracy']
    )

    for file in DATASET:
        print('Loading the dataset')
        (x_train, y_train) = load(train_file=file)

        print('Training the model')
        model.fit(x_train, y_train, epochs=EPOCHS, batch_size=BATCH_SIZE)
    
    model.save('save_model')