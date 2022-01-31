"""
    This file should have flags to start the training process and to evaluate the audio.
    In both cases it should pre-process the audio before the pipeline continue. After
    training the Neural Network it should save the NN data into a file.

    FLAGS:
    -t [training_folder]: Train the neural neural network according with the data inside the folder
    -l [load_trained_NN]: Load previous trained neural network
    -e [audio_file] [text_file]: Compare the audio file with a file
"""

import sys

if __name__ == "__main__":
    if sys.argv[1] == "-t":
        pass
    elif sys.argv[1] == "-l":
        pass
    elif sys.argv[1] == "-e":
        pass