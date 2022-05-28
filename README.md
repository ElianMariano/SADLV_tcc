# SADLV
SADLV is a platform which can facilitate the proccess that a phoaudiologist takes in order to evaluate the progress of their patients.
To achieve this result, the project implements an _Automatic Speech Recognition System_ in order to predict the accuracy of speech inside an audio data.

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

[Click here,](docs/core.md) if you want to know more about how the _ASR_ system used in this project works.

## Backend
The Backend used in this project is based on the __Flask__ library.
The Database used is __PostgreSql__.

## Frontend
The Frontend of the project is developend with the __ReactJs__ Framework.