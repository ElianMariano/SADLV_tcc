### load_audio.py

This file contains functions which are used to treat the audio before it go to the training or testing A.I. model.
If you want to understand more, please read the following description of these functions:

```
def load(phoneme_code, quantity, folder):
    ...
```
This function load and prepare the dataset for the training process.

- _phoneme\_code:_ A _.csv_ file which contains all the possible phonemes of the language.
- _quantity \[optional\]:_ The quantity of data which will be read inside the dataset. By default the whole dataset will be read.
- _folder \[optional\]:_ The folder which the dataset is located. By default the folder with the name \'timit\' is considered.

```
def read_phoneme(phoneme_files, phoneme_labels):
    ...
```
This function assign each phoneme in a specif file to its corresponding phoneme code.

- _phoneme\_file:_ A file with the extension \'.PHN\' containing the time stamp in which the phonemes appear in a specific audio signal.
- _phoneme\_labels:_ A dictionary mapping a phoneme into its unique code number.

```
def cut_spectrogram(mel_spectrogram, cut_width):
    ...
```
Divides the mel spectrogram into sections.

- _mel\_spectrogram:_ A mel spectrogram of a specif audio signal.
- _cut\_width:_ The width of every section of spectrogram. By the default the value is 8.

```
def index_to_seconds(coded_phonemes, sr):
    ...
```
Assign every phoneme to its actual time stamp.

- _coded\_phonemes:_ An array containing all the phonemes and its respective time stamp in which it occurs inside an specif audio signal.
- _sr:_ The sample rate of the audio signal.