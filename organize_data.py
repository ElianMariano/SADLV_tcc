"""
    Read the directory for the audio files inside a .csv file.
"""

import os
import csv

def training_resources(folder='timit'):
    dir = os.listdir()

    if folder not in dir:
        raise RuntimeError('Could not find folder {folder}'.format(folder = folder))

    os.chdir(folder)

    rows = []
    with open("train_data.csv") as f:
        csvreader = csv.reader(f)

        # Skips header
        next(csvreader)

        for row in csvreader:
            if row[0] == '':
                break

            rows.append(row)

        f.close()
    
    os.chdir('..')

    return rows