"""
    This file should have flags to start the training process and to evaluate the audio.
    In both cases it should pre-process the audio before the pipeline continue. After
    training the Neural Network it should save the NN data into a file."""

HELP = """FLAGS:
    -t [training_folder]: Train the neural neural network according with the data inside the folder
    -l [load_trained_nn]: Load previous trained neural network
    -e [audio_file] [text_file]: Compare the audio file with a file
    -b [start_index] [end_index]: Choose a limited batch of training data
    -h|-help: Show this help information
"""

import sys
import organize_data
import load_audio

# TODO Make the -t parameter receive the datased location and the phoneme labels
if __name__ == "__main__":
    if "-t" in sys.argv:
        if "-b" in sys.argv:
            try:
                start_index, end_index = int(sys.argv[sys.argv.index("-b")+1]), int(sys.argv[sys.argv.index("-b")+2])
            except Exception as ex:
                print("Please inform the start and end index")
                print(HELP)

        data = organize_data.training_resources()

        audio = load_audio.load(data, "phoneme_code.csv")
        print(audio)

    if "-l" in sys.argv:
        try:
            trained_nn = sys.argv[sys.argv.index("-l")+1]
            print(trained_nn)
        except IndexError as ex:
            print("Please inform the path to the trained neural network")
            print(HELP)

    if "-e" in sys.argv:
        try:
            audio_file, text_file = sys.argv[sys.argv.index("-e")+1], sys.argv[sys.argv.index("-e")+2]
            print(audio_file)
            print(text_file)
        except IndexError:
            print("Please inform the audio and text file")
            print(HELP)

    if "-b" in sys.argv and "-t" not in sys.argv:
        print("Please inform the training option '-t' in order to train a limited batch of data")
        print(HELP)

    if "-h" in sys.argv or "-help" in sys.argv:
        print(HELP)

    if "-t" not in sys.argv and "-l" not in sys.argv and "-e" not in sys.argv and "-b" not in sys.argv and "-h" not in sys.argv and "-help" not in sys.argv:
        print("Please inform a desired flag option")
        print(HELP)