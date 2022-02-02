"""
    This file contain functions responsable for analyzing a folder and returning a list of files
    organized according to a hierarchy. The result of it will be the input for the next process of
    the pipeline.
    The training files should be organized in folders by similar name.
    Example:
    data/
       |
       |----folder1/
                 |---f1.txt
                 |---f1.wav
                 |---f2.txt
                 |---f2.wav
       |
       |----folder2/
                 |---f1.txt
                 |---f1.wav
                 |---f2.txt
                 |---f2.wav
"""

import os

def training_resources(folder='data', show_path=False):
    dir = os.listdir()

    if folder not in dir:
        raise RuntimeError('Could not find folder {folder}'.format(folder = folder))

    os.chdir(folder)

    sub = []

    for f in os.listdir():
        path = os.path.join(os.getcwd(), f)
        if os.path.isdir(path):
            os.chdir(f)

            folder = []
            for fi in os.listdir():
                if (show_path): folder.append(os.path.join(os.getcwd(), fi))
                else: folder.append(fi)

            os.chdir('..')
            sub.append(folder)
        else:
            sub.append(f)

    return sub