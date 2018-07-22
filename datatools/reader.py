import click
import numpy as np
from PIL import Image
from termcolor import cprint
from datatools import common
from datatools.logger import logger


@click.command(help='Display numpy array content')
@click.argument('file', type=click.File('rb'))
def readnpy(file):
    a = np.load(file)
    print('shape: ', a.shape)
    print('dtype: ', a.dtype)
    print(a)


@click.command(help='Display numpy array content')
@click.argument('file', nargs=-1, type=click.Path(exists=True, dir_okay=False))
def readnpys(file):
    print('SHAPE', 'DTYPE')
    for f in file:
        a = np.load(f)
        cprint(f + ':', 'magenta', end='')
        print(a.shape, a.dtype)


@click.command(help='Show image')
@click.argument('file', nargs=-1, type=click.Path(exists=True, dir_okay=False))
@click.option('--palette', '-p', type=int, help='Palette mode')
def readimg(file, palette):
    is_single_file = (len(file) == 1)
    print('FORMAT HxW MODE')
    for f in file:
        image = Image.open(f)
        if not is_single_file:
            cprint(f + ':', 'magenta', end='')
        w, h = image.size
        print('{} {}x{} {}'.format(image.format, h, w, image.mode))
        if palette is not None:
            palette_value = common.PALETTES[palette]
            image.putpalette(palette_value)
        if is_single_file:
            image.show()

