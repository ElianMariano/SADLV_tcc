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

import code
from email.mime import audio
from scipy.io import wavfile
import re
import csv
import os

def load(files, phoneme_code):
    audio_files = []

    phoneme_labels = load_phoneme_labels(phoneme_code)
    
    os.chdir(os.path.join('timit', 'data'))

    # Current audio data
    data = []
    # Phoneme with code
    coded_phonemes = []

    for file in files:
        if os.name == 'nt':
            if bool(re.search(r"(\.WAV)(\.wav)", file[6])):
                samplerate, data = wavfile.read(file[6])
                
                phoneme_file = re.sub(r"(\.WAV)(\.wav)", ".PHN", file[6])

                # Returns a labeled phoneme with stops
                coded_phonemes = read_phoneme(phoneme_file, phoneme_labels)
        else:
            if bool(re.search(r"(\.WAV)(\.wav)", file[5])):
                samplerate, data = wavfile.read(file[5])
                
                phoneme_file = re.sub(r"(\.WAV)(\.wav)", ".PHN", file[5])

                # Returns a labeled phoneme with stops
                coded_phonemes = read_phoneme(phoneme_file, phoneme_labels)
        
        if len(data) != 0 and len(coded_phonemes) != 0:
            audio_files.append(labeled_audio(coded_phonemes, data))
            coded_phonemes = []
            data = []

    return audio_files

# Separerates the audio segment with a phoneme code for each specific chunk of the audio
def labeled_audio(coded_phonemes, audio_data):
    audio = []
    for constraints in coded_phonemes:
        chunk = []
        for i in range(0, len(audio_data)):
            if i >= int(constraints[0]) and i < int(constraints[1]):
                chunk.append(audio_data[i])
        
        audio.append([constraints[2], chunk])
    
    return audio

# Returns the audio data for a specif file, labeled as phoneme
def read_phoneme(phoneme_file, phoneme_labels):
    phoneme_data = []

    with open(phoneme_file) as f:
        for line in f:
            data = line.split(" ")
            data[2] = phoneme_labels[data[2].replace('\n', '')]
            phoneme_data.append(data)

        f.close()

    return phoneme_data

# Returns an dictionary of phonemes linking the label with the code
def load_phoneme_labels(file):
    with open(file) as f:
        csvreader = csv.reader(f)

        # Skips the header
        next(csvreader)

        rows = {}
        for row in csvreader:
            rows[row[0]] = row[1]
        
        f.close()

        return rows