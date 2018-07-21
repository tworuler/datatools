import click
import numpy as np
from PIL import Image
from datatools import common
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


@click.command(help='Show image')
@click.argument('file')
@click.option('--palette', '-p', type=int, help='Palette mode')
def readimg(file, palette):
    image = Image.open(file)
    print(image.format, image.size, image.mode)
    if palette is not None:
        palette_value = common.PALETTES[palette]
        image.putpalette(palette_value)
    image.show()

