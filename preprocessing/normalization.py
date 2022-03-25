"""
This file only takes the numpy array which represents
the not normalized audio signal and results in a normalized numpy array. 
You can either import it to use its functions or you can execute as a main
file, pass the audio path and see the audio result.
If the audio is already normalized, this program will take no result.
FLAGS:
    -p: Plot the input and output audio
    -w [file_name]: Writes the result into .wav file
    -a [audio_path]: Selects a audio file
"""

import numpy as np
from scipy.io import wavfile
import matplotlib.pyplot as plt
import sys

def normalize(audio_signal):
    ratio = 32767 / np.max(np.abs(audio_signal))
    normalized_signal = audio_signal

    for i in range(0, len(normalized_signal)):
        if (normalized_signal.ndim == 1):
            normalized_signal[i] = round(normalized_signal[i]*ratio)
        elif (normalized_signal.ndim == 2):
            normalized_signal[i, 0] = round(normalized_signal[i, 0]*ratio)
            normalized_signal[i, 1] = round(normalized_signal[i, 1]*ratio)
        
    return normalized_signal

if __name__ == '__main__':
    samplerate = 0
    audio_data = []

    normalized_audio = []

    if ('-a' in sys.argv):
        try:
            audio_path = str(sys.argv[sys.argv.index('-a')+1])
            samplerate, audio_data = wavfile.read(audio_path)

            normalized_audio = normalize(audio_data)
        except Exception:
            print("Please inform a audio file")        

    if ('-w' in sys.argv):
        try:
            output = str(sys.argv[sys.argv.index('-w')+1])
            wavfile.write("{filename}.wav".format(filename = output), samplerate, normalized_audio)
        except Exception:
            print("Please inform the name of the output file")

    if '-p' in sys.argv and '-a' in sys.argv:
        #time = len(audio_data) / float(samplerate)
        #print(time)

        # Input audio
        plt.figure(1)
        plt.subplot(131)
        plt.plot(audio_data)
        plt.ylabel("Wave")
        plt.title("Not normalized audio")
        #plt.show()

        # Normalized audio
        plt.figure(1)
        plt.subplot(133)
        plt.plot(normalized_audio)
        plt.ylabel("Wave")
        plt.suptitle("Normalization camparison")
        plt.title("Normalized audio")
        plt.show()