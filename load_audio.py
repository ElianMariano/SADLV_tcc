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

from scipy.io import wavfile
import numpy as np
import re
import pandas as pd
import os

def load(phoneme_code, quantity=0, folder='timit'):
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
        if os.name == 'nt':
            if bool(re.search(r"(\.WAV)(\.wav)", file[6])):
                # TODO Convert the audio into a mel spectrogram
                samplerate, data = wavfile.read(file[6])
                
                phoneme_file = re.sub(r"(\.WAV)(\.wav)", ".PHN", file[6])

                # Returns a labeled phoneme with stops
                coded_phonemes = read_phoneme(phoneme_file, phoneme_labels)
                print(coded_phonemes)
        else:
            if bool(re.search(r"(\.WAV)(\.wav)", file[5])):
                samplerate, data = wavfile.read(file[5])
                
                phoneme_file = re.sub(r"(\.WAV)(\.wav)", ".PHN", file[5])

                # Returns a labeled phoneme with stops
                coded_phonemes = read_phoneme(phoneme_file, phoneme_labels)
        
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

# TODO Cut the mel spectrogram into frames
def melToFrames(cutWidth=6):
    pass

# TODO Converts a index number of an audio signal into the actual second of the audio clip
def indexToSeconds(coded_phonemes):
    pass

# TODO Use this function to assign every mel spectrogram frame to a phoneme code
def labeled_audio(coded_phonemes, audio_data):
    pass