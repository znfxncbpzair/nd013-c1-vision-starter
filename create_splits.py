import argparse
import glob
import os
import random

import numpy as np

from utils import get_module_logger
import shutil


def split(source, destination):
    """
    Create three splits from the processed records. The files should be moved to new folders in the
    same directory. This folder should be named train, val and test.

    args:
        - source [str]: source data directory, contains the processed tf records
        - destination [str]: destination data directory, contains 3 sub folders: train / val / test
    """
    # TODO: Implement function
    #Get data from filename
    try:
        files = [filename for filename in glob.glob(f'{source}/*.tfrecord')]
    except Exception as err:
        print("Unable to access file")
    np.random.shuffle(files)

    # spliting files
    train_files, val_file, test_file = np.split(files, [int(.75*len(files)), int(.9*len(files))])

    # create dirs and move data files into them
    train_dir = os.path.join(destination, 'train', '')
    os.makedirs(train_dir, exist_ok=True)
    for f in train_files:
        shutil.move(f, train_dir)

    val_dir = os.path.join(destination, 'val', '')
    os.makedirs(val_dir, exist_ok=True)
    for f in val_file:
        shutil.move(f, val_dir)

    test_dir = os.path.join(destination, 'test', '')
    os.makedirs(test_dir, exist_ok=True)
    for f in test_file:
        shutil.move(f, test_dir)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Split data into training / validation / testing')
    parser.add_argument('--source', required=True,
                        help='source data directory')
    parser.add_argument('--destination', required=True,
                        help='destination data directory')
    args = parser.parse_args()

    logger = get_module_logger(__name__)
    logger.info('Creating splits...')
    split(args.source, args.destination)