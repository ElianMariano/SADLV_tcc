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
    Each number will be stored inside a main .csv file.
"""

from email.mime import audio
from scipy.io import wavfile
import numpy as np
import re

def load(files, read_labels=False):
    audio_files = []

    for folder in files:
        for file in folder:
            if bool(re.search(r"\.wav", file)):
                samplerate, data = wavfile.read(file)

                if read_labels:
                    read_phoneme(data, file)
                else:
                    audio_files.append(data)

    return audio_files

# Returns the date for a specif file, labeled as phoneme
def read_phoneme(audio_data, audio_file):
    phn_file = re.sub("(\.WAV.wav)", ".PHN", audio_file)

    audio_labels = []
    with open(phn_file) as f:
        labeled_audio = []
        for line in f:
            line = line.split(" ")

            audio_frame = []
            for i in range(int(line[0]), int(line[1])):
                audio_frame.append(audio_data[i])

            labeled_audio.append([line[2][:-1], audio_frame])

        return labeled_audio