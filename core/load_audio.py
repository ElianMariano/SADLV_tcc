"""
    This file loads the wave files an organize everything inside a numpy array.
    If is needed, it will load the traning labels together with the audio files
    based on the TIMIT audio database, segmenting the audio in frames.
    The current file format needed to define the label should be as follows (ending with .PHN extension):
        <stating_frame> <ending_frame> <phoneme> \n
            where:
                <starting_frame> := Number of the first frame of the phoneme
                <ending_frame> := Number of the last frame of the phoneme
                <phoneme> := Specific phoneme written as text (N for none)
    Every specic sound phoneme will be translated as a number label in order to train the Neural Network.
    Each number will be stored inside a main .csv file inside the database main folder.
"""

import numpy as np
import re
import pandas as pd
import librosa
import os
import warnings

def load(phoneme_code, quantity=0, folder='timit'):
    # Ignores the warnings thrown by pandas library
    warnings.simplefilter(action='ignore', category=FutureWarning)

    dir = os.listdir()
    if folder not in dir:
        raise RuntimeError('Could not find folder {folder}'.format(folder = folder))

    train_data = pd.read_csv(os.path.join(folder, 'train_data.csv')).to_numpy()

    if quantity > 0:
        train_data = train_data[:quantity]

    x_train = np.empty(shape=(0, 16, 8, 1))
    y_train = np.empty(shape=(0))

    phoneme_labels = pd.read_csv(phoneme_code).set_index('phoneme_label').T.to_dict('list')

    os.chdir(os.path.join(folder, 'data'))

    # Phoneme with code
    coded_phonemes = []

    for file in train_data:
        file_name = ''
        if os.name == 'nt':
            file_name = file[6]
        else:
            file_name = file[5]

        if bool(re.search(r"(\.WAV)(\.wav)", file_name)):
            y, sr = librosa.load(file_name)

            # Create a mel spectrogram from the audio
            mel_spectrogram = librosa.feature.melspectrogram(y=y, sr=sr, n_mels=128, fmax=8000)
            mel_spectrogram = cut_spectrogram(mel_spectrogram)

            phoneme_file = re.sub(r"(\.WAV)(\.wav)", ".PHN", file_name)

            # Returns a labeled phoneme start and ending index
            coded_phonemes = read_phoneme(phoneme_file, phoneme_labels)
            # time_label = index_to_seconds(coded_phonemes, sr)

            # Returns the probabities for a specific spectrogram
            probabilities = probability_vector(spectrogram=mel_spectrogram, phn_data=coded_phonemes, phoneme_labels=phoneme_labels)

            # print(mel_spectrogram.shape)
            # print(probabilities.shape)
            # print(x_train.shape)

            x_train = np.concatenate((x_train, mel_spectrogram), axis=0)
            y_train = np.concatenate((y_train, probabilities), axis=0)

    return (x_train, y_train)

# Returns the audio data for a specif file, labeled as phoneme
def read_phoneme(phoneme_file, phoneme_labels) -> np.ndarray:
    sa1 = pd.read_csv(phoneme_file, ' ').to_numpy()

    data = []
    for i in range(0, len(sa1)):
        data.append([sa1[i, 0], sa1[i, 1], phoneme_labels[sa1[i, 2]][0]])

    return np.array(data)

# Cut the mel spectrogram into frames using np.reshape
# cutWidth variable should be power of 2
def cut_spectrogram(mel_spectrogram, cut_width=8) -> np.ndarray:
    SHAPE = mel_spectrogram.shape

    return np.reshape(mel_spectrogram, (SHAPE[1], int(SHAPE[0]/cut_width), cut_width, 1))

# Returns a matrix of probabilities for a specific spectrogram
def probability_matrix(spectrogram, phn_data, phoneme_labels, null_character=False) -> np.ndarray:
    prob_shape = (spectrogram.shape[0], len(phoneme_labels))

    if null_character:
        prob_shape = (spectrogram.shape[0], len(phoneme_labels)+1)

    # Probabilities by spectrogram
    probabilities = np.zeros(prob_shape)

    # Label width
    WIDTH = phn_data[len(phn_data)-1][1] / spectrogram.shape[0]

    # Run through all the probability set in order to assign the probabilities
    current = 0
    for i in range(0, len(probabilities)-1):
        phoneme = find_phoneme_code_by_position(current, phn_data)
        probabilities[i, phoneme] = 1

        current += WIDTH

    return probabilities

# Return a vector of probabilites
def probability_vector(spectrogram, phn_data, phoneme_labels, null_character=False) -> np.ndarray:
    prob_shape = (len(phoneme_labels))

    if null_character:
        prob_shape = (len(phoneme_labels)+1)

    # Probabilities by spectrogram
    probabilities = np.zeros(prob_shape)

    # Label width
    WIDTH = phn_data[len(phn_data)-1][1] / spectrogram.shape[0]

    # Run through all the probability set in order to assign the probabilities
    current = 0
    for i in range(0, len(probabilities)-1):
        phoneme = find_phoneme_code_by_position(current, phn_data)
        probabilities[i] = phoneme

        current += WIDTH

    return probabilities

# Returns the phoneme based on the time
def find_phoneme_code_by_position(current, phn_data) -> int:
    if current < phn_data[0, 0]:
        return 0
    
    if current >= phn_data[len(phn_data)-1, 0]:
        return 0
    
    for i in range(0, len(phn_data)):
        if current >= phn_data[i, 0] and current < phn_data[i, 1]:
            return phn_data[i, 2]

# Loads a test data in order to evaluate the model
def load_test_data():
    pass

# Converts the phoneme label index into the actual time stamp of the audio signal
def index_to_seconds(coded_phonemes, sr) -> np.ndarray:
    data = coded_phonemes.astype('float64')

    for i in range(0, len(coded_phonemes)):
        data[i][0] = coded_phonemes[i][0] / sr
        data[i][1] = coded_phonemes[i][1] / sr

    return data