"""
This file only takes the numpy array which represents
the not normalized audio signal and results in a normalized numpy array. 
You can either import it to use its functions or you can execute as a main
file, pass the audio path and see the audio result.
FLAGS:
    -p: Plot the input and output audio
"""

from email.mime import audio
import numpy as np
from scipy.io import wavfile
import matplotlib.pyplot as plt
import sys

if (__name__ == '__main__'):
    try:
        audio_path = str(sys.argv[1])
        samplerate, audio_data = wavfile.read(audio_path)

        ratio = 32767 / np.max(np.abs(audio_data))
        normalized_signal = audio_data

        for i in range(0, len(normalized_signal)):
            if (normalized_signal.ndim == 1):
                normalized_signal[i] = round(normalized_signal[i]*ratio)
            elif (normalized_signal.ndim == 2):
                normalized_signal[i, 0] = round(normalized_signal[i, 0]*ratio)
                normalized_signal[i, 1] = round(normalized_signal[i, 1]*ratio)

        if ('-p' in sys.argv):
            time = len(audio_data) / float(samplerate)
            print(time)

            # Input audio
            plt.figure(1)
            plt.subplot(131)
            plt.plot(audio_data)
            plt.ylabel("Wave")
            #plt.show()

            # Normalized audio
            plt.figure(1)
            plt.subplot(133)
            plt.plot(normalized_signal)
            plt.ylabel("Wave")
            plt.suptitle("Not normalized/Normalized")
            plt.show()

    except IndexError:
        print("Please inform the audio file")
    except FileNotFoundError:
        print("Could not find the file")