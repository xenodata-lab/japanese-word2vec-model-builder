import bz2
import csv
from glob import glob
import os
import sys


def iter_docs(csv_path, dir_path):
    """
    Parameters
    ----------
    csv_path : string
        File path of CSV datasets
    dir_path : string
        Directory path where extracted text files are put
    """

    extracted_file_path_pattern = os.path.join(csv_path, '*.csv')
    extracted_file_paths = glob(extracted_file_path_pattern)

    for fpath in extracted_file_paths:
        print(fpath)
        with open(fpath, newline='') as f:
            reader = csv.DictReader(f)
            for row in reader:
                text = row['text']
                lines = text.split('<br>')
                yield '\n'.join(lines)
