# TCC-Automatic-Speech-Recognition
This project aims to create a _RNN_ which is capable to map audio input signals into a corresponding text phoneme.

## Creating the Virtual Environment

> python -m venv env

## Installing the Dependencies

> python -m pip install -r requirements.txt

## Automatic Speech Recognition
This a _ASR (Automatic Speech Recognition)_ based system, so it means that its processing pipeline cosists in the following phases:

- Pre-processing
- Feature extraction
    - Artificial neural networks
- Classification
    - Language model

### Pre-processing

The pre-processing stage cleans the speech signal in order to make the speech as clear as possible. To do so, it uses a lot of diffirent techniques like audio normalising and noise reduction.

### Feature extraction

The feature extraction stage is responsable for taking the audio signal organize into its most important parts, which may be a word, sillable or phoneme. This proccess can be done in a lot of different ways, but for the current project it will be used __Artificial Neural Networks__ more specifically __Recurrent Neural Networks.__

### Classification

The classification stage takes the result gathered in the feature extraction stage and relates to the corresponding __Language model__ unit. The language model can be anything up to phrase, word, sillable or phoneme.

## Recurrent neural network

A recurrent neural netork is a special kind of _RN_ calculates its result based on iteration, which means it runs inside a loop feeding the last iteration into the current one and so on.
