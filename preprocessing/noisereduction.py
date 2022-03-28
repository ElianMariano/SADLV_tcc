"""
This file abstracts the noisereduce library in order to work well with
the rest of the program.
FLAGS:
    -p: Plot the input and output audio
    -w [file_name]: Writes the result into .wav file
    -a [audio_path]: Selects a audio file
"""

from scipy.io import wavfile
import matplotlib.pyplot as plt
import noisereduce as nr
import sys

def denoise(rate, audio_signal):
    # Coverts the data to mono
    if audio_signal.ndim == 2:
        audio_signal = audio_signal[:, 0]

    # Noise reduced audio
    return nr.reduce_noise(y=audio_signal, sr=rate)

if __name__ == '__main__':
    try:
        samplerate = 0
        audio_data = []

        noise_reduced_audio = []

        if '-a' in sys.argv:
            try:
                audio_path = str(sys.argv[sys.argv.index('-a')+1])
                samplerate, audio_data = wavfile.read(audio_path)

                noise_reduced_audio = denoise(samplerate, audio_data)
            except Exception as ex:
                print("Please inform the audio file")

        if '-w' in sys.argv:
            try:
                output = str(sys.argv[sys.argv.index('-w')+1])
                wavfile.write("{filename}.wav".format(filename=output), samplerate, noise_reduced_audio)
            except Exception:
                print("Please inform the name of the output file")

        if "-p" in sys.argv and '-a' in sys.argv:
            # Input audio
            plt.figure(1)
            plt.subplot(131)
            plt.plot(audio_data)
            plt.ylabel("Wave")
            #plt.show()

            # Normalized audio
            plt.figure(1)
            plt.subplot(133)
            plt.plot(noise_reduced_audio)
            plt.ylabel("Wave")
            plt.suptitle("Noisy audio/Noise reduced audio")
            plt.show()
    except Exception as ex:
        print(ex)