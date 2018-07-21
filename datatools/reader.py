import click
import numpy as np
from datatools.logger import logger


@click.command(help='Display numpy array content')
@click.argument('file')
def readnpy(file):
    try:
        a = np.load(file)
    except FileNotFoundError:
        logger.error('File not exits.')
        exit(0)

    print('shape: ', a.shape)
    print('dtype: ', a.dtype)
    print(a) 

