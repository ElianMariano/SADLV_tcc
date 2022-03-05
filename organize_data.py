"""
    TODO Read files by .csv
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

    os.chdir('..')

    return sub