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

    audio_files = []

    phoneme_labels = pd.read_csv(phoneme_code).set_index('phoneme_label').T.to_dict('list')

    os.chdir(os.path.join(folder, 'data'))

    # Current audio data
    data = []
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

            TIME = len(y) / sr

            # Returns a labeled phoneme start and ending index
            coded_phonemes = read_phoneme(phoneme_file, phoneme_labels)
            time_label = index_to_seconds(coded_phonemes, sr)
            print(phoneme_labels)

            # labeled_audio(mel_spectrogram, time_label, TIME, phoneme_labels)

        # if len(data) != 0 and len(coded_phonemes) != 0:
        #     audio_files.append(labeled_audio(coded_phonemes, data))
        #     coded_phonemes = []
        #     data = []

    return audio_files

# Returns the audio data for a specif file, labeled as phoneme
def read_phoneme(phoneme_file, phoneme_labels):
    sa1 = pd.read_csv(phoneme_file, ' ').to_numpy()

    data = []
    for i in range(0, len(sa1)):
        data.append([sa1[i, 0], sa1[i, 1], phoneme_labels[sa1[i, 2]][0]])

    return np.array(data)

# Cut the mel spectrogram into frames using np.reshape
# cutWidth variable should be power of 2
def cut_spectrogram(mel_spectrogram, cut_width=8):
    SHAPE = mel_spectrogram.shape

    return np.reshape(mel_spectrogram, (int(SHAPE[0]/cut_width), SHAPE[1], cut_width))

# Converts the phoneme label index into the actual time stamp of the audio signal
def index_to_seconds(coded_phonemes, sr):
    data = coded_phonemes.astype('float64')

    for i in range(0, len(coded_phonemes)):
        data[i][0] = coded_phonemes[i][0] / sr
        data[i][1] = coded_phonemes[i][1] / sr

    return data

# TODO Use this function to assign every mel spectrogram frame to a probability set
def labeled_audio(spectrogram, time_label, time, phoneme_labels):
    SHAPE = spectrogram.shape

    # data = np.array([])
    # print(f"TIME: {time}")
    for i in range(0, SHAPE[0]):
        START, END = (i*time/SHAPE[0], (i+1)*time/SHAPE[0])
        print(f"Starting Time: {START}, Ending Time: {END}")
        # print(phoneme_by_time(spectrogram, START, END, time_label, phoneme_labels))

    # print('\n')

# TODO Return a vector of probabilities for a given time chunk
# spectrogram: The audio spectrogram
# start, end: Where the chunk is located
# time_label: A label containing the time stamps which every phoneme occurs
# phoneme_labels: A dictionary which translates the phoneme label to the phoneme index code
# null_character: Defines if a null character is needed or not
def phoneme_by_time(spectrogram, start, end, time_label, phoneme_labels, null_character=False):
    # Start the result probilities with 0
    probabilties = np.array([0] * len(phoneme_labels), dtype=np.float32)

    # Start and ending index for search
    a, b = (0, len(time_label)-1)

    # Ignore edges while searching
    if end < time_label[0][0]:
        pass
    elif start >= time_label[len(time_label)-1][1]:
        pass

    while start >= time_label[a][1] or end <= time_label[b][0]:
        if start >= time_label[a][1]:
            a += 1
        elif end <= time_label[b][0]:
            b -= 1

    # Stores the result chunk
    result = spectrogram[a:b]